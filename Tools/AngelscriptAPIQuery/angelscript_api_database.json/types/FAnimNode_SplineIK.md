# FAnimNode_SplineIK

## 属性

### StartBone
- **类型**: `FBoneReference`
- **描述**: Name of root bone from which the spline extends *

### EndBone
- **类型**: `FBoneReference`
- **描述**: Name of bone at the end of the spline chain. Bones after this will not be altered by the controller.

### BoneAxis
- **类型**: `ESplineBoneAxis`
- **描述**: Axis of the controlled bone (ie the direction of the spline) to use as the direction for the curve.

### bAutoCalculateSpline
- **类型**: `bool`
- **描述**: The number of points in the spline if we are specifying it directly

### PointCount
- **类型**: `int`
- **描述**: The number of points in the spline if we are not auto-calculating

### ControlPoints
- **类型**: `TArray<FTransform>`

### Roll
- **类型**: `float32`

### TwistStart
- **类型**: `float32`

### TwistEnd
- **类型**: `float32`

### TwistBlend
- **类型**: `FAlphaBlend`
- **描述**: How to interpolate twist along the length of the spline

### Stretch
- **类型**: `float32`

### Offset
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
FAnimNode_SplineIK& opAssign(FAnimNode_SplineIK Other)
```

