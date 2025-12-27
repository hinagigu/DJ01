# FAnimNode_Fabrik

Controller which implements the FABRIK IK approximation algorithm -  see http://www.academia.edu/9165835/FABRIK_A_fast_iterative_solver_for_the_Inverse_Kinematics_problem for details

## 属性

### EffectorTransform
- **类型**: `FTransform`

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

### EffectorTransformSpace
- **类型**: `EBoneControlSpace`
- **描述**: Reference frame of Effector Transform.

### EffectorRotationSource
- **类型**: `EBoneRotationSource`

### bEnableDebugDraw
- **类型**: `bool`
- **描述**: Toggle drawing of axes to debug joint rotation

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
FAnimNode_Fabrik& opAssign(FAnimNode_Fabrik Other)
```

