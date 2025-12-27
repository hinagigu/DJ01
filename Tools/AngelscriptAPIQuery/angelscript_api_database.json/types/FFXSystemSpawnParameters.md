# FFXSystemSpawnParameters

Parameters controlling the spawning behavior of FX systems via the SpawnSystemAtLocation and SpawnSystemAttached.

## 属性

### WorldContextObject
- **类型**: `const UObject`

### SystemTemplate
- **类型**: `UFXSystemAsset`

### Location
- **类型**: `FVector`

### Rotation
- **类型**: `FRotator`

### Scale
- **类型**: `FVector`

### AttachToComponent
- **类型**: `USceneComponent`

### AttachPointName
- **类型**: `FName`

### LocationType
- **类型**: `EAttachLocation`

### bAutoDestroy
- **类型**: `bool`

### bAutoActivate
- **类型**: `bool`

### PoolingMethod
- **类型**: `EPSCPoolMethod`

### bPreCullCheck
- **类型**: `bool`

### bIsPlayerEffect
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FFXSystemSpawnParameters& opAssign(FFXSystemSpawnParameters Other)
```

