# FRigUnit_ModifyBoneTransforms

ModifyBonetransforms is used to perform a change in the hierarchy by setting one or more bones' transforms.

## 属性

### BoneToModify
- **类型**: `TArray<FRigUnit_ModifyBoneTransforms_PerBone>`

### Weight
- **类型**: `float32`

### WeightMinimum
- **类型**: `float32`
- **描述**: The minimum of the weight - defaults to 0.0

### WeightMaximum
- **类型**: `float32`
- **描述**: The maximum of the weight - defaults to 1.0

### Mode
- **类型**: `EControlRigModifyBoneMode`
- **描述**: Defines if the bone's transform should be set
in local or global space, additive or override.

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_ModifyBoneTransforms& opAssign(FRigUnit_ModifyBoneTransforms Other)
```

