# FSimplifyConvexHullsDataflowNode

## 属性

### SimplifyMethod
- **类型**: `EConvexHullSimplifyMethod`

### SimplificationAngleThreshold
- **类型**: `float32`
- **描述**: Simplified hull should preserve angles larger than this (in degrees).  Used by the AngleTolerance simplification method.

### SimplificationDistanceThreshold
- **类型**: `float32`
- **描述**: Simplified hull should stay within this distance of the initial convex hull. Used by the MeshQSlim simplification method.

### MinTargetTriangleCount
- **类型**: `int`
- **描述**: The minimum number of faces to use for the convex hull. For MeshQSlim simplification, this is a triangle count, which may be further reduced on conversion back to a convex hull.

### bUseExistingVertices
- **类型**: `bool`
- **描述**: Whether to restrict the simplified hulls to only use vertices from the original hulls.

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FSimplifyConvexHullsDataflowNode& opAssign(FSimplifyConvexHullsDataflowNode Other)
```

