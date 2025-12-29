# FInstancedStruct

FInstancedStruct works similarly as instanced UObject* property but is USTRUCTs.

Example:

    UPROPERTY(EditAnywhere, Category = Foo, meta = (BaseStruct = "/Script/ModuleName.TestStructBase"))
    FInstancedStruct Test;

    UPROPERTY(EditAnywhere, Category = Foo, meta = (BaseStruct = "/Script/ModuleName.TestStructBase"))
    TArray<FInstancedStruct> TestArray;

## 方法

### opEquals
```angelscript
bool opEquals(FInstancedStruct Other)
```
Comparison operators. Deep compares the struct instance when identical.

### InitializeAs
```angelscript
void InitializeAs(? Struct)
```
Initializes from struct type and emplace construct.

### Get
```angelscript
void Get(? Struct)
```
Returns a copy of the struct. This getter assumes that all data is valid.

### Reset
```angelscript
void Reset()
```

### IsValid
```angelscript
bool IsValid()
```
Returns True if the struct is valid.

### opAssign
```angelscript
FInstancedStruct& opAssign(FInstancedStruct Other)
```

