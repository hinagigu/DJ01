# FRigUnit_TwoBoneIKSimple

Solves the two bone IK given two bones.
Note: This node operates in world space!

## 属性

### BoneA
- **类型**: `FName`

### BoneB
- **类型**: `FName`

### EffectorBone
- **类型**: `FName`

### Effector
- **类型**: `FTransform`

### PrimaryAxis
- **类型**: `FVector`

### SecondaryAxis
- **类型**: `FVector`

### SecondaryAxisWeight
- **类型**: `float32`

### PoleVector
- **类型**: `FVector`

### PoleVectorKind
- **类型**: `EControlRigVectorKind`

### PoleVectorSpace
- **类型**: `FName`

### bEnableStretch
- **类型**: `bool`

### StretchStartRatio
- **类型**: `float32`

### StretchMaximumRatio
- **类型**: `float32`

### Weight
- **类型**: `float32`

### BoneALength
- **类型**: `float32`

### BoneBLength
- **类型**: `float32`

### bPropagateToChildren
- **类型**: `bool`
- **描述**: If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

### DebugSettings
- **类型**: `FRigUnit_TwoBoneIKSimple_DebugSettings`

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_TwoBoneIKSimple& opAssign(FRigUnit_TwoBoneIKSimple Other)
```

