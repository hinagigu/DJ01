# ComboGraph 设计难点与解决方案

本文分析 ComboGraph 开发过程中的技术挑战及解决思路。

## 1. 编辑器与运行时数据分离

### 挑战

UE 的图编辑器（EdGraph）使用 `UEdGraphNode`，但游戏运行时不需要这些编辑器数据。如何：
- 在编辑器中提供丰富的可视化
- 打包时只包含必要的游戏数据
- 保持两者同步

### 解决方案：双层节点设计

```cpp
// 编辑器节点（仅编辑器）
UCLASS()
class UComboGraphEdNode : public UEdGraphNode
{
    // 位置、Pin、颜色等编辑器属性
    // 不会被打包
    
    // 引用运行时节点
    UPROPERTY(VisibleAnywhere, Instanced)
    UComboGraphNodeBase* ComboGraphNode;
};

// 运行时节点（打包后存在）
UCLASS()
class UComboGraphNodeBase : public UObject
{
    // 动画、Effect、输入等游戏数据
    // 会被序列化到资产
};
```

```
┌─────────────────────────────────────┐
│  编辑器数据 (EdNode)                 │
│  - 节点位置                          │
│  - Pin 连接                          │
│  - 可视化样式                        │
├───────────────┬─────────────────────┤
│               │                     │
│               ▼                     │
│  ┌─────────────────────────────┐    │
│  │ 运行时数据 (ComboGraphNode) │    │
│  │ - 动画资产                   │    │
│  │ - Effect 容器               │    │
│  │ - Cost 配置                 │    │
│  └─────────────────────────────┘    │
│               │                     │
└───────────────┼─────────────────────┘
                │
                ▼ 序列化
        ┌───────────────┐
        │ .uasset 文件   │
        │ 只包含运行时   │
        │ 数据          │
        └───────────────┘
```

---

## 2. 连招窗口时序控制

### 挑战

连招系统需要精确的时序控制：
- 只在特定时间窗口接受输入
- 窗口与动画帧精确同步
- 不同动画有不同的窗口时机

### 解决方案：AnimNotifyState + GameplayEvent

```cpp
// AnimNotifyState 发送事件
class UComboGraphANS_ComboWindow : public UAnimNotifyState
{
    virtual void NotifyBegin(...) override
    {
        // 窗口开始 -> 发送事件
        SendEvent(MeshComp, FComboGraphNativeTags::Get().ComboBegin);
    }
    
    virtual void NotifyEnd(...) override
    {
        // 窗口结束 -> 发送事件
        SendEvent(MeshComp, FComboGraphNativeTags::Get().ComboEnd);
    }
    
    void SendEvent(USkeletalMeshComponent* Comp, FGameplayTag Tag)
    {
        AActor* Owner = Comp->GetOwner();
        UComboGraphBlueprintLibrary::SendGameplayEventToActor(Owner, Tag, {});
    }
};

// Task 响应事件
void UComboGraphAbilityTask_StartGraph::HandleEventReceived(FGameplayTag Tag, ...)
{
    if (Tag == FComboGraphNativeTags::Get().ComboBegin)
    {
        bComboWindowOpened = true;  // 开放输入
    }
    else if (Tag == FComboGraphNativeTags::Get().ComboEnd)
    {
        bComboWindowOpened = false;  // 关闭输入
        
        if (bComboQueued)
        {
            HandleComboTransition();  // 执行排队的转换
        }
    }
}
```

**设计优势**：
- 时序由美术在动画中控制
- 代码逻辑与动画解耦
- 易于调整和调试

---

## 3. Enhanced Input 集成

### 挑战

Enhanced Input 系统与传统输入系统不同：
- 使用 `UInputAction` 而非直接的按键
- 有多种触发类型（Triggered、Started、Completed 等）
- 需要处理输入值（Axis、Duration 等）

### 解决方案：Edge 配置 + 动态绑定

```cpp
// Edge 配置输入
UCLASS()
class UComboGraphEdge : public UObject
{
    UPROPERTY(EditDefaultsOnly)
    UInputAction* TransitionInput;
    
    UPROPERTY(EditDefaultsOnly)
    EComboGraphTransitionInputEvent TriggerEvent;  // Triggered/Started/Completed...
    
    // 保存输入实例（包含时长等信息）
    UPROPERTY(Replicated)
    FInputActionInstance CurrentInputActionInstance;
};

// 动态绑定
void UComboGraphAbilityTask_StartGraph::SetupInputBindings()
{
    for (auto& [ChildNode, Edge] : CurrentNode->Edges)
    {
        if (!Edge->TransitionInput) continue;
        
        // 获取 Enhanced Input 触发类型
        ETriggerEvent TriggerEvent = Edge->GetEnhancedInputTriggerEvent();
        
        // 绑定到输入组件
        FInputActionBinding& Binding = InputComponent->BindAction(
            Edge->TransitionInput,
            TriggerEvent,
            this,
            &ThisClass::ReceivedInputConfirm,
            Edge  // 传递边作为参数
        );
        
        InputHandles.Add(Binding.GetHandle());
    }
}
```

---

## 4. 节点 Cost 独立计算

### 挑战

不同于 Ability 的整体 Cost，连招系统需要：
- 每个节点可以有独立的消耗
- 消耗不足时阻止转换到该节点
- 与 Ability 的 Cost 系统共存

### 解决方案：节点级 Cost GE

```cpp
// 节点配置 Cost
UCLASS()
class UComboGraphNodeAnimBase : public UComboGraphNodeBase
{
    UPROPERTY(EditDefaultsOnly)
    TSubclassOf<UGameplayEffect> CostGameplayEffect;
};

// 推进节点前检查
bool UComboGraphAbilityTask_StartGraph::AdvanceNextNode(UComboGraphNodeAnimBase* NextNode, ...)
{
    // 1. 检查 BP 可激活条件
    if (!NextNode->K2_CanActivateNode())
    {
        return false;
    }
    
    // 2. 检查并提交 Cost
    if (!CommitAbilityCostForNode(NextNode, FailReason))
    {
        return false;  // 资源不足，不转换
    }
    
    // 3. 继续执行...
}

bool UComboGraphAbilityTask_StartGraph::CheckCostForNode(UComboGraphNodeAnimBase* Node, ...)
{
    const UGameplayEffect* CostGE = Node->CostGameplayEffect.GetDefaultObject();
    if (!CostGE) return true;
    
    // 使用 Ability 的上下文检查
    return CanApplyAttributeModifiers(
        CostGE,
        Ability->GetAbilityLevel(...),
        Ability->MakeEffectContext(...)
    );
}
```

---

## 5. Cue 参数传递

### 挑战

Gameplay Cue 需要接收额外参数（如 Niagara 特效、音效资源），但标准的 `FGameplayCueParameters` 不支持自定义数据。

### 解决方案：自定义 EffectContext

```cpp
// 扩展 EffectContext
USTRUCT()
struct FComboGraphGameplayEffectContext : public FGameplayEffectContext
{
    // 额外的 Cue 参数
    UPROPERTY()
    TArray<TWeakObjectPtr<UObject>> CueParamsObjects;
    
    UPROPERTY()
    TArray<FSoftObjectPath> CueParamsObjectsPaths;
    
    // 网络序列化
    virtual bool NetSerialize(FArchive& Ar, ...) override
    {
        FGameplayEffectContext::NetSerialize(Ar, ...);
        
        // 序列化额外数据
        if (CueParamsObjects.Num() > 0)
        {
            SafeNetSerializeTArray_Default<31>(Ar, CueParamsObjects);
        }
        if (CueParamsObjectsPaths.Num() > 0)
        {
            SafeNetSerializeTArray_Default<31>(Ar, CueParamsObjectsPaths);
        }
        
        return true;
    }
};

// 配置全局使用
UCLASS()
class UComboGraphAbilitySystemGlobals : public UAbilitySystemGlobals
{
    virtual FGameplayEffectContext* AllocGameplayEffectContext() const override
    {
        return new FComboGraphGameplayEffectContext();
    }
};

// DefaultGame.ini
// [/Script/GameplayAbilities.AbilitySystemGlobals]
// AbilitySystemGlobalsClassName=/Script/ComboGraph.ComboGraphAbilitySystemGlobals
```

---

## 6. 资产拖放创建节点

### 挑战

希望用户可以直接从内容浏览器拖动 Montage/Sequence 到图编辑器创建节点。

### 解决方案：Schema 重写拖放方法

```cpp
// ComboGraphSchema.cpp

void UComboGraphSchema::DroppedAssetsOnGraph(
    const TArray<FAssetData>& Assets,
    const FVector2D& GraphPosition,
    UEdGraph* Graph
) const
{
    for (const FAssetData& AssetData : Assets)
    {
        UAnimationAsset* AnimAsset = Cast<UAnimationAsset>(AssetData.GetAsset());
        if (AnimAsset && (AnimAsset->IsA<UAnimMontage>() || AnimAsset->IsA<UAnimSequence>()))
        {
            SpawnNodeFromAsset(AnimAsset, GraphPosition, Graph, nullptr);
        }
    }
}

void UComboGraphSchema::SpawnNodeFromAsset(
    UAnimationAsset* Asset,
    const FVector2D& GraphPosition,
    UEdGraph* Graph,
    UEdGraphPin* PinIfAvailable
)
{
    // 1. 确定节点类型
    TSubclassOf<UComboGraphNodeAnimBase> RuntimeClass = 
        GetRuntimeClassForAnimAsset(Asset, Graph);
    
    // 2. 创建运行时节点
    UComboGraphNodeAnimBase* RuntimeNode = NewObject<UComboGraphNodeAnimBase>(
        Graph->GetOuter(), RuntimeClass
    );
    RuntimeNode->SetAnimationAsset(Asset);
    
    // 3. 创建编辑器节点
    FComboGraphSchemaAction_NewNode Action;
    Action.NodeTemplate = NewObject<UComboGraphEdNode>(Graph);
    Action.NodeTemplate->SetComboGraphNode(RuntimeNode);
    
    // 4. 添加到图
    Action.PerformAction(Graph, PinIfAvailable, GraphPosition);
}

UClass* UComboGraphSchema::GetNodeClassForAnimAsset(const UAnimationAsset* Asset, ...)
{
    if (Asset->IsA<UAnimMontage>())
    {
        return UComboGraphEdNode::StaticClass();  // Montage 节点
    }
    else if (Asset->IsA<UAnimSequence>())
    {
        return UComboGraphEdNode::StaticClass();  // Sequence 节点
    }
    return nullptr;
}
```

---

## 7. 调试可视化

### 挑战

复杂的连招需要直观的调试方式：
- 当前节点高亮
- 状态变化历史
- 输入时序可视化

### 解决方案：委托广播 + 编辑器集成

```cpp
// 定义全局委托
DECLARE_MULTICAST_DELEGATE_TwoParams(FOnComboGraphStarted, const UGameplayTask&, const UComboGraph&);
DECLARE_MULTICAST_DELEGATE_TwoParams(FOnComboGraphEnded, const UGameplayTask&, const UComboGraph&);
DECLARE_MULTICAST_DELEGATE_ThreeParams(FOnComboNodeChanged, const UGameplayTask&, const UComboGraphNodeBase*, const UComboGraphNodeBase*);

struct FComboGraphDelegates
{
    static FOnComboGraphStarted OnComboGraphStarted;
    static FOnComboGraphEnded OnComboGraphEnded;
    static FOnComboNodeChanged OnComboNodeChanged;
};

// Task 中广播
void UComboGraphAbilityTask_StartGraph::AdvanceNextNode(...)
{
    // ... 逻辑 ...
    
    // 广播状态变化
    FComboGraphDelegates::OnComboNodeChanged.Broadcast(*this, PreviousNode, CurrentNode);
}

// 编辑器监听
class FComboGraphDebugger
{
    void Initialize()
    {
        FComboGraphDelegates::OnComboNodeChanged.AddRaw(
            this, 
            &FComboGraphDebugger::OnNodeChanged
        );
    }
    
    void OnNodeChanged(const UGameplayTask& Task, const UComboGraphNodeBase* Prev, const UComboGraphNodeBase* Curr)
    {
        // 更新编辑器 UI 显示
        HighlightNode(Curr);
        AddToHistory(Prev, Curr);
    }
};
```

---

## 8. Conduit 分支路由

### 挑战

有时需要根据不同输入进入不同的连招分支，例如：
- 轻攻击 -> 轻攻击连招
- 重攻击 -> 重攻击连招

### 解决方案：Conduit 节点

```cpp
// Conduit 作为分支路由器
UCLASS()
class UComboGraphNodeConduit : public UComboGraphNodeBase
{
    // Conduit 没有动画，只做分支
};

// 启动时处理
bool UComboGraphAbilityTask_StartGraph::StartComboGraph(...)
{
    UComboGraphNodeBase* FirstRootNode = RunningGraph->FirstNode;
    
    // 检查是否是 Conduit
    UComboGraphNodeConduit* ConduitNode = Cast<UComboGraphNodeConduit>(FirstRootNode);
    if (ConduitNode)
    {
        // 根据初始输入选择分支
        const UComboGraphEdge* Edge = ConduitNode->GetEdgeWithInput(InitialInput);
        if (!Edge)
        {
            FailReason = "No matching edge for InitialInput";
            return false;
        }
        
        // 跳过 Conduit，使用选中的分支
        FirstRootNode = Edge->EndNode;
    }
    
    CurrentNode = Cast<UComboGraphNodeAnimBase>(FirstRootNode);
    // ...
}
```

```
        ┌─────────┐
        │  Entry  │
        └────┬────┘
             │
        ┌────▼────┐
        │ Conduit │  ← 分支路由
        └────┬────┘
      ┌──────┴──────┐
      │             │
   轻攻击         重攻击
      │             │
┌─────▼─────┐ ┌─────▼─────┐
│ Light 1   │ │ Heavy 1   │
└─────┬─────┘ └─────┬─────┘
      │             │
┌─────▼─────┐ ┌─────▼─────┐
│ Light 2   │ │ Heavy 2   │
└───────────┘ └───────────┘
```

---

*下一篇：[08-学习收获总结](./08-LearningPoints.md)*