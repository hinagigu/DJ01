# FAnimNode_LegIK

## 属性

### ReachPrecision
- **类型**: `float32`
- **描述**: Tolerance for reaching IK Target, in unreal units.

### MaxIterations
- **类型**: `int`
- **描述**: Max Number of Iterations.

### SoftPercentLength
- **类型**: `float32`
- **描述**: Default is 1.0 (off). Range is 0.1 to 1.0. When set to a value less than 1, will "softly" approach full extension starting when the effector
distance from the root of the chain is greater than this percent length of the bone chain. Typical values are around 0.97.
This is useful for preventing the knee from "popping" when approaching full extension.

### SoftAlpha
- **类型**: `float32`
- **描述**: Default is 1.0 (full). Range is 0 to 1. Blends the effect of the "softness" on/off.

### LegsDefinition
- **类型**: `TArray<FAnimLegIKDefinition>`

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
FAnimNode_LegIK& opAssign(FAnimNode_LegIK Other)
```

