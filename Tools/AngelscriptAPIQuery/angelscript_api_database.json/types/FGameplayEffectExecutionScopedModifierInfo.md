# FGameplayEffectExecutionScopedModifierInfo

Struct representing modifier info used exclusively for "scoped" executions that happen instantaneously. These are
folded into a calculation only for the extent of the calculation and never permanently added to an aggregator.

## 属性

### ModifierOp
- **类型**: `EGameplayModOp`
- **描述**: Modifier operation to perform

### ModifierMagnitude
- **类型**: `FGameplayEffectModifierMagnitude`
- **描述**: Magnitude of the scoped modifier

### EvaluationChannelSettings
- **类型**: `FGameplayModEvaluationChannelSettings`
- **描述**: Evaluation channel settings of the scoped modifier

### SourceTags
- **类型**: `FGameplayTagRequirements`
- **描述**: Source tag requirements for the modifier to apply

### TargetTags
- **类型**: `FGameplayTagRequirements`
- **描述**: Target tag requirements for the modifier to apply

## 方法

### opAssign
```angelscript
FGameplayEffectExecutionScopedModifierInfo& opAssign(FGameplayEffectExecutionScopedModifierInfo Other)
```

