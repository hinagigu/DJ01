# FAnimNode_HandIKRetargeting

Node to handle re-targeting of Hand IK bone chain.
It looks at position in Mesh Space of Left and Right FK bones, and moves Left and Right IK bones to those.
based on HandFKWeight. (0 = favor left hand, 1 = favor right hand, 0.5 = equal weight).
This is used so characters of different proportions can handle the same props.

## 属性

### RightHandFK
- **类型**: `FBoneReference`
- **描述**: Bone for Right Hand FK

### LeftHandFK
- **类型**: `FBoneReference`
- **描述**: Bone for Left Hand FK

### RightHandIK
- **类型**: `FBoneReference`
- **描述**: Bone for Right Hand IK

### LeftHandIK
- **类型**: `FBoneReference`
- **描述**: Bone for Left Hand IK

### IKBonesToMove
- **类型**: `TArray<FBoneReference>`
- **描述**: IK Bones to move.

### PerAxisAlpha
- **类型**: `FVector`

### HandFKWeight
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
FAnimNode_HandIKRetargeting& opAssign(FAnimNode_HandIKRetargeting Other)
```

