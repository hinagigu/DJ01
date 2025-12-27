# FAnimNode_ObserveBone

Debugging node that displays the current value of a bone in a specific space.

## 属性

### BoneToObserve
- **类型**: `FBoneReference`
- **描述**: Name of bone to observe.

### DisplaySpace
- **类型**: `EBoneControlSpace`
- **描述**: Reference frame to display the bone transform in.

### bRelativeToRefPose
- **类型**: `bool`
- **描述**: Show the difference from the reference pose?

### ComponentPose
- **类型**: `FComponentSpacePoseLink`

### LODThreshold
- **类型**: `int`

### AlphaInputType
- **类型**: `EAnimAlphaInputType`

### bAlphaBoolEnabled
- **类型**: `bool`

### Alpha
- **类型**: `float32`

### AlphaScaleBias
- **类型**: `FInputScaleBias`

### AlphaBoolBlend
- **类型**: `FInputAlphaBoolBlend`

### AlphaCurveName
- **类型**: `FName`

### AlphaScaleBiasClamp
- **类型**: `FInputScaleBiasClamp`

## 方法

### opAssign
```angelscript
FAnimNode_ObserveBone& opAssign(FAnimNode_ObserveBone Other)
```

