# 伤害公式配置系统指南

本文档描述 DJ01 项目中数据驱动的伤害计算系统的配置方法。

---

## 目录

1. [系统架构](#系统架构)
2. [核心组件](#核心组件)
3. [修正器配置详解](#修正器配置详解)
4. [配置示例](#配置示例)
5. [扩展属性集](#扩展属性集)
6. [常见问题](#常见问题)

---

## 系统架构

```
┌─────────────────────────────────────────────────────────────────────┐
│                        伤害计算流程                                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  BaseDamage ──→ [攻击方修正器链] ──→ [防守方修正器链] ──→ [最终修正器链] ──→ FinalDamage │
│                                                                     │
│  例: 100 ──→ 攻击力加成(×1.5) ──→ 防御减免(×0.5) ──→ 弱点(×1.5) ──→ 112.5  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 工作模式

| 模式 | 触发条件 | 描述 |
|-----|---------|------|
| **数据驱动模式** | `DefaultFormulaConfig` 已配置 | 使用 DataAsset 中的修正器链计算 |
| **硬编码后备模式** | `DefaultFormulaConfig` 为空 | 使用简化的硬编码公式 |

---

## 核心组件

### 文件结构

```
Executions/
├── DJ01DamageExecution.h/.cpp      # 主执行类，GAS 入口
├── DJ01DamageCalculator.h/.cpp     # 计算引擎，执行修正器链
├── DJ01DamageFormulaConfig.h/.cpp  # DataAsset 定义
├── DJ01DamageModifierTypes.h       # 枚举和结构体定义
└── DamageSystem_Configuration_Guide.md  # 本文档
```

### 类职责

| 类名 | 职责 |
|-----|------|
| `UDJ01DamageExecution` | GAS 执行计算入口，处理团队/距离衰减 |
| `UDJ01DamageCalculator` | 静态工具类，执行修正器链计算 |
| `UDJ01DamageFormulaConfig` | DataAsset，存储公式配置 |
| `FDamageModifierConfig` | 单个修正器的配置结构体 |

---

## 修正器配置详解

### FDamageModifierConfig 属性

| 属性 | 类型 | 描述 |
|-----|------|------|
| `ModifierName` | FString | 调试用名称 |
| `bEnabled` | bool | 是否启用 |
| `Source` | EDamageModifierSource | 数据来源（攻击方/防守方/上下文） |
| `SourceAttribute` | FGameplayAttribute | 读取的属性 |
| `Operation` | EDamageModifierOperation | 计算方式 |
| `CompareAttribute` | FGameplayAttribute | 对抗属性（仅 Compare/Penetration） |
| `Coefficient` | float | 系数 |
| `Constant` | float | 常数（仅 Reduction） |
| `Condition` | FDamageModifierCondition | 触发条件 |
| `Priority` | int32 | 优先级（小值先执行） |

### 五种计算方式 (EDamageModifierOperation)

#### 1. Scale (属性缩放)
```
公式: Damage *= (1 + Attribute * Coefficient)
用途: 攻击力/魔法力加成
示例: AttackPower=100, Coefficient=0.01 → Damage *= 2.0 (+100%)
```

#### 2. Reduction (减伤公式)
```
公式: Damage *= Constant / (Constant + Attribute)
用途: 防御减免
示例: Defense=100, Constant=100 → Damage *= 0.5 (-50%)
特点: 收益递减，永远不会达到100%减伤
```

#### 3. Multiply (直接倍乘)
```
公式: Damage *= Coefficient
用途: 弱点加成、BUFF加成
示例: 命中弱点时 Coefficient=1.5 → Damage *= 1.5 (+50%)
通常配合 Condition 使用
```

#### 4. Compare (攻防对抗)
```
公式: 攻方属性 vs 守方属性，决定是否触发效果
用途: 暴击率 vs 暴击抗性、命中 vs 闪避
示例: CritRate=50, CritResist=20 → 实际暴击率 30%
```

#### 5. Penetration (穿透减免)
```
公式: 先削弱对方防御，再计算减伤
用途: 护甲穿透
示例: ArmorPen=30 → 敌方 Defense 视为减少 30
```

### 触发条件 (FDamageModifierCondition)

| 属性 | 描述 |
|-----|------|
| `bCheckTag` | 是否检查 Tag |
| `RequiredAttackerTag` | 攻击方必须拥有的 Tag |
| `RequiredDefenderTag` | 防守方必须拥有的 Tag |
| `bRequireBothTags` | 是否需要双方都满足 |

---

## 配置示例

### 示例1: 标准物理伤害 (DA_PhysicalDamage)

```
FormulaName: "标准物理伤害"
MinimumDamage: 1.0
MaximumDamage: 0 (无限制)

AttackerModifiers:
┌────────────────────────────────────────────────────────────┐
│ ModifierName: "物理攻击加成"                                │
│ Source: Attacker                                           │
│ SourceAttribute: UDJ01CombatSet::AttackPower              │
│ Operation: Scale                                           │
│ Coefficient: 0.01                                          │
│ Priority: 100                                              │
└────────────────────────────────────────────────────────────┘

DefenderModifiers:
┌────────────────────────────────────────────────────────────┐
│ ModifierName: "物理防御减伤"                                │
│ Source: Defender                                           │
│ SourceAttribute: UDJ01CombatSet::Defense                  │
│ Operation: Reduction                                       │
│ Constant: 100.0                                            │
│ Priority: 100                                              │
└────────────────────────────────────────────────────────────┘

FinalModifiers:
┌────────────────────────────────────────────────────────────┐
│ ModifierName: "元素弱点加成"                                │
│ Operation: Multiply                                        │
│ Coefficient: 1.5                                           │
│ Condition:                                                 │
│   bCheckTag: true                                          │
│   RequiredAttackerTag: Damage.Element (任意子Tag)          │
│   RequiredDefenderTag: Weakness.Element (对应子Tag)        │
│   bRequireBothTags: true                                   │
│ Priority: 100                                              │
└────────────────────────────────────────────────────────────┘
```

**计算过程:**
```
BaseDamage = 100
AttackPower = 50, Defense = 100

Step 1 (攻击加成): 100 × (1 + 50 × 0.01) = 100 × 1.5 = 150
Step 2 (防御减伤): 150 × (100 / (100 + 100)) = 150 × 0.5 = 75
Step 3 (弱点命中): 75 × 1.5 = 112.5

FinalDamage = 112.5
```

### 示例2: 魔法伤害 (DA_MagicalDamage)

```
AttackerModifiers:
┌────────────────────────────────────────────────────────────┐
│ ModifierName: "魔法攻击加成"                                │
│ Source: Attacker                                           │
│ SourceAttribute: UDJ01CombatSet::MagicPower               │
│ Operation: Scale                                           │
│ Coefficient: 0.01                                          │
│ Priority: 100                                              │
└────────────────────────────────────────────────────────────┘

DefenderModifiers:
┌────────────────────────────────────────────────────────────┐
│ ModifierName: "魔法防御减伤"                                │
│ Source: Defender                                           │
│ SourceAttribute: UDJ01CombatSet::MagicDefense             │
│ Operation: Reduction                                       │
│ Constant: 100.0                                            │
│ Priority: 100                                              │
└────────────────────────────────────────────────────────────┘
```

### 示例3: 真实伤害 (DA_TrueDamage)

```
FormulaName: "真实伤害"

AttackerModifiers: [] (空)
DefenderModifiers: [] (空)
FinalModifiers: [] (空)

# 无任何修正器 = 直接输出 BaseDamage
```

---

## 扩展属性集

### 添加新属性的完整流程

```
┌─────────────────────────────────────────────────────────────────────┐
│                        添加新属性流程                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. DJ01CombatSet.h 添加属性声明                                     │
│     ↓                                                               │
│  2. DJ01CombatSet.cpp 添加复制和初始化                               │
│     ↓                                                               │
│  3. 重新编译项目                                                     │
│     ↓                                                               │
│  4. 在编辑器中创建/修改 FormulaConfig                                │
│     ↓                                                               │
│  5. 选择新属性并配置计算方式                                          │
│                                                                     │
│  ※ 如需新的计算公式，才需要修改 DJ01DamageCalculator                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 示例: 添加暴击系统

**Step 1: 在 DJ01CombatSet.h 添加属性**

```cpp
// 暴击率 (0-100)
UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_CriticalRate, Category = "Combat Attributes")
FGameplayAttributeData CriticalRate;
ATTRIBUTE_ACCESSORS(UDJ01CombatSet, CriticalRate);

// 暴击伤害倍率 (默认150 = 150%)
UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_CriticalDamage, Category = "Combat Attributes")
FGameplayAttributeData CriticalDamage;
ATTRIBUTE_ACCESSORS(UDJ01CombatSet, CriticalDamage);

// 暴击抗性
UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_CriticalResist, Category = "Combat Attributes")
FGameplayAttributeData CriticalResist;
ATTRIBUTE_ACCESSORS(UDJ01CombatSet, CriticalResist);
```

**Step 2: 在 DJ01CombatSet.cpp 添加复制**

```cpp
void UDJ01CombatSet::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    // ... 现有属性 ...
    DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, CriticalRate, COND_None, REPNOTIFY_Always);
    DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, CriticalDamage, COND_None, REPNOTIFY_Always);
    DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, CriticalResist, COND_None, REPNOTIFY_Always);
}
```

**Step 3: 在编辑器配置使用**

```
AttackerModifiers:
┌────────────────────────────────────────────────────────────┐
│ ModifierName: "暴击判定"                                    │
│ Source: Attacker                                           │
│ SourceAttribute: UDJ01CombatSet::CriticalRate             │
│ Operation: Compare                                         │
│ CompareAttribute: UDJ01CombatSet::CriticalResist          │
│ Priority: 50                                               │
├────────────────────────────────────────────────────────────┤
│ ModifierName: "暴击伤害加成"                                │
│ Source: Attacker                                           │
│ SourceAttribute: UDJ01CombatSet::CriticalDamage           │
│ Operation: Scale                                           │
│ Coefficient: 0.01                                          │
│ Condition:                                                 │
│   bCheckTag: true                                          │
│   RequiredAttackerTag: Combat.Status.Critical              │
│ Priority: 60                                               │
└────────────────────────────────────────────────────────────┘
```

---

## 常见问题

### Q1: 如何创建 FormulaConfig 资产？

1. 在内容浏览器右键 → **Miscellaneous** → **Data Asset**
2. 选择 `DJ01DamageFormulaConfig` 类
3. 命名为 `DA_物理伤害` 或类似名称
4. 双击打开编辑修正器

### Q2: 如何让 DamageExecution 使用我的配置？

1. 创建 `UDJ01DamageExecution` 的蓝图子类
2. 在 Details 面板设置 `DefaultFormulaConfig`
3. 在 GameplayEffect 中使用这个子类

或者直接修改 C++ 中的默认值。

### Q3: 修正器的执行顺序是什么？

1. 按 `Priority` 从小到大排序
2. 同优先级按数组顺序
3. 先 AttackerModifiers → 再 DefenderModifiers → 最后 FinalModifiers

### Q4: 条件检查失败会怎样？

修正器会被跳过，伤害值保持不变，继续执行下一个修正器。

### Q5: 如何调试伤害计算？

1. 设置 `bEnableDebugLog = true`
2. 查看输出日志中的详细计算过程
3. 每个修正器的输入输出都会被记录

---

## GameplayTag 约定

### 伤害类型
```
Damage.Type.Physical   - 物理伤害（使用 AttackPower/Defense）
Damage.Type.Magical    - 魔法伤害（使用 MagicPower/MagicDefense）
Damage.Type.True       - 真实伤害（无视防御）
```

### 元素类型
```
Damage.Element.Fire    - 火焰
Damage.Element.Ice     - 冰霜
Damage.Element.Thunder - 雷电
Damage.Element.Wind    - 风
Damage.Element.Light   - 光明
Damage.Element.Dark    - 黑暗
Damage.Element.Water   - 水
```

### 弱点标记
```
Weakness.Element.Fire    - 对火焰弱点
Weakness.Element.Ice     - 对冰霜弱点
... (与元素类型对应)
```

---

## 版本历史

| 版本 | 日期 | 变更 |
|-----|------|------|
| 1.0 | 2024-12 | 初始版本，支持5种计算方式 |
