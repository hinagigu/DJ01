# FRigUnit_GetTransform

GetTransform is used to retrieve a single transform from a hierarchy.

## 属性

### Item
- **类型**: `FRigElementKey`

### Space
- **类型**: `ERigVMTransformSpace`

### bInitial
- **类型**: `bool`

### Transform
- **类型**: `FTransform`
- **描述**: The current transform of the given item - or identity in case it wasn't found.

## 方法

### opAssign
```angelscript
FRigUnit_GetTransform& opAssign(FRigUnit_GetTransform Other)
```

