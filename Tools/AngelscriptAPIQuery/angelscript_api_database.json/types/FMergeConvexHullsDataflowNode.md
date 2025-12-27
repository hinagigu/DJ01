# FMergeConvexHullsDataflowNode

Merge convex hulls on transforms with multiple hulls

## 属性

### MaxConvexCount
- **类型**: `int`
- **描述**: Maximum number of convex to generate per transform. Ignored if < 0.

### ErrorTolerance
- **类型**: `float`
- **描述**: Error tolerance to use to decide to merge leaf convex together.
This is in centimeters and represents the side of a cube, the volume of which will be used as threshold
to know if the volume of the generated convex is too large compared to the sum of the volume of the leaf convex

### bProtectNegativeSpace
- **类型**: `bool`
- **描述**: Whether to use a sphere cover to define negative space that should not be covered by convex hulls

### bComputeNegativeSpacePerBone
- **类型**: `bool`
- **描述**: Whether to compute separate negative space for each bone. Otherwise, a single negative space will be computed once and re-used for all bones.

### SampleMethod
- **类型**: `ENegativeSpaceSampleMethodDataflowEnum`
- **描述**: Method to use to find and sample negative space

### bRequireSearchSampleCoverage
- **类型**: `bool`
- **描述**: Whether to require that all candidate locations identified by Voxel Search are covered by negative space samples, up to the specified Min Sample Spacing. Only applies to Voxel Search.

### bOnlyConnectedToHull
- **类型**: `bool`
- **描述**: When performing Voxel Search, only look for negative space that is connected out to the convex hull. This removes inaccessable internal negative space from consideration. Only applies to Voxel Search.

### TargetNumSamples
- **类型**: `int`
- **描述**: Approximate number of spheres to consider when covering negative space

### MinSampleSpacing
- **类型**: `float`
- **描述**: Minimum desired spacing between spheres; if > 0, will attempt not to place sphere centers closer than this

### NegativeSpaceTolerance
- **类型**: `float`
- **描述**: Amount of space to leave between convex hulls and protected negative space

### MinRadius
- **类型**: `float`
- **描述**: Spheres smaller than this are not included in the negative space

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FMergeConvexHullsDataflowNode& opAssign(FMergeConvexHullsDataflowNode Other)
```

