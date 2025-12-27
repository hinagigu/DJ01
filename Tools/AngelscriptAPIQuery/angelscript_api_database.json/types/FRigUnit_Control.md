# FRigUnit_Control

A control unit used to drive a transform from an external source

## 属性

### Transform
- **类型**: `FEulerTransform`

### Base
- **类型**: `FTransform`

### InitTransform
- **类型**: `FTransform`

### Result
- **类型**: `FTransform`
- **描述**: The resultant transform of this unit (Base * Filter(Transform))

### Filter
- **类型**: `FTransformFilter`

## 方法

### opAssign
```angelscript
FRigUnit_Control& opAssign(FRigUnit_Control Other)
```

