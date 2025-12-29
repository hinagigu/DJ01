# 第4章：FBind 绑定机制

## 核心概念

FBind 是 UE-Angelscript 的绑定注册机制，它利用 **全局变量构造函数** 在程序启动时自动收集所有绑定：

```cpp
// FBind 结构体定义
struct FBind
{
    // 构造函数 - 注册绑定
    FBind(int32 BindOrder, TFunction<void()> Function)
    {
        FAngelscriptBinds::RegisterBinds(BindOrder, Function);
    }
    
    FBind(EOrder BindOrder, TFunction<void()> Function)
    {
        FAngelscriptBinds::RegisterBinds((int32)BindOrder, Function);
    }
    
    FBind(TFunction<void()> Function)
    {
        FAngelscriptBinds::RegisterBinds(0, Function);
    }
};

// 绑定顺序枚举
enum class EOrder : int32
{
    Early  = -100,  // 早期：声明类型
    Normal = 0,     // 普通：一般绑定
    Late   = 100,   // 晚期：绑定成员/函数
};
```

## 绑定存储与执行

```cpp
// 绑定函数信息
struct FBindFunction
{
    int32 BindOrder;           // 执行顺序
    TFunction<void()> Function; // 绑定逻辑
    
    bool operator<(const FBindFunction& Other) const
    {
        return BindOrder < Other.BindOrder;
    }
};

// 全局绑定数组（单例）
static TArray<FBindFunction>& GetBindArray()
{
    static TArray<FBindFunction> BindArray;
    return BindArray;
}

// 注册绑定
void FAngelscriptBinds::RegisterBinds(int32 BindOrder, TFunction<void()> Function)
{
    GetBindArray().Add({BindOrder, Function});
}

// 执行所有绑定
void FAngelscriptBinds::CallBinds()
{
    // 1. 排序
    GetBindArray().Sort();
    
    // 2. 按顺序执行
    for (auto& Bind : GetBindArray())
    {
        Bind.Function();
    }
}
```

## 绑定顺序详解

```
时间线 ────────────────────────────────────────────────────►

Early (-100)          Normal (0)           Late (100)
    │                     │                     │
    │ 声明类型            │ 一般绑定           │ 成员/函数
    │                     │                     │
    ▼                     ▼                     ▼
┌─────────┐         ┌─────────┐         ┌─────────┐
│ UObject │         │  工具   │         │ 方法    │
│ UStruct │         │  函数   │         │ 属性    │
│ UEnum   │         │         │         │ 继承    │
└─────────┘         └─────────┘         └─────────┘

为什么需要分阶段？
- Early: 必须先声明类型，AS 才能识别
- Late: 成员函数可能依赖其他类型（参数、返回值）
         必须等那些类型先声明
```

## 绑定示例

```cpp
// 示例 1: 早期声明类型
AS_FORCE_LINK const FAngelscriptBinds::FBind Bind_FVector_Declaration(
    FAngelscriptBinds::EOrder::Early, 
    []
{
    FBindFlags Flags;
    auto FVector_ = FAngelscriptBinds::ValueClass<FVector>("FVector", Flags);
    
    // 注册类型信息
    auto VectorType = MakeShared<FVectorType>();
    FAngelscriptType::Register(VectorType);
});

// 示例 2: 晚期绑定成员
AS_FORCE_LINK const FAngelscriptBinds::FBind Bind_FVector(
    FAngelscriptBinds::EOrder::Late, 
    []
{
    auto FVector_ = FAngelscriptBinds::ExistingClass("FVector");
    
    // 绑定属性
    FVector_.Property("float64 X", &FVector::X);
    FVector_.Property("float64 Y", &FVector::Y);
    FVector_.Property("float64 Z", &FVector::Z);
    
    // 绑定方法
    FVector_.Method("float64 Size() const", METHOD_TRIVIAL(FVector, Size));
    FVector_.Method("FVector GetSafeNormal() const", 
                    METHOD_TRIVIAL(FVector, GetSafeNormal));
});
```

## AS_FORCE_LINK 宏

```cpp
// 确保绑定对象不会被链接器优化掉
#define AS_FORCE_LINK __pragma(comment(linker, "/include:" ...))
```

这个宏防止未被直接引用的全局变量被链接器优化移除。

---

**上一章**: [03_类型系统.md](./03_类型系统.md)  
**下一章**: [05_UObject绑定.md](./05_UObject绑定.md) - 了解 UClass 的完整绑定流程