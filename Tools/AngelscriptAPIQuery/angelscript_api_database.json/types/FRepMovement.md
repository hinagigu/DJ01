# FRepMovement

Replicated movement data of our RootComponent.
Struct used for efficient replication as velocity and location are generally replicated together (this saves a repindex)
and velocity.Z is commonly zero (most position replications are for walking pawns).

## 属性

### LocationQuantizationLevel
- **类型**: `EVectorQuantization`
- **描述**: Allows tuning the compression level for the replicated location vector. You should only need to change this from the default if you see visual artifacts.

### VelocityQuantizationLevel
- **类型**: `EVectorQuantization`
- **描述**: Allows tuning the compression level for the replicated velocity vectors. You should only need to change this from the default if you see visual artifacts.

### RotationQuantizationLevel
- **类型**: `ERotatorQuantization`
- **描述**: Allows tuning the compression level for replicated rotation. You should only need to change this from the default if you see visual artifacts.

## 方法

### opAssign
```angelscript
FRepMovement& opAssign(FRepMovement Other)
```

