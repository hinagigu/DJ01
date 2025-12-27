# FLiveLinkTimeSynchronizationSettings

## 属性

### FrameRate
- **类型**: `FFrameRate`
- **描述**: The frame rate of the source.
This should be the frame rate the source is "stamped" at, not necessarily the frame rate the source is sending.
The source should supply this whenever possible.

### FrameOffset
- **类型**: `FFrameNumber`
- **描述**: When evaluating: how far back from current timecode should we read the buffer (in frame number)

## 方法

### opAssign
```angelscript
FLiveLinkTimeSynchronizationSettings& opAssign(FLiveLinkTimeSynchronizationSettings Other)
```

