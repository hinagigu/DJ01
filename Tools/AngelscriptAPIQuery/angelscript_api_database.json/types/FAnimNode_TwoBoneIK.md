# FAnimNode_TwoBoneIK

Simple 2 Bone IK Controller.

## 属性

### IKBone
- **类型**: `FBoneReference`
- **描述**: Name of bone to control. This is the main bone chain to modify from. *

### StartStretchRatio
- **类型**: `float`
- **描述**: Limits to use if stretching is allowed. This value determines when to start stretch. For example, 0.9 means once it reaches 90% of the whole length of the limb, it will start apply.

### MaxStretchScale
- **类型**: `float`
- **描述**: Limits to use if stretching is allowed. This value determins what is the max stretch scale. For example, 1.5 means it will stretch until 150 % of the whole length of the limb.

### EffectorLocation
- **类型**: `FVector`

### EffectorTarget
- **类型**: `FBoneSocketTarget`

### JointTargetLocation
- **类型**: `FVector`

### JointTarget
- **类型**: `FBoneSocketTarget`

### TwistAxis
- **类型**: `FAxis`
- **描述**: Specify which axis it's aligned. Used when removing twist

### EffectorLocationSpace
- **类型**: `EBoneControlSpace`
- **描述**: Reference frame of Effector Location.

### JointTargetLocationSpace
- **类型**: `EBoneControlSpace`
- **描述**: Reference frame of Joint Target Location.

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

### bAllowStretching
- **类型**: `bool`

### bTakeRotationFromEffectorSpace
- **类型**: `bool`

### bMaintainEffectorRelRot
- **类型**: `bool`

### bAllowTwist
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FAnimNode_TwoBoneIK& opAssign(FAnimNode_TwoBoneIK Other)
```

