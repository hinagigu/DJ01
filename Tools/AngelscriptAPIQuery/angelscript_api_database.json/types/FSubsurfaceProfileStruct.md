# FSubsurfaceProfileStruct

struct with all the settings we want in USubsurfaceProfile, separate to make it easer to pass this data around in the engine.

## 属性

### SurfaceAlbedo
- **类型**: `FLinearColor`

### MeanFreePathColor
- **类型**: `FLinearColor`

### MeanFreePathDistance
- **类型**: `float32`

### WorldUnitScale
- **类型**: `float32`

### bEnableBurley
- **类型**: `bool`

### bEnableMeanFreePath
- **类型**: `bool`

### Tint
- **类型**: `FLinearColor`

### BoundaryColorBleed
- **类型**: `FLinearColor`

### ExtinctionScale
- **类型**: `float32`

### NormalScale
- **类型**: `float32`

### ScatteringDistribution
- **类型**: `float32`

### IOR
- **类型**: `float32`

### Roughness0
- **类型**: `float32`

### Roughness1
- **类型**: `float32`

### LobeMix
- **类型**: `float32`

### TransmissionTintColor
- **类型**: `FLinearColor`

## 方法

### opAssign
```angelscript
FSubsurfaceProfileStruct& opAssign(FSubsurfaceProfileStruct Other)
```

