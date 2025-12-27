# FAnimSegment

this is anim segment that defines what animation and how *

## 属性

### AnimReference
- **类型**: `UAnimSequenceBase`
- **描述**: Anim Reference to play - only allow AnimSequence or AnimComposite *

### CachedPlayLength
- **类型**: `float32`

### AnimStartTime
- **类型**: `float32`
- **描述**: Time to start playing AnimSequence at.

### AnimEndTime
- **类型**: `float32`
- **描述**: Time to end playing the AnimSequence at.

### AnimPlayRate
- **类型**: `float32`
- **描述**: Playback speed of this animation. If you'd like to reverse, set -1

### LoopingCount
- **类型**: `int`

## 方法

### opAssign
```angelscript
FAnimSegment& opAssign(FAnimSegment Other)
```

