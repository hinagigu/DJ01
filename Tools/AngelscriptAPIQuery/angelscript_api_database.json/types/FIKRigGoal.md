# FIKRigGoal

## 属性

### Name
- **类型**: `FName`

### TransformSource
- **类型**: `EIKRigGoalTransformSource`

### SourceBone
- **类型**: `FBoneReference`
- **描述**: When TransformSource is set to "Bone" mode, the Position and Rotation will be driven by this Bone's input transform.
When using a Bone as the transform source, the Position and Rotation Alpha values can still be set as desired.
But the PositionSpace and RotationSpace are no longer relevant and will not be used.

### Position
- **类型**: `FVector`

### Rotation
- **类型**: `FRotator`

### PositionAlpha
- **类型**: `float32`

### RotationAlpha
- **类型**: `float32`

### PositionSpace
- **类型**: `EIKRigGoalSpace`

### RotationSpace
- **类型**: `EIKRigGoalSpace`

## 方法

### opAssign
```angelscript
FIKRigGoal& opAssign(FIKRigGoal Other)
```

