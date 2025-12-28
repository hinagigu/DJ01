# BindingSet 使用指南

## 概述

BindingSet 是 DJ01 项目中的一个代码生成系统，用于自动化 GAS（Gameplay Ability System）属性和 Tag 的监听绑定。它让 AnimInstance、UI Widget 等组件能够以**声明式**的方式响应 GAS 系统的变化，无需手动编写大量样板代码。

## 设计目标

- **一行声明，一行初始化**：极简的 API 设计
- **类型安全**：生成的代码完全是强类型的 C++
- **自动响应**：属性/Tag 变化时自动更新变量
- **团队协作**：配置存储在 JSON 中，便于版本控制

## 架构图

```
┌─────────────────────────────────────────────────────────────────┐
│                    AttributeGenerator 工具                       │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │  Attribute  │  │    Tag      │  │      BindingSet        │  │
│  │   Editor    │  │   Editor    │  │       Editor           │  │
│  └──────┬──────┘  └──────┬──────┘  └───────────┬─────────────┘  │
│         │                │                     │                │
│         ▼                ▼                     ▼                │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │              BindingSetDefinitions.json                     ││
│  │         (配置存储 - 版本控制友好)                             ││
│  └─────────────────────────────────────────────────────────────┘│
│                              │                                  │
│                              ▼                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                    Generator 代码生成                        ││
│  │                                                              ││
│  │  BindingSet_XXX.h  ──►  变量声明、回调函数、注册/注销宏       ││
│  │  BindingSets.h     ──►  统一入口、二次宏展开                  ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                      C++ 项目代码                                │
├─────────────────────────────────────────────────────────────────┤
│  UTestAnimInstance                    UMyHealthBarWidget        │
│  ┌─────────────────────────┐         ┌─────────────────────────┐│
│  │ DJ01_DECLARE_BINDING_SET│         │ DJ01_DECLARE_BINDING_SET││
│  │ (Test)                  │         │ (HUD)                   ││
│  │                         │         │                         ││
│  │ // 自动生成:            │         │ // 自动生成:            ││
│  │ bool bStunned;          │         │ float CurrentHealth;    ││
│  │ float CurrentHealth;    │         │ float MaxHealth;        ││
│  │ ...                     │         │ ...                     ││
│  └─────────────────────────┘         └─────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

## 快速开始

### 1. 创建 BindingSet

1. 打开 `AttributeGenerator` 工具
2. 切换到 `BindingSet` 标签页
3. 点击 `新建 BindingSet`，输入名称（如 `PlayerHUD`）
4. 添加需要监听的 Tag 和 Attribute 绑定
5. 点击 `生成代码`

### 2. 应用到类

1. 点击 `应用到类` 按钮
2. 选择目标类（如 `UTestAnimInstance`）
3. 点击 `添加 BindingSet`

工具会自动：
- 添加 `#include "DJ01/GAS/Generated/BindingSets/BindingSets.h"`
- 在 `GENERATED_BODY()` 后插入 `DJ01_DECLARE_BINDING_SET(PlayerHUD)`

### 3. 初始化绑定

宏会自动生成蓝图可调用的初始化函数，C++ 和蓝图都可以使用：

**C++ 中：**
```cpp
void UMyAnimInstance::InitializeWithAbilitySystem(UAbilitySystemComponent* ASC)
{
    // 直接调用自动生成的函数！
    InitBindingSet_PlayerHUD(ASC);
}
```

**蓝图中：**
```
┌─────────────────────────────────────┐
│  Get Ability System Component       │
└───────────┬─────────────────────────┘
            │
            ▼
┌─────────────────────────────────────┐
│  Init Binding Set Player HUD        │  ◀── 自动生成的蓝图节点！
│  ┌─────────────────────┐            │
│  │ In ASC ●────────────│            │
│  └─────────────────────┘            │
└─────────────────────────────────────┘
```

### 4. 使用绑定的变量

在蓝图或 C++ 中直接使用自动生成的变量：

```cpp
// AnimInstance 中
void UMyAnimInstance::NativeUpdateAnimation(float DeltaSeconds)
{
    Super::NativeUpdateAnimation(DeltaSeconds);
    
    // 直接使用 BindingSet 提供的变量
    if (bStunned)
    {
        // 播放眩晕动画
    }
    
    // CurrentHealth 会自动更新，无需手动获取
    float HealthPercent = CurrentHealth / MaxHealth;
}
```

## API 参考

### 宏和函数

| API | 用途 | 说明 |
|---|---|---|
| `DJ01_DECLARE_BINDING_SET(Name)` | 声明变量、回调和函数 | 放在类定义中（GENERATED_BODY 后） |
| `InitBindingSet_Name(ASC)` | 注册监听并获取当前值 | **自动生成的函数**，蓝图可调用 |
| `CleanupBindingSet_Name(ASC)` | 注销所有监听器 | **自动生成的函数**，蓝图可调用 |

### 生成的变量命名规则

#### Tag 绑定
| 配置 | 生成的变量 | 类型 |
|---|---|---|
| Tag: `Status.Condition.Stunned` | `bStunned` | `bool` |
| Tag: `Status.Buff.Hasted` | `bHasted` | `bool` |

#### Attribute 绑定
| 配置 | 生成的变量 | 类型 |
|---|---|---|
| Attribute: `Health`, ValueType: `Current` | `CurrentHealth` | `float` |
| Attribute: `Health`, ValueType: `Max` | `MaxHealth` | `float` |
| Attribute: `Health`, ValueType: `Total` | `TotalHealth` | `float` |
| Attribute: `MoveSpeed`, ValueType: `Base` | `BaseMoveSpeed` | `float` |

## 二次宏展开原理

### 为什么需要二次展开？

C++ 预处理器的 `##` 拼接操作符**不会展开参数**，所以需要两层宏来确保参数先被展开：

```cpp
// 错误示例：直接拼接
#define WRONG_CONCAT(a, b) a##b
#define NAME Test
WRONG_CONCAT(PREFIX_, NAME)  // 结果: PREFIX_NAME (错误!)

// 正确示例：二次展开
#define CONCAT_IMPL(a, b) a##b
#define CONCAT(a, b) CONCAT_IMPL(a, b)
CONCAT(PREFIX_, NAME)  // 结果: PREFIX_Test (正确!)
```

### 展开流程

```
DJ01_DECLARE_BINDING_SET(Test)
    │
    ▼ Step 1: 替换通用宏
DJ01_BINDING_SET_CONCAT(DJ01_DECLARE_BINDING_SET_, Test)()
    │
    ▼ Step 2: 第一层 - 参数展开（Test 已是字面量）
DJ01_BINDING_SET_CONCAT_IMPL(DJ01_DECLARE_BINDING_SET_, Test)()
    │
    ▼ Step 3: 第二层 - 执行 ## 拼接
DJ01_DECLARE_BINDING_SET_Test()
    │
    ▼ Step 4: 继续展开目标宏
DJ01_BINDING_SET_TEST_VARS()
DJ01_BINDING_SET_TEST_CALLBACKS()
DJ01_BINDING_SET_TEST_INIT_FUNC()      ◀── 自动生成初始化函数
DJ01_BINDING_SET_TEST_CLEANUP_FUNC()   ◀── 自动生成清理函数
    │
    ▼ Step 5: 最终代码
UPROPERTY(BlueprintReadOnly, Category = "Bindings|Tags|Test")
bool bStunned = false;
UPROPERTY(BlueprintReadOnly, Category = "Bindings|Attributes|Test")
float CurrentHealth = 0.0f;

UFUNCTION(BlueprintCallable, Category = "GAS|BindingSet|Test")
void InitBindingSet_Test(UAbilitySystemComponent* InASC) { ... }

UFUNCTION(BlueprintCallable, Category = "GAS|BindingSet|Test")
void CleanupBindingSet_Test(UAbilitySystemComponent* InASC) { ... }
```

### 生成的宏结构

```cpp
// BindingSets.h 中的宏定义

// 辅助宏：二次展开
#define DJ01_BINDING_SET_CONCAT_IMPL(a, b) a##b
#define DJ01_BINDING_SET_CONCAT(a, b) DJ01_BINDING_SET_CONCAT_IMPL(a, b)

// 通用入口宏 - 只需要一个！
#define DJ01_DECLARE_BINDING_SET(Name) \
    DJ01_BINDING_SET_CONCAT(DJ01_DECLARE_BINDING_SET_, Name)()

// 具体 BindingSet 的宏（每个 BindingSet 一组）
#define DJ01_DECLARE_BINDING_SET_Test() \
    DJ01_BINDING_SET_TEST_VARS() \
    DJ01_BINDING_SET_TEST_CALLBACKS() \
    DJ01_BINDING_SET_TEST_INIT_FUNC() \
    DJ01_BINDING_SET_TEST_CLEANUP_FUNC()

// 自动生成的函数宏
#define DJ01_BINDING_SET_TEST_INIT_FUNC() \
    UFUNCTION(BlueprintCallable, Category = "GAS|BindingSet|Test") \
    void InitBindingSet_Test(UAbilitySystemComponent* InASC) \
    { \
        if (!InASC) return; \
        DJ01_BINDING_SET_TEST_REGISTER(InASC) \
        DJ01_BINDING_SET_TEST_INIT_VALUES(InASC) \
    }

#define DJ01_BINDING_SET_TEST_CLEANUP_FUNC() \
    UFUNCTION(BlueprintCallable, Category = "GAS|BindingSet|Test") \
    void CleanupBindingSet_Test(UAbilitySystemComponent* InASC) \
    { \
        DJ01_BINDING_SET_TEST_UNREGISTER(InASC) \
    }
```

## 生成的文件

### 目录结构

```
Source/DJ01/GAS/Generated/BindingSets/
├── BindingSets.h           # 统一入口，包含所有 BindingSet 和通用宏
├── BindingSet_Test.h       # Test BindingSet 的具体实现
├── BindingSet_PlayerHUD.h  # PlayerHUD BindingSet 的具体实现
└── ...
```

### BindingSet_XXX.h 内容

每个 BindingSet 头文件包含 4 个宏：

```cpp
// 1. 变量声明
#define DJ01_BINDING_SET_TEST_VARS() \
    UPROPERTY(BlueprintReadOnly, Category = "Bindings|Tags|Test") \
    bool bStunned = false; \
    UPROPERTY(BlueprintReadOnly, Category = "Bindings|Attributes|Test") \
    float CurrentHealth = 0.0f;

// 2. 回调函数
#define DJ01_BINDING_SET_TEST_CALLBACKS() \
    void OnStunnedTagChanged(const FGameplayTag Tag, int32 NewCount) { \
        bStunned = (NewCount > 0); \
    } \
    void OnHealthChanged(const FOnAttributeChangeData& Data) { \
        CurrentHealth = Data.NewValue; \
    }

// 3. 注册监听
#define DJ01_BINDING_SET_TEST_REGISTER(ASC) \
    ASC->RegisterGameplayTagEvent(...).AddUObject(this, &ThisClass::OnStunnedTagChanged); \
    ASC->GetGameplayAttributeValueChangeDelegate(...).AddUObject(this, &ThisClass::OnHealthChanged);

// 4. 初始化当前值
#define DJ01_BINDING_SET_TEST_INIT_VALUES(ASC) \
    bStunned = ASC->HasMatchingGameplayTag(...); \
    CurrentHealth = ASC->GetNumericAttribute(...);
```

## 配置文件

### BindingSetDefinitions.json

```json
{
    "version": "1.0",
    "binding_sets": [
        {
            "name": "Test",
            "description": "测试用 BindingSet",
            "tag_bindings": [
                {
                    "tag": "Status.Condition.Stunned",
                    "variable_name": "bStunned",
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
                }
            ]
        }
    ]
}
```

## 最佳实践

### 1. BindingSet 命名

- 按用途命名：`PlayerHUD`、`EnemyAI`、`DamageNumbers`
- 避免过于通用的名称：不要用 `Common`、`Default`

### 2. 变量分组

- 一个 BindingSet 应该服务于**一个特定场景**
- 不要把所有绑定都放在一个 BindingSet 中
- 例如：AnimInstance 用 `AnimState`，血条 UI 用 `HealthBar`

### 3. 性能考虑

- BindingSet 使用委托监听，只在值变化时触发
- 避免在 `Tick` 中轮询，直接读取绑定变量即可
- 对于不再需要的绑定，调用 `DJ01_CLEANUP_BINDING_SET` 清理

### 4. 调试技巧

```cpp
// 在初始化后打印绑定的值
DJ01_INIT_BINDING_SET(Test, ASC)
UE_LOG(LogTemp, Log, TEXT("BindingSet initialized: Health=%.1f, bStunned=%d"), 
       CurrentHealth, bStunned);
```

## 常见问题

### Q: 为什么变量没有更新？

1. 确认已调用 `DJ01_INIT_BINDING_SET`
2. 确认 ASC 指针有效
3. 确认属性/Tag 的名称与配置匹配

### Q: 编译错误：未定义的宏？

1. 确认已添加 `#include "DJ01/GAS/Generated/BindingSets/BindingSets.h"`
2. 确认已生成代码（点击工具中的"生成代码"按钮）

### Q: 如何添加新的 BindingSet？

1. 在工具中创建新的 BindingSet
2. 配置 Tag/Attribute 绑定
3. 点击"生成代码"
4. 使用"应用到类"添加到目标类

## 相关文件

| 文件 | 说明 |
|---|---|
| `Tools/AttributeGenerator/bindingset/` | BindingSet 编辑器模块 |
| `Tools/AttributeGenerator/bindingset/generator.py` | 代码生成器 |
| `Tools/AttributeGenerator/bindingset/class_scanner.py` | 类扫描和代码注入 |
| `Source/DJ01/GAS/Config/BindingSetDefinitions.json` | 配置存储 |
| `Source/DJ01/GAS/Generated/BindingSets/` | 生成的头文件 |