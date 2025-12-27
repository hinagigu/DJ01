# UGizmoCircleComponent

**继承自**: `UGizmoBaseComponent`

Simple Component intended to be used as part of 3D Gizmos.
Draws a 3D circle based on parameters.

## 属性

### Normal
- **类型**: `FVector`

### Radius
- **类型**: `float32`

### Thickness
- **类型**: `float32`

### NumSides
- **类型**: `int`

### bViewAligned
- **类型**: `bool`

### bDrawFullCircle
- **类型**: `bool`

### bOnlyAllowFrontFacingHits
- **类型**: `bool`
- **描述**: If the circle was on a 3D sphere, then only the 'front' part of the circle can be hit,
(in other words, if the ray would hit the sphere first, ignore the hit).
Dynamically disabled if the circle is parallel to the view plane (ie "fully visible")

