# FAnimNode_Constraint

Constraint node to parent or world transform for rotation/translation

## 属性

### BoneToModify
- **类型**: `FBoneReference`
- **描述**: Name of bone to control. This is the main bone chain to modify from. *

### ConstraintSetup
- **类型**: `TArray<FConstraint>`
- **描述**: List of constraints

### ConstraintWeights
- **类型**: `TArray<float32>`
- **描述**: Weight data - post edit syncs up to ConstraintSetups

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
FAnimNode_Constraint& opAssign(FAnimNode_Constraint Other)
```

