# FRigUnit_FABRIKItemArray

The FABRIK solver can solve N-Bone chains using
the Forward and Backward Reaching Inverse Kinematics algorithm.
For now this node supports single effector chains only.

## 属性

### Items
- **类型**: `TArray<FRigElementKey>`

### EffectorTransform
- **类型**: `FTransform`

### Precision
- **类型**: `float32`
- **描述**: The precision to use for the fabrik solver

### Weight
- **类型**: `float32`

### bPropagateToChildren
- **类型**: `bool`
- **描述**: If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

### MaxIterations
- **类型**: `int`

### bSetEffectorTransform
- **类型**: `bool`

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_FABRIKItemArray& opAssign(FRigUnit_FABRIKItemArray Other)
```

