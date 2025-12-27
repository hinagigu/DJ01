# FHierarchicalSimplification

## 属性

### TransitionScreenSize
- **类型**: `float32`
- **描述**: The screen radius an mesh object should reach before swapping to the LOD actor, once one of parent displays, it won't draw any of children.

### OverrideDrawDistance
- **类型**: `float32`

### SimplificationMethod
- **类型**: `EHierarchicalSimplificationMethod`

### ProxySetting
- **类型**: `FMeshProxySettings`
- **描述**: Simplification settings, used if SimplificationMethod is Simplify

### MergeSetting
- **类型**: `FMeshMergingSettings`
- **描述**: Merge settings, used if SimplificationMethod is Merge

### ApproximateSettings
- **类型**: `FMeshApproximationSettings`
- **描述**: Approximate settings, used if SimplificationMethod is Approximate

### DesiredBoundRadius
- **类型**: `float32`
- **描述**: Desired Bounding Radius for clustering - this is not guaranteed but used to calculate filling factor for auto clustering

### DesiredFillingPercentage
- **类型**: `float32`
- **描述**: Desired Filling Percentage for clustering - this is not guaranteed but used to calculate filling factor  for auto clustering

### MinNumberOfActorsToBuild
- **类型**: `int`
- **描述**: Min number of actors to build LODActor

### bUseOverrideDrawDistance
- **类型**: `bool`

### bAllowSpecificExclusion
- **类型**: `bool`

### bOnlyGenerateClustersForVolumes
- **类型**: `bool`

### bReusePreviousLevelClusters
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FHierarchicalSimplification& opAssign(FHierarchicalSimplification Other)
```

