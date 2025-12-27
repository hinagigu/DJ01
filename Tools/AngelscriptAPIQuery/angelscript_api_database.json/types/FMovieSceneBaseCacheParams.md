# FMovieSceneBaseCacheParams

Base class for the cache parameters that will be used in all the cache sections

## 属性

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
FMovieSceneBaseCacheParams& opAssign(FMovieSceneBaseCacheParams Other)
```

