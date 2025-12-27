# UResonanceAudioSpatializationSourceSettings

**继承自**: `USpatializationPluginSourceSettingsBase`

## 属性

### SpatializationMethod
- **类型**: `ERaSpatializationMethod`
- **描述**: Spatialization method to use for sound object(s). NOTE: Has no effect if 'Stereo Panning' global quality mode is selected for the project

### Pattern
- **类型**: `float32`
- **描述**: Directivity pattern: 0.0 (omnidirectional), 0.5 (cardioid), 1.0 (figure-of-8)

### Sharpness
- **类型**: `float32`
- **描述**: Sharpness of the directivity pattern. Higher values result in a narrower sound emission beam

### bToggleVisualization
- **类型**: `bool`
- **描述**: Whether to visualize directivity pattern in the viewport.

### Scale
- **类型**: `float32`
- **描述**: Scale (for directivity pattern visualization only).

### Spread
- **类型**: `float32`
- **描述**: Spread (width) of the sound source (in degrees). Note: spread control is not available if 'Stereo Panning' global quality mode is enabled for the project and / or 'Stereo Panning' spatialization mode is enabled for the sound source

### Rolloff
- **类型**: `ERaDistanceRolloffModel`
- **描述**: Roll-off model to use for sound source distance attenuation. Select 'None' (default) to use Unreal attenuation settings

### MinDistance
- **类型**: `float32`
- **描述**: Minimum distance to apply the chosen attenuation method (default = 100.0 cm)

### MaxDistance
- **类型**: `float32`
- **描述**: Maximum distance to apply the chosen attenuation method ((default = 50000.0 cm)

## 方法

### SetSoundSourceDirectivity
```angelscript
void SetSoundSourceDirectivity(float32 InPattern, float32 InSharpness)
```
Sets the sound source directivity, applies, and updates

### SetSoundSourceSpread
```angelscript
void SetSoundSourceSpread(float32 InSpread)
```
Sets the sound source spread (width), applies, and updates

