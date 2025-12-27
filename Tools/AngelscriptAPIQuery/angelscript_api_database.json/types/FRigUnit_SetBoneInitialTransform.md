# FRigUnit_SetBoneInitialTransform

SetBoneInitialTransform is used to perform a change in the hierarchy by setting a single bone's transform.

## 属性

### Bone
- **类型**: `FName`

### Transform
- **类型**: `FTransform`

### Result
- **类型**: `FTransform`
- **描述**: The transform value result (after weighting)

### Space
- **类型**: `ERigVMTransformSpace`

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
FRigUnit_SetBoneInitialTransform& opAssign(FRigUnit_SetBoneInitialTransform Other)
```

