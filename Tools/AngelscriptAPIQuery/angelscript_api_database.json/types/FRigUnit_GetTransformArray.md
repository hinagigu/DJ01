# FRigUnit_GetTransformArray

GetTransformArray is used to retrieve an array of transforms from the hierarchy.

## 属性

### Items
- **类型**: `FRigElementKeyCollection`

### Space
- **类型**: `ERigVMTransformSpace`

### bInitial
- **类型**: `bool`

### Transforms
- **类型**: `TArray<FTransform>`
- **描述**: The current transform of the given item - or identity in case it wasn't found.

## 方法

### opAssign
```angelscript
FRigUnit_GetTransformArray& opAssign(FRigUnit_GetTransformArray Other)
```

