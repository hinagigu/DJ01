# FGenerateStaticMeshLODProcess_CollisionSettings

## 属性

### CollisionType
- **类型**: `EGenerateStaticMeshLODSimpleCollisionGeometryType`
- **描述**: Type of simple collision objects to produce

### ConvexTriangleCount
- **类型**: `int`
- **描述**: Target triangle count for each convex hull after simplification

### bPrefilterVertices
- **类型**: `bool`
- **描述**: Whether to subsample input vertices using a regular grid before computing the convex hull

### PrefilterGridResolution
- **类型**: `int`
- **描述**: Grid resolution (along the maximum-length axis) for subsampling before computing the convex hull

### bSimplifyPolygons
- **类型**: `bool`
- **描述**: Whether to simplify polygons used for swept convex hulls

### HullTolerance
- **类型**: `float32`
- **描述**: Target minumum edge length for simplified swept convex hulls

### SweepAxis
- **类型**: `EGenerateStaticMeshLODProjectedHullAxisMode`
- **描述**: Which axis to sweep along when computing swept convex hulls

## 方法

### opAssign
```angelscript
FGenerateStaticMeshLODProcess_CollisionSettings& opAssign(FGenerateStaticMeshLODProcess_CollisionSettings Other)
```

