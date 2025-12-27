# USelfUnionMeshesToolProperties

**继承自**: `UInteractiveToolPropertySet`

Standard properties of the self-union operation

## 属性

### bTrimFlaps
- **类型**: `bool`
- **描述**: If true, remove open, visible geometry

### bTryFixHoles
- **类型**: `bool`
- **描述**: Try to fill holes created by the merge, e.g. due to numerical errors

### bTryCollapseEdges
- **类型**: `bool`
- **描述**: Try to collapse extra edges created by the merge

### WindingThreshold
- **类型**: `float32`
- **描述**: Threshold to determine whether a triangle in one mesh is inside or outside of the other

### bShowNewBoundaryEdges
- **类型**: `bool`
- **描述**: Show boundary edges created by the merge (often due to numerical error)

### bOnlyUseFirstMeshMaterials
- **类型**: `bool`
- **描述**: If true, only the first mesh will keep its materials assignments; all other triangles will be assigned material 0

