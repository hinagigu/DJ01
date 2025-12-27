# UAnimDataModel

**继承自**: `UObject`

The Model represents the source data for animations. It contains both bone animation data as well as animated curves.
They are currently only a sub-object of a AnimSequenceBase instance. The instance derives all runtime data from the source data.

## 属性

### ModifiedEvent
- **类型**: `FAnimDataModelModifiedDynamicEvent`

### BoneAnimationTracks
- **类型**: `TArray<FBoneAnimationTrack>`
- **描述**: All individual bone animation tracks

### PlayLength
- **类型**: `float32`

### FrameRate
- **类型**: `FFrameRate`
- **描述**: Rate at which the animated data is sampled

### NumberOfFrames
- **类型**: `int`
- **描述**: Total number of sampled animated frames

### NumberOfKeys
- **类型**: `int`
- **描述**: Total number of sampled animated keys

### CurveData
- **类型**: `FAnimationCurveData`
- **描述**: Container with all animated curve data

### AnimatedBoneAttributes
- **类型**: `TArray<FAnimatedBoneAttribute>`
- **描述**: Container with all animated (bone) attribute data

