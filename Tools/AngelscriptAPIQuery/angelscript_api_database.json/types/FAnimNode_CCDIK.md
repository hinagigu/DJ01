# FAnimNode_CCDIK

Controller which implements the CCDIK IK approximation algorithm

## 属性

### EffectorLocation
- **类型**: `FVector`
- **描述**: Coordinates for target location of tip bone - if EffectorLocationSpace is bone, this is the offset from Target Bone to use as target location

### EffectorLocationSpace
- **类型**: `EBoneControlSpace`
- **描述**: Reference frame of Effector Transform.

### EffectorTarget
- **类型**: `FBoneSocketTarget`
- **描述**: If EffectorTransformSpace is a bone, this is the bone to use. *

### TipBone
- **类型**: `FBoneReference`
- **描述**: Name of tip bone

### RootBone
- **类型**: `FBoneReference`
- **描述**: Name of the root bone

### Precision
- **类型**: `float32`
- **描述**: Tolerance for final tip location delta from EffectorLocation

### MaxIterations
- **类型**: `int`
- **描述**: Maximum number of iterations allowed, to control performance.

### bStartFromTail
- **类型**: `bool`
- **描述**: Toggle drawing of axes to debug joint rotation

### bEnableRotationLimit
- **类型**: `bool`
- **描述**: Tolerance for final tip location delta from EffectorLocation

### RotationLimitPerJoints
- **类型**: `TArray<float32>`
- **描述**: symmetry rotation limit per joint. Index 0 matches with root bone and last index matches with tip bone.

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
FAnimNode_CCDIK& opAssign(FAnimNode_CCDIK Other)
```

