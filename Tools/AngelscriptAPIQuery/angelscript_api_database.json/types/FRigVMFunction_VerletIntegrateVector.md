# FRigVMFunction_VerletIntegrateVector

Simulates a single position over time using Verlet integration. It is recommended to use SpringInterp instead as it
is more accurate and stable, and has more meaningful parameters.

## 属性

### Target
- **类型**: `FVector`

### Strength
- **类型**: `float32`

### Damp
- **类型**: `float32`

### Blend
- **类型**: `float32`

### Force
- **类型**: `FVector`

### Position
- **类型**: `FVector`

### Velocity
- **类型**: `FVector`

### Acceleration
- **类型**: `FVector`

## 方法

### opAssign
```angelscript
FRigVMFunction_VerletIntegrateVector& opAssign(FRigVMFunction_VerletIntegrateVector Other)
```

