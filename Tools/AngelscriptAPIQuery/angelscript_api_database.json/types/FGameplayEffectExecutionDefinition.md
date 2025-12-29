# FGameplayEffectExecutionDefinition

Struct representing the definition of a custom execution for a gameplay effect.
Custom executions run special logic from an outside class each time the gameplay effect executes.

## 方法

### AddCalculationModifier
```angelscript
void AddCalculationModifier(FGameplayEffectExecutionScopedModifierInfo CalculationModifier)
```

### AddConditionalGameplayEffect
```angelscript
void AddConditionalGameplayEffect(FConditionalGameplayEffect ConditionalGameplayEffect)
```

### GetCalculationClass
```angelscript
TSubclassOf<UGameplayEffectExecutionCalculation>& GetCalculationClass()
```

### GetCalculationModifiers
```angelscript
TArray<FGameplayEffectExecutionScopedModifierInfo>& GetCalculationModifiers()
```

### GetConditionalGameplayEffects
```angelscript
TArray<FConditionalGameplayEffect>& GetConditionalGameplayEffects()
```

### GetPassedInTags
```angelscript
FGameplayTagContainer& GetPassedInTags()
```

### SetCalculationClass
```angelscript
void SetCalculationClass(TSubclassOf<UGameplayEffectExecutionCalculation> CalculationClass)
```

### SetCalculationModifiers
```angelscript
void SetCalculationModifiers(TArray<FGameplayEffectExecutionScopedModifierInfo> CalculationModifiers)
```

### SetConditionalGameplayEffects
```angelscript
void SetConditionalGameplayEffects(TArray<FConditionalGameplayEffect> ConditionalGameplayEffects)
```

### SetPassedInTags
```angelscript
void SetPassedInTags(FGameplayTagContainer PassedInTags)
```

### opAssign
```angelscript
FGameplayEffectExecutionDefinition& opAssign(FGameplayEffectExecutionDefinition Other)
```

