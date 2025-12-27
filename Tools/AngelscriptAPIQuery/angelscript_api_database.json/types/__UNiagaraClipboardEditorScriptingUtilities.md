# __UNiagaraClipboardEditorScriptingUtilities

## 方法

### CreateBoolLocalValueInput
```angelscript
UNiagaraClipboardFunctionInput CreateBoolLocalValueInput(UObject InOuter, FName InInputName, bool bInHasEditCondition, bool bInEditConditionValue, bool InBoolValue)
```

### CreateDataValueInput
```angelscript
UNiagaraClipboardFunctionInput CreateDataValueInput(UObject InOuter, FName InInputName, bool bInHasEditCondition, bool bInEditConditionValue, UNiagaraDataInterface InDataValue)
```

### CreateDynamicValueInput
```angelscript
UNiagaraClipboardFunctionInput CreateDynamicValueInput(UObject InOuter, FName InInputName, FName InInputTypeName, bool bInHasEditCondition, bool bInEditConditionValue, FString InDynamicValueName, UNiagaraScript InDynamicValue)
```

### CreateEnumLocalValueInput
```angelscript
UNiagaraClipboardFunctionInput CreateEnumLocalValueInput(UObject InOuter, FName InInputName, bool bInHasEditCondition, bool bInEditCoditionValue, UUserDefinedEnum InEnumType, int InEnumValue)
```

### CreateExpressionValueInput
```angelscript
UNiagaraClipboardFunctionInput CreateExpressionValueInput(UObject InOuter, FName InInputName, FName InInputTypeName, bool bInHasEditCondition, bool bInEditConditionValue, FString InExpressionValue)
```

### CreateFloatLocalValueInput
```angelscript
UNiagaraClipboardFunctionInput CreateFloatLocalValueInput(UObject InOuter, FName InInputName, bool bInHasEditCondition, bool bInEditConditionValue, float32 InLocalValue)
```

### CreateIntLocalValueInput
```angelscript
UNiagaraClipboardFunctionInput CreateIntLocalValueInput(UObject InOuter, FName InInputName, bool bInHasEditCondition, bool bInEditConditionValue, int InLocalValue)
```

### CreateLinkedValueInput
```angelscript
UNiagaraClipboardFunctionInput CreateLinkedValueInput(UObject InOuter, FName InInputName, FName InInputTypeName, bool bInHasEditCondition, bool bInEditConditionValue, FName InLinkedValue)
```

### CreateStructLocalValueInput
```angelscript
UNiagaraClipboardFunctionInput CreateStructLocalValueInput(UObject InOuter, FName InInputName, bool bInHasEditCondition, bool bInEditConditionValue, UUserDefinedStruct InStructValue)
```

### CreateVec2LocalValueInput
```angelscript
UNiagaraClipboardFunctionInput CreateVec2LocalValueInput(UObject InOuter, FName InInputName, bool bInHasEditCondition, bool bInEditConditionValue, FVector2D InVec2Value)
```

### CreateVec3LocalValueInput
```angelscript
UNiagaraClipboardFunctionInput CreateVec3LocalValueInput(UObject InOuter, FName InInputName, bool bInHasEditCondition, bool bInEditConditionValue, FVector InVec3Value)
```

### GetTypeName
```angelscript
FName GetTypeName(const UNiagaraClipboardFunctionInput InInput)
```

### TryGetInputByName
```angelscript
void TryGetInputByName(TArray<UNiagaraClipboardFunctionInput> InInputs, FName InInputName, bool& bOutSucceeded, UNiagaraClipboardFunctionInput& OutInput)
```

### TryGetLocalValueAsFloat
```angelscript
void TryGetLocalValueAsFloat(const UNiagaraClipboardFunctionInput InInput, bool& bOutSucceeded, float32& OutValue)
```

### TryGetLocalValueAsInt
```angelscript
void TryGetLocalValueAsInt(const UNiagaraClipboardFunctionInput InInput, bool& bOutSucceeded, int& OutValue)
```

### TrySetLocalValueAsInt
```angelscript
void TrySetLocalValueAsInt(UNiagaraClipboardFunctionInput InInput, bool& bOutSucceeded, int InValue, bool bLooseTyping)
```

### StaticClass
```angelscript
UClass StaticClass()
```

