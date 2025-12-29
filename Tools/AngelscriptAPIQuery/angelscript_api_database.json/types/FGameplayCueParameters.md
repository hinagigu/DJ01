# FGameplayCueParameters

Metadata about a gameplay cue execution

## 属性

### NormalizedMagnitude
- **类型**: `float32`
- **描述**: Magnitude of source gameplay effect, normalzed from 0-1. Use this for "how strong is the gameplay effect" (0=min, 1=,max)

### RawMagnitude
- **类型**: `float32`
- **描述**: Raw final magnitude of source gameplay effect. Use this is you need to display numbers or for other informational purposes.

### EffectContext
- **类型**: `FGameplayEffectContextHandle`
- **描述**: Effect context, contains information about hit result, etc

### MatchedTagName
- **类型**: `FGameplayTag`
- **描述**: The tag name that matched this specific gameplay cue handler

### OriginalTag
- **类型**: `FGameplayTag`
- **描述**: The original tag of the gameplay cue

### AggregatedSourceTags
- **类型**: `FGameplayTagContainer`
- **描述**: The aggregated source tags taken from the effect spec

### AggregatedTargetTags
- **类型**: `FGameplayTagContainer`
- **描述**: The aggregated target tags taken from the effect spec

### Location
- **类型**: `FVector`
- **描述**: Location cue took place at

### Normal
- **类型**: `FVector`
- **描述**: Normal of impact that caused cue

### GameplayEffectLevel
- **类型**: `int`
- **描述**: If originating from a GameplayEffect, the level of that GameplayEffect

### AbilityLevel
- **类型**: `int`
- **描述**: If originating from an ability, this will be the level of that ability

### bReplicateLocationWhenUsingMinimalRepProxy
- **类型**: `bool`
- **描述**: If we're using a minimal replication proxy, should we replicate location for this cue

## 方法

### GetEffectCauser
```angelscript
AActor GetEffectCauser()
```

### GetInstigator
```angelscript
AActor GetInstigator()
```

### GetPhysicalMaterial
```angelscript
const UPhysicalMaterial GetPhysicalMaterial()
```

### GetSourceObject
```angelscript
const UObject GetSourceObject()
```

### GetTargetAttachComponent
```angelscript
USceneComponent GetTargetAttachComponent()
```

### SetEffectCauser
```angelscript
void SetEffectCauser(AActor EffectCauser)
```

### SetInstigator
```angelscript
void SetInstigator(AActor Instigator)
```

### SetPhysicalMaterial
```angelscript
void SetPhysicalMaterial(const UPhysicalMaterial PhysicalMaterial)
```

### SetSourceObject
```angelscript
void SetSourceObject(const UObject SourceObject)
```

### SetTargetAttachComponent
```angelscript
void SetTargetAttachComponent(USceneComponent TargetAttachComponent)
```

### opAssign
```angelscript
FGameplayCueParameters& opAssign(FGameplayCueParameters Other)
```

