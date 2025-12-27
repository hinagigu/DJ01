# ULightComponentBase

**继承自**: `USceneComponent`

## 属性

### Intensity
- **类型**: `float32`

### DeepShadowLayerDistribution
- **类型**: `float32`

### IndirectLightingIntensity
- **类型**: `float32`

### VolumetricScatteringIntensity
- **类型**: `float32`

### LightColor
- **类型**: `FColor`

### bAffectsWorld
- **类型**: `bool`

### CastShadows
- **类型**: `bool`

### CastStaticShadows
- **类型**: `bool`

### CastDynamicShadows
- **类型**: `bool`

### bAffectTranslucentLighting
- **类型**: `bool`

### bTransmission
- **类型**: `bool`

### bCastVolumetricShadow
- **类型**: `bool`

### bCastDeepShadow
- **类型**: `bool`

### CastRaytracedShadow
- **类型**: `ECastRayTracedShadow`

### bAffectReflection
- **类型**: `bool`

### bAffectGlobalIllumination
- **类型**: `bool`

### SamplesPerPixel
- **类型**: `int`

## 方法

### GetLightColor
```angelscript
FLinearColor GetLightColor()
```
Gets the light color as a linear color

### SetAffectGlobalIllumination
```angelscript
void SetAffectGlobalIllumination(bool bNewValue)
```

### SetAffectReflection
```angelscript
void SetAffectReflection(bool bNewValue)
```

### SetCastDeepShadow
```angelscript
void SetCastDeepShadow(bool bNewValue)
```

### SetCastRaytracedShadows
```angelscript
void SetCastRaytracedShadows(ECastRayTracedShadow bNewValue)
```

### SetCastShadows
```angelscript
void SetCastShadows(bool bNewValue)
```
Sets whether this light casts shadows

### SetCastVolumetricShadow
```angelscript
void SetCastVolumetricShadow(bool bNewValue)
```

### SetSamplesPerPixel
```angelscript
void SetSamplesPerPixel(int NewValue)
```

