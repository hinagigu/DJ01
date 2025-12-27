# UDirectionalLightComponent

**继承自**: `ULightComponent`

A light component that has parallel rays. Will provide a uniform lighting across any affected surface (eg. The Sun). This will affect all objects in the defined light-mass importance volume.

## 属性

### FarShadowCascadeCount
- **类型**: `int`

### FarShadowDistance
- **类型**: `float32`

### DistanceFieldShadowDistance
- **类型**: `float32`

### TraceDistance
- **类型**: `float32`

### AtmosphereSunDiskColorScale
- **类型**: `FLinearColor`

### CloudShadowStrength
- **类型**: `float32`

### CloudShadowOnAtmosphereStrength
- **类型**: `float32`

### CloudShadowOnSurfaceStrength
- **类型**: `float32`

### CloudShadowDepthBias
- **类型**: `float32`

### CloudShadowExtent
- **类型**: `float32`

### CloudShadowMapResolutionScale
- **类型**: `float32`

### CloudShadowRaySampleCountScale
- **类型**: `float32`

### CloudScatteredLuminanceScale
- **类型**: `FLinearColor`

### LightmassSettings
- **类型**: `FLightmassDirectionalLightSettings`
- **描述**: The Lightmass settings for this object.

### ModulatedShadowColor
- **类型**: `FColor`

### ShadowCascadeBiasDistribution
- **类型**: `float32`

### bEnableLightShaftOcclusion
- **类型**: `bool`

### OcclusionMaskDarkness
- **类型**: `float32`

### OcclusionDepthRange
- **类型**: `float32`

### LightShaftOverrideDirection
- **类型**: `FVector`

### DynamicShadowDistanceMovableLight
- **类型**: `float32`

### DynamicShadowDistanceStationaryLight
- **类型**: `float32`

### DynamicShadowCascades
- **类型**: `int`

### CascadeDistributionExponent
- **类型**: `float32`

### CascadeTransitionFraction
- **类型**: `float32`

### ShadowDistanceFadeoutFraction
- **类型**: `float32`

### bUseInsetShadowsForMovableObjects
- **类型**: `bool`

### ForwardShadingPriority
- **类型**: `int`

### LightSourceAngle
- **类型**: `float32`

### LightSourceSoftAngle
- **类型**: `float32`

### ShadowSourceAngleFactor
- **类型**: `float32`

### bAtmosphereSunLight
- **类型**: `bool`

### AtmosphereSunLightIndex
- **类型**: `int`

### bPerPixelAtmosphereTransmittance
- **类型**: `bool`

### bCastShadowsOnClouds
- **类型**: `bool`

### bCastShadowsOnAtmosphere
- **类型**: `bool`

### bCastCloudShadows
- **类型**: `bool`

### bCastModulatedShadows
- **类型**: `bool`

### ShadowAmount
- **类型**: `float32`

## 方法

### SetAtmosphereSunLight
```angelscript
void SetAtmosphereSunLight(bool bNewValue)
```

### SetAtmosphereSunLightIndex
```angelscript
void SetAtmosphereSunLightIndex(int NewValue)
```

### SetCascadeDistributionExponent
```angelscript
void SetCascadeDistributionExponent(float32 NewValue)
```

### SetCascadeTransitionFraction
```angelscript
void SetCascadeTransitionFraction(float32 NewValue)
```

### SetDynamicShadowCascades
```angelscript
void SetDynamicShadowCascades(int NewValue)
```

### SetDynamicShadowDistanceMovableLight
```angelscript
void SetDynamicShadowDistanceMovableLight(float32 NewValue)
```

### SetDynamicShadowDistanceStationaryLight
```angelscript
void SetDynamicShadowDistanceStationaryLight(float32 NewValue)
```

### SetEnableLightShaftOcclusion
```angelscript
void SetEnableLightShaftOcclusion(bool bNewValue)
```

### SetForwardShadingPriority
```angelscript
void SetForwardShadingPriority(int NewValue)
```

### SetLightShaftOverrideDirection
```angelscript
void SetLightShaftOverrideDirection(FVector NewValue)
```

### SetLightSourceAngle
```angelscript
void SetLightSourceAngle(float32 NewValue)
```

### SetLightSourceSoftAngle
```angelscript
void SetLightSourceSoftAngle(float32 NewValue)
```

### SetOcclusionDepthRange
```angelscript
void SetOcclusionDepthRange(float32 NewValue)
```

### SetOcclusionMaskDarkness
```angelscript
void SetOcclusionMaskDarkness(float32 NewValue)
```

### SetShadowAmount
```angelscript
void SetShadowAmount(float32 NewValue)
```

### SetShadowCascadeBiasDistribution
```angelscript
void SetShadowCascadeBiasDistribution(float32 NewValue)
```

### SetShadowDistanceFadeoutFraction
```angelscript
void SetShadowDistanceFadeoutFraction(float32 NewValue)
```

### SetShadowSourceAngleFactor
```angelscript
void SetShadowSourceAngleFactor(float32 NewValue)
```

