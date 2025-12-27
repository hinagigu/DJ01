# UFractureAutoClusterSettings

**继承自**: `UFractureToolSettings`

## 属性

### ClusterSizeMethod
- **类型**: `EClusterSizeMethod`
- **描述**: How to choose the size of the clusters to create

### SiteCount
- **类型**: `uint`
- **描述**: Use a Voronoi diagram with this many Voronoi sites as a guide for deciding cluster boundaries

### SiteCountFraction
- **类型**: `float32`
- **描述**: Choose the number of Voronoi sites used for clustering as a fraction of the number of child bones to process

### SiteSize
- **类型**: `float32`
- **描述**: Choose the Edge-Size of the cube used to groups bones under a cluster (in cm).

### ClusterGridWidth
- **类型**: `int`
- **描述**: Choose the number of cluster sites to distribute along the X axis

### ClusterGridDepth
- **类型**: `int`
- **描述**: Choose the number of cluster sites to distribute along the Y axis

### ClusterGridHeight
- **类型**: `int`
- **描述**: Choose the number of cluster sites to distribute along the Z axis

### bShowGridLines
- **类型**: `bool`
- **描述**: If true, show the cluster grid boundary lines.

### MinimumSize
- **类型**: `float32`
- **描述**: If a cluster has volume less than this value (in cm) cubed, then the auto-cluster process will attempt to merge it into a neighboring cluster.

### DriftIterations
- **类型**: `int`
- **描述**: For a grid distribution, optionally iteratively recenter the grid points to the center of the cluster geometry (technically: applying K-Means iterations) to balance the shape and distribution of the clusters

### bPreferConvexity
- **类型**: `bool`
- **描述**: Whether to favor clusters that have a convex shape. (Note: Does not support ByGrid clustering.)

### ConcavityTolerance
- **类型**: `float`
- **描述**: If > 0, cube root of maximum concave volume to add per cluster (ignoring concavity of individual parts)

### bEnforceConnectivity
- **类型**: `bool`
- **描述**: If true, bones will only be added to the same cluster if they are physically connected (either directly, or via other bones in the same cluster)

### bEnforceSiteParameters
- **类型**: `bool`
- **描述**: If true, make sure the site parameters are matched as close as possible ( bEnforceConnectivity can make the number of site larger than the requested input may produce without it )

### bAvoidIsolated
- **类型**: `bool`
- **描述**: If true, prevent the creation of clusters with only a single child, skipping creation of a new cluster in such cases.

