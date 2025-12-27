# UAdditionalEffectsGameplayEffectComponent

**继承自**: `UGameplayEffectComponent`

Add additional Gameplay Effects that attempt to activate under certain conditions (or no conditions)

## 属性

### bOnApplicationCopyDataFromOriginalSpec
- **类型**: `bool`
- **描述**: This will copy all of the data (e.g. SetByCallerMagnitudes) from the GESpec that Applied this GameplayEffect to the new OnApplicationGameplayEffect Specs.
One would think this is normally desirable (and how OnComplete works by default), but we default to false here for backwards compatability.

### OnApplicationGameplayEffects
- **类型**: `TArray<FConditionalGameplayEffect>`
- **描述**: Other gameplay effects that will be applied to the target of this effect if the owning effect applies

### OnCompleteAlways
- **类型**: `TArray<TSubclassOf<UGameplayEffect>>`
- **描述**: Effects to apply when this effect completes, regardless of how it ends

### OnCompleteNormal
- **类型**: `TArray<TSubclassOf<UGameplayEffect>>`
- **描述**: Effects to apply when this effect expires naturally via its duration

### OnCompletePrematurely
- **类型**: `TArray<TSubclassOf<UGameplayEffect>>`
- **描述**: Effects to apply when this effect is made to expire prematurely (e.g. via a forced removal, clear tags, etc.)

