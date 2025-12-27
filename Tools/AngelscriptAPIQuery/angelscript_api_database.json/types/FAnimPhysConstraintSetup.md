# FAnimPhysConstraintSetup

Constraint setup struct, holds data required to build a physics constraint

## 属性

### LinearXLimitType
- **类型**: `AnimPhysLinearConstraintType`
- **描述**: Whether to limit the linear X axis

### LinearYLimitType
- **类型**: `AnimPhysLinearConstraintType`
- **描述**: Whether to limit the linear Y axis

### LinearZLimitType
- **类型**: `AnimPhysLinearConstraintType`
- **描述**: Whether to limit the linear Z axis

### LinearAxesMin
- **类型**: `FVector`
- **描述**: Minimum linear movement per-axis (Set zero here and in the max limit to lock)

### LinearAxesMax
- **类型**: `FVector`
- **描述**: Maximum linear movement per-axis (Set zero here and in the min limit to lock)

### AngularConstraintType
- **类型**: `AnimPhysAngularConstraintType`
- **描述**: Method to use when constraining angular motion

### TwistAxis
- **类型**: `AnimPhysTwistAxis`
- **描述**: Axis to consider for twist when constraining angular motion (forward axis)

### AngularTargetAxis
- **类型**: `AnimPhysTwistAxis`
- **描述**: The axis in the simulation pose to align to the Angular Target.
This is typically the axis pointing along the bone.
Note: This is affected by the Angular Spring Constant.

### ConeAngle
- **类型**: `float32`
- **描述**: Angle to use when constraining using a cone

### AngularLimitsMin
- **类型**: `FVector`

### AngularLimitsMax
- **类型**: `FVector`

### AngularTarget
- **类型**: `FVector`
- **描述**: The axis to align the angular spring constraint to in the animation pose.
This typically points down the bone - so values of (1.0, 0.0, 0.0) are common,
but you can pick other values to align the spring to a different direction.
Note: This is affected by the Angular Spring Constant.

## 方法

### opAssign
```angelscript
FAnimPhysConstraintSetup& opAssign(FAnimPhysConstraintSetup Other)
```

