# UGranularSynth

**继承自**: `USynthComponent`

## 方法

### GetCurrentPlayheadTime
```angelscript
float32 GetCurrentPlayheadTime()
```

### GetSampleDuration
```angelscript
float32 GetSampleDuration()
```

### IsLoaded
```angelscript
bool IsLoaded()
```

### NoteOff
```angelscript
void NoteOff(float32 Note, bool bKill)
```

### NoteOn
```angelscript
void NoteOn(float32 Note, int Velocity, float32 Duration)
```

### SetAttackTime
```angelscript
void SetAttackTime(float32 AttackTimeMsec)
```

### SetDecayTime
```angelscript
void SetDecayTime(float32 DecayTimeMsec)
```

### SetGrainDuration
```angelscript
void SetGrainDuration(float32 BaseDurationMsec, FVector2D DurationRange)
```

### SetGrainEnvelopeType
```angelscript
void SetGrainEnvelopeType(EGranularSynthEnvelopeType EnvelopeType)
```

### SetGrainPan
```angelscript
void SetGrainPan(float32 BasePan, FVector2D PanRange)
```

### SetGrainPitch
```angelscript
void SetGrainPitch(float32 BasePitch, FVector2D PitchRange)
```

### SetGrainProbability
```angelscript
void SetGrainProbability(float32 InGrainProbability)
```

### SetGrainsPerSecond
```angelscript
void SetGrainsPerSecond(float32 InGrainsPerSecond)
```

### SetGrainVolume
```angelscript
void SetGrainVolume(float32 BaseVolume, FVector2D VolumeRange)
```

### SetPlaybackSpeed
```angelscript
void SetPlaybackSpeed(float32 InPlayheadRate)
```

### SetPlayheadTime
```angelscript
void SetPlayheadTime(float32 InPositionSec, float32 LerpTimeSec, EGranularSynthSeekType SeekType)
```

### SetReleaseTimeMsec
```angelscript
void SetReleaseTimeMsec(float32 ReleaseTimeMsec)
```

### SetScrubMode
```angelscript
void SetScrubMode(bool bScrubMode)
```

### SetSoundWave
```angelscript
void SetSoundWave(USoundWave InSoundWave)
```
This will override the current sound wave if one is set, stop audio, and reload the new sound wave

### SetSustainGain
```angelscript
void SetSustainGain(float32 SustainGain)
```

