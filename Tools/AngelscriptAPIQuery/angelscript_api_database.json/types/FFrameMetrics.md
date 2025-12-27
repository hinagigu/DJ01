# FFrameMetrics

Metrics that correspond to a particular frame

## 属性

### TotalElapsedTime
- **类型**: `float32`
- **描述**: The total amount of time, in seconds, since the capture started

### FrameDelta
- **类型**: `float32`
- **描述**: The total amount of time, in seconds, that this specific frame took to render (not accounting for dropped frames)

### FrameNumber
- **类型**: `int`
- **描述**: The index of this frame from the start of the capture, including dropped frames

### NumDroppedFrames
- **类型**: `int`
- **描述**: The number of frames we dropped in-between this frame, and the last one we captured

## 方法

### opAssign
```angelscript
FFrameMetrics& opAssign(FFrameMetrics Other)
```

