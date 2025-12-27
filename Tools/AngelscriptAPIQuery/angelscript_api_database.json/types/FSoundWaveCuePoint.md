# FSoundWaveCuePoint

Struct defining a cue point in a sound wave asset

## 属性

### CuePointID
- **类型**: `int`
- **描述**: Unique identifier for the wave cue point

### Label
- **类型**: `FString`
- **描述**: The label for the cue point

### FramePosition
- **类型**: `int`
- **描述**: The frame position of the cue point

### FrameLength
- **类型**: `int`
- **描述**: The frame length of the cue point (non-zero if it's a region)

## 方法

### opAssign
```angelscript
FSoundWaveCuePoint& opAssign(FSoundWaveCuePoint Other)
```

