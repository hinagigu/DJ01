# USkyLightComponent

**继承自**: `ULightComponentBase`

## 属性

### bRealTimeCapture
- **类型**: `bool`

### SourceType
- **类型**: `ESkyLightSourceType`

### CubemapResolution
- **类型**: `int`

### SkyDistanceThreshold
- **类型**: `float32`

### bCaptureEmissiveOnly
- **类型**: `bool`

### bLowerHemisphereIsBlack
- **类型**: `bool`

### OcclusionMaxDistance
- **类型**: `float32`

### Contrast
- **类型**: `float32`

### CloudAmbientOcclusionStrength
- **类型**: `float32`

### CloudAmbientOcclusionExtent
- **类型**: `float32`

### CloudAmbientOcclusionMapResolutionScale
- **类型**: `float32`

### CloudAmbientOcclusionApertureScale
- **类型**: `float32`

### OcclusionCombineMode
- **类型**: `EOcclusionCombineMode`

### Cubemap
- **类型**: `UTextureCube`

### SourceCubemapAngle
- **类型**: `float32`

### LowerHemisphereColor
- **类型**: `FLinearColor`

### OcclusionExponent
- **类型**: `float32`

### MinOcclusion
- **类型**: `float32`

### OcclusionTint
- **类型**: `FColor`

### bCloudAmbientOcclusion
- **类型**: `bool`

## 方法

### RecaptureSky
```angelscript
void RecaptureSky()
```
Recaptures the scene for the skylight.
This is useful for making sure the sky light is up to date after changing something in the world that it would capture.
Warning: this is very costly and will definitely cause a hitch.

### SetCubemap
```angelscript
void SetCubemap(UTextureCube NewCubemap)
```
Sets the cubemap used when SourceType is set to SpecifiedCubemap, and causes a skylight update on the next tick.

### SetCubemapBlend
```angelscript
void SetCubemapBlend(UTextureCube SourceCubemap, UTextureCube DestinationCubemap, float32 InBlendFraction)
```
Creates sky lighting from a blend between two cubemaps, which is only valid when SourceType is set to SpecifiedCubemap.
This can be used to seamlessly transition sky lighting between different times of day.
The caller should continue to update the blend until BlendFraction is 0 or 1 to reduce rendering cost.
The caller is responsible for avoiding pops due to changing the source or destination.

### SetIndirectLightingIntensity
```angelscript
void SetIndirectLightingIntensity(float32 NewIntensity)
```

### SetIntensity
```angelscript
void SetIntensity(float32 NewIntensity)
```

### SetLightColor
```angelscript
void SetLightColor(FLinearColor NewLightColor)
```
Set color of the light

### SetLowerHemisphereColor
```angelscript
void SetLowerHemisphereColor(FLinearColor InLowerHemisphereColor)
```

### SetMinOcclusion
```angelscript
void SetMinOcclusion(float32 InMinOcclusion)
```

### SetOcclusionContrast
```angelscript
void SetOcclusionContrast(float32 InOcclusionContrast)
```

### SetOcclusionExponent
```angelscript
void SetOcclusionExponent(float32 InOcclusionExponent)
```

### SetOcclusionTint
```angelscript
void SetOcclusionTint(FColor InTint)
```

### SetSourceCubemapAngle
```angelscript
void SetSourceCubemapAngle(float32 NewValue)
```
Sets the angle of the cubemap used when SourceType is set to SpecifiedCubemap and it is non static. It will cause the skylight to update on the next tick.

### SetVolumetricScatteringIntensity
```angelscript
void SetVolumetricScatteringIntensity(float32 NewIntensity)
```

