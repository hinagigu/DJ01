# UFractureConvexSettings

**继承自**: `UFractureToolSettings`

Settings controlling how convex hulls are generated for geometry collections

## 属性

### CanExceedFraction
- **类型**: `float`
- **描述**: Fraction (of geometry volume) by which a cluster's convex hull volume can exceed the actual geometry volume before instead using the hulls of the children.  0 means the convex volume cannot exceed the geometry volume; 1 means the convex volume is allowed to be 100% larger (2x) the geometry volume.

### SimplificationDistanceThreshold
- **类型**: `float`
- **描述**: We simplify the convex shape to keep points spaced at least this far apart (except to keep the hull from collapsing to zero volume)

### RemoveOverlaps
- **类型**: `EConvexOverlapRemoval`
- **描述**: Whether to automatically cut away overlapping parts of the convex hulls, to avoid the simulation 'popping' to fix the overlaps

### OverlapRemovalShrinkPercent
- **类型**: `float`
- **描述**: Overlap removal will be computed as if convex hulls were this percentage smaller (in range 0-100)

### FractionAllowRemove
- **类型**: `float`
- **描述**: Fraction of the convex hulls for a cluster that we can remove before using the hulls of the children

### bSeeThroughLines
- **类型**: `bool`
- **描述**: When enabled, convex visualization lines will show through the actual geometry

### LineThickness
- **类型**: `float32`
- **描述**: line thickness

