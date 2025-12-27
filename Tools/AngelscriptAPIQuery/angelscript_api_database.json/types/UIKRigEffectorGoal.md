# UIKRigEffectorGoal

**继承自**: `UObject`

## 属性

### GoalName
- **类型**: `FName`
- **描述**: The name used to refer to this goal from outside systems.
This is the name to use when referring to this Goal from Blueprint, Anim Graph, Control Rig or IK Retargeter.

### BoneName
- **类型**: `FName`
- **描述**: The name of the bone that this Goal is located at.

### PositionAlpha
- **类型**: `float32`

### RotationAlpha
- **类型**: `float32`

### CurrentTransform
- **类型**: `FTransform`

### InitialTransform
- **类型**: `FTransform`
- **描述**: The initial transform of this Goal, as defined by the initial transform of the Goal's bone in the retarget pose.

### PreviewMode
- **类型**: `EIKRigGoalPreviewMode`

### SizeMultiplier
- **类型**: `float32`

### ThicknessMultiplier
- **类型**: `float32`

### bExposePosition
- **类型**: `bool`

### bExposeRotation
- **类型**: `bool`

