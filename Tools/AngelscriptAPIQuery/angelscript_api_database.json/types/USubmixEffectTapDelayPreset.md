# USubmixEffectTapDelayPreset

**继承自**: `USoundEffectSubmixPreset`

UTapDelaySubmixPreset
Class which processes audio streams and uses parameters defined in the preset class.

## 属性

### Settings
- **类型**: `FSubmixEffectTapDelaySettings`

## 方法

### AddTap
```angelscript
void AddTap(int& TapId)
```
Adds a dynamic tap delay with the given settings. Returns the tap id.

### GetMaxDelayInMilliseconds
```angelscript
float32 GetMaxDelayInMilliseconds()
```
Get the maximum delay possible.

### GetTap
```angelscript
void GetTap(int TapId, FTapDelayInfo& TapInfo)
```
Get the current info about a specific tap.

### GetTapIds
```angelscript
void GetTapIds(TArray<int>& TapIds)
```
Retrieve an array of all tap ids for the submix effect.

### RemoveTap
```angelscript
void RemoveTap(int TapId)
```
Remove the tap from the preset.

### SetInterpolationTime
```angelscript
void SetInterpolationTime(float32 Time)
```
Set the time it takes to interpolate between parameters, in milliseconds.

### SetSettings
```angelscript
void SetSettings(FSubmixEffectTapDelaySettings InSettings)
```
Set all tap delay setting. This will replace any dynamically added or modified taps.

### SetTap
```angelscript
void SetTap(int TapId, FTapDelayInfo TapInfo)
```
Modify a specific tap.

