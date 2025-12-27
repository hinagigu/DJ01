# FGrassVariety

## 属性

### GrassMesh
- **类型**: `UStaticMesh`

### OverrideMaterials
- **类型**: `TArray<TObjectPtr<UMaterialInterface>>`

### GrassDensity
- **类型**: `FPerPlatformFloat`

### GrassDensityQuality
- **类型**: `FPerQualityLevelFloat`

### bUseGrid
- **类型**: `bool`

### PlacementJitter
- **类型**: `float32`

### StartCullDistance
- **类型**: `FPerPlatformInt`

### StartCullDistanceQuality
- **类型**: `FPerQualityLevelInt`

### EndCullDistance
- **类型**: `FPerPlatformInt`

### EndCullDistanceQuality
- **类型**: `FPerQualityLevelInt`

### MinLOD
- **类型**: `int`

### Scaling
- **类型**: `EGrassScaling`

### ScaleX
- **类型**: `FFloatInterval`

### ScaleY
- **类型**: `FFloatInterval`

### ScaleZ
- **类型**: `FFloatInterval`

### bWeightAttenuatesMaxScale
- **类型**: `bool`

### MaxScaleWeightAttenuation
- **类型**: `float32`

### RandomRotation
- **类型**: `bool`

### AlignToSurface
- **类型**: `bool`

### bUseLandscapeLightmap
- **类型**: `bool`

### LightingChannels
- **类型**: `FLightingChannels`

### bReceivesDecals
- **类型**: `bool`

### bAffectDistanceFieldLighting
- **类型**: `bool`

### bCastDynamicShadow
- **类型**: `bool`

### bCastContactShadow
- **类型**: `bool`

### bKeepInstanceBufferCPUCopy
- **类型**: `bool`

### InstanceWorldPositionOffsetDisableDistance
- **类型**: `uint`
- **描述**: Distance at which to grass instances should disable WPO for performance reasons

### ShadowCacheInvalidationBehavior
- **类型**: `EShadowCacheInvalidationBehavior`

## 方法

### opAssign
```angelscript
FGrassVariety& opAssign(FGrassVariety Other)
```

