# UDrawPolygonToolStandardProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### PolygonDrawMode
- **类型**: `EDrawPolygonDrawMode`
- **描述**: Type of polygon to draw in the viewport

### bAllowSelfIntersections
- **类型**: `bool`
- **描述**: Allow freehand drawn polygons to self-intersect

### FeatureSizeRatio
- **类型**: `float32`
- **描述**: Size of secondary features, e.g. the rounded corners of a rounded rectangle, as fraction of the overall shape size

### RadialSlices
- **类型**: `int`
- **描述**: Number of radial subdivisions in round features, e.g. circles or rounded corners

### bShowGridGizmo
- **类型**: `bool`
- **描述**: If true, shows a gizmo to manipulate the additional grid used to draw the polygon on

### ExtrudeMode
- **类型**: `EDrawPolygonExtrudeMode`
- **描述**: If and how the drawn polygon gets extruded

### ExtrudeHeight
- **类型**: `float32`
- **描述**: Extrude distance when using the Fixed extrude mode

