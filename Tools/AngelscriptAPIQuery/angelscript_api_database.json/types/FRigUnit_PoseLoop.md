# FRigUnit_PoseLoop

Given a pose, execute iteratively across all items in the pose

## 属性

### Pose
- **类型**: `FRigPose`

### Item
- **类型**: `FRigElementKey`

### GlobalTransform
- **类型**: `FTransform`

### LocalTransform
- **类型**: `FTransform`

### CurveValue
- **类型**: `float32`

### Index
- **类型**: `int`

### Count
- **类型**: `int`

### Ratio
- **类型**: `float32`
- **描述**: Ranging from 0.0 (first item) and 1.0 (last item)
This is useful to drive a consecutive node with a
curve or an ease to distribute a value.

### Completed
- **类型**: `FControlRigExecuteContext`

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_PoseLoop& opAssign(FRigUnit_PoseLoop Other)
```

