# UProceduralRectangleToolProperties

**继承自**: `UProceduralShapeToolProperties`

## 属性

### RectangleType
- **类型**: `EProceduralRectType`
- **描述**: Type of rectangle

### Width
- **类型**: `float32`
- **描述**: Width of the rectangle

### Depth
- **类型**: `float32`
- **描述**: Depth of the rectangle

### WidthSubdivisions
- **类型**: `int`
- **描述**: Number of subdivisions along the width

### DepthSubdivisions
- **类型**: `int`
- **描述**: Number of subdivisions along the depth

### bMaintainDimension
- **类型**: `bool`
- **描述**: Whether to preserve the overall Width and Depth for a Rounded Rectangle, or to allow the rounded corners to extend outside those dimensions.

### CornerRadius
- **类型**: `float32`
- **描述**: Radius of rounded corners. This is only available for Rounded Rectangles.

### CornerSlices
- **类型**: `int`
- **描述**: Number of radial slices for each rounded corner. This is only available for Rounded Rectangles.

