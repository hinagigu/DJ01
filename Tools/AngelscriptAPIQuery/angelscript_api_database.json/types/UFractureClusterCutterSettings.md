# UFractureClusterCutterSettings

**继承自**: `UFractureToolSettings`

## 属性

### NumberClustersMin
- **类型**: `int`
- **描述**: Minimum number of clusters of Voronoi sites to create. The amount of clusters created will be chosen at random between Min and Max

### NumberClustersMax
- **类型**: `int`
- **描述**: Maximum number of clusters of Voronoi sites to create. The amount of clusters created will be chosen at random between Min and Max

### SitesPerClusterMin
- **类型**: `int`
- **描述**: Minimum number of Voronoi sites per cluster. The amount of sites in each cluster will be chosen at random between Min and Max

### SitesPerClusterMax
- **类型**: `int`
- **描述**: Maximum number of Voronoi sites per cluster. The amount of sites in each cluster will be chosen at random between Min and Max

### ClusterRadiusFractionMin
- **类型**: `float32`
- **描述**: Minimum cluster radius (as fraction of the overall Voronoi diagram size). Cluster Radius Offset will be added to this
Each Voronoi site will be placed at least this far (plus the Cluster Radius Offset) from its cluster center

### ClusterRadiusFractionMax
- **类型**: `float32`
- **描述**: Maximum cluster radius (as fraction of the overall Voronoi diagram size). Cluster Radius Offset will be added to this
Each Voronoi site will be placed at most this far (plus the Cluster Radius Offset) from its cluster center

### ClusterRadiusOffset
- **类型**: `float32`
- **描述**: Cluster radius offset (in cm). This offset will be added to the 'Min/Max Dist from Center' distance

