# USimplifyMeshToolProperties

**继承自**: `UMeshConstraintProperties`

Standard properties of the Simplify operation

## 属性

### SimplifierType
- **类型**: `ESimplifyType`
- **描述**: Simplification Scheme

### TargetMode
- **类型**: `ESimplifyTargetType`
- **描述**: Simplification Target Type

### TargetPercentage
- **类型**: `int`
- **描述**: Target percentage of original triangle count

### TargetEdgeLength
- **类型**: `float32`
- **描述**: Target edge length

### TargetTriangleCount
- **类型**: `int`
- **描述**: Target triangle count

### TargetVertexCount
- **类型**: `int`
- **描述**: Target vertex count

### PolyEdgeAngleTolerance
- **类型**: `float32`
- **描述**: Threshold angle change (in degrees) along a polygroup edge, above which a vertex must be added

### bDiscardAttributes
- **类型**: `bool`
- **描述**: Discard UVs and existing normals, allowing the simplifier to ignore any UV and normal seams. New per-vertex normals are computed.

### bGeometricConstraint
- **类型**: `bool`
- **描述**: If true, then simplification will consider geometric deviation with the input mesh

### GeometricTolerance
- **类型**: `float32`
- **描述**: Geometric deviation tolerance used when bGeometricConstraint is enabled, to limit the geometric deviation between the simplified and original meshes

### bShowGroupColors
- **类型**: `bool`
- **描述**: Display colors corresponding to the mesh's polygon groups

### bReproject
- **类型**: `bool`
- **描述**: Enable projection back to input mesh

