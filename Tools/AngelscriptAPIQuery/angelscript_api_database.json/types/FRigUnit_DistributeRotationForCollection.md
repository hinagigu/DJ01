# FRigUnit_DistributeRotationForCollection

Distributes rotations provided across a collection of items.
Each rotation is expressed by a quaternion and a ratio, where the ratio is between 0.0 and 1.0
Note: This node adds rotation in local space of each item!

## 属性

### Items
- **类型**: `FRigElementKeyCollection`

### Rotations
- **类型**: `TArray<FRigUnit_DistributeRotation_Rotation>`

### RotationEaseType
- **类型**: `ERigVMAnimEasingType`
- **描述**: The easing to use between to rotations.

### Weight
- **类型**: `float32`

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_DistributeRotationForCollection& opAssign(FRigUnit_DistributeRotationForCollection Other)
```

