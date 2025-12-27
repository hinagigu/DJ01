# UDrawPolyPathProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### WidthMode
- **类型**: `EDrawPolyPathWidthMode`
- **描述**: How the drawn path width gets set

### Width
- **类型**: `float32`
- **描述**: Width of the drawn path when using Fixed width mode; also shows the width in Interactive width mode

### bRoundedCorners
- **类型**: `bool`
- **描述**: Use arc segments instead of straight lines in corners

### RadiusMode
- **类型**: `EDrawPolyPathRadiusMode`
- **描述**: How the rounded corner radius gets set

### CornerRadius
- **类型**: `float32`
- **描述**: Radius of the corner arcs, as a fraction of path width. This is only available if Rounded Corners is enabled.

### RadialSlices
- **类型**: `int`
- **描述**: Number of radial subdivisions for rounded corners

### bSinglePolyGroup
- **类型**: `bool`
- **描述**: If true, all quads on the path will belong to the same polygon. If false, each quad gets its own polygon.

### ExtrudeMode
- **类型**: `EDrawPolyPathExtrudeMode`
- **描述**: If and how the drawn path gets extruded

### ExtrudeHeight
- **类型**: `float32`
- **描述**: Extrusion distance when using the Fixed extrude modes; also shows the distance in Interactive extrude modes

### RampStartRatio
- **类型**: `float32`
- **描述**: Height of the start of the ramp as a fraction of the Extrude Height property

