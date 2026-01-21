# 第五章：AngelScript 技能

> **预计耗时**: 2小时  
> **前置要求**: 已完成 [04_TagsAndBindings.md](./04_TagsAndBindings.md)  
> **本章目标**: 使用 AngelScript 编写连招技能类，集成 ComboGraph

---

## 📋 本章任务清单

- [ ] 理解项目技能基类结构
- [ ] 理解 ComboGraph AbilityTask
- [ ] 创建 AngelScript 连招技能类
- [ ] 配置技能输入绑定
- [ ] 集成 ComboGraph 资产
- [ ] 处理技能结束与状态

---

## 5.1 技能系统概述

### 架构图

```
┌─────────────────────────────────────────────────────────────────┐
│                         技能层级                                 │
├─────────────────────────────────────────────────────────────────┤
│  UGameplayAbility (UE 基类)                                     │
│       │                                                         │
│       ▼                                                         │
│  UDJ01GameplayAbility (项目基类, C++)                           │
│       │   • 阶段状态机 (Startup/Active/Recovery)                 │
│       │   • 资源消耗与冷却                                       │
│       │   • 伤害计算辅助                                         │
│       │                                                         │
│       ▼                                                         │
│  UGA_WeaponCombo (AngelScript 连招技能)                         │
│           • ComboGraph 集成                                     │
│           • 输入处理                                            │
│           • 动画控制                                            │
└─────────────────────────────────────────────────────────────────┘
```

### 项目技能基类特性

根据现有代码 (`GA_CastStone.as`)，项目的 `UDJ01GameplayAbility` 基类提供：

| 特性 | 说明 |
|------|------|
| **阶段状态机** | `Startup` → `Active` → `Recovery` → `Ended` |
| **阶段配置** | `PhaseConfig` 结构体，配置时长和可打断性 |
| **阶段回调** | `OnPhaseEnter` / `OnPhaseExit` |
| **伤害计算** | `CalculateFinalDamage()` 带 AD/AP 加成 |

---

## 5.2 ComboGraph AbilityTask

### Task 功能

`UComboGraphAbilityTask_StartGraph` 是连招的核心运行时组件：

| 功能 | 说明 |
|------|------|
| **播放 Montage** | 根据节点配置自动播放 |
| **输入监听** | 自动绑定 Edge 的 InputAction |
| **Combo Window** | 处理连招窗口开关 |
| **节点转换** | 根据输入和条件切换节点 |
| **Effect 应用** | 触发配置的 GameplayEffect |
| **事件广播** | 通过委托通知技能层 |

### Task 创建

```cpp
// C++ 示例
UComboGraphAbilityTask_StartGraph* ComboTask;

ComboTask = UComboGraphAbilityTask_StartGraph::CreateStartComboGraph(
    this,           // OwningAbility
    ComboGraph,     // UComboGraph*
    InitialInput,   // UInputAction* (用于 Conduit，可为 nullptr)
    true            // bBroadcastInternalEvents
);

ComboTask->OnGraphEnd.AddDynamic(this, &ThisClass::OnComboGraphEnd);
ComboTask->ReadyForActivation();
```

### Task 委托

| 委托 | 触发时机 |
|------|---------|
| `OnGraphStart` | 图开始执行 |
| `OnGraphEnd` | 图执行结束 |
| `EventReceived` | 收到 Gameplay Event |

---

## 5.3 创建连招技能类

### 文件位置

```
Script/GameAbilityAS/GA_WeaponCombo.as
```

### 完整示例代码

```angelscript filePath=Script/GameAbilityAS/GA_WeaponCombo.as
// ============================================================
// GA_WeaponCombo.as
// 武器连招技能 - AngelScript 版本
// 
// 功能:
// 1. 启动 ComboGraph 执行连招
// 2. 处理连招结束
// 3. 支持轻攻击/重攻击分支
// ============================================================

class UGA_WeaponCombo : UDJ01GameplayAbility
{
    // ========== 连招配置 ==========
    
    // ComboGraph 资产引用
    UPROPERTY(EditDefaultsOnly, Category = "Combo")
    UComboGraph ComboGraph;
    
    // 初始输入动作 (用于 Conduit 分支)
    // 如果 ComboGraph 有 Conduit 节点，这决定初始路径
    UPROPERTY(EditDefaultsOnly, Category = "Combo")
    UInputAction InitialInputAction;
    
    // 是否广播内部事件 (用于调试)
    UPROPERTY(EditDefaultsOnly, Category = "Combo")
    bool bBroadcastInternalEvents = true;
    
    // ========== 内部状态 ==========
    
    // ComboGraph Task 引用
    UComboGraphAbilityTask_StartGraph ComboTask;
    
    // ========== 技能激活 ==========
    
    UFUNCTION(BlueprintOverride)
    void ActivateAbility()
    {
        Print("[WeaponCombo] ===== 技能激活 =====");
        
        // 验证 ComboGraph
        if (!IsValid(ComboGraph))
        {
            Print("[WeaponCombo] 错误: ComboGraph 未设置!");
            EndAbility();
            return;
        }
        
        // 提交技能 (消耗资源、应用冷却)
        if (!CommitAbility())
        {
            Print("[WeaponCombo] CommitAbility 失败");
            EndAbility();
            return;
        }
        
        // 启动 ComboGraph
        StartComboGraph();
    }
    
    // ========== ComboGraph 控制 ==========
    
    void StartComboGraph()
    {
        Print(f"[WeaponCombo] 启动 ComboGraph: {ComboGraph.GetName()}");
        
        // 创建 ComboGraph Task
        ComboTask = UComboGraphAbilityTask_StartGraph::CreateStartComboGraph(
            this,
            ComboGraph,
            InitialInputAction,
            bBroadcastInternalEvents
        );
        
        if (!IsValid(ComboTask))
        {
            Print("[WeaponCombo] 错误: 创建 ComboTask 失败!");
            EndAbility();
            return;
        }
        
        // 绑定回调
        ComboTask.OnGraphEnd.AddDynamic(this, n"OnComboGraphEnd");
        ComboTask.EventReceived.AddDynamic(this, n"OnComboEventReceived");
        
        // 激活 Task
        ComboTask.ReadyForActivation();
        
        Print("[WeaponCombo] ComboGraph Task 已激活");
    }
    
    // ========== 回调处理 ==========
    
    // ComboGraph 结束回调
    UFUNCTION()
    void OnComboGraphEnd(FGameplayTag EventTag, FGameplayEventData EventData)
    {
        Print(f"[WeaponCombo] ComboGraph 结束, Tag: {EventTag.ToString()}");
        
        // 清理并结束技能
        CleanupAndEnd();
    }
    
    // 事件接收回调
    UFUNCTION()
    void OnComboEventReceived(FGameplayTag EventTag, FGameplayEventData EventData)
    {
        Print(f"[WeaponCombo] 收到事件: {EventTag.ToString()}");
        
        // 可以在这里处理自定义事件
        // 例如: Event.Damage.Hit, Event.Combo.Finisher
        HandleCustomEvent(EventTag, EventData);
    }
    
    // ========== 自定义事件处理 ==========
    
    void HandleCustomEvent(FGameplayTag EventTag, FGameplayEventData EventData)
    {
        // 示例: 处理伤害命中事件
        if (EventTag.MatchesTag(FGameplayTag::RequestGameplayTag(n"Event.Damage")))
        {
            Print("[WeaponCombo] 处理伤害事件");
            // 可以添加额外的伤害处理逻辑
        }
        
        // 示例: 处理终结技事件
        if (EventTag.MatchesTag(FGameplayTag::RequestGameplayTag(n"Event.Combo.Finisher")))
        {
            Print("[WeaponCombo] 处理终结技事件");
            // 可以播放额外特效、相机震动等
        }
    }
    
    // ========== 技能取消 ==========
    
    UFUNCTION(BlueprintOverride)
    void CancelAbility()
    {
        Print("[WeaponCombo] 技能被取消");
        
        // 取消 ComboTask
        if (IsValid(ComboTask))
        {
            ComboTask.EndTask();
        }
        
        Super::CancelAbility();
    }
    
    // ========== 清理 ==========
    
    void CleanupAndEnd()
    {
        // 清理 Task 引用
        ComboTask = nullptr;
        
        // 结束技能
        EndAbility();
        
        Print("[WeaponCombo] 技能已结束");
    }
    
    // ========== 辅助函数 ==========
    
    // 获取当前执行的节点
    UComboGraphNodeAnimBase GetCurrentNode()
    {
        if (IsValid(ComboTask))
        {
            return ComboTask.GetCurrentNode();
        }
        return nullptr;
    }
    
    // 获取之前的节点
    UComboGraphNodeAnimBase GetPreviousNode()
    {
        if (IsValid(ComboTask))
        {
            return ComboTask.GetPreviousNode();
        }
        return nullptr;
    }
}
```

---

## 5.4 技能变体

### 轻攻击技能

```angelscript filePath=Script/GameAbilityAS/GA_LightAttack.as
// GA_LightAttack.as
// 轻攻击专用技能

class UGA_LightAttack : UGA_WeaponCombo
{
    // 无需额外配置，使用父类逻辑
    // 在蓝图子类中设置 ComboGraph 和 InitialInputAction
}
```

### 重攻击技能

```angelscript filePath=Script/GameAbilityAS/GA_HeavyAttack.as
// GA_HeavyAttack.as
// 重攻击专用技能

class UGA_HeavyAttack : UGA_WeaponCombo
{
    // 可以覆盖特定行为
    
    UFUNCTION(BlueprintOverride)
    void ActivateAbility()
    {
        Print("[HeavyAttack] 重攻击激活");
        
        // 重攻击可能有额外的蓄力逻辑
        // 这里直接调用父类
        Super::ActivateAbility();
    }
}
```

---

## 5.5 配置技能输入

### 使用 Gameplay Event 触发

推荐通过 GameplayEvent 触发技能，更灵活：

```angelscript
// 在角色或输入处理类中
void OnLightAttackPressed()
{
    FGameplayEventData EventData;
    
    // 发送事件激活技能
    UAbilitySystemBlueprintLibrary::SendGameplayEventToActor(
        GetOwner(),
        FGameplayTag::RequestGameplayTag(n"Event.Input.LightAttack"),
        EventData
    );
}
```

### 技能配置

在技能的默认属性中配置：

| 属性 | 值 |
|------|-----|
| **Ability Triggers** | Tag: `Event.Input.LightAttack` |
| **Ability Tags** | `Ability.Action.Attack` |
| **Cancel Abilities With Tag** | `Ability.Action.Attack` |
| **Block Abilities With Tag** | (根据需要) |

---

## 5.6 蓝图子类配置

### 创建蓝图子类

1. 在内容浏览器中
2. **右键** → **Blueprint Class**
3. 搜索并选择 `GA_WeaponCombo`
4. 命名为 `GA_Katana_LightCombo`

### 配置属性

在蓝图默认值中设置：

| 属性 | 值 |
|------|-----|
| **ComboGraph** | `CG_Katana_LightCombo` (稍后创建) |
| **InitialInputAction** | `IA_LightAttack` 或 nullptr |

### 配置 Ability Tags

在 Class Defaults 中：

```
Ability Tags:
  └─ Ability.Action.Attack.Light

Activation Required Tags: (空或根据需要)

Cancel Abilities With Tag:
  └─ Ability.Action.Attack

Activation Blocked Tags:
  └─ Status.Condition.Stunned
  └─ Status.Condition.Dead
```

---

## 5.7 技能授予

### 在角色初始化时授予

```cpp
// 在角色的 PostInitializeComponents 或 BeginPlay 中
void ADJ01Character::InitializeAbilities()
{
    if (!AbilitySystemComponent) return;
    
    // 授予连招技能
    AbilitySystemComponent->GiveAbility(
        FGameplayAbilitySpec(
            UGA_Katana_LightCombo::StaticClass(),
            1,  // Level
            INDEX_NONE  // InputID
        )
    );
}
```

### 使用 Ability Set (推荐)

如果项目有 AbilitySet 系统：

```cpp
// 在数据资产中配置
UPROPERTY(EditDefaultsOnly)
TArray<TSubclassOf<UGameplayAbility>> DefaultAbilities;

// DefaultAbilities:
// - GA_Katana_LightCombo
// - GA_Katana_HeavyCombo
// - ...
```

---

## 5.8 调试技巧

### 添加调试日志

```angelscript
// 在关键位置添加 Print
Print(f"[WeaponCombo] 当前节点: {GetCurrentNode().GetName()}");
```

### 控制台命令

```
// 启用 ComboGraph 详细日志
Log LogComboGraph Verbose

// 显示技能系统调试信息
ShowDebug AbilitySystem
```

### 常见问题排查

| 问题 | 检查点 |
|------|--------|
| 技能不激活 | 检查 Ability 是否已授予，Tag 是否阻止 |
| ComboGraph 不启动 | 检查 ComboGraph 资产引用是否有效 |
| 输入不响应 | 检查 InputAction 配置和 EnhancedInput 组件 |
| 动画不播放 | 检查 Montage 配置和 Slot 名称 |

---

## 5.9 高级: 与阶段状态机结合

如果需要使用项目的阶段状态机:

```angelscript
class UGA_ComboWithPhases : UDJ01GameplayAbility
{
    UFUNCTION(BlueprintOverride)
    void OnAbilityAdded()
    {
        // 禁用阶段状态机，让 ComboGraph 完全控制
        bUsePhaseStateMachine = false;
        
        // 或者启用，用于前摇阶段
        // bUsePhaseStateMachine = true;
    }
    
    UFUNCTION(BlueprintOverride)
    void OnPhaseEnter(EDJ01AbilityPhase Phase)
    {
        if (Phase == EDJ01AbilityPhase::Active)
        {
            // 在激活阶段启动 ComboGraph
            StartComboGraph();
        }
    }
}
```

---

## 5.10 验证清单

### 代码验证

- [ ] AngelScript 文件无语法错误
- [ ] 热重载后技能类出现在编辑器中

### 蓝图子类验证

- [ ] ComboGraph 属性已设置
- [ ] Ability Tags 配置正确
- [ ] 技能已授予角色

### 运行时验证

- [ ] 按下攻击键技能激活
- [ ] ComboGraph 开始执行
- [ ] 动画正确播放
- [ ] 连招窗口可接受输入
- [ ] 连招结束后技能正确结束

---

## 5.11 下一步

完成本章后，你应该有:

✅ `GA_WeaponCombo.as` 基础连招技能类  
✅ 蓝图子类 `GA_Katana_LightCombo`  
✅ 技能正确授予并可激活  
✅ 理解 ComboGraph Task 的使用方式

接下来我们将创建 ComboGraph 资产并配置连招节点。

---

👉 **[进入第六章：ComboGraph 配置](./06_ComboGraph.md)**