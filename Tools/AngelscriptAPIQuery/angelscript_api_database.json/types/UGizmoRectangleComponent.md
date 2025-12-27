# UGizmoRectangleComponent

**继承自**: `UGizmoBaseComponent`

Simple Component intended to be used as part of 3D Gizmos.
Draws outline of 3D rectangle based on parameters.

## 属性

### DirectionX
- **类型**: `FVector`

### DirectionY
- **类型**: `FVector`

### bOrientYAccordingToCamera
- **类型**: `bool`
- **描述**: When true, instead of using the provided DirectionY, the component will
use a direction orthogonal to the camera direction and DirectionX. This
keeps the rectangle pinned along DirectionX but spun to be flatter
relative the camera.

### OffsetX
- **类型**: `float32`

### OffsetY
- **类型**: `float32`

### LengthX
- **类型**: `float32`

### LengthY
- **类型**: `float32`

### Thickness
- **类型**: `float32`

### SegmentFlags
- **类型**: `uint8`

