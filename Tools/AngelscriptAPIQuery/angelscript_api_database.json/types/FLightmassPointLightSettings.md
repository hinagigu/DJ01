# FLightmassPointLightSettings

Point/spot settings for Lightmass

## 属性

### IndirectLightingSaturation
- **类型**: `float32`
- **描述**: 0 will be completely desaturated, 1 will be unchanged

### ShadowExponent
- **类型**: `float32`
- **描述**: Controls the falloff of shadow penumbras

### bUseAreaShadowsForStationaryLight
- **类型**: `bool`
- **描述**: Whether to use area shadows for stationary light precomputed shadowmaps.
Area shadows get softer the further they are from shadow casters, but require higher lightmap resolution to get the same quality where the shadow is sharp.

## 方法

### opAssign
```angelscript
FLightmassPointLightSettings& opAssign(FLightmassPointLightSettings Other)
```

