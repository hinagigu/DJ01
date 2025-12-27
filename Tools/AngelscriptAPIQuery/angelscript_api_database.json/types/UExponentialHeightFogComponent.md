# UExponentialHeightFogComponent

**继承自**: `USceneComponent`

Used to create fogging effects such as clouds but with a density that is related to the height of the fog.

## 属性

### FogInscatteringLuminance
- **类型**: `FLinearColor`

### SkyAtmosphereAmbientContributionColorScale
- **类型**: `FLinearColor`

### DirectionalInscatteringLuminance
- **类型**: `FLinearColor`

### bEnableVolumetricFog
- **类型**: `bool`

### VolumetricFogStartDistance
- **类型**: `float32`

### VolumetricFogNearFadeInDistance
- **类型**: `float32`

### VolumetricFogStaticLightingScatteringIntensity
- **类型**: `float32`

### bOverrideLightColorsWithFogInscatteringColors
- **类型**: `bool`

### FogDensity
- **类型**: `float32`

### FogHeightFalloff
- **类型**: `float32`

### SecondFogData
- **类型**: `FExponentialHeightFogData`

### InscatteringColorCubemap
- **类型**: `UTextureCube`

### InscatteringColorCubemapAngle
- **类型**: `float32`

### InscatteringTextureTint
- **类型**: `FLinearColor`

### FullyDirectionalInscatteringColorDistance
- **类型**: `float32`

### NonDirectionalInscatteringColorDistance
- **类型**: `float32`

### DirectionalInscatteringExponent
- **类型**: `float32`

### DirectionalInscatteringStartDistance
- **类型**: `float32`

### FogMaxOpacity
- **类型**: `float32`

### StartDistance
- **类型**: `float32`

### FogCutoffDistance
- **类型**: `float32`

### VolumetricFogScatteringDistribution
- **类型**: `float32`

### VolumetricFogAlbedo
- **类型**: `FColor`

### VolumetricFogEmissive
- **类型**: `FLinearColor`

### VolumetricFogExtinctionScale
- **类型**: `float32`

### VolumetricFogDistance
- **类型**: `float32`

### bHoldout
- **类型**: `bool`

### bRenderInMainPass
- **类型**: `bool`

## 方法

### SetDirectionalInscatteringColor
```angelscript
void SetDirectionalInscatteringColor(FLinearColor Value)
```

### SetDirectionalInscatteringExponent
```angelscript
void SetDirectionalInscatteringExponent(float32 Value)
```

### SetDirectionalInscatteringStartDistance
```angelscript
void SetDirectionalInscatteringStartDistance(float32 Value)
```

### SetFogCutoffDistance
```angelscript
void SetFogCutoffDistance(float32 Value)
```

### SetFogDensity
```angelscript
void SetFogDensity(float32 Value)
```

### SetFogHeightFalloff
```angelscript
void SetFogHeightFalloff(float32 Value)
```

### SetFogInscatteringColor
```angelscript
void SetFogInscatteringColor(FLinearColor Value)
```

### SetFogMaxOpacity
```angelscript
void SetFogMaxOpacity(float32 Value)
```

### SetFullyDirectionalInscatteringColorDistance
```angelscript
void SetFullyDirectionalInscatteringColorDistance(float32 Value)
```

### SetHoldout
```angelscript
void SetHoldout(bool bNewHoldout)
```

### SetInscatteringColorCubemap
```angelscript
void SetInscatteringColorCubemap(UTextureCube Value)
```

### SetInscatteringColorCubemapAngle
```angelscript
void SetInscatteringColorCubemapAngle(float32 Value)
```

### SetInscatteringTextureTint
```angelscript
void SetInscatteringTextureTint(FLinearColor Value)
```

### SetNonDirectionalInscatteringColorDistance
```angelscript
void SetNonDirectionalInscatteringColorDistance(float32 Value)
```

### SetRenderInMainPass
```angelscript
void SetRenderInMainPass(bool bValue)
```

### SetSecondFogData
```angelscript
void SetSecondFogData(FExponentialHeightFogData NewValue)
```

### SetSecondFogDensity
```angelscript
void SetSecondFogDensity(float32 Value)
```

### SetSecondFogHeightFalloff
```angelscript
void SetSecondFogHeightFalloff(float32 Value)
```

### SetSecondFogHeightOffset
```angelscript
void SetSecondFogHeightOffset(float32 Value)
```

### SetStartDistance
```angelscript
void SetStartDistance(float32 Value)
```

### SetVolumetricFog
```angelscript
void SetVolumetricFog(bool bNewValue)
```

### SetVolumetricFogAlbedo
```angelscript
void SetVolumetricFogAlbedo(FColor NewValue)
```

### SetVolumetricFogDistance
```angelscript
void SetVolumetricFogDistance(float32 NewValue)
```

### SetVolumetricFogEmissive
```angelscript
void SetVolumetricFogEmissive(FLinearColor NewValue)
```

### SetVolumetricFogExtinctionScale
```angelscript
void SetVolumetricFogExtinctionScale(float32 NewValue)
```

### SetVolumetricFogScatteringDistribution
```angelscript
void SetVolumetricFogScatteringDistribution(float32 NewValue)
```

