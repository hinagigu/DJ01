# 第6章：UScriptStruct 绑定流程

## 与 UObject 的关键区别

| 特性 | UObject | UScriptStruct |
|------|---------|---------------|
| 内存分配 | 堆（GC 管理） | 栈或内嵌 |
| AS 类型 | 引用类型 | **值类型** |
| AS 标志 | `asOBJ_REF` | `asOBJ_VALUE` |
| 句柄语法 | `AActor@` | 无（直接使用） |
| 生命周期 | UE GC | 作用域自动管理 |

## 绑定实现

```cpp
AS_FORCE_LINK const FAngelscriptBinds::FBind Bind_StructDeclarations(
    (int32)FAngelscriptBinds::EOrder::Early + 1, 
    []
{
    for (UScriptStruct* Struct : TObjectRange<UScriptStruct>())
    {
        if (!ShouldBindEngineType(Struct))
            continue;
        
        FString TypeName = Struct->GetStructCPPName();
        
        // 设置绑定标志
        FBindFlags BindFlags;
        if (Struct->StructFlags & STRUCT_IsPlainOldData)
            BindFlags.ExtraFlags |= asOBJ_POD;  // POD 类型优化
        
        BindStructType(TypeName, Struct, BindFlags);
    }
    
    BindStructTypeLookups();
});

static void BindStructType(const FString& TypeName, UScriptStruct* Struct, 
                           FBindFlags& BindFlags)
{
    // 关键：使用 ValueClass 而非 ReferenceClass
    auto Binds = FAngelscriptBinds::ValueClass(TypeName, Struct, BindFlags);
    
    // 注册类型信息
    auto Type = MakeShared<FUStructType>(Struct, TypeName);
    Type->ScriptTypeInfo = Binds.GetTypeInfo();
    Type->ScriptTypeInfo->SetUserData(Struct);
    FAngelscriptType::Register(Type);
}
```

## ValueClass vs ReferenceClass

```cpp
// 值类型绑定
static FAngelscriptBinds ValueClass(FBindString Name, UScriptStruct* StructType, 
                                    FBindFlags Flags)
{
    int Size;
    auto* Ops = StructType->GetCppStructOps();
    if (Ops != nullptr)
        Size = Ops->GetSize();
    else
        Size = StructType->GetPropertiesSize();
    
    if (Flags.Alignment == -1)
        Flags.Alignment = StructType->GetMinAlignment();
    
    return ValueClass(Name, Flags, Size);
}

static FAngelscriptBinds ValueClass(FBindString Name, FBindFlags Flags, int Size)
{
    int32 ASFlags = asOBJ_VALUE |       // 值类型
                    asOBJ_APP_CLASS;    // C++ 定义的类
    
    if (Flags.ExtraFlags & asOBJ_POD)
    {
        // POD 类型可以简单复制
        ASFlags |= asOBJ_POD;
    }
    
    return FAngelscriptBinds(Name, ASFlags | Flags.ExtraFlags, Size);
}
```

## 值类型 vs 引用类型在 AS 中的使用

```angelscript
// 值类型（FVector）
FVector Position;           // 栈上分配，无需 @
Position.X = 100.0f;
Position = FVector(1, 2, 3); // 直接赋值（复制）

FVector Other = Position;   // 复制语义
Other.X = 200.0f;           // 不影响 Position

// 引用类型（AActor）
AActor Actor;               // 实际上是 AActor@，初始为 nullptr
Actor = SpawnActor(...);    // 赋值为实际对象

AActor Other = Actor;       // 引用同一对象
Other.SetActorLocation(...); // 影响 Actor
```

## POD 类型优化

POD (Plain Old Data) 类型可以使用简单的内存复制，无需调用构造/析构函数：

```cpp
// 检查是否为 POD
if (Struct->StructFlags & STRUCT_IsPlainOldData)
{
    BindFlags.ExtraFlags |= asOBJ_POD;
}

// POD 类型的好处：
// - 可以用 memcpy 复制
// - 不需要调用构造/析构函数
// - 更高的性能
```

---

**上一章**: [05_UObject绑定.md](./05_UObject绑定.md)  
**下一章**: [07_手工绑定.md](./07_手工绑定.md) - 学习手动绑定自定义类型