# UAutomatedLevelSequenceCapture

**继承自**: `UMovieSceneCapture`

## 属性

### LevelSequenceAsset
- **类型**: `FSoftObjectPath`
- **描述**: A level sequence asset to playback at runtime - used where the level sequence does not already exist in the world.

### ShotName
- **类型**: `FString`
- **描述**: Optional shot name to render. The frame range to render will be set to the shot frame range.

### bUseCustomStartFrame
- **类型**: `bool`

### CustomStartFrame
- **类型**: `FFrameNumber`

### bUseCustomEndFrame
- **类型**: `bool`

### CustomEndFrame
- **类型**: `FFrameNumber`

### WarmUpFrameCount
- **类型**: `int`

### DelayBeforeWarmUp
- **类型**: `float32`

### DelayBeforeShotWarmUp
- **类型**: `float32`

### DelayEveryFrame
- **类型**: `float32`

### BurnInOptions
- **类型**: `ULevelSequenceBurnInOptions`

### bWriteEditDecisionList
- **类型**: `bool`

### bWriteFinalCutProXML
- **类型**: `bool`

