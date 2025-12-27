# FRigUnit_SetBoneTranslation

SetBoneTranslation is used to perform a change in the hierarchy by setting a single bone's Translation.

## 属性

### Bone
- **类型**: `FName`

### Translation
- **类型**: `FVector`

### Space
- **类型**: `ERigVMTransformSpace`

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
FRigUnit_SetBoneTranslation& opAssign(FRigUnit_SetBoneTranslation Other)
```

