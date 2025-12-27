# FRigUnit_GetControlInitialTransform

GetControlTransform is used to retrieve a single transform from a hierarchy.

## 属性

### Control
- **类型**: `FName`

### Space
- **类型**: `ERigVMTransformSpace`

### Transform
- **类型**: `FTransform`
- **描述**: The current transform of the given bone - or identity in case it wasn't found.

## 方法

### opAssign
```angelscript
FRigUnit_GetControlInitialTransform& opAssign(FRigUnit_GetControlInitialTransform Other)
```

