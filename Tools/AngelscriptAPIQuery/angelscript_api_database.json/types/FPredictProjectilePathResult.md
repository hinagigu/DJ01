# FPredictProjectilePathResult

Container for the result of a projectile path trace (using PredictProjectilePath).

## 属性

### PathData
- **类型**: `TArray<FPredictProjectilePathPointData>`
- **描述**: Info for each point on the path.

### LastTraceDestination
- **类型**: `FPredictProjectilePathPointData`
- **描述**: Info on the last point we tried to trace to, which may have been beyond the final hit.

### HitResult
- **类型**: `FHitResult`
- **描述**: Hit along the trace, if tracing with collision was enabled.

## 方法

### opAssign
```angelscript
FPredictProjectilePathResult& opAssign(FPredictProjectilePathResult Other)
```

