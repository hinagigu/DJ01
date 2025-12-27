# USubmixEffectStereoToQuadPreset

**继承自**: `USoundEffectSubmixPreset`

Submix effect which sends stereo audio to quad (left surround and right surround) if the channel count is greater than 2.

## 属性

### Settings
- **类型**: `FSubmixEffectStereoToQuadSettings`

## 方法

### SetSettings
```angelscript
void SetSettings(FSubmixEffectStereoToQuadSettings InSettings)
```
Set all tap delay settings. This will replace any dynamically added or modified taps.

