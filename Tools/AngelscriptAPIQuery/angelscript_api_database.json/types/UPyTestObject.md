# UPyTestObject

**继承自**: `UObject`

Object to allow testing of the various UObject features that are exposed to Python wrapped types.

## 属性

### Bool
- **类型**: `bool`

### Int
- **类型**: `int`

### Float
- **类型**: `float32`

### Enum
- **类型**: `EPyTestEnum`

### String
- **类型**: `FString`

### Text
- **类型**: `FText`

### StringArray
- **类型**: `TArray<FString>`

### StringSet
- **类型**: `TSet<FString>`

### StringIntMap
- **类型**: `TMap<FString,int>`

### Delegate
- **类型**: `FPyTestDelegate`

### MulticastDelegate
- **类型**: `FPyTestMulticastDelegate`

### Struct
- **类型**: `FPyTestStruct`

### StructArray
- **类型**: `TArray<FPyTestStruct>`

### ChildStruct
- **类型**: `FPyTestChildStruct`

### BoolInstanceOnly
- **类型**: `bool`

### BoolDefaultsOnly
- **类型**: `bool`

### Name
- **类型**: `FName`

## 方法

### CallFuncBlueprintImplementable
```angelscript
int CallFuncBlueprintImplementable(int InValue)
```

### CallFuncBlueprintImplementablePackedGetter
```angelscript
bool CallFuncBlueprintImplementablePackedGetter(int& OutValue)
```

### CallFuncBlueprintNative
```angelscript
int CallFuncBlueprintNative(int InValue)
```

### CallFuncBlueprintNativeRef
```angelscript
void CallFuncBlueprintNativeRef(FPyTestStruct& InOutStruct)
```

### DelegatePropertyCallback
```angelscript
int DelegatePropertyCallback(int InValue)
```
UHT couldn't parse any default value for the FieldPath.

### FuncBlueprintImplementable
```angelscript
int FuncBlueprintImplementable(int InValue)
```

### FuncBlueprintImplementablePackedGetter
```angelscript
bool FuncBlueprintImplementablePackedGetter(int& OutValue)
```

### FuncBlueprintNative
```angelscript
int FuncBlueprintNative(int InValue)
```

### FuncBlueprintNativeRef
```angelscript
void FuncBlueprintNativeRef(FPyTestStruct& InOutStruct)
```

### FuncTakingPyTestChildStruct
```angelscript
void FuncTakingPyTestChildStruct(FPyTestChildStruct InStruct)
```

### FuncTakingPyTestDelegate
```angelscript
int FuncTakingPyTestDelegate(FPyTestDelegate InDelegate, int InValue)
```

### FuncTakingPyTestStruct
```angelscript
void FuncTakingPyTestStruct(FPyTestStruct InStruct)
```

### FuncTakingPyTestStructDefault
```angelscript
void FuncTakingPyTestStructDefault(FPyTestStruct InStruct)
```

### MulticastDelegatePropertyCallback
```angelscript
void MulticastDelegatePropertyCallback(FString InStr)
```

