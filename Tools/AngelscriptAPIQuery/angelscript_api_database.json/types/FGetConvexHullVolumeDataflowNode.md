# FGetConvexHullVolumeDataflowNode

Get the sum of volumes of the convex hulls on the selected nodes

## 属性

### bSumChildrenForClustersWithoutHulls
- **类型**: `bool`
- **描述**: For any cluster transform that has no convex hulls, whether to fall back to the convex hulls of the cluster's children. Otherwise, the cluster will not add to the total volume sum.

### bVolumeOfUnion
- **类型**: `bool`
- **描述**: Whether to take the volume of the union of selected hulls, rather than the sum of each hull volume separately. This is more expensive but more accurate when hulls overlap.

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FGetConvexHullVolumeDataflowNode& opAssign(FGetConvexHullVolumeDataflowNode Other)
```

