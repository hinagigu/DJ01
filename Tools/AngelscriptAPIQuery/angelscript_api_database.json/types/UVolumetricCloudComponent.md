# UVolumetricCloudComponent

**继承自**: `USceneComponent`

A component that represents a participating media material around a planet, e.g. clouds.

## 属性

### TracingMaxDistanceMode
- **类型**: `EVolumetricCloudTracingMaxDistanceMode`

### ReflectionViewSampleCountScaleValue
- **类型**: `float32`

### ShadowReflectionViewSampleCountScaleValue
- **类型**: `float32`

### AerialPespectiveRayleighScatteringStartDistance
- **类型**: `float32`

### AerialPespectiveRayleighScatteringFadeDistance
- **类型**: `float32`

### AerialPespectiveMieScatteringStartDistance
- **类型**: `float32`

### AerialPespectiveMieScatteringFadeDistance
- **类型**: `float32`

### LayerBottomAltitude
- **类型**: `float32`

### LayerHeight
- **类型**: `float32`

### TracingStartMaxDistance
- **类型**: `float32`

### TracingStartDistanceFromCamera
- **类型**: `float32`

### TracingMaxDistance
- **类型**: `float32`

### PlanetRadius
- **类型**: `float32`

### GroundAlbedo
- **类型**: `FColor`

### Material
- **类型**: `UMaterialInterface`

### bUsePerSampleAtmosphericLightTransmittance
- **类型**: `bool`

### SkyLightCloudBottomOcclusion
- **类型**: `float32`

### ViewSampleCountScale
- **类型**: `float32`

### ShadowViewSampleCountScale
- **类型**: `float32`

### ShadowTracingDistance
- **类型**: `float32`

### StopTracingTransmittanceThreshold
- **类型**: `float32`

### bHoldout
- **类型**: `bool`

### bRenderInMainPass
- **类型**: `bool`

## 方法

### SetbUsePerSampleAtmosphericLightTransmittance
```angelscript
void SetbUsePerSampleAtmosphericLightTransmittance(bool NewValue)
```

### SetGroundAlbedo
```angelscript
void SetGroundAlbedo(FColor NewValue)
```

### SetHoldout
```angelscript
void SetHoldout(bool bNewHoldout)
```

### SetLayerBottomAltitude
```angelscript
void SetLayerBottomAltitude(float32 NewValue)
```

### SetLayerHeight
```angelscript
void SetLayerHeight(float32 NewValue)
```

### SetMaterial
```angelscript
void SetMaterial(UMaterialInterface NewValue)
```

### SetPlanetRadius
```angelscript
void SetPlanetRadius(float32 NewValue)
```

### SetReflectionViewSampleCountScale
```angelscript
void SetReflectionViewSampleCountScale(float32 NewValue)
```

### SetRenderInMainPass
```angelscript
void SetRenderInMainPass(bool bValue)
```

### SetShadowReflectionViewSampleCountScale
```angelscript
void SetShadowReflectionViewSampleCountScale(float32 NewValue)
```

### SetShadowTracingDistance
```angelscript
void SetShadowTracingDistance(float32 NewValue)
```

### SetShadowViewSampleCountScale
```angelscript
void SetShadowViewSampleCountScale(float32 NewValue)
```

### SetSkyLightCloudBottomOcclusion
```angelscript
void SetSkyLightCloudBottomOcclusion(float32 NewValue)
```

### SetStopTracingTransmittanceThreshold
```angelscript
void SetStopTracingTransmittanceThreshold(float32 NewValue)
```

### SetTracingMaxDistance
```angelscript
void SetTracingMaxDistance(float32 NewValue)
```

### SetTracingStartDistanceFromCamera
```angelscript
void SetTracingStartDistanceFromCamera(float32 NewValue)
```

### SetTracingStartMaxDistance
```angelscript
void SetTracingStartMaxDistance(float32 NewValue)
```

### SetViewSampleCountScale
```angelscript
void SetViewSampleCountScale(float32 NewValue)
```

