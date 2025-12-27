# FGameplayModifierInfo

FGameplayModifierInfo
    Tells us "Who/What we" modify
    Does not tell us how exactly

## 属性

### Attribute
- **类型**: `FGameplayAttribute`
- **描述**: The Attribute we modify or the GE we modify modifies.

### ModifierOp
- **类型**: `EGameplayModOp`
- **描述**: The numeric operation of this modifier: Override, Add, Multiply, etc

### ModifierMagnitude
- **类型**: `FGameplayEffectModifierMagnitude`
- **描述**: Magnitude of the modifier

### EvaluationChannelSettings
- **类型**: `FGameplayModEvaluationChannelSettings`
- **描述**: Evaluation channel settings of the modifier

### SourceTags
- **类型**: `FGameplayTagRequirements`

### TargetTags
- **类型**: `FGameplayTagRequirements`

## 方法

### opAssign
```angelscript
FGameplayModifierInfo& opAssign(FGameplayModifierInfo Other)
```

