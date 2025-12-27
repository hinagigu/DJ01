# FRigUnit_DistributeRotation

Distributes rotations provided along a chain.
Each rotation is expressed by a quaternion and a ratio, where the ratio is between 0.0 and 1.0
Note: This node adds rotation in local space of each bone!

## 属性

### StartBone
- **类型**: `FName`

### EndBone
- **类型**: `FName`

### Rotations
- **类型**: `TArray<FRigUnit_DistributeRotation_Rotation>`

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

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_DistributeRotation& opAssign(FRigUnit_DistributeRotation Other)
```

