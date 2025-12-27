# FRigUnit_MultiFABRIK

The FABRIK solver can solve multi chains within a root using multi effectors
the Forward and Backward Reaching Inverse Kinematics algorithm.
For now this node supports single effector chains only.

## 属性

### RootBone
- **类型**: `FName`

### Effectors
- **类型**: `TArray<FRigUnit_MultiFABRIK_EndEffector>`

### Precision
- **类型**: `float32`
- **描述**: The precision to use for the fabrik solver

### bPropagateToChildren
- **类型**: `bool`

### MaxIterations
- **类型**: `int`

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_MultiFABRIK& opAssign(FRigUnit_MultiFABRIK Other)
```

