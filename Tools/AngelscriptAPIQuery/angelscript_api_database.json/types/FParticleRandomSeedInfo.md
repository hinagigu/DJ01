# FParticleRandomSeedInfo

## 属性

### ParameterName
- **类型**: `FName`
- **描述**: The name to expose to the placed instances for setting this seed

### RandomSeeds
- **类型**: `TArray<int>`
- **描述**: The random seed values to utilize for the module.
More than 1 means the instance will randomly select one.

### bGetSeedFromInstance
- **类型**: `bool`

### bInstanceSeedIsIndex
- **类型**: `bool`

### bResetSeedOnEmitterLooping
- **类型**: `bool`

### bRandomlySelectSeedArray
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FParticleRandomSeedInfo& opAssign(FParticleRandomSeedInfo Other)
```

