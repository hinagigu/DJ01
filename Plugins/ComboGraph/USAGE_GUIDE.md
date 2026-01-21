# ComboGraph 插件使用指南

> 版本: 1.4.0 (适配 UE 5.4)  
> 官方文档: https://combo-graph.github.io  
> Discord: https://discord.gg/d4rs4vcX6t

---

## 目录

1. [插件概述](#插件概述)
2. [核心概念](#核心概念)
3. [快速开始](#快速开始)
4. [节点详解](#节点详解)
5. [Edge 配置](#edge-配置)
6. [运行 ComboGraph](#运行-combograph)
7. [伤害与效果系统](#伤害与效果系统)
8. [碰撞检测](#碰撞检测)
9. [常用配置](#常用配置)
10. [蓝图 API](#蓝图-api)
11. [C++ API](#c-api)
12. [最佳实践](#最佳实践)
13. [常见问题](#常见问题)

---

## 插件概述

ComboGraph 是一个基于 **GAS (Gameplay Ability System)** 的连招系统插件，提供可视化节点编辑器来设计连招流程。

### 主要功能

| 功能 | 描述 |
|------|------|
| 可视化编辑器 | 节点图编辑，直观设计连招流程 |
| EnhancedInput 集成 | 直接绑定 InputAction 作为过渡条件 |
| GAS 深度集成 | AbilityTask 驱动，支持 GE/Cue |
| 多种伤害处理 | 支持 GAS 方式或 UE 原生伤害系统 |
| 碰撞检测组件 | 内置武器追踪碰撞检测 |
| 网络同步 | 服务端/客户端同步支持 |

### 架构图

```
┌─────────────────────────────────────────────────────────────────┐
│                        ComboGraph                               │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────┐    ┌─────────────┐    ┌─────────────┐             │
│  │  Entry  │───→│ MontageNode │───→│ MontageNode │───→ ...     │
│  └─────────┘    └─────────────┘    └─────────────┘             │
│                       │ Edge            │ Edge                  │
│                       ▼                 ▼                       │
│               ┌─────────────┐    ┌─────────────┐               │
│               │ MontageNode │    │ MontageNode │               │
│               └─────────────┘    └─────────────┘               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   AbilityTask_StartGraph                        │
├─────────────────────────────────────────────────────────────────┤
│  • 播放 Montage                                                 │
│  • 监听 EnhancedInput                                           │
│  • 处理 Combo Window                                            │
│  • 应用 GameplayEffect / Damage                                 │
│  • 触发 GameplayCue                                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 核心概念

### 1. ComboGraph 资产

`UComboGraph` - 连招图资产，包含所有节点和连线定义。

### 2. 节点类型

| 节点类型 | 类名 | 用途 |
|---------|------|------|
| Entry | `UComboGraphNodeEntry` | 入口节点，自动创建 |
| Conduit | `UComboGraphNodeConduit` | 分支入口，根据输入选择路径 |
| Montage | `UComboGraphNodeMontage` | 播放动画蒙太奇 |
| Sequence | `UComboGraphNodeSequence` | 播放动画序列（自动转蒙太奇） |

### 3. Edge (边/连线)

`UComboGraphEdge` - 定义节点间的过渡条件：
- 输入条件 (InputAction)
- 过渡时机 (立即/通知/窗口结束)
- 触发方式 (Started/Triggered/Canceled)

### 4. Combo Window (连招窗口)

连招输入的有效时间窗口，通过 AnimNotify 控制开启/关闭。

---

## 快速开始

### 步骤 1: 创建 ComboGraph 资产

1. Content Browser 右键
2. **Miscellaneous** → **Combo Graph**
3. 命名并保存

### 步骤 2: 编辑连招图

1. 双击打开编辑器
2. 右键空白处添加节点
3. 从节点拖出连线到另一节点
4. 选中连线配置输入条件

### 步骤 3: 配置动画节点

选中 Montage 节点，在 Details 面板设置：
- **Montage**: 选择动画蒙太奇
- **MontagePlayRate**: 播放速率 (默认 1.0)
- **Effects Container Map**: 效果容器 (可选)
- **Cues Container Map**: Cue 容器 (可选)

### 步骤 4: 配置 Edge

选中连线，设置：
- **Transition Input**: 触发过渡的 InputAction
- **Transition Behavior**: 过渡行为
- **Trigger Event**: 输入触发类型

### 步骤 5: 添加 ComboWindow Notify

在动画蒙太奇中添加 `ANS_ComboGraphWindow` 通知状态，标记输入窗口。

### 步骤 6: 创建并运行 Ability

创建 GameplayAbility，使用 `ComboGraphAbilityTask_StartGraph` 运行连招图。

---

## 节点详解

### Entry 节点

- 自动存在于每个 ComboGraph
- 作为连招的起始点
- 不可删除

### Conduit 节点

用于入口分支，适合场景：
- 轻攻击 / 重攻击 从不同路径开始
- 地面 / 空中 不同连招树

```
         ┌──→ [轻攻击链]
[Entry]──┤
         └──→ [重攻击链]
```

### Montage 节点

主要属性：

| 属性 | 类型 | 描述 |
|------|------|------|
| `Montage` | UAnimMontage* | 动画蒙太奇 |
| `MontagePlayRate` | float | 播放速率 |
| `MontageStartSection` | FName | 起始 Section |
| `bStopAnimationWhenAbilityEnds` | bool | 技能结束时停止动画 |
| `RootMotionScale` | FVector | 根运动缩放 |
| `CostGameplayEffect` | TSubclassOf<UGameplayEffect> | 消耗效果 |
| `EventTags` | FGameplayTagContainer | 监听的事件标签 |
| `EffectsContainerMap` | TMap<FGameplayTag, Container> | 效果容器 |
| `CuesContainerMap` | TMap<FGameplayTag, Container> | Cue 容器 |
| `DamageHandlingMethod` | Enum | 伤害处理方式 |

### Sequence 节点

与 Montage 节点类似，但使用 AnimSequence。
> ⚠️ **注意**: Sequence 节点在网络环境中不推荐使用。

---

## Edge 配置

### Transition Input

设置触发过渡的 `UInputAction`。

### Transition Behavior

| 值 | 描述 |
|----|------|
| `Immediately` | 立即过渡，不等待 |
| `OnAnimNotifyClass` | 等待指定 AnimNotify 类触发 |
| `OnAnimNotifyName` | 等待指定名称的通知触发 |
| `OnComboWindowEnd` | 等待 Combo Window 结束 |

### Trigger Event

| 值 | 描述 |
|----|------|
| `Started` | 按键按下时触发 |
| `Triggered` | 持续触发 (默认) |
| `Canceled` | 按键释放时触发 |

### 示例配置

```
Edge: Attack1 → Attack2
├── TransitionInput: IA_LightAttack
├── TransitionBehavior: OnComboWindowEnd
└── TriggerEvent: Started
```

---

## 运行 ComboGraph

### 方式一: 通过 Native Ability (推荐)

插件提供 `UComboGraphNativeAbility`，通过 Gameplay Event 触发：

```cpp
// 发送事件启动 ComboGraph
FGameplayEventData EventData;
EventData.OptionalObject = MyComboGraph;        // UComboGraph*
EventData.OptionalObject2 = InitialInputAction; // UInputAction* (用于 Conduit)

UAbilitySystemBlueprintLibrary::SendGameplayEventToActor(
    TargetActor,
    FGameplayTag::RequestGameplayTag("ComboGraph.Event.Received"),
    EventData
);
```

### 方式二: 自定义 Ability + AbilityTask

```cpp
// MyComboAbility.h
UCLASS()
class UMyComboAbility : public UGameplayAbility
{
    GENERATED_BODY()

public:
    UPROPERTY(EditDefaultsOnly, Category = "Combo")
    TObjectPtr<UComboGraph> ComboGraph;

protected:
    virtual void ActivateAbility(...) override;
    
    UFUNCTION()
    void OnComboGraphEnd(FGameplayTag EventTag, FGameplayEventData EventData);

private:
    UPROPERTY()
    TObjectPtr<UComboGraphAbilityTask_StartGraph> ComboTask;
};

// MyComboAbility.cpp
void UMyComboAbility::ActivateAbility(...)
{
    Super::ActivateAbility(...);
    
    if (!ComboGraph)
    {
        EndAbility(...);
        return;
    }
    
    // 创建并启动 ComboGraph Task
    ComboTask = UComboGraphAbilityTask_StartGraph::CreateStartComboGraph(
        this,
        ComboGraph,
        nullptr,  // InitialInput, 用于 Conduit 节点
        true      // bBroadcastInternalEvents
    );
    
    ComboTask->OnGraphEnd.AddDynamic(this, &UMyComboAbility::OnComboGraphEnd);
    ComboTask->ReadyForActivation();
}

void UMyComboAbility::OnComboGraphEnd(FGameplayTag EventTag, FGameplayEventData EventData)
{
    EndAbility(CurrentSpecHandle, CurrentActorInfo, CurrentActivationInfo, true, false);
}
```

### 方式三: 蓝图

1. 创建 GameplayAbility 蓝图
2. 在 ActivateAbility 中使用 `Start Combo Graph` 节点
3. 绑定 `OnGraphEnd` 回调结束技能

---

## 伤害与效果系统

### Damage Handling Method

| 方式 | 描述 |
|------|------|
| `AbilitySystem` | 使用 GAS 的 GameplayEffect |
| `DamageSystem` | 使用 UE 的 ApplyDamage |

### Effects Container Map

配置按 GameplayTag 触发的 GameplayEffect：

```
EffectsContainerMap:
├── Event.Damage.Hit
│   ├── TargetGameplayEffectClasses: [GE_Damage_Light]
│   ├── bUseSetByCallerMagnitude: true
│   ├── SetByCallerMagnitude: 25.0
│   └── SetByCallerDataTag: Data.Damage
└── Event.Damage.Critical
    └── TargetGameplayEffectClasses: [GE_Damage_Critical]
```

### Cues Container Map

配置按 GameplayTag 触发的 GameplayCue：

```
CuesContainerMap:
├── Event.Damage.Hit
│   └── CueTags: [GameplayCue.Combat.Hit]
└── Event.Combo.Finisher
    └── CueTags: [GameplayCue.Combat.Finisher]
```

---

## 碰撞检测

### ComboGraphCollisionComponent

武器追踪碰撞检测组件，用于命中检测。

#### 设置

```cpp
// 在角色中添加组件
UPROPERTY(VisibleAnywhere)
TObjectPtr<UComboGraphCollisionComponent> ComboCollision;

// BeginPlay 中注册武器 Mesh
void AMyCharacter::BeginPlay()
{
    Super::BeginPlay();
    
    if (ComboCollision && WeaponMesh)
    {
        ComboCollision->RegisterCollisionMesh(WeaponMesh);
    }
}
```

#### 在动画中控制

使用 AnimNotify 控制追踪开始/结束：
- `AN_ComboGraphStartTrace` - 开始追踪
- `AN_ComboGraphEndTrace` - 结束追踪

---

## 常用配置

### 项目设置

`Project Settings` → `Plugins` → `Combo Graph`

| 设置 | 描述 |
|------|------|
| `bSequencesNetworkedWarning` | 网络环境使用 Sequence 时警告 |
| `NotifyStates` | 全局 AnimNotifyState 自动设置 |

### Notify States Auto Setup

配置自动应用到蒙太奇的 NotifyState：

```
NotifyStates:
├── ANS_ComboGraphWindow
│   ├── StartPercent: 0.2
│   └── EndPercent: 0.8
└── ANS_MyCustomNotify
    └── ...
```

---

## 蓝图 API

### Task 节点

| 节点 | 描述 |
|------|------|
| `Start Combo Graph` | 启动 ComboGraph Task |

### Task 事件

| 事件 | 描述 |
|------|------|
| `OnGraphStart` | 图开始执行 |
| `OnGraphEnd` | 图执行结束 |
| `EventReceived` | 接收到 Gameplay Event |

### 节点蓝图事件 (ComboGraphNodeAnimBase)

| 事件 | 描述 |
|------|------|
| `CanActivateNode` | 判断节点是否可激活 |
| `OnInitialized` | 节点初始化 |
| `OnActivated` | 节点激活 |
| `OnDeactivated` | 节点停用 |
| `OnMontagePlay` | 蒙太奇开始播放 |
| `OnEventReceived` | 接收到事件 |

---

## C++ API

### 关键类

```cpp
// 连招图资产
class UComboGraph : public UObject

// 节点基类
class UComboGraphNodeBase : public UObject
class UComboGraphNodeAnimBase : public UComboGraphNodeBase
class UComboGraphNodeMontage : public UComboGraphNodeAnimBase
class UComboGraphNodeSequence : public UComboGraphNodeAnimBase
class UComboGraphNodeEntry : public UComboGraphNodeBase
class UComboGraphNodeConduit : public UComboGraphNodeBase

// 边
class UComboGraphEdge : public UObject

// 运行时 Task
class UComboGraphAbilityTask_StartGraph : public UAbilityTask

// 组件
class UComboGraphGameplayTasksComponent : public UGameplayTasksComponent
class UComboGraphCollisionComponent : public UActorComponent
```

### Task 创建

```cpp
static UComboGraphAbilityTask_StartGraph* CreateStartComboGraph(
    UGameplayAbility* OwningAbility,
    UComboGraph* ComboGraph,
    UInputAction* InitialInput = nullptr,
    bool bBroadcastInternalEvents = true
);
```

### 委托

```cpp
// Task 级别
DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(
    FComboGraphEventReceivedDelegate, 
    FGameplayTag, EventTag, 
    FGameplayEventData, EventData
);

// 全局委托 (FComboGraphDelegates)
static FOnComboGraphStarted OnComboGraphStarted;
static FOnComboGraphEnded OnComboGraphEnded;
```

---

## 最佳实践

### 1. 动画蒙太奇设置

- 在蒙太奇中添加 `ANS_ComboGraphWindow` 标记输入窗口
- 窗口建议从攻击动作开始后 20%-80% 位置
- 使用 Section 划分复杂动画

### 2. 输入配置

- 使用 `Started` 触发类型获得最佳响应
- 为不同攻击创建独立的 InputAction
- Conduit 节点适合处理轻/重攻击分支

### 3. 性能优化

- 避免在单个节点配置过多 GameplayEffect
- 合理使用 Cue 容器而非直接在节点触发
- 网络游戏避免使用 Sequence 节点

### 4. 调试

启用日志：
```cpp
// 控制台
Log LogComboGraph Verbose
```

---

## 常见问题

### Q: 连招窗口不生效？

A: 检查动画蒙太奇是否添加了 `ANS_ComboGraphWindow` 通知。

### Q: 输入没有响应？

A: 确认：
1. Edge 的 `TransitionInput` 已设置
2. 角色有 EnhancedInput 组件
3. InputAction 已正确映射

### Q: 网络同步问题？

A: 
- 确保使用 Montage 而非 Sequence
- 检查 `UComboGraphGameplayTasksComponent` 是否存在
- 使用 `OnComboWindowEnd` 过渡行为更稳定

### Q: 如何获取当前节点信息？

A: 
```cpp
// 在 Task 回调中
UComboGraphNodeAnimBase* CurrentNode = Task->GetCurrentNode();
UComboGraphNodeAnimBase* PreviousNode = Task->GetPreviousNode();
```

### Q: 如何中断连招？

A: 
```cpp
// 取消技能会自动结束 ComboGraph
AbilitySystemComponent->CancelAbilityHandle(AbilityHandle);

// 或直接结束 Task
ComboTask->EndTask();
```

---

## 参考链接

- [官方文档](https://combo-graph.github.io)
- [Marketplace](https://www.unrealengine.com/marketplace/product/0211d0b7c514480c8e6ef338999d63c2)
- [Discord 社区](https://discord.gg/d4rs4vcX6t)

---

*文档更新于 2026-01-04*