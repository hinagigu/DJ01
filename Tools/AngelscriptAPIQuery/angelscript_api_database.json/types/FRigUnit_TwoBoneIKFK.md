# FRigUnit_TwoBoneIKFK

## 属性

### StartJoint
- **类型**: `FName`

### EndJoint
- **类型**: `FName`

### PoleTarget
- **类型**: `FVector`

### Spin
- **类型**: `float32`

### EndEffector
- **类型**: `FTransform`

### IKBlend
- **类型**: `float32`

### StartJointFKTransform
- **类型**: `FTransform`
- **描述**: Transform : Start Joint FK Transform         # Transform for the Start Joint when in FK mode
Transform: Mid Joint FK Transform           # Transform for the Mid Joint when in FK mode
Transform : End Joint FK Transform          # Transform for the End Joint when in FK mode

### MidJointFKTransform
- **类型**: `FTransform`

### EndJointFKTransform
- **类型**: `FTransform`

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_TwoBoneIKFK& opAssign(FRigUnit_TwoBoneIKFK Other)
```

