# 第四章：Tags 与 BindingSet

> **预计耗时**: 1小时  
> **前置要求**: 已完成 [03_AnimLayers.md](./03_AnimLayers.md)  
> **本章目标**: 使用 AttributeGenerator 工具配置连招系统所需的 Tags 和 BindingSet

---

## 📋 本章任务清单

- [ ] 理解 BindingSet 系统
- [ ] 运行 AttributeGenerator 工具
- [ ] 创建连招相关的 GameplayTags
- [ ] 创建 AnimInstance 用的 BindingSet
- [ ] 应用 BindingSet 到动画蓝图
- [ ] 验证绑定生效

---

## 4.1 BindingSet 系统概述

### 什么是 BindingSet？

BindingSet 是项目中的**自动化 GAS 绑定系统**，它能够：

1. 自动生成变量声明
2. 自动注册 GAS 监听回调
3. 自动同步 Tag/Attribute 变化到变量
4. 提供蓝图可调用的初始化函数

### 传统方式 vs BindingSet

**传统方式 (大量样板代码)**:
```cpp
// 1. 手动声明变量
UPROPERTY()
bool bIsStunned;

// 2. 手动写回调
void OnStunnedTagChanged(const FGameplayTag Tag, int32 NewCount)
{
    bIsStunned = (NewCount > 0);
}

// 3. 手动注册
ASC->RegisterGameplayTagEvent(StunnedTag, EGameplayTagEventType::NewOrRemoved)
    .AddUObject(this, &ThisClass::OnStunnedTagChanged);

// 4. 手动初始化当前值
bIsStunned = ASC->HasMatchingGameplayTag(StunnedTag);
```

**使用 BindingSet (一行搞定)**:
```cpp
// 只需声明一个宏！
DJ01_DECLARE_BINDING_SET(AnimState)

// 调用自动生成的初始化函数
InitBindingSet_AnimState(ASC);
```

### 架构图

```
┌─────────────────────────────────────────────────────────────────┐
│                    AttributeGenerator 工具                       │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │              BindingSet Editor                               ││
│  │  ┌───────────────────────┐  ┌───────────────────────────┐   ││
│  │  │  Tag Bindings         │  │  Attribute Bindings       │   ││
│  │  │  ├─ Stunned → bStunned│  │  ├─ Health → CurrentHealth│   ││
│  │  │  ├─ Rooted → bRooted  │  │  └─ Mana → CurrentMana    │   ││
│  │  │  └─ Dead → bIsDead    │  │                           │   ││
│  │  └───────────────────────┘  └───────────────────────────┘   ││
│  └─────────────────────────────────────────────────────────────┘│
│                              │                                  │
│                              ▼ 生成代码                         │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  Generated/BindingSet_AnimState.h                           ││
│  │                                                              ││
│  │  DJ01_BINDING_SET_ANIMSTATE_VARS()      // 变量              ││
│  │  DJ01_BINDING_SET_ANIMSTATE_CALLBACKS() // 回调              ││
│  │  InitBindingSet_AnimState(ASC)          // 初始化函数        ││
│  │  CleanupBindingSet_AnimState(ASC)       // 清理函数          ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

---

## 4.2 运行 AttributeGenerator 工具

### 启动方式

**方式 1: Python 脚本**
```bash
cd D:\UnrealProjects\DJ01\Tools\AttributeGenerator
python main.py
```

**方式 2: 打包的 EXE**
```bash
D:\UnrealProjects\DJ01\DJ01_GAS_Generator.exe
```

### 工具界面

启动后你会看到带有多个标签页的界面：

| 标签页 | 功能 |
|--------|------|
| **Attribute** | 管理 Gameplay Attributes |
| **Tag** | 管理 Gameplay Tags |
| **BindingSet** | 管理绑定集 (本章重点) |
| **MMC** | 管理 Modifier Magnitude Calculations |
| **Execution** | 管理 Gameplay Effect Execution Calculations |

---

## 4.3 创建连招相关的 GameplayTags

### 需要的标签

| 标签 | 用途 |
|------|------|
| `Status.Condition.Stunned` | 眩晕状态 |
| `Status.Condition.Rooted` | 定身状态 |
| `Status.Condition.Silenced` | 沉默状态 |
| `Status.Condition.Dead` | 死亡状态 |
| `Ability.ComboWindow.Light` | 轻攻击连招窗口 |
| `Ability.ComboWindow.Heavy` | 重攻击连招窗口 |
| `Weapon.Type.Katana` | 刀武器类型 |
| `Weapon.Type.SwordShield` | 剑盾武器类型 |
| `Event.Montage.DamageWindow` | 伤害窗口事件 |

### 创建步骤

1. 切换到 **Tag** 标签页
2. 点击 **新建 Tag**
3. 输入完整的标签路径，如 `Status.Condition.Stunned`
4. 添加描述（可选）
5. 重复上述步骤添加所有需要的标签
6. 点击 **生成代码**

### 生成结果

工具会更新以下文件：
```
Source/DJ01/AbilitySystem/GameplayTags/
├── DJ01GameplayTags.h    // 标签声明
└── DJ01GameplayTags.cpp  // 标签定义
```

---

## 4.4 创建 AnimInstance 用的 BindingSet

### 步骤 1: 新建 BindingSet

1. 切换到 **BindingSet** 标签页
2. 点击 **新建 BindingSet**
3. 输入名称: `AnimState`
4. 输入描述: `动画实例用的状态绑定`

### 步骤 2: 添加 Tag 绑定

在 **Tag Bindings** 区域，添加以下绑定：

| Tag | Variable Name | Type |
|-----|---------------|------|
| `Status.Condition.Stunned` | `bIsStunned` | `bool` |
| `Status.Condition.Rooted` | `bIsRooted` | `bool` |
| `Status.Condition.Silenced` | `bIsSilenced` | `bool` |
| `Status.Condition.Dead` | `bIsDead` | `bool` |

### 步骤 3: 添加 Attribute 绑定（可选）

如果需要在动画中使用血量等属性：

| Attribute Set | Attribute | Variable Name | Value Type |
|---------------|-----------|---------------|------------|
| `ResourceSet` | `Health` | `CurrentHealth` | `Current` |
| `ResourceSet` | `Health` | `MaxHealth` | `Max` |

### 步骤 4: 生成代码

1. 点击 **生成代码** 按钮
2. 等待生成完成

### 生成的文件

```
Source/DJ01/AbilitySystem/Attributes/BindingSets/Generated/
├── BindingSets.h              // 统一入口
└── BindingSet_AnimState.h     // AnimState 具体实现
```

---

## 4.5 应用 BindingSet 到动画蓝图

### 步骤 1: 使用"应用到类"功能

1. 在 BindingSet 编辑器中，点击 **应用到类**
2. 选择目标文件: `Source/DJ01/Animation/DJ01AnimInstance.h`
3. 点击 **添加 BindingSet**

工具会自动：
- 添加 `#include` 语句
- 在 `GENERATED_BODY()` 后插入宏

### 步骤 2: 手动验证（如果自动应用失败）

打开 `DJ01AnimInstance.h`，确保有以下内容：

```cpp filePath=Source/DJ01/Animation/DJ01AnimInstance.h
#pragma once

#include "CoreMinimal.h"
#include "Animation/AnimInstance.h"
// 确保有这个 include
#include "DJ01/AbilitySystem/Attributes/BindingSets/Generated/BindingSets.h"
#include "DJ01AnimInstance.generated.h"

UCLASS(Config = Game)
class DJ01_API UDJ01AnimInstance : public UAnimInstance
{
    GENERATED_BODY()
    
    // 确保有这个宏
    DJ01_DECLARE_BINDING_SET(AnimState)

public:
    // ... 其他代码
};
```

### 步骤 3: 初始化绑定

在 `DJ01AnimInstance.cpp` 的 `InitializeWithAbilitySystem` 函数中调用：

```cpp filePath=Source/DJ01/Animation/DJ01AnimInstance.cpp
void UDJ01AnimInstance::InitializeWithAbilitySystem(UAbilitySystemComponent* ASC)
{
    if (!ASC) return;
    
    // 调用自动生成的初始化函数
    InitBindingSet_AnimState(ASC);
}
```

### 蓝图中初始化（替代方案）

如果使用蓝图子类，可以在 EventGraph 中：

```
Event Blueprint Initialize Animation
          │
          ▼
[Try Get Pawn Owner] → [Get Component: AbilitySystemComponent]
                                  │
                                  ▼
                    [Init Binding Set Anim State]
                        (自动生成的蓝图节点)
```

---

## 4.6 在动画蓝图中使用绑定变量

### 变量访问

BindingSet 生成的变量可以直接在蓝图中访问：

```
[Get bIsStunned] ──→ [Branch]
                         │
              ┌──────────┴──────────┐
              │                     │
          True                   False
              │                     │
              ▼                     ▼
    [播放眩晕动画]          [正常状态机]
```

### 典型使用场景

#### 1. 状态条件判断

在状态机转换中使用：
```
Transition Rule: Idle → Stunned
Condition: bIsStunned == true
```

#### 2. 动画混合权重

```
[Get bIsRooted] → [Select Float]
                      │
           ┌─────────┴─────────┐
           │                   │
       True: 0.0          False: 1.0
           │                   │
           └─────────┬─────────┘
                     │
                     ▼
              [Blend Weight]
```

#### 3. 死亡动画触发

```
[Get bIsDead] → [Do Once] → [Play Death Montage]
```

---

## 4.7 调试 BindingSet

### 打印绑定值

在 C++ 中：
```cpp
void UDJ01AnimInstance::NativeUpdateAnimation(float DeltaSeconds)
{
    Super::NativeUpdateAnimation(DeltaSeconds);
    
    // 调试打印
    UE_LOG(LogAnimation, Verbose, 
        TEXT("BindingSet: Stunned=%d, Rooted=%d, Health=%.1f"),
        bIsStunned, bIsRooted, CurrentHealth);
}
```

### 蓝图中调试

添加 Print String 节点显示变量值。

### 常见问题

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| 变量未更新 | 未调用初始化函数 | 确保调用了 `InitBindingSet_XXX` |
| 编译错误 | 缺少 include | 添加 `BindingSets.h` 的 include |
| 变量不存在 | 宏未添加 | 确保添加了 `DJ01_DECLARE_BINDING_SET` |
| Tag 不生效 | Tag 名称不匹配 | 检查 JSON 配置中的 Tag 路径 |

---

## 4.8 完整配置示例

### BindingSetDefinitions.json

```json
{
    "version": "1.0",
    "binding_sets": [
        {
            "name": "AnimState",
            "description": "动画实例用的状态绑定",
            "tag_bindings": [
                {
                    "tag": "Status.Condition.Stunned",
                    "variable_name": "bIsStunned",
                    "variable_type": "bool"
                },
                {
                    "tag": "Status.Condition.Rooted",
                    "variable_name": "bIsRooted",
                    "variable_type": "bool"
                },
                {
                    "tag": "Status.Condition.Silenced",
                    "variable_name": "bIsSilenced",
                    "variable_type": "bool"
                },
                {
                    "tag": "Status.Condition.Dead",
                    "variable_name": "bIsDead",
                    "variable_type": "bool"
                }
            ],
            "attribute_bindings": [
                {
                    "attribute_set": "ResourceSet",
                    "attribute_name": "Health",
                    "variable_name": "CurrentHealth",
                    "variable_type": "float",
                    "value_type": "Current"
                },
                {
                    "attribute_set": "ResourceSet",
                    "attribute_name": "Health",
                    "variable_name": "MaxHealth",
                    "variable_type": "float",
                    "value_type": "Max"
                }
            ]
        }
    ]
}
```

---

## 4.9 验证清单

### 代码生成验证

- [ ] `BindingSets.h` 已生成
- [ ] `BindingSet_AnimState.h` 已生成
- [ ] 包含所有配置的 Tag 和 Attribute 绑定

### 集成验证

- [ ] `DJ01AnimInstance.h` 包含正确的 include
- [ ] `DJ01AnimInstance.h` 包含 `DJ01_DECLARE_BINDING_SET(AnimState)` 宏
- [ ] `InitializeWithAbilitySystem` 调用了 `InitBindingSet_AnimState`

### 运行时验证

- [ ] 变量在蓝图中可见
- [ ] 应用 Stunned Tag 后 `bIsStunned` 变为 true
- [ ] 移除 Tag 后变量恢复 false
- [ ] 属性变化后变量自动更新

---

## 4.10 下一步

完成本章后，你应该有:

✅ 创建了连招系统需要的所有 GameplayTags  
✅ 创建了 `AnimState` BindingSet  
✅ 将 BindingSet 应用到了 `DJ01AnimInstance`  
✅ 理解了如何在动画蓝图中使用绑定变量

接下来我们将编写 AngelScript 连招技能类。

---

## 📚 扩展阅读

详细的 BindingSet 系统文档请参阅：
- [BindingSet 使用指南](../../Tools/AttributeGenerator/docs/BindingSet使用指南.md)

---

👉 **[进入第五章：AngelScript 技能](./05_AbilityScript.md)**