# UResonanceAudioReverbPluginPreset

**继承自**: `USoundEffectSubmixPreset`

## 属性

### Settings
- **类型**: `FResonanceAudioReverbPluginSettings`

## 方法

### SetEnableRoomEffects
```angelscript
void SetEnableRoomEffects(bool bInEnableRoomEffects)
```
Enables/disables Resonance Audio room effects

### SetReflectionScalar
```angelscript
void SetReflectionScalar(float32 InReflectionScalar)
```
Sets early reflections gain multiplier

### SetReverbBrightness
```angelscript
void SetReverbBrightness(float32 InReverbBrightness)
```
Increases high frequency reverberation times when positive, decreases when negative.
Has no effect when set to 0.0

### SetReverbGain
```angelscript
void SetReverbGain(float32 InReverbGain)
```
Sets reverb gain multiplier

### SetReverbTimeModifier
```angelscript
void SetReverbTimeModifier(float32 InReverbTimeModifier)
```
Adjusts the reverberation time across all frequency bands by multiplying the computed values by this factor.
Has no effect when set to 1.0

### SetRoomDimensions
```angelscript
void SetRoomDimensions(FVector InDimensions)
```
Sets room dimensions in 3D space

### SetRoomMaterials
```angelscript
void SetRoomMaterials(TArray<ERaMaterialName> InMaterials)
```
Sets Resonance Audio room's acoustic materials

### SetRoomPosition
```angelscript
void SetRoomPosition(FVector InPosition)
```
Sets room position in 3D space

### SetRoomRotation
```angelscript
void SetRoomRotation(FQuat InRotation)
```
Sets room rotation in 3D space

