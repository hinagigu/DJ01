# USynthSamplePlayer

**继承自**: `USynthComponent`

## 属性

### OnSampleLoaded
- **类型**: `FOnSampleLoaded`

### OnSamplePlaybackProgress
- **类型**: `FOnSamplePlaybackProgress`

### SoundWave
- **类型**: `USoundWave`

## 方法

### GetCurrentPlaybackProgressPercent
```angelscript
float32 GetCurrentPlaybackProgressPercent()
```

### GetCurrentPlaybackProgressTime
```angelscript
float32 GetCurrentPlaybackProgressTime()
```

### GetSampleDuration
```angelscript
float32 GetSampleDuration()
```

### IsLoaded
```angelscript
bool IsLoaded()
```

### SeekToTime
```angelscript
void SeekToTime(float32 TimeSec, ESamplePlayerSeekType SeekType, bool bWrap)
```

### SetPitch
```angelscript
void SetPitch(float32 InPitch, float32 TimeSec)
```

### SetScrubMode
```angelscript
void SetScrubMode(bool bScrubMode)
```

### SetScrubTimeWidth
```angelscript
void SetScrubTimeWidth(float32 InScrubTimeWidthSec)
```

### SetSoundWave
```angelscript
void SetSoundWave(USoundWave InSoundWave)
```
This will override the current sound wave if one is set, stop audio, and reload the new sound wave

