# FLiveLinkSourceBufferManagementSettings

## 属性

### bValidEngineTimeEnabled
- **类型**: `bool`
- **描述**: Enabled the ValidEngineTime setting.

### ValidEngineTime
- **类型**: `float32`
- **描述**: If the frame is older than ValidTime, remove it from the buffer list (in seconds).

### EngineTimeOffset
- **类型**: `float32`
- **描述**: When evaluating with time: how far back from current time should we read the buffer (in seconds)

### bGenerateSubFrame
- **类型**: `bool`

### bUseTimecodeSmoothLatest
- **类型**: `bool`
- **描述**: When evaluating with timecode, align source timecode using a continuous clock offset to do a smooth latest
This means that even if engine Timecode and source Timecode are not aligned, the offset between both clocks
will be tracked to keep them aligned. With an additionnal offset, 1.5 is a good number, you can evaluate
your subject using the latest frame by keeping just enough margin to have a smooth playback and avoid starving.

### SourceTimecodeFrameRate
- **类型**: `FFrameRate`
- **描述**: What is the source frame rate.
When the refresh rate of the source is bigger than the timecode frame rate, LiveLink will try to generate sub frame numbers.
@note The source should generate the sub frame numbers. Use this setting when the source is not able to do so.
@note The generated sub frame numbers will not be saved by Sequencer.

### bValidTimecodeFrameEnabled
- **类型**: `bool`
- **描述**: If the frame timecode is older than ValidTimecodeFrame, remove it from the buffer list (in TimecodeFrameRate).

### ValidTimecodeFrame
- **类型**: `int`
- **描述**: If the frame timecode is older than ValidTimecodeFrame, remove it from the buffer list (in TimecodeFrameRate).

### TimecodeFrameOffset
- **类型**: `float32`
- **描述**: When evaluating with timecode: how far back from current timecode should we read the buffer (in TimecodeFrameRate).

### LatestOffset
- **类型**: `int`
- **描述**: When evaluating with latest: how far back from latest frame should we read the buffer

### MaxNumberOfFrameToBuffered
- **类型**: `int`
- **描述**: Maximum number of frame to keep in memory.

### bKeepAtLeastOneFrame
- **类型**: `bool`
- **描述**: When cleaning the buffer keep at least one frame, even if the frame doesn't matches the other options.

## 方法

### opAssign
```angelscript
FLiveLinkSourceBufferManagementSettings& opAssign(FLiveLinkSourceBufferManagementSettings Other)
```

