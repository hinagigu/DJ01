# ULightComponent

**继承自**: `ULightComponentBase`

## 属性

### MaxDrawDistance
- **类型**: `float32`

### MaxDistanceFadeRange
- **类型**: `float32`

### ShadowResolutionScale
- **类型**: `float32`

### ShadowSharpen
- **类型**: `float32`

### ContactShadowLength
- **类型**: `float32`

### ContactShadowCastingIntensity
- **类型**: `float32`

### ContactShadowNonCastingIntensity
- **类型**: `float32`

### DisabledBrightness
- **类型**: `float32`

### bUseRayTracedDistanceFieldShadows
- **类型**: `bool`

### RayStartOffsetDepthScale
- **类型**: `float32`

### Temperature
- **类型**: `float32`

### bUseTemperature
- **类型**: `bool`

### SpecularScale
- **类型**: `float32`

### ShadowBias
- **类型**: `float32`

### ShadowSlopeBias
- **类型**: `float32`

### ContactShadowLengthInWS
- **类型**: `bool`

### CastTranslucentShadows
- **类型**: `bool`

### bCastShadowsFromCinematicObjectsOnly
- **类型**: `bool`

### bForceCachedShadowsForMovablePrimitives
- **类型**: `bool`

### LightingChannels
- **类型**: `FLightingChannels`

### LightFunctionMaterial
- **类型**: `UMaterialInterface`

### LightFunctionScale
- **类型**: `FVector`

### IESTexture
- **类型**: `UTextureLightProfile`

### bUseIESBrightness
- **类型**: `bool`

### IESBrightnessScale
- **类型**: `float32`

### LightFunctionFadeDistance
- **类型**: `float32`

### bEnableLightShaftBloom
- **类型**: `bool`

### BloomScale
- **类型**: `float32`

### BloomThreshold
- **类型**: `float32`

### BloomMaxBrightness
- **类型**: `float32`

### BloomTint
- **类型**: `FColor`

## 方法

### SetAffectTranslucentLighting
```angelscript
void SetAffectTranslucentLighting(bool bNewValue)
```

### SetBloomMaxBrightness
```angelscript
void SetBloomMaxBrightness(float32 NewValue)
```

### SetBloomScale
```angelscript
void SetBloomScale(float32 NewValue)
```

### SetBloomThreshold
```angelscript
void SetBloomThreshold(float32 NewValue)
```

### SetBloomTint
```angelscript
void SetBloomTint(FColor NewValue)
```

### SetEnableLightShaftBloom
```angelscript
void SetEnableLightShaftBloom(bool bNewValue)
```

### SetForceCachedShadowsForMovablePrimitives
```angelscript
void SetForceCachedShadowsForMovablePrimitives(bool bNewValue)
```

### SetIESBrightnessScale
```angelscript
void SetIESBrightnessScale(float32 NewValue)
```

### SetIESTexture
```angelscript
void SetIESTexture(UTextureLightProfile NewValue)
```

### SetIndirectLightingIntensity
```angelscript
void SetIndirectLightingIntensity(float32 NewIntensity)
```

### SetIntensity
```angelscript
void SetIntensity(float32 NewIntensity)
```
Set intensity of the light

### SetLightColor
```angelscript
void SetLightColor(FLinearColor NewLightColor, bool bSRGB)
```
Set color of the light

### SetLightFunctionDisabledBrightness
```angelscript
void SetLightFunctionDisabledBrightness(float32 NewValue)
```

### SetLightFunctionFadeDistance
```angelscript
void SetLightFunctionFadeDistance(float32 NewLightFunctionFadeDistance)
```

### SetLightFunctionMaterial
```angelscript
void SetLightFunctionMaterial(UMaterialInterface NewLightFunctionMaterial)
```

### SetLightFunctionScale
```angelscript
void SetLightFunctionScale(FVector NewLightFunctionScale)
```

### SetLightingChannels
```angelscript
void SetLightingChannels(bool bChannel0, bool bChannel1, bool bChannel2)
```

### SetShadowBias
```angelscript
void SetShadowBias(float32 NewValue)
```

### SetShadowSlopeBias
```angelscript
void SetShadowSlopeBias(float32 NewValue)
```

### SetSpecularScale
```angelscript
void SetSpecularScale(float32 NewValue)
```

### SetTemperature
```angelscript
void SetTemperature(float32 NewTemperature)
```

### SetTransmission
```angelscript
void SetTransmission(bool bNewValue)
```

### SetUseIESBrightness
```angelscript
void SetUseIESBrightness(bool bNewValue)
```

### SetUseTemperature
```angelscript
void SetUseTemperature(bool bNewValue)
```

### SetVolumetricScatteringIntensity
```angelscript
void SetVolumetricScatteringIntensity(float32 NewIntensity)
```

