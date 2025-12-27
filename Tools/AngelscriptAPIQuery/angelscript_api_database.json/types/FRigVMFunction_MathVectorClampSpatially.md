# FRigVMFunction_MathVectorClampSpatially

Clamps a position using a plane collision, cylindric collision or spherical collision.
The collision happens both towards an inner envelope (minimum) and towards an outer envelope (maximum).
You can disable the inner / outer envelope / collision by setting the minimum / maximum to 0.0.

## 属性

### Value
- **类型**: `FVector`

### Axis
- **类型**: `EAxis`

### Type
- **类型**: `ERigVMClampSpatialMode`

### Minimum
- **类型**: `float32`

### Maximum
- **类型**: `float32`

### Space
- **类型**: `FTransform`

### bDrawDebug
- **类型**: `bool`

### DebugColor
- **类型**: `FLinearColor`

### DebugThickness
- **类型**: `float32`

### Result
- **类型**: `FVector`

## 方法

### opAssign
```angelscript
FRigVMFunction_MathVectorClampSpatially& opAssign(FRigVMFunction_MathVectorClampSpatially Other)
```

