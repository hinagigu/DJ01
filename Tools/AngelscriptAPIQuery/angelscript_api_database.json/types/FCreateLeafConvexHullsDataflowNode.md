# FCreateLeafConvexHullsDataflowNode

## 属性

### GenerateMethod
- **类型**: `EGenerateConvexMethod`
- **描述**: How convex hulls are generated -- computed from geometry, imported from external collision shapes, or an intersection of both options.

### IntersectIfComputedIsSmallerByFactor
- **类型**: `float32`
- **描述**: If GenerateMethod is Intersect, only actually intersect when the volume of the Computed Hull is less than this fraction of the volume of the External Hull(s).

### MinExternalVolumeToIntersect
- **类型**: `float32`
- **描述**: If GenerateMethod is Intersect, only actually intersect if the volume of the External Hull(s) exceed this threshold.

### bComputeIntersectionsBeforeHull
- **类型**: `bool`
- **描述**: Whether to compute the intersection before computing convex hulls. Typically should be enabled.

### SimplificationDistanceThreshold
- **类型**: `float32`
- **描述**: Computed convex hulls are simplified to keep points spaced at least this far apart (except where needed to keep the hull from collapsing to zero volume).

### ConvexDecompositionSettings
- **类型**: `FDataflowConvexDecompositionSettings`

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FCreateLeafConvexHullsDataflowNode& opAssign(FCreateLeafConvexHullsDataflowNode Other)
```

