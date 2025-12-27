# UFractureRecomputeNormalsSettings

**继承自**: `UFractureToolSettings`

Settings for visualizing and recomputing normals and tangents

## 属性

### bShowNormals
- **类型**: `bool`
- **描述**: Whether to display normal vectors

### bShowTangents
- **类型**: `bool`
- **描述**: Whether to display tangent and bitangent vectors

### Length
- **类型**: `float32`
- **描述**: Length of display normal and tangent vectors

### bOnlyTangents
- **类型**: `bool`
- **描述**: Whether to only recompute tangents, and leave normals as they were

### bRecomputeSharpEdges
- **类型**: `bool`
- **描述**: If true, update where edges are 'sharp' by comparing adjacent triangle face normals vs the Sharp Edge Angle Threshold.

### SharpEdgeAngleThreshold
- **类型**: `float32`
- **描述**: Threshold on angle of change in face normals across an edge, above which we create a sharp edge if bRecomputeSharpEdges is true

### bOnlyInternalSurfaces
- **类型**: `bool`
- **描述**: Whether to only change internal surface normals / tangents

