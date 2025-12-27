# FRigUnit_TwoBoneIKSimplePerItem

Solves the two bone IK given two bones.
Note: This node operates in world space!

## 属性

### ItemA
- **类型**: `FRigElementKey`

### ItemB
- **类型**: `FRigElementKey`

### EffectorItem
- **类型**: `FRigElementKey`

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
- **类型**: `FRigElementKey`

### bEnableStretch
- **类型**: `bool`

### StretchStartRatio
- **类型**: `float32`

### StretchMaximumRatio
- **类型**: `float32`

### Weight
- **类型**: `float32`

### ItemALength
- **类型**: `float32`

### ItemBLength
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
FRigUnit_TwoBoneIKSimplePerItem& opAssign(FRigUnit_TwoBoneIKSimplePerItem Other)
```

