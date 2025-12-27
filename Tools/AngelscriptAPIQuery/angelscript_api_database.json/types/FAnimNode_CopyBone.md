# FAnimNode_CopyBone

Simple controller to copy a bone's transform to another one.

## 属性

### SourceBone
- **类型**: `FBoneReference`
- **描述**: Source Bone Name to get transform from

### TargetBone
- **类型**: `FBoneReference`
- **描述**: Name of bone to control. This is the main bone chain to modify from. *

### bCopyTranslation
- **类型**: `bool`

### bCopyRotation
- **类型**: `bool`

### bCopyScale
- **类型**: `bool`

### ControlSpace
- **类型**: `EBoneControlSpace`
- **描述**: Space to convert transforms into prior to copying components

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
FAnimNode_CopyBone& opAssign(FAnimNode_CopyBone Other)
```

