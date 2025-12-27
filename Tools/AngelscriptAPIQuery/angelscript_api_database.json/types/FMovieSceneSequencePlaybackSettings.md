# FMovieSceneSequencePlaybackSettings

Settings for the level sequence player actor.

## 属性

### LoopCount
- **类型**: `FMovieSceneSequenceLoopCount`

### TickInterval
- **类型**: `FMovieSceneSequenceTickInterval`
- **描述**: Overridable tick interval for this sequence to update at. When not overridden, the owning actor or component's tick interval will be used

### PlayRate
- **类型**: `float32`

### StartTime
- **类型**: `float32`

### FinishCompletionStateOverride
- **类型**: `EMovieSceneCompletionModeOverride`

### bAutoPlay
- **类型**: `bool`

### bRandomStartTime
- **类型**: `bool`

### bDisableMovementInput
- **类型**: `bool`

### bDisableLookAtInput
- **类型**: `bool`

### bHidePlayer
- **类型**: `bool`

### bHideHud
- **类型**: `bool`

### bDisableCameraCuts
- **类型**: `bool`

### bPauseAtEnd
- **类型**: `bool`

### bInheritTickIntervalFromOwner
- **类型**: `bool`

### bDynamicWeighting
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FMovieSceneSequencePlaybackSettings& opAssign(FMovieSceneSequencePlaybackSettings Other)
```

