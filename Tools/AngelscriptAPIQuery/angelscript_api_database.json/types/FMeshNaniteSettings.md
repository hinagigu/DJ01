# FMeshNaniteSettings

Settings applied when building Nanite data.

## 属性

### PositionPrecision
- **类型**: `int`

### NormalPrecision
- **类型**: `int`

### TangentPrecision
- **类型**: `int`

### TargetMinimumResidencyInKB
- **类型**: `uint`
- **描述**: How much of the resource should always be resident (In KB). Approximate due to paging. 0: Minimum size (single page). MAX_uint32: Entire mesh.

### KeepPercentTriangles
- **类型**: `float32`

### TrimRelativeError
- **类型**: `float32`

### FallbackTarget
- **类型**: `ENaniteFallbackTarget`

### FallbackPercentTriangles
- **类型**: `float32`

### FallbackRelativeError
- **类型**: `float32`

### MaxEdgeLengthFactor
- **类型**: `float32`

### DisplacementUVChannel
- **类型**: `int`

### DisplacementMaps
- **类型**: `TArray<FMeshDisplacementMap>`

### bEnabled
- **类型**: `bool`

### bPreserveArea
- **类型**: `bool`

### bExplicitTangents
- **类型**: `bool`

### bLerpUVs
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FMeshNaniteSettings& opAssign(FMeshNaniteSettings Other)
```

