# FMovieSceneGameplayCueKey

## 属性

### Cue
- **类型**: `FGameplayCueTag`

### Location
- **类型**: `FVector`
- **描述**: Location cue took place at - relative to the attached component if applicable

### Normal
- **类型**: `FVector`
- **描述**: Normal of impact that caused cue

### AttachSocketName
- **类型**: `FName`
- **描述**: When attached to a skeletal mesh component, specifies a socket to trigger the cue at

### NormalizedMagnitude
- **类型**: `float32`
- **描述**: Magnitude of source gameplay effect, normalzed from 0-1. Use this for "how strong is the gameplay effect" (0=min, 1=,max)

### Instigator
- **类型**: `FMovieSceneObjectBindingID`
- **描述**: Instigator actor, the actor that owns the ability system component.

### EffectCauser
- **类型**: `FMovieSceneObjectBindingID`
- **描述**: The physical actor that actually did the damage, can be a weapon or projectile

### PhysicalMaterial
- **类型**: `const UPhysicalMaterial`
- **描述**: PhysMat of the hit, if there was a hit.

### GameplayEffectLevel
- **类型**: `int`
- **描述**: The level of that GameplayEffect

### AbilityLevel
- **类型**: `int`
- **描述**: If originating from an ability, this will be the level of that ability

### bAttachToBinding
- **类型**: `bool`
- **描述**: Attach the gameplay cue to the track's bound object in sequencer

## 方法

### opAssign
```angelscript
FMovieSceneGameplayCueKey& opAssign(FMovieSceneGameplayCueKey Other)
```

