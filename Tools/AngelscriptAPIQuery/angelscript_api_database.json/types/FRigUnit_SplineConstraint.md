# FRigUnit_SplineConstraint

Fits a given chain to a spline curve.
Additionally provides rotational control matching the features of the Distribute Rotation node.

## 属性

### Items
- **类型**: `TArray<FRigElementKey>`

### Spline
- **类型**: `FControlRigSpline`

### Alignment
- **类型**: `EControlRigCurveAlignment`
- **描述**: Specifies how to align the chain on the curve

### Minimum
- **类型**: `float32`

### Maximum
- **类型**: `float32`

### PrimaryAxis
- **类型**: `FVector`

### SecondaryAxis
- **类型**: `FVector`

### bPropagateToChildren
- **类型**: `bool`
- **描述**: If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_SplineConstraint& opAssign(FRigUnit_SplineConstraint Other)
```

