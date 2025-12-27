# FGameplayEffectCue

FGameplayEffectCue
    This is a cosmetic cue that can be tied to a UGameplayEffect.
 This is essentially a GameplayTag + a Min/Max level range that is used to map the level of a GameplayEffect to a normalized value used by the GameplayCue system.

## 属性

### MagnitudeAttribute
- **类型**: `FGameplayAttribute`
- **描述**: The attribute to use as the source for cue magnitude. If none use level

### MinLevel
- **类型**: `float32`
- **描述**: The minimum level that this Cue supports

### MaxLevel
- **类型**: `float32`
- **描述**: The maximum level that this Cue supports

### GameplayCueTags
- **类型**: `FGameplayTagContainer`
- **描述**: Tags passed to the gameplay cue handler when this cue is activated

## 方法

### opAssign
```angelscript
FGameplayEffectCue& opAssign(FGameplayEffectCue Other)
```

