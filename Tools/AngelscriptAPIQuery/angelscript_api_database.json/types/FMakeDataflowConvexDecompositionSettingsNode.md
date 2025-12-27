# FMakeDataflowConvexDecompositionSettingsNode

Provide settings for running convex decomposition of geometry

## 属性

### MinSizeToDecompose
- **类型**: `float32`
- **描述**: If greater than zero, the minimum geometry size (cube root of volume) to consider for convex decomposition

### MaxGeoToHullVolumeRatioToDecompose
- **类型**: `float32`
- **描述**: If the geo volume / hull volume ratio is greater than this, do not consider convex decomposition

### ErrorTolerance
- **类型**: `float32`
- **描述**: Stop splitting when hulls have error less than this (expressed in cm; will be cubed for volumetric error).
Note: ErrorTolerance must be > 0 or MaxHullsPerGeometry > 1, or decomposition will not be performed.

### MaxHullsPerGeometry
- **类型**: `int`
- **描述**: If greater than zero, maximum number of convex hulls to use in each convex decomposition.
Note: ErrorTolerance must be > 0 or MaxHullsPerGeometry > 1, or decomposition will not be performed.

### MinThicknessTolerance
- **类型**: `float32`
- **描述**: Optionally specify a minimum thickness (in cm) for convex parts; parts below this thickness will always be merged away. Overrides NumOutputHulls and ErrorTolerance when needed.

### NumAdditionalSplits
- **类型**: `int`
- **描述**: Control the search effort spent per convex decomposition: larger values will require more computation but may find better convex decompositions

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FMakeDataflowConvexDecompositionSettingsNode& opAssign(FMakeDataflowConvexDecompositionSettingsNode Other)
```

