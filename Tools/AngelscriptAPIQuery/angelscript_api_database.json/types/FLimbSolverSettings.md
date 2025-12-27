# FLimbSolverSettings

## 属性

### ReachPrecision
- **类型**: `float32`
- **描述**: Precision (distance to the target)

### HingeRotationAxis
- **类型**: `EAxis`
- **描述**: Hinge Bones Rotation Axis. This is essentially the plane normal for (hip - knee - foot).

### MaxIterations
- **类型**: `int`
- **描述**: Number of Max Iterations to reach the target

### bEnableLimit
- **类型**: `bool`
- **描述**: Enable/Disable rotational limits

### MinRotationAngle
- **类型**: `float32`
- **描述**: Only used if bEnableRotationLimit is enabled. Prevents the leg from folding onto itself,
and forces at least this angle between Parent and Child bone.

### bAveragePull
- **类型**: `bool`
- **描述**: Pull averaging only has a visual impact when we have more than 2 bones (3 links).

### PullDistribution
- **类型**: `float32`
- **描述**: Re-position limb to distribute pull: 0 = foot, 0.5 = balanced, 1.f = hip

### ReachStepAlpha
- **类型**: `float32`
- **描述**: Move end effector towards target. If we are compressing the chain, limit displacement.

### bEnableTwistCorrection
- **类型**: `bool`
- **描述**: Enable Knee Twist correction, by comparing Foot FK with Foot IK orientation.

### EndBoneForwardAxis
- **类型**: `EAxis`
- **描述**: Forward Axis for Foot bone.

## 方法

### opAssign
```angelscript
FLimbSolverSettings& opAssign(FLimbSolverSettings Other)
```

