# FSourceEffectMotionFilterSettings

FSourceEffectMotionFilterSettings
This is the source effect's setting struct.

## 属性

### MotionFilterTopology
- **类型**: `ESourceEffectMotionFilterTopology`

### MotionFilterMix
- **类型**: `float32`

### FilterASettings
- **类型**: `FSourceEffectIndividualFilterSettings`

### FilterBSettings
- **类型**: `FSourceEffectIndividualFilterSettings`

### ModulationMappings
- **类型**: `TMap<ESourceEffectMotionFilterModDestination,FSourceEffectMotionFilterModulationSettings>`

### DryVolumeDb
- **类型**: `float32`

## 方法

### opAssign
```angelscript
FSourceEffectMotionFilterSettings& opAssign(FSourceEffectMotionFilterSettings Other)
```

