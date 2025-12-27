# FRigUnit_SetTransformItemArray

SetTransformArray is used to set an array of transforms on the hierarchy.

Note: For Controls when setting the initial transform this node
actually sets the Control's offset transform and resets the local
values to (0, 0, 0).

## 属性

### Items
- **类型**: `TArray<FRigElementKey>`

### Space
- **类型**: `ERigVMTransformSpace`

### bInitial
- **类型**: `bool`

### Transforms
- **类型**: `TArray<FTransform>`

### Weight
- **类型**: `float32`

### bPropagateToChildren
- **类型**: `bool`

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_SetTransformItemArray& opAssign(FRigUnit_SetTransformItemArray Other)
```

