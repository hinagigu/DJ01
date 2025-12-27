# UGameplayEffect

**继承自**: `UObject`

UGameplayEffect
    The GameplayEffect definition. This is the data asset defined in the editor that drives everything.
 This is only blueprintable to allow for templating gameplay effects. Gameplay effects should NOT contain blueprint graphs.

## 属性

### DurationPolicy
- **类型**: `EGameplayEffectDurationType`
- **描述**: Policy for the duration of this effect

### DurationMagnitude
- **类型**: `FGameplayEffectModifierMagnitude`
- **描述**: Duration in seconds. 0.0 for instantaneous effects; -1.0 for infinite duration.

### Period
- **类型**: `FScalableFloat`

### bExecutePeriodicEffectOnApplication
- **类型**: `bool`

### PeriodicInhibitionPolicy
- **类型**: `EGameplayEffectPeriodInhibitionRemovedPolicy`

### Modifiers
- **类型**: `TArray<FGameplayModifierInfo>`

### Executions
- **类型**: `TArray<FGameplayEffectExecutionDefinition>`

### OverflowEffects
- **类型**: `TArray<TSubclassOf<UGameplayEffect>>`

### bDenyOverflowApplication
- **类型**: `bool`

### bClearStackOnOverflow
- **类型**: `bool`

### bRequireModifierSuccessToTriggerCues
- **类型**: `bool`

### bSuppressStackingCues
- **类型**: `bool`
- **描述**: If true, GameplayCues will only be triggered for the first instance in a stacking GameplayEffect.

### GameplayCues
- **类型**: `TArray<FGameplayEffectCue>`

### StackingType
- **类型**: `EGameplayEffectStackingType`

### StackLimitCount
- **类型**: `int`

### StackDurationRefreshPolicy
- **类型**: `EGameplayEffectStackingDurationPolicy`

### StackPeriodResetPolicy
- **类型**: `EGameplayEffectStackingPeriodPolicy`

### StackExpirationPolicy
- **类型**: `EGameplayEffectStackingExpirationPolicy`

### GrantedAbilities
- **类型**: `TArray<FGameplayAbilitySpecDef>`

### GEComponents
- **类型**: `TArray<TObjectPtr<UGameplayEffectComponent>>`

