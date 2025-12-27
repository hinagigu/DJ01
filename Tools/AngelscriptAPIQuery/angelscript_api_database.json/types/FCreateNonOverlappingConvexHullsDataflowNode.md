# FCreateNonOverlappingConvexHullsDataflowNode

Generates convex hull representation for the bones for simulation

## 属性

### CanExceedFraction
- **类型**: `float32`
- **描述**: Fraction (of geometry volume) by which a cluster's convex hull volume can exceed the actual geometry volume before instead using the hulls of the children.  0 means the convex volume cannot exceed the geometry volume; 1 means the convex volume is allowed to be 100% larger (2x) the geometry volume.

### SimplificationDistanceThreshold
- **类型**: `float32`
- **描述**: Computed convex hulls are simplified to keep points spaced at least this far apart (except where needed to keep the hull from collapsing to zero volume)

### OverlapRemovalMethod
- **类型**: `EConvexOverlapRemovalMethodEnum`
- **描述**: Whether and in what cases to automatically cut away overlapping parts of the convex hulls, to avoid the simulation 'popping' to fix the overlaps

### OverlapRemovalShrinkPercent
- **类型**: `float32`
- **描述**: Overlap removal will be computed as if convex hulls were this percentage smaller (in range 0-100)

### CanRemoveFraction
- **类型**: `float32`
- **描述**: Fraction of the convex hulls for a cluster that we can remove before using the hulls of the children

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FCreateNonOverlappingConvexHullsDataflowNode& opAssign(FCreateNonOverlappingConvexHullsDataflowNode Other)
```

