# USubUVAnimation

**继承自**: `UObject`

SubUV animation asset, which caches bounding geometry for regions in the SubUVTexture with non-zero opacity.
Particle emitters with a SubUV module which use this asset leverage the optimal bounding geometry to reduce overdraw.

## 属性

### SubUVTexture
- **类型**: `UTexture2D`
- **描述**: Texture to generate bounding geometry from.

### SubImages_Horizontal
- **类型**: `int`
- **描述**: The number of sub-images horizontally in the texture

### SubImages_Vertical
- **类型**: `int`
- **描述**: The number of sub-images vertically in the texture

### BoundingMode
- **类型**: `ESubUVBoundingVertexCount`
- **描述**: More bounding vertices results in reduced overdraw, but adds more triangle overhead.
The eight vertex mode is best used when the SubUV texture has a lot of space to cut out that is not captured by the four vertex version,
and when the particles using the texture will be few and large.

### OpacitySourceMode
- **类型**: `EOpacitySourceMode`

### AlphaThreshold
- **类型**: `float32`
- **描述**: Alpha channel values larger than the threshold are considered occupied and will be contained in the bounding geometry.
Raising this threshold slightly can reduce overdraw in particles using this animation asset.

