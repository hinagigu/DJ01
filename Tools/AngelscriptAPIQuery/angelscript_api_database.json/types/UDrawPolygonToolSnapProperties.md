# UDrawPolygonToolSnapProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### bEnableSnapping
- **类型**: `bool`
- **描述**: Enables additional snapping controls. If false, all snapping is disabled.

### bSnapToVertices
- **类型**: `bool`
- **描述**: Snap to vertices in other meshes. Requires Enable Snapping to be true.

### bSnapToEdges
- **类型**: `bool`
- **描述**: Snap to edges in other meshes. Requires Enable Snapping to be true.

### bSnapToAxes
- **类型**: `bool`
- **描述**: Snap to axes of the drawing grid and axes relative to the last segment. Requires grid snapping to be disabled in viewport, and Enable Snapping to be true.

### bSnapToLengths
- **类型**: `bool`
- **描述**: When snapping to axes, also try to snap to the length of an existing segment in the polygon. Requires grid snapping to be disabled in viewport, and Snap to Axes and Enable Snapping to be true.

### bSnapToSurfaces
- **类型**: `bool`
- **描述**: Snap to surfaces of existing objects. Requires grid snapping to be disabled in viewport, and Enable Snapping to be true.

### SnapToSurfacesOffset
- **类型**: `float32`
- **描述**: Offset for snap point on the surface of an existing object in the direction of the surface normal. Requires grid snapping to be disabled in viewport, and Snap to Surfaces and Enable Snapping to be true.

