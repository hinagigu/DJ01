# FDJ01PenetrationAvoidanceFeeler

Struct defining a feeler ray used for camera penetration avoidance.

## 属性

### AdjustmentRot
- **类型**: `FRotator`
- **描述**: FRotator describing deviance from main ray

### WorldWeight
- **类型**: `float32`
- **描述**: how much this feeler affects the final position if it hits the world

### PawnWeight
- **类型**: `float32`
- **描述**: how much this feeler affects the final position if it hits a APawn (setting to 0 will not attempt to collide with pawns at all)

### Extent
- **类型**: `float32`
- **描述**: extent to use for collision when tracing this feeler

### TraceInterval
- **类型**: `int`
- **描述**: minimum frame interval between traces with this feeler if nothing was hit last frame

## 方法

### opAssign
```angelscript
FDJ01PenetrationAvoidanceFeeler& opAssign(FDJ01PenetrationAvoidanceFeeler Other)
```

