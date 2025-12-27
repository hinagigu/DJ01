# FRigUnit_AimBone

Aligns the rotation of a primary and secondary axis of a bone to a global target.
Note: This node operates in global space!

## 属性

### Bone
- **类型**: `FName`

### Primary
- **类型**: `FRigUnit_AimBone_Target`

### Secondary
- **类型**: `FRigUnit_AimBone_Target`

### Weight
- **类型**: `float32`

### bPropagateToChildren
- **类型**: `bool`
- **描述**: If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

### DebugSettings
- **类型**: `FRigUnit_AimBone_DebugSettings`

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_AimBone& opAssign(FRigUnit_AimBone Other)
```

