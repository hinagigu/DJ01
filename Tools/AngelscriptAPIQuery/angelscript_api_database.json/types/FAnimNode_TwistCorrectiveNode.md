# FAnimNode_TwistCorrectiveNode

This is the node that apply corrective morphtarget for twist
Good example is that if you twist your neck too far right or left, you're going to see odd stretch shape of neck,
This node can detect the angle and apply morphtarget curve
This isn't the twist control node for bone twist

## 属性

### BaseFrame
- **类型**: `FReferenceBoneFrame`
- **描述**: Base Frame of the reference for the twist node

### TwistFrame
- **类型**: `FReferenceBoneFrame`
- **描述**: Transform component to use as input

### TwistPlaneNormalAxis
- **类型**: `FAxis`
- **描述**: Normal of the Plane that we'd like to calculate angle calculation from in BaseFrame. Please note we're looking for Normal Axis

### RangeMax
- **类型**: `float32`
- **描述**: Maximum limit of the input value (mapped to RemappedMax, only used when limiting the source range)
We can't go more than 180 right now because this is dot product driver

### RemappedMin
- **类型**: `float32`
- **描述**: Minimum value to apply to the destination (remapped from the input range)

### RemappedMax
- **类型**: `float32`
- **描述**: Maximum value to apply to the destination (remapped from the input range)

### CurveName
- **类型**: `FName`

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
FAnimNode_TwistCorrectiveNode& opAssign(FAnimNode_TwistCorrectiveNode Other)
```

