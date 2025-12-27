# USequenceCameraShakePattern

**继承自**: `UCameraShakePattern`

A camera shake pattern that plays a sequencer animation.

## 属性

### Sequence
- **类型**: `UCameraAnimationSequence`
- **描述**: Source camera animation sequence to play.

### PlayRate
- **类型**: `float32`
- **描述**: Scalar defining how fast to play the anim.

### Scale
- **类型**: `float32`
- **描述**: Scalar defining how "intense" to play the anim.

### BlendInTime
- **类型**: `float32`
- **描述**: Linear blend-in time.

### BlendOutTime
- **类型**: `float32`
- **描述**: Linear blend-out time.

### RandomSegmentDuration
- **类型**: `float32`
- **描述**: When bRandomSegment is true, defines how long the sequence should play.

### bRandomSegment
- **类型**: `bool`
- **描述**: When true, plays a random snippet of the sequence for RandomSegmentDuration seconds.

@note The sequence we be forced to loop when bRandomSegment is enabled, in case the duration
      is longer than what's left to play from the random start time.

