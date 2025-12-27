# USoundCue

**继承自**: `USoundBase`

The behavior of audio playback is defined within Sound Cues.

## 属性

### FirstNode
- **类型**: `USoundNode`

### VolumeMultiplier
- **类型**: `float32`

### PitchMultiplier
- **类型**: `float32`

### AttenuationOverrides
- **类型**: `FSoundAttenuationSettings`
- **描述**: Attenuation settings to use if Override Attenuation is set to true

### SubtitlePriority
- **类型**: `float32`
- **描述**: The priority of the subtitle.  Defaults to 10000.  Higher values will play instead of lower values.

### bPrimeOnLoad
- **类型**: `bool`

### bOverrideAttenuation
- **类型**: `bool`

### bExcludeFromRandomNodeBranchCulling
- **类型**: `bool`

