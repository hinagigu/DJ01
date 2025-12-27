# FRigVMSimPoint

## 属性

### Mass
- **类型**: `float32`
- **描述**: The mass of the point

### Size
- **类型**: `float32`
- **描述**: Size of the point - only used for collision

### LinearDamping
- **类型**: `float32`
- **描述**: The linear damping of the point

### InheritMotion
- **类型**: `float32`
- **描述**: Defines how much the point will inherit motion from its input.
This does not have an effect on passive (mass == 0.0) points.
Values can be higher than 1 due to timestep - but they are clamped internally.

### Position
- **类型**: `FVector`
- **描述**: The position of the point

### LinearVelocity
- **类型**: `FVector`
- **描述**: The velocity of the point per second

## 方法

### opAssign
```angelscript
FRigVMSimPoint& opAssign(FRigVMSimPoint Other)
```

