# FRigUnit_FitChainToSplineCurve

Fits a given chain to a spline curve.
Additionally provides rotational control matching the features of the Distribute Rotation node.

## 属性

### Items
- **类型**: `FRigElementKeyCollection`

### Spline
- **类型**: `FControlRigSpline`

### Alignment
- **类型**: `EControlRigCurveAlignment`
- **描述**: Specifies how to align the chain on the curve

### Minimum
- **类型**: `float32`
- **描述**: The minimum U value to use on the curve

### Maximum
- **类型**: `float32`
- **描述**: The maximum U value to use on the curve

### SamplingPrecision
- **类型**: `int`
- **描述**: The number of samples to use on the curve. Clamped at 64.

### PrimaryAxis
- **类型**: `FVector`

### SecondaryAxis
- **类型**: `FVector`

### PoleVectorPosition
- **类型**: `FVector`

### Rotations
- **类型**: `TArray<FRigUnit_FitChainToCurve_Rotation>`

### RotationEaseType
- **类型**: `ERigVMAnimEasingType`
- **描述**: The easing to use between to rotations.

### Weight
- **类型**: `float32`

### bPropagateToChildren
- **类型**: `bool`
- **描述**: If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

### DebugSettings
- **类型**: `FRigUnit_FitChainToCurve_DebugSettings`

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_FitChainToSplineCurve& opAssign(FRigUnit_FitChainToSplineCurve Other)
```

