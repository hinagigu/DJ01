# __UAngelscriptGameplayEffectUtils

## 方法

### CaptureGameplayAttribute
```angelscript
FGameplayEffectAttributeCaptureDefinition CaptureGameplayAttribute(UStruct AttributeSetType, FName AttributeName, EGameplayEffectAttributeCaptureSource InSource, bool bIsSnapshot)
```

### MakeGameplayEffectExecutionScopedModifierInfo
```angelscript
FGameplayEffectExecutionScopedModifierInfo MakeGameplayEffectExecutionScopedModifierInfo(FGameplayEffectAttributeCaptureDefinition InCaptureDef)
```

### MakeGameplayModifierEvaluationData
```angelscript
FGameplayModifierEvaluatedData MakeGameplayModifierEvaluationData(FGameplayAttribute InAttribute, EGameplayModOp InModOp, float32 InMagnitude)
```

### StaticClass
```angelscript
UClass StaticClass()
```

