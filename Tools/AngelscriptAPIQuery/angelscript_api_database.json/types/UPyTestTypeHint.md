# UPyTestTypeHint

**继承自**: `UObject`

Used to verify if the generated Python stub is correctly type-hinted (if type hint is enabled). The stub is generated
* in the project intermediate folder when the Python developer mode is enabled (Editor preferences). The type hints can
* be checked in the stub itself or PythonScriptPlugin/Content/Python/test_type_hints.py can be loaded in a Python IDE that
* supports type checking and look at the code to verify that there is not problems with the types.

## 属性

### BoolProp
- **类型**: `bool`

### IntProp
- **类型**: `int`

### FloatProp
- **类型**: `float32`

### EnumProp
- **类型**: `EPyTestEnum`

### StringProp
- **类型**: `FString`

### NameProp
- **类型**: `FName`

### TextProp
- **类型**: `FText`

### StructProp
- **类型**: `FPyTestStruct`

### ObjectProp
- **类型**: `UPyTestObject`

### StrArrayProp
- **类型**: `TArray<FString>`

### NameArrayProp
- **类型**: `TArray<FName>`

### TextArrayProp
- **类型**: `TArray<FText>`

### ObjectArrayProp
- **类型**: `TArray<TObjectPtr<UObject>>`

### SetProp
- **类型**: `TSet<FString>`

### MapProp
- **类型**: `TMap<int,FString>`

### DelegateProp
- **类型**: `FPyTestDelegate`

### MulticastDelegateProp
- **类型**: `FPyTestMulticastDelegate`

### SlateTickDelegate
- **类型**: `FPyTestSlateTickDelegate`

## 方法

### CheckArrayTypeHints
```angelscript
TArray<FText> CheckArrayTypeHints(TArray<FString> Param1, TArray<FName> Param2, TArray<FText> Param3, TArray<UObject> Param4)
```

### CheckBoolTypeHints
```angelscript
bool CheckBoolTypeHints(bool bParam1, bool bParam2, bool bParam3)
```
Check type hinted methods.

### CheckDelegateTypeHints
```angelscript
FPyTestDelegate& CheckDelegateTypeHints(FPyTestDelegate Param1)
```

### CheckEnumTypeHints
```angelscript
EPyTestEnum CheckEnumTypeHints(EPyTestEnum Param1, EPyTestEnum Param2)
```

### CheckFloatTypeHints
```angelscript
float CheckFloatTypeHints(float32 Param1, float Param2, float32 Param3, float Param4)
```

### CheckIntegerTypeHints
```angelscript
int CheckIntegerTypeHints(uint8 Param1, int Param2, int64 Param3)
```

### CheckMapTypeHints
```angelscript
TMap<FString,UObject> CheckMapTypeHints(TMap<int,FString> Param1, TMap<int,FName> Param2, TMap<int,FText> Param3, TMap<int,UObject> Param4)
```

### CheckNameTypeHints
```angelscript
FName CheckNameTypeHints(FName Param1, FName Param2)
```

### CheckObjectTypeHints
```angelscript
UPyTestObject CheckObjectTypeHints(const UPyTestObject Param1, const UPyTestObject Param4)
```

### CheckSetTypeHints
```angelscript
TSet<FName> CheckSetTypeHints(TSet<FString> Param1, TSet<FName> Param2, TSet<UObject> Param3)
```

### CheckStringTypeHints
```angelscript
FString CheckStringTypeHints(FString Param1, FString Param2)
```

### CheckStructTypeHints
```angelscript
FPyTestStruct CheckStructTypeHints(FPyTestStruct Param1, FPyTestStruct Param2)
```

### CheckTextTypeHints
```angelscript
FText CheckTextTypeHints(FText Param1, FText Param2)
```

