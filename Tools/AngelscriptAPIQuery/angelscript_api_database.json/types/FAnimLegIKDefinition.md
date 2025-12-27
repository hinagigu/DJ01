# FAnimLegIKDefinition

Per foot definitions

## 属性

### IKFootBone
- **类型**: `FBoneReference`

### FKFootBone
- **类型**: `FBoneReference`

### NumBonesInLimb
- **类型**: `int`

### MinRotationAngle
- **类型**: `float32`
- **描述**: Only used if bEnableRotationLimit is enabled. Prevents the leg from folding onto itself,
and forces at least this angle between Parent and Child bone.

### FootBoneForwardAxis
- **类型**: `EAxis`
- **描述**: Forward Axis for Foot bone.

### HingeRotationAxis
- **类型**: `EAxis`
- **描述**: Hinge Bones Rotation Axis. This is essentially the plane normal for (hip - knee - foot).

### bEnableRotationLimit
- **类型**: `bool`
- **描述**: If enabled, we prevent the leg from bending backwards and enforce a min compression angle

### bEnableKneeTwistCorrection
- **类型**: `bool`
- **描述**: Enable Knee Twist correction, by comparing Foot FK with Foot IK orientation.

### TwistOffsetCurveName
- **类型**: `FName`
- **描述**: Name of the curve to use as the twist offset angle(in degrees).
This is useful for injecting knee motion, while keeping the IK chain's goal/hand and root/hip locked in place.
Reasonable values are usually between -+15 degrees, although this is depends on how far in/out the knee is in the original pose.

## 方法

### opAssign
```angelscript
FAnimLegIKDefinition& opAssign(FAnimLegIKDefinition Other)
```

