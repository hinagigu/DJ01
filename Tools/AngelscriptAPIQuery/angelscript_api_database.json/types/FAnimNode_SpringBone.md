# FAnimNode_SpringBone

Simple controller that replaces or adds to the translation/rotation of a single bone.

## 属性

### SpringBone
- **类型**: `FBoneReference`
- **描述**: Name of bone to control. This is the main bone chain to modify from. *

### MaxDisplacement
- **类型**: `float`

### SpringStiffness
- **类型**: `float`
- **描述**: Stiffness of spring

### SpringDamping
- **类型**: `float`
- **描述**: Damping of spring

### ErrorResetThresh
- **类型**: `float`
- **描述**: If spring stretches more than this, reset it. Useful for catching teleports etc

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

### bLimitDisplacement
- **类型**: `bool`

### bTranslateX
- **类型**: `bool`

### bTranslateY
- **类型**: `bool`

### bTranslateZ
- **类型**: `bool`

### bRotateX
- **类型**: `bool`

### bRotateY
- **类型**: `bool`

### bRotateZ
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FAnimNode_SpringBone& opAssign(FAnimNode_SpringBone Other)
```

