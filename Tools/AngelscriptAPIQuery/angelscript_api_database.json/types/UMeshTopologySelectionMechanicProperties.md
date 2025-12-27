# UMeshTopologySelectionMechanicProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### bSelectVertices
- **类型**: `bool`

### bSelectEdges
- **类型**: `bool`

### bSelectFaces
- **类型**: `bool`

### bSelectEdgeLoops
- **类型**: `bool`
- **描述**: When true, will select edge loops. Edge loops are either paths through vertices with 4 edges, or boundaries of holes.

### bSelectEdgeRings
- **类型**: `bool`
- **描述**: When set, will select rings of edges that are opposite each other across a quad face.

### bHitBackFaces
- **类型**: `bool`
- **描述**: When set, faces that face away from the camera are ignored in selection and occlusion. Useful for working with inside-out meshes.

### bEnableMarquee
- **类型**: `bool`

### bMarqueeIgnoreOcclusion
- **类型**: `bool`
- **描述**: Determines whether vertices should be checked for occlusion in marquee select (Note: marquee select currently only works with edges and vertices)

### bPreferProjectedElement
- **类型**: `bool`
- **描述**: Prefer to select an edge projected to a point rather than the point, or a face projected to an edge rather than the edge.

### bSelectDownRay
- **类型**: `bool`
- **描述**: If the closest element is valid, select other elements behind it that are aligned with it.

### bIgnoreOcclusion
- **类型**: `bool`
- **描述**: Do not check whether the closest element is occluded from the current view.

