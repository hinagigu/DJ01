# FClusterMagnetDataflowNode

Cluster by grouping the selected bones with their adjacent, neighboring bones.

## 属性

### Iterations
- **类型**: `int`
- **描述**: How many layers of neighbors to include in the clusters -- i.e. if 1, only direct neighbors are clustered; if 2, neighbors of neighbors are included, etc.

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FClusterMagnetDataflowNode& opAssign(FClusterMagnetDataflowNode Other)
```

