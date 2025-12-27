# UCSGMeshesToolProperties

**继承自**: `UInteractiveToolPropertySet`

Standard properties of the CSG operation

## 属性

### Operation
- **类型**: `ECSGOperation`
- **描述**: Type of Boolean operation

### bTryFixHoles
- **类型**: `bool`
- **描述**: Try to fill holes created by the Boolean operation, e.g. due to numerical errors

### bTryCollapseEdges
- **类型**: `bool`
- **描述**: Try to collapse extra edges created by the Boolean operation

### WindingThreshold
- **类型**: `float32`
- **描述**: Threshold to determine whether a triangle in one mesh is inside or outside of the other

### bShowNewBoundaries
- **类型**: `bool`
- **描述**: Show boundary edges created by the Boolean operation, which might happen due to numerical errors

### bShowSubtractedMesh
- **类型**: `bool`
- **描述**: Show a translucent version of the subtracted mesh, to help visualize geometry that is being removed

### SubtractedMeshOpacity
- **类型**: `float32`
- **描述**: Opacity of the translucent subtracted mesh

### SubtractedMeshColor
- **类型**: `FLinearColor`
- **描述**: Color of the translucent subtracted mesh

### bUseFirstMeshMaterials
- **类型**: `bool`
- **描述**: If true, only the first mesh will keep its material assignments, and all other faces will have the first material assigned

