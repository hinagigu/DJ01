# UMeshTexturePaintingToolProperties

**继承自**: `UBrushBaseProperties`

## 属性

### PaintColor
- **类型**: `FLinearColor`
- **描述**: Color used for Applying Texture Color Painting

### EraseColor
- **类型**: `FLinearColor`
- **描述**: Color used for Erasing Texture Color Painting

### bWriteRed
- **类型**: `bool`
- **描述**: Whether or not to apply Texture Color Painting to the Red Channel

### bWriteGreen
- **类型**: `bool`
- **描述**: Whether or not to apply Texture Color Painting to the Green Channel

### bWriteBlue
- **类型**: `bool`
- **描述**: Whether or not to apply Texture Color Painting to the Blue Channel

### bWriteAlpha
- **类型**: `bool`
- **描述**: Whether or not to apply Texture Color Painting to the Alpha Channel

### UVChannel
- **类型**: `int`
- **描述**: UV channel which should be used for paint textures

### bEnableSeamPainting
- **类型**: `bool`
- **描述**: Seam painting flag, True if we should enable dilation to allow the painting of texture seams

### PaintTexture
- **类型**: `UTexture2D`
- **描述**: Texture to which Painting should be Applied

### PaintBrush
- **类型**: `UTexture2D`
- **描述**: Optional Texture Brush to which Painting should use

### PaintBrushRotationOffset
- **类型**: `float32`
- **描述**: Initial Rotation offset to apply to our paint brush

### bRotateBrushTowardsDirection
- **类型**: `bool`
- **描述**: Whether or not to continously rotate the brush towards the painting direction

### bEnableFlow
- **类型**: `bool`
- **描述**: Enables "Flow" painting where paint is continually applied from the brush every tick

### bOnlyFrontFacingTriangles
- **类型**: `bool`
- **描述**: Whether back-facing triangles should be ignored

