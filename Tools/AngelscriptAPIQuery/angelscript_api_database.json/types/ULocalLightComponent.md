# ULocalLightComponent

**继承自**: `ULightComponent`

A light component which emits light from a single point equally in all directions.

## 属性

### InverseExposureBlend
- **类型**: `float32`

### LightmassSettings
- **类型**: `FLightmassPointLightSettings`
- **描述**: The Lightmass settings for this object.

### IntensityUnits
- **类型**: `ELightUnits`

### AttenuationRadius
- **类型**: `float32`

## 方法

### SetAttenuationRadius
```angelscript
void SetAttenuationRadius(float32 NewRadius)
```

### SetIntensityUnits
```angelscript
void SetIntensityUnits(ELightUnits NewIntensityUnits)
```
Set the units used for the intensity of the light

