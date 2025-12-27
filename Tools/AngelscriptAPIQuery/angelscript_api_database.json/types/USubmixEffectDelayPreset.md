# USubmixEffectDelayPreset

**继承自**: `USoundEffectSubmixPreset`

USubmixEffectDelayPreset
Class which processes audio streams and uses parameters defined in the preset class.

## 属性

### Settings
- **类型**: `FSubmixEffectDelaySettings`

## 方法

### GetMaxDelayInMilliseconds
```angelscript
float32 GetMaxDelayInMilliseconds()
```
Get the maximum delay possible.

### SetDefaultSettings
```angelscript
void SetDefaultSettings(FSubmixEffectDelaySettings InSettings)
```
Sets object's default settings. This will update both the default UObject settings (and mark it as dirty),
as well as any dynamically set settings.

### SetDelay
```angelscript
void SetDelay(float32 Length)
```
Set how long the delay actually is, in milliseconds.

### SetInterpolationTime
```angelscript
void SetInterpolationTime(float32 Time)
```
Set the time it takes to interpolate between parameters, in milliseconds.

### SetSettings
```angelscript
void SetSettings(FSubmixEffectDelaySettings InSettings)
```
Sets runtime delay settings. This will replace any dynamically added or modified settings without modifying
the original UObject.

