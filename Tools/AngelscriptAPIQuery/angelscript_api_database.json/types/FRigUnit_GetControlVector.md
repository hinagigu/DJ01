# FRigUnit_GetControlVector

GetControlVector is used to retrieve a single Vector from a hierarchy, can be used for Controls of type "Position" or "Scale".

## 属性

### Control
- **类型**: `FName`

### Space
- **类型**: `ERigVMTransformSpace`

### Vector
- **类型**: `FVector`
- **描述**: The current value of the control.

### Minimum
- **类型**: `FVector`
- **描述**: The minimum value of the control.

### Maximum
- **类型**: `FVector`
- **描述**: The maximum value of the control.

## 方法

### opAssign
```angelscript
FRigUnit_GetControlVector& opAssign(FRigUnit_GetControlVector Other)
```

