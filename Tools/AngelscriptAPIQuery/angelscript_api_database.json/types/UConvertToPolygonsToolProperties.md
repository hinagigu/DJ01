# UConvertToPolygonsToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### ConversionMode
- **类型**: `EConvertToPolygonsMode`
- **描述**: Strategy to use to group triangles

### AngleTolerance
- **类型**: `float32`
- **描述**: Tolerance for planarity

### bUseAverageGroupNormal
- **类型**: `bool`
- **描述**: Whether to compute Face Normal Deviation based on the overall PolyGroup's average normal, or to only consider the normals of the individual triangles

### NumPoints
- **类型**: `int`
- **描述**: Furthest-Point Sample count, approximately this number of polygroups will be generated

### bSplitExisting
- **类型**: `bool`
- **描述**: If enabled, then furthest-point sampling happens with respect to existing Polygroups, ie the existing groups are further subdivided

### bNormalWeighted
- **类型**: `bool`
- **描述**: If true, region-growing in Sampling modes will be controlled by face normals, resulting in regions with borders that are more-aligned with curvature ridges

### NormalWeighting
- **类型**: `float32`
- **描述**: This parameter modulates the effect of normal weighting during region-growing

### QuadAdjacencyWeight
- **类型**: `float32`
- **描述**: Bias for Quads that are adjacent to already-discovered Quads. Set to 0 to disable.

### QuadMetricClamp
- **类型**: `float32`
- **描述**: Set to values below 1 to ignore less-likely triangle pairings

### QuadSearchRounds
- **类型**: `int`
- **描述**: Iteratively repeat quad-searching in uncertain areas, to try to slightly improve results

### bRespectUVSeams
- **类型**: `bool`
- **描述**: If true, polygroup borders will not cross existing UV seams

### bRespectHardNormals
- **类型**: `bool`
- **描述**: If true, polygroup borders will not cross existing hard normal seams

### MinGroupSize
- **类型**: `int`
- **描述**: group filtering

### bCalculateNormals
- **类型**: `bool`
- **描述**: If true, normals are recomputed per-group, with hard edges at group boundaries

### bShowGroupColors
- **类型**: `bool`
- **描述**: Display each group with a different auto-generated color

