# FAngelscriptAttributeChangedData

The RegisterAttributeChangedCallback functions use this as their parameter, not the wrapped one!
Since no type checking occurs for delegates, this still works as the base offset of the wrapper and the wrapped are the same.

## 方法

### GetEffectSpec
```angelscript
FGameplayEffectSpec GetEffectSpec(bool& bIsValid)
```

### GetGameplayAttribute
```angelscript
FGameplayAttribute GetGameplayAttribute()
```

### GetGameplayModifierEvaluatedData
```angelscript
FGameplayModifierEvaluatedData GetGameplayModifierEvaluatedData(bool& bIsValid)
```

### GetNewValue
```angelscript
float32 GetNewValue()
```

### GetOldValue
```angelscript
float32 GetOldValue()
```

### GetTargetAbilitySystemComponent
```angelscript
UAbilitySystemComponent GetTargetAbilitySystemComponent()
```

### opAssign
```angelscript
FAngelscriptAttributeChangedData& opAssign(FAngelscriptAttributeChangedData Other)
```

