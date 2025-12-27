# UForceFeedbackComponent

**继承自**: `USceneComponent`

ForceFeedbackComponent allows placing a rumble effect in to the world and having it apply to player characters who come near it

## 属性

### AttenuationSettings
- **类型**: `UForceFeedbackAttenuation`

### AttenuationOverrides
- **类型**: `FForceFeedbackAttenuationSettings`

### OnForceFeedbackFinished
- **类型**: `FOnForceFeedbackFinished`

### ForceFeedbackEffect
- **类型**: `UForceFeedbackEffect`

### bLooping
- **类型**: `bool`

### bIgnoreTimeDilation
- **类型**: `bool`

### bOverrideAttenuation
- **类型**: `bool`

### IntensityMultiplier
- **类型**: `float32`

## 方法

### AdjustAttenuation
```angelscript
void AdjustAttenuation(FForceFeedbackAttenuationSettings InAttenuationSettings)
```
Modify the attenuation settings of the component

### GetAttenuationSettingsToApply
```angelscript
bool GetAttenuationSettingsToApply(FForceFeedbackAttenuationSettings& OutAttenuationSettings)
```

### Play
```angelscript
void Play(float32 StartTime)
```
Start a feedback effect playing

### SetForceFeedbackEffect
```angelscript
void SetForceFeedbackEffect(UForceFeedbackEffect NewForceFeedbackEffect)
```
Set what force feedback effect is played by this component

### SetIntensityMultiplier
```angelscript
void SetIntensityMultiplier(float32 NewIntensityMultiplier)
```
Set a new intensity multiplier

### Stop
```angelscript
void Stop()
```
Stop playing the feedback effect

