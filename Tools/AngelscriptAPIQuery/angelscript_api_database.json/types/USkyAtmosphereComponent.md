# USkyAtmosphereComponent

**继承自**: `USceneComponent`

A component that represents a planet atmosphere material and simulates sky and light scattering within it.
@see https://docs.unrealengine.com/en-US/Engine/Actors/FogEffects/SkyAtmosphere/index.html

## 属性

### TransformMode
- **类型**: `ESkyAtmosphereTransformMode`

### TraceSampleCountScale
- **类型**: `float32`

### OtherTentDistribution
- **类型**: `FTentDistribution`

### TransmittanceMinLightElevationAngle
- **类型**: `float32`

### AerialPerspectiveStartDepth
- **类型**: `float32`

### BottomRadius
- **类型**: `float32`

### GroundAlbedo
- **类型**: `FColor`

### AtmosphereHeight
- **类型**: `float32`

### MultiScatteringFactor
- **类型**: `float32`

### RayleighScatteringScale
- **类型**: `float32`

### RayleighScattering
- **类型**: `FLinearColor`

### RayleighExponentialDistribution
- **类型**: `float32`

### MieScatteringScale
- **类型**: `float32`

### MieScattering
- **类型**: `FLinearColor`

### MieAbsorptionScale
- **类型**: `float32`

### MieAbsorption
- **类型**: `FLinearColor`

### MieAnisotropy
- **类型**: `float32`

### MieExponentialDistribution
- **类型**: `float32`

### OtherAbsorptionScale
- **类型**: `float32`

### OtherAbsorption
- **类型**: `FLinearColor`

### SkyLuminanceFactor
- **类型**: `FLinearColor`

### AerialPespectiveViewDistanceScale
- **类型**: `float32`

### HeightFogContribution
- **类型**: `float32`

### bHoldout
- **类型**: `bool`

### bRenderInMainPass
- **类型**: `bool`

## 方法

### GetAtmosphereTransmitanceOnGroundAtPlanetTop
```angelscript
FLinearColor GetAtmosphereTransmitanceOnGroundAtPlanetTop(UDirectionalLightComponent DirectionalLight)
```

### GetOverridenAtmosphereLightDirection
```angelscript
FVector GetOverridenAtmosphereLightDirection(int AtmosphereLightIndex)
```

### IsAtmosphereLightDirectionOverriden
```angelscript
bool IsAtmosphereLightDirectionOverriden(int AtmosphereLightIndex)
```

### OverrideAtmosphereLightDirection
```angelscript
void OverrideAtmosphereLightDirection(int AtmosphereLightIndex, FVector LightDirection)
```

### ResetAtmosphereLightDirectionOverride
```angelscript
void ResetAtmosphereLightDirectionOverride(int AtmosphereLightIndex)
```

### SetAerialPespectiveViewDistanceScale
```angelscript
void SetAerialPespectiveViewDistanceScale(float32 NewValue)
```

### SetAtmosphereHeight
```angelscript
void SetAtmosphereHeight(float32 NewValue)
```

### SetBottomRadius
```angelscript
void SetBottomRadius(float32 NewValue)
```

### SetGroundAlbedo
```angelscript
void SetGroundAlbedo(FColor NewValue)
```

### SetHeightFogContribution
```angelscript
void SetHeightFogContribution(float32 NewValue)
```

### SetHoldout
```angelscript
void SetHoldout(bool bNewHoldout)
```

### SetMieAbsorption
```angelscript
void SetMieAbsorption(FLinearColor NewValue)
```

### SetMieAbsorptionScale
```angelscript
void SetMieAbsorptionScale(float32 NewValue)
```

### SetMieAnisotropy
```angelscript
void SetMieAnisotropy(float32 NewValue)
```

### SetMieExponentialDistribution
```angelscript
void SetMieExponentialDistribution(float32 NewValue)
```

### SetMieScattering
```angelscript
void SetMieScattering(FLinearColor NewValue)
```

### SetMieScatteringScale
```angelscript
void SetMieScatteringScale(float32 NewValue)
```

### SetMultiScatteringFactor
```angelscript
void SetMultiScatteringFactor(float32 NewValue)
```

### SetOtherAbsorption
```angelscript
void SetOtherAbsorption(FLinearColor NewValue)
```

### SetOtherAbsorptionScale
```angelscript
void SetOtherAbsorptionScale(float32 NewValue)
```

### SetRayleighExponentialDistribution
```angelscript
void SetRayleighExponentialDistribution(float32 NewValue)
```

### SetRayleighScattering
```angelscript
void SetRayleighScattering(FLinearColor NewValue)
```

### SetRayleighScatteringScale
```angelscript
void SetRayleighScatteringScale(float32 NewValue)
```

### SetRenderInMainPass
```angelscript
void SetRenderInMainPass(bool bValue)
```

### SetSkyLuminanceFactor
```angelscript
void SetSkyLuminanceFactor(FLinearColor NewValue)
```

