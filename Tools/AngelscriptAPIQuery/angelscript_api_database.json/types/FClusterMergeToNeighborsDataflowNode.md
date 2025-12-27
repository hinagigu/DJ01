# FClusterMergeToNeighborsDataflowNode

Merge selected bones to their neighbors

## 属性

### NeighborSelectionMethod
- **类型**: `EClusterNeighborSelectionMethodEnum`
- **描述**: Method to choose which neighbor to merge

### MinVolumeCubeRoot
- **类型**: `float32`
- **描述**: Size (cube root of volume) of minimum desired post-merge clusters; if > 0, selected clusters may be merged multiple times until the cluster size is above this value

### bOnlyToConnected
- **类型**: `bool`
- **描述**: Whether to only allow clusters to merge if their bones are connected in the proximity graph

### bOnlySameParent
- **类型**: `bool`
- **描述**: Whether to only allow clusters to merge if they have the same parent bone

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FClusterMergeToNeighborsDataflowNode& opAssign(FClusterMergeToNeighborsDataflowNode Other)
```

