# UVolumeToMeshToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### bWeldEdges
- **类型**: `bool`
- **描述**: Weld coincident vertices and edges together in the resulting mesh to form a closed mesh surface.

### bAutoRepair
- **类型**: `bool`
- **描述**: If WeldEdges is enabled, attempt to fill any small holes or cracks in the resulting mesh to form a closed surface.

### bOptimizeMesh
- **类型**: `bool`
- **描述**: If WeldEdges is enabled, and after mesh generation is complete, flip edges in planar regions to improve triangle quality.

### bShowWireframe
- **类型**: `bool`
- **描述**: Show the wireframe of the resulting converted mesh geometry.

