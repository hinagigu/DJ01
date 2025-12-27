# UWindDirectionalSourceComponent

**继承自**: `USceneComponent`

Component that provides a directional wind source. Only affects SpeedTree assets.

## 属性

### MinGustAmount
- **类型**: `float32`

### MaxGustAmount
- **类型**: `float32`

### Strength
- **类型**: `float32`

### Speed
- **类型**: `float32`

### Radius
- **类型**: `float32`

### bPointWind
- **类型**: `bool`

## 方法

### SetMaximumGustAmount
```angelscript
void SetMaximumGustAmount(float32 InNewMaxGust)
```
Set maximum deviation for wind gusts

### SetMinimumGustAmount
```angelscript
void SetMinimumGustAmount(float32 InNewMinGust)
```
Set minimum deviation for wind gusts

### SetRadius
```angelscript
void SetRadius(float32 InNewRadius)
```
Set the effect radius for point wind

### SetSpeed
```angelscript
void SetSpeed(float32 InNewSpeed)
```
Sets the windspeed of the generated wind

### SetStrength
```angelscript
void SetStrength(float32 InNewStrength)
```
Sets the strength of the generated wind

### SetWindType
```angelscript
void SetWindType(EWindSourceType InNewType)
```
Set the type of wind generator to use

