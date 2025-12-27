# FAnimNode_RotationMultiplier

Simple controller that multiplies scalar value to the translation/rotation/scale of a single bone.

## 属性

### TargetBone
- **类型**: `FBoneReference`
- **描述**: Name of bone to control. This is the main bone chain to modify from.

### SourceBone
- **类型**: `FBoneReference`
- **描述**: Source to get transform from

### Multiplier
- **类型**: `float32`

### RotationAxisToRefer
- **类型**: `EBoneAxis`

### bIsAdditive
- **类型**: `bool`

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
FAnimNode_RotationMultiplier& opAssign(FAnimNode_RotationMultiplier Other)
```

