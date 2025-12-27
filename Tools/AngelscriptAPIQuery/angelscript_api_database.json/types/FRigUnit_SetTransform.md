# FRigUnit_SetTransform

SetTransform is used to set a single transform on hierarchy.

Note: For Controls when setting the initial transform this node
actually sets the Control's offset transform and resets the local
values to (0, 0, 0).

## 属性

### Item
- **类型**: `FRigElementKey`

### Space
- **类型**: `ERigVMTransformSpace`

### bInitial
- **类型**: `bool`

### Value
- **类型**: `FTransform`

### Weight
- **类型**: `float32`

### bPropagateToChildren
- **类型**: `bool`

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_SetTransform& opAssign(FRigUnit_SetTransform Other)
```

