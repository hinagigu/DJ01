# FPlatformRuntimeAudioCompressionOverrides

## 属性

### bOverrideCompressionTimes
- **类型**: `bool`
- **描述**: When true, overrides the Sound Group on each Sound Wave, and instead uses the Duration Threshold value to determine whether a sound should be fully decompressed during initial loading.

### DurationThreshold
- **类型**: `float32`
- **描述**: When Override Compression Times is set to true, any sound under this threshold (in seconds) will be fully decompressed on load.
Otherwise the first chunk of this sound is cached at load and the rest is decompressed in real time.
If set to zero, will default to the Sound Group on the relevant Sound Wave

### MaxNumRandomBranches
- **类型**: `int`
- **描述**: On this platform, any random nodes on Sound Cues will automatically only preload this number of branches and dispose of any others
on load. This can drastically cut down on memory usage. If set to 0, no branches are culled.

### SoundCueQualityIndex
- **类型**: `int`
- **描述**: On this platform, use the specified quality at this index to override the quality used for SoundCues on this platform

## 方法

### opAssign
```angelscript
FPlatformRuntimeAudioCompressionOverrides& opAssign(FPlatformRuntimeAudioCompressionOverrides Other)
```

