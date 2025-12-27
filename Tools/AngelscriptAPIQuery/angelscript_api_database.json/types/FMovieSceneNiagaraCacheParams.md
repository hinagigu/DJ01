# FMovieSceneNiagaraCacheParams

## 属性

### CacheParameters
- **类型**: `FNiagaraSimCacheCreateParameters`

### SimCache
- **类型**: `UNiagaraSimCache`
- **描述**: The sim cache this section plays and records into

### bLockCacheToReadOnly
- **类型**: `bool`
- **描述**: If true then the section properties might still be changed (so the section itself is not locked), but the cache cannot be rerecorded to prevent accidentally overriding the data within

### bOverrideQualityLevel
- **类型**: `bool`

### RecordQualityLevel
- **类型**: `EPerQualityLevels`
- **描述**: If set, then the engine scalability setting will be overriden with this value when recording a new cache for this track

### CacheReplayPlayMode
- **类型**: `ENiagaraSimCacheSectionPlayMode`
- **描述**: What should the effect do when the track has no cache data to display

### SectionStretchMode
- **类型**: `ENiagaraSimCacheSectionStretchMode`
- **描述**: What should the effect do when the cache section is stretched?

### FirstLoopStartFrameOffset
- **类型**: `FFrameNumber`
- **描述**: The offset for the first loop of the animation clip

### StartFrameOffset
- **类型**: `FFrameNumber`
- **描述**: The offset into the beginning of the animation clip

### EndFrameOffset
- **类型**: `FFrameNumber`
- **描述**: The offset into the end of the animation clip

### PlayRate
- **类型**: `float32`
- **描述**: The playback rate of the animation clip

### bReverse
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FMovieSceneNiagaraCacheParams& opAssign(FMovieSceneNiagaraCacheParams Other)
```

