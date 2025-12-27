# FRigUnit_TwistBones

Creates a gradient of twist rotation along a chain.

## 属性

### StartBone
- **类型**: `FName`

### EndBone
- **类型**: `FName`

### TwistAxis
- **类型**: `FVector`
- **描述**: The axis to twist the bones around

### PoleAxis
- **类型**: `FVector`
- **描述**: The axis to use for the pole vector for each bone

### TwistEaseType
- **类型**: `ERigVMAnimEasingType`
- **描述**: The easing to use between two twists.

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
FRigUnit_TwistBones& opAssign(FRigUnit_TwistBones Other)
```

