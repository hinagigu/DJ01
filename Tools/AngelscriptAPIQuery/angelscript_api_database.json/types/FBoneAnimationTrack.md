# FBoneAnimationTrack

Structure encapsulating a single bone animation track.

## 属性

### InternalTrackData
- **类型**: `FRawAnimSequenceTrack`
- **描述**: Internally stored data representing the animation bone data

### BoneTreeIndex
- **类型**: `int`
- **描述**: Index corresponding to the bone this track corresponds to within the target USkeleton

### Name
- **类型**: `FName`
- **描述**: Name of the bone this track corresponds to

## 方法

### opAssign
```angelscript
FBoneAnimationTrack& opAssign(FBoneAnimationTrack Other)
```

