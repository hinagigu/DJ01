# FPredictProjectilePathParams

Input parameters to PredictProjectilePath functions.

## 属性

### StartLocation
- **类型**: `FVector`

### LaunchVelocity
- **类型**: `FVector`

### bTraceWithCollision
- **类型**: `bool`

### ProjectileRadius
- **类型**: `float32`

### MaxSimTime
- **类型**: `float32`

### bTraceWithChannel
- **类型**: `bool`

### TraceChannel
- **类型**: `ECollisionChannel`

### ObjectTypes
- **类型**: `TArray<EObjectTypeQuery>`

### ActorsToIgnore
- **类型**: `TArray<TObjectPtr<AActor>>`

### SimFrequency
- **类型**: `float32`

### OverrideGravityZ
- **类型**: `float32`

### DrawDebugType
- **类型**: `EDrawDebugTrace`

### DrawDebugTime
- **类型**: `float32`

### bTraceComplex
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FPredictProjectilePathParams& opAssign(FPredictProjectilePathParams Other)
```

