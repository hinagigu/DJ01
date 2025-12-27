# FRigUnit_CCDIKPerItem

The CCID solver can solve N-Bone chains using
the Cyclic Coordinate Descent Inverse Kinematics algorithm.
For now this node supports single effector chains only.

## 属性

### Items
- **类型**: `FRigElementKeyCollection`

### EffectorTransform
- **类型**: `FTransform`

### Precision
- **类型**: `float32`
- **描述**: The precision to use for the fabrik solver

### Weight
- **类型**: `float32`

### MaxIterations
- **类型**: `int`

### bStartFromTail
- **类型**: `bool`
- **描述**: If set to true the direction of the solvers is flipped.

### BaseRotationLimit
- **类型**: `float32`
- **描述**: The general rotation limit to be applied to bones

### RotationLimits
- **类型**: `TArray<FRigUnit_CCDIK_RotationLimitPerItem>`
- **描述**: Defines the limits of rotation per bone.

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
FRigUnit_CCDIKPerItem& opAssign(FRigUnit_CCDIKPerItem Other)
```

