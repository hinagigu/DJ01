# FGameplayEffectExecutionDefinition

Struct representing the definition of a custom execution for a gameplay effect.
Custom executions run special logic from an outside class each time the gameplay effect executes.

## 属性

### CalculationClass
- **类型**: `TSubclassOf<UGameplayEffectExecutionCalculation>`
- **描述**: Custom execution calculation class to run when the gameplay effect executes

### PassedInTags
- **类型**: `FGameplayTagContainer`
- **描述**: These tags are passed into the execution as is, and may be used to do conditional logic

### CalculationModifiers
- **类型**: `TArray<FGameplayEffectExecutionScopedModifierInfo>`
- **描述**: Modifiers that are applied "in place" during the execution calculation

### ConditionalGameplayEffects
- **类型**: `TArray<FConditionalGameplayEffect>`
- **描述**: Other Gameplay Effects that will be applied to the target of this execution if the execution is successful. Note if no execution class is selected, these will always apply.

## 方法

### opAssign
```angelscript
FGameplayEffectExecutionDefinition& opAssign(FGameplayEffectExecutionDefinition Other)
```

