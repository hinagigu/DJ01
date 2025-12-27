# FSequenceLengthChangedPayload

## 属性

### PreviousLength
- **类型**: `float32`

### T0
- **类型**: `float32`

### T1
- **类型**: `float32`

### PreviousNumberOfFrames
- **类型**: `FFrameNumber`
- **描述**: Previous playable number of frames for the Model

### Frame0
- **类型**: `FFrameNumber`
- **描述**: Frame number at which the change in frames has been made

### Frame1
- **类型**: `FFrameNumber`
- **描述**: Amount of frames which is inserted or removed starting at Frame0

## 方法

### opAssign
```angelscript
FSequenceLengthChangedPayload& opAssign(FSequenceLengthChangedPayload Other)
```

