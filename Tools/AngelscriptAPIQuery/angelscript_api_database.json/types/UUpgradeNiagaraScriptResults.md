# UUpgradeNiagaraScriptResults

**继承自**: `UObject`

Wrapper class for passing results back from the version upgrade python script.

## 属性

### bCancelledByPythonError
- **类型**: `bool`
- **描述**: Whether the converter process was cancelled due to an unrecoverable error in the python script process.

### OldInputs
- **类型**: `TArray<TObjectPtr<UNiagaraPythonScriptModuleInput>>`

### NewInputs
- **类型**: `TArray<TObjectPtr<UNiagaraPythonScriptModuleInput>>`

## 方法

### GetOldInput
```angelscript
UNiagaraPythonScriptModuleInput GetOldInput(FString InputName)
```

### ResetToDefault
```angelscript
void ResetToDefault(FString InputName)
```

### SetBoolInput
```angelscript
void SetBoolInput(FString InputName, bool Value)
```

### SetColorInput
```angelscript
void SetColorInput(FString InputName, FLinearColor Value)
```

### SetEnumInput
```angelscript
void SetEnumInput(FString InputName, FString Value)
```

### SetFloatInput
```angelscript
void SetFloatInput(FString InputName, float32 Value)
```

### SetIntInput
```angelscript
void SetIntInput(FString InputName, int Value)
```

### SetLinkedInput
```angelscript
void SetLinkedInput(FString InputName, FString Value)
```

### SetNewInput
```angelscript
void SetNewInput(FString InputName, UNiagaraPythonScriptModuleInput Value)
```

### SetQuatInput
```angelscript
void SetQuatInput(FString InputName, FQuat Value)
```

### SetVec2Input
```angelscript
void SetVec2Input(FString InputName, FVector2D Value)
```

### SetVec3Input
```angelscript
void SetVec3Input(FString InputName, FVector Value)
```

### SetVec4Input
```angelscript
void SetVec4Input(FString InputName, FVector4 Value)
```

