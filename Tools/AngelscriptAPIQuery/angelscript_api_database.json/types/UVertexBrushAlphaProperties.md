# UVertexBrushAlphaProperties

**继承自**: `UInteractiveToolPropertySet`

Tool Properties for a brush alpha mask

## 属性

### Alpha
- **类型**: `UTexture2D`
- **描述**: Alpha mask applied to brush stamp. Red channel is used.

### RotationAngle
- **类型**: `float32`
- **描述**: Alpha is rotated by this angle, inside the brush stamp frame (vertically aligned)

### bRandomize
- **类型**: `bool`
- **描述**: If true, a random angle in +/- RandomRange is added to Rotation angle for each stamp

### RandomRange
- **类型**: `float32`
- **描述**: Bounds of random generation (positive and negative) for randomized stamps

