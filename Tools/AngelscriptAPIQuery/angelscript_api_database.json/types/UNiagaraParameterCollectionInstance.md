# UNiagaraParameterCollectionInstance

**继承自**: `UObject`

## 属性

### Collection
- **类型**: `UNiagaraParameterCollection`
- **描述**: TODO: Abstract to some interface to allow a hierarchy like UMaterialInstance?

## 方法

### GetBoolParameter
```angelscript
bool GetBoolParameter(FString InVariableName)
```
Accessors from Blueprint. For now just exposing common types but ideally we can expose any somehow in future.

### GetColorParameter
```angelscript
FLinearColor GetColorParameter(FString InVariableName)
```

### GetFloatParameter
```angelscript
float32 GetFloatParameter(FString InVariableName)
```

### GetIntParameter
```angelscript
int GetIntParameter(FString InVariableName)
```

### GetQuatParameter
```angelscript
FQuat GetQuatParameter(FString InVariableName)
```

### GetVector2DParameter
```angelscript
FVector2D GetVector2DParameter(FString InVariableName)
```

### GetVector4Parameter
```angelscript
FVector4 GetVector4Parameter(FString InVariableName)
```

### GetVectorParameter
```angelscript
FVector GetVectorParameter(FString InVariableName)
```

### SetBoolParameter
```angelscript
void SetBoolParameter(FString InVariableName, bool InValue)
```

### SetColorParameter
```angelscript
void SetColorParameter(FString InVariableName, FLinearColor InValue)
```

### SetFloatParameter
```angelscript
void SetFloatParameter(FString InVariableName, float32 InValue)
```

### SetIntParameter
```angelscript
void SetIntParameter(FString InVariableName, int InValue)
```

### SetQuatParameter
```angelscript
void SetQuatParameter(FString InVariableName, FQuat InValue)
```

### SetVector2DParameter
```angelscript
void SetVector2DParameter(FString InVariableName, FVector2D InValue)
```

### SetVector4Parameter
```angelscript
void SetVector4Parameter(FString InVariableName, FVector4 InValue)
```
TODO[mg]: add position setter for LWC

### SetVectorParameter
```angelscript
void SetVectorParameter(FString InVariableName, FVector InValue)
```

