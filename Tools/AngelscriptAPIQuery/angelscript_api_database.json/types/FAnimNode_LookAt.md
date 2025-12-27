# FAnimNode_LookAt

Simple controller that make a bone to look at the point or another bone

## 属性

### BoneToModify
- **类型**: `FBoneReference`
- **描述**: Name of bone to control. This is the main bone chain to modify from. *

### LookAtTarget
- **类型**: `FBoneSocketTarget`
- **描述**: Target socket to look at. Used if LookAtBone is empty. - You can use  LookAtLocation if you need offset from this point. That location will be used in their local space. *

### LookAtLocation
- **类型**: `FVector`

### LookAt_Axis
- **类型**: `FAxis`

### bUseLookUpAxis
- **类型**: `bool`
- **描述**: Whether or not to use Look up axis

### InterpolationType
- **类型**: `EInterpolationBlend`

### LookUp_Axis
- **类型**: `FAxis`

### LookAtClamp
- **类型**: `float32`

### InterpolationTime
- **类型**: `float32`

### InterpolationTriggerThreashold
- **类型**: `float32`

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
FAnimNode_LookAt& opAssign(FAnimNode_LookAt Other)
```

