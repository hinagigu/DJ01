# 06. BindingSet 集成

> **预计耗时**: 30 分钟  
> **前置条件**: 已完成 05_武器动画层创建

---

## 🎯 本章目标

使用项目的 BindingSet 系统，实现：

1. ✅ GAS 属性自动同步到动画蓝图变量
2. ✅ GameplayTag 状态自动映射到布尔变量
3. ✅ 无需手动编写同步代码

---

## 📚 BindingSet 系统概述

```
┌─────────────────────────────────────────────────────────────┐
│                   Gameplay Ability System                    │
│                                                              │
│  Attributes:          GameplayTags:                         │
│  • Health = 100       • Status.Stunned (active)             │
│  • Stamina = 50       • Status.Rooted (inactive)            │
│  • MoveSpeed = 600    • Combat.Attacking (active)           │
│                                                              │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ BindingSet 自动同步
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   Animation Blueprint                        │
│                                                              │
│  Variables:                                                  │
│  • Health = 100       ← 自动同步                            │
│  • bIsStunned = true  ← Tag 激活时 = true                   │
│  • bIsRooted = false  ← Tag 未激活时 = false                │
│  • bIsAttacking = true                                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 项目的 BindingSet 机制

项目使用 `AttributeGenerator` 工具生成 BindingSet 代码：

```
Tools/AttributeGenerator/
├── main.py                  ← 主程序
├── BindingSetDefinitions.json  ← 配置文件
└── Templates/              ← 代码模板
```

生成的代码位于：
```
Source/DJ01/AbilitySystem/Attributes/BindingSets/
```

---

## 📝 使用 AttributeGenerator 添加 BindingSet

### Step 1: 定义 BindingSet

编辑 `BindingSetDefinitions.json`:

```json
{
  "BindingSets": {
    "AnimState": {
      "Description": "动画状态绑定",
      "Tags": [
        {
          "Tag": "Status.Condition.Stunned",
          "Variable": "bIsStunned",
          "Type": "bool"
        },
        {
          "Tag": "Status.Condition.Rooted",
          "Variable": "bIsRooted",
          "Type": "bool"
        },
        {
          "Tag": "Combat.Attacking",
          "Variable": "bIsAttacking",
          "Type": "bool"
        },
        {
          "Tag": "Combat.Blocking",
          "Variable": "bIsBlocking",
          "Type": "bool"
        }
      ],
      "Attributes": [
        {
          "Attribute": "DJ01AttributeSet.MoveSpeed",
          "Variable": "MoveSpeedMultiplier",
          "Type": "float"
        }
      ]
    }
  }
}
```

### Step 2: 运行生成器

```bash
cd D:\UnrealProjects\DJ01\Tools\AttributeGenerator
python main.py
```

或使用打包的 exe：
```bash
D:\UnrealProjects\DJ01\DJ01_GAS_Generator.exe
```

### Step 3: 查看生成的代码

生成器会创建/更新：

```cpp
// BindingSet_AnimState.h
#pragma once

#include "CoreMinimal.h"

// 在动画蓝图中使用这个宏声明变量
#define DJ01_BINDING_SET_ANIMSTATE_VARS() \
    UPROPERTY(BlueprintReadOnly, Category = "BindingSet|AnimState") \
    bool bIsStunned = false; \
    UPROPERTY(BlueprintReadOnly, Category = "BindingSet|AnimState") \
    bool bIsRooted = false; \
    UPROPERTY(BlueprintReadOnly, Category = "BindingSet|AnimState") \
    bool bIsAttacking = false; \
    UPROPERTY(BlueprintReadOnly, Category = "BindingSet|AnimState") \
    bool bIsBlocking = false; \
    UPROPERTY(BlueprintReadOnly, Category = "BindingSet|AnimState") \
    float MoveSpeedMultiplier = 1.0f;

// 在初始化时调用这个宏注册回调
#define DJ01_BINDING_SET_ANIMSTATE_REGISTER(ASC) \
    // ... 注册 Tag 监听和属性变更回调的代码
```

---

## 📝 在 AnimInstance 中使用 BindingSet

### Step 1: 修改 DJ01AnimInstance.h

```cpp
// DJ01AnimInstance.h

#pragma once

#include "CoreMinimal.h"
#include "Animation/AnimInstance.h"
#include "AbilitySystem/Attributes/BindingSets/BindingSet_AnimState.h"  // 添加
#include "DJ01AnimInstance.generated.h"

UCLASS(Config = Game)
class DJ01_API UDJ01AnimInstance : public UAnimInstance
{
    GENERATED_BODY()

public:
    // ... 现有代码 ...

protected:
    //========================================
    // BindingSet 变量 (自动与 GAS 同步)
    //========================================
    
    DJ01_BINDING_SET_ANIMSTATE_VARS()  // 使用宏声明变量
    
    // ... 其他代码 ...
};
```

### Step 2: 修改 DJ01AnimInstance.cpp

```cpp
// DJ01AnimInstance.cpp

void UDJ01AnimInstance::InitializeWithAbilitySystem(UAbilitySystemComponent* ASC)
{
    if (!ASC)
    {
        return;
    }
    
    // 注册 BindingSet 回调
    DJ01_BINDING_SET_ANIMSTATE_REGISTER(ASC)
    
    // ... 其他初始化代码 ...
}
```

### Step 3: 编译项目

```bash
# 在 UE 编辑器中编译，或使用命令行
"C:\Program Files\Epic Games\UE_5.x\Engine\Build\BatchFiles\Build.bat" DJ01Editor Win64 Development
```

---

## 📝 在动画蓝图中使用绑定变量

编译后，这些变量会自动出现在动画蓝图中：

```
My Blueprint
└── Variables
    ├── bIsStunned       ← BindingSet 生成
    ├── bIsRooted        ← BindingSet 生成
    ├── bIsAttacking     ← BindingSet 生成
    ├── bIsBlocking      ← BindingSet 生成
    ├── MoveSpeedMultiplier  ← BindingSet 生成
    ├── GroundSpeed      ← 原有
    └── GroundDistance   ← 原有
```

### 使用示例：根据眩晕状态切换动画

在状态机中添加 Stunned 状态：

```
┌───────────────────────────────────────────────────────┐
│                    LocomotionSM                        │
├───────────────────────────────────────────────────────┤
│                                                        │
│  ┌─────────┐         ┌─────────┐                      │
│  │ OnGround│ ←─────→ │ Stunned │                      │
│  └─────────┘         └─────────┘                      │
│       ▲                   │                            │
│       │    bIsStunned     │                            │
│       └───────────────────┘                            │
│                                                        │
└───────────────────────────────────────────────────────┘
```

**转换规则**:
- OnGround → Stunned: `bIsStunned == true`
- Stunned → OnGround: `bIsStunned == false`

### 使用示例：根据攻击状态调整移动

在 BlendSpace 输入中使用 MoveSpeedMultiplier：

```
[GroundSpeed] ──→ [×] ──→ [BlendSpace Speed Input]
                   │
[MoveSpeedMultiplier]─┘
```

---

## 🔄 数据流示意图

```
┌─────────────────────────────────────────────────────────────┐
│                      Ability 激活攻击                        │
│  UAbilitySystemComponent::AddLooseGameplayTag               │
│      (GameplayTag: Combat.Attacking)                        │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               BindingSet 回调触发                            │
│  OnTagChanged → 设置 bIsAttacking = true                    │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               动画蓝图读取变量                               │
│  状态机/BlendSpace 使用 bIsAttacking 进行判断               │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧪 测试 BindingSet

### 方法 1: 使用 GAS 调试控制台

1. PIE 运行
2. 按 ` 打开控制台
3. 输入: `AbilitySystem.Debug.AddLooseGameplayTag Status.Condition.Stunned`
4. 观察动画蓝图中 `bIsStunned` 变为 true

### 方法 2: 在 Ability 中设置 Tag

```angelscript
// 在技能中添加眩晕 Tag
class UGA_StunAbility : UDJ01GameplayAbility
{
    UFUNCTION(BlueprintOverride)
    void ActivateAbility()
    {
        // 给目标添加眩晕 Tag
        UAbilitySystemComponent ASC = GetAbilitySystemComponentFromActorInfo();
        ASC.AddLooseGameplayTag(FGameplayTag::RequestGameplayTag(n"Status.Condition.Stunned"));
    }
}
```

---

## ✅ 完成检查清单

- [ ] 配置了 BindingSetDefinitions.json
- [ ] 运行了 AttributeGenerator
- [ ] 在 DJ01AnimInstance.h 中添加了变量宏
- [ ] 在 DJ01AnimInstance.cpp 中添加了注册宏
- [ ] 项目编译成功
- [ ] 动画蓝图中可以看到绑定变量
- [ ] 测试 Tag 变更能正确更新变量

---

## ⚠️ 常见问题

### Q: 变量没有出现在蓝图中？

**A**: 
1. 确保 C++ 代码已编译
2. 检查宏是否正确放置在 `protected:` 区域
3. 尝试关闭并重新打开动画蓝图

### Q: 变量值不更新？

**A**: 
1. 确保调用了 `InitializeWithAbilitySystem`
2. 检查 ASC 是否有效
3. 确认 Tag/Attribute 名称拼写正确

### Q: 编译报错 "undefined macro"？

**A**: 
1. 确保包含了正确的头文件
2. 检查 AttributeGenerator 是否正确运行
3. 确认生成的文件在正确位置

---

## 📞 下一步

BindingSet 集成完成！最后一章学习如何在运行时切换动画层。

👉 **[进入第七章：动画层切换](./07_动画层切换.md)**