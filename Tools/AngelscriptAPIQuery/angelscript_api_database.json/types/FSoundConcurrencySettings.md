# FSoundConcurrencySettings

## 属性

### MaxCount
- **类型**: `int`

### ResolutionRule
- **类型**: `EMaxConcurrentResolutionRule`

### RetriggerTime
- **类型**: `float32`

### VolumeScale
- **类型**: `float32`
- **描述**: Ducking factor to apply per older voice instance (generation), which compounds based on scaling mode
and (optionally) revives them as they stop according to the provided attack/release times.

Note: This is not applied until after StopQuietest rules are evaluated, in order to avoid thrashing sounds.

AppliedVolumeScale = Math.Pow(DuckingScale, VoiceGeneration)

### VolumeScaleMode
- **类型**: `EConcurrencyVolumeScaleMode`

### VolumeScaleAttackTime
- **类型**: `float32`

### VolumeScaleReleaseTime
- **类型**: `float32`

### VoiceStealReleaseTime
- **类型**: `float32`

### bLimitToOwner
- **类型**: `bool`

### bVolumeScaleCanRelease
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FSoundConcurrencySettings& opAssign(FSoundConcurrencySettings Other)
```

