# FComboGraphCueContainerDefinition

Struct defining a list of gameplay tags, and optional source object to pass arbitrary data to GameplayCues (in GameplayCueParameters' SourceObject)

## 属性

### GameplayCueTags
- **类型**: `FGameplayTagContainer`

### CueSourceObjectType
- **类型**: `EComboGraphCueSourceObjectType`
- **描述**: Specify here which type of SourceObject you'd like to pass down to GameplayCues.

Allows to pass arbitrary data down to GameplayCues, made available in GameplayCueParameters' Effect Context.

Example usage: Pass down a Niagara Emitter or Cascade Particle System, or SoundCues.

### NiagaraSystem
- **类型**: `TSoftObjectPtr<UNiagaraSystem>`

### CascadeSystem
- **类型**: `TSoftObjectPtr<UParticleSystem>`

### SoundEffect
- **类型**: `TSoftObjectPtr<USoundBase>`

## 方法

### opAssign
```angelscript
FComboGraphCueContainerDefinition& opAssign(FComboGraphCueContainerDefinition Other)
```

