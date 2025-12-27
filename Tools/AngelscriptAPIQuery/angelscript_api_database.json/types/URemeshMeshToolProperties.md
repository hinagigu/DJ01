# URemeshMeshToolProperties

**继承自**: `URemeshProperties`

Standard properties of the Remesh operation

## 属性

### TargetTriangleCount
- **类型**: `int`
- **描述**: Target triangle count

### SmoothingType
- **类型**: `ERemeshSmoothingType`
- **描述**: Smoothing type

### bDiscardAttributes
- **类型**: `bool`
- **描述**: Discard UVs and existing normals, allowing the remesher to ignore any UV and normal seams. New per-vertex normals are computed.

### bShowGroupColors
- **类型**: `bool`
- **描述**: Display colors corresponding to the mesh's polygon groups

### RemeshType
- **类型**: `ERemeshType`
- **描述**: Remeshing type

### RemeshIterations
- **类型**: `int`
- **描述**: Number of Remeshing passes

### MaxRemeshIterations
- **类型**: `int`
- **描述**: Maximum number of Remeshing passes, for Remeshers that have convergence criteria

### ExtraProjectionIterations
- **类型**: `int`
- **描述**: For NormalFlowRemesher: extra iterations of normal flow with no remeshing

### bUseTargetEdgeLength
- **类型**: `bool`
- **描述**: If true, the target count is ignored and the target edge length is used directly

### TargetEdgeLength
- **类型**: `float32`
- **描述**: Remesh to have edges approximately this length. An attempt at a reasonable value is computed automatically for this field based on the selected target mesh.

### bReproject
- **类型**: `bool`
- **描述**: Enable projection back to input mesh

### bReprojectConstraints
- **类型**: `bool`
- **描述**: Project constrained vertices back to original constraint curves

### BoundaryCornerAngleThreshold
- **类型**: `float32`
- **描述**: Angle threshold in degrees for classifying a boundary vertex as a corner. Corners will be fixed if Reproject Constraints is active.

