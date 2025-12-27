# UVectorFieldAnimated

**继承自**: `UVectorField`

## 属性

### Texture
- **类型**: `UTexture2D`
- **描述**: The texture from which to create the vector field.

### ConstructionOp
- **类型**: `EVectorFieldConstructionOp`
- **描述**: The operation used to construct the vector field.

### VolumeSizeX
- **类型**: `int`
- **描述**: The size of the volume. Valid sizes: 16, 32, 64.

### VolumeSizeY
- **类型**: `int`
- **描述**: The size of the volume. Valid sizes: 16, 32, 64.

### VolumeSizeZ
- **类型**: `int`
- **描述**: The size of the volume. Valid sizes: 16, 32, 64.

### SubImagesX
- **类型**: `int`
- **描述**: The number of horizontal subimages in the texture atlas.

### SubImagesY
- **类型**: `int`
- **描述**: The number of vertical subimages in the texture atlas.

### FrameCount
- **类型**: `int`
- **描述**: The number of frames in the atlas.

### FramesPerSecond
- **类型**: `float32`
- **描述**: The rate at which to interpolate between frames.

### NoiseField
- **类型**: `UVectorFieldStatic`
- **描述**: A static vector field used to add noise.

### NoiseScale
- **类型**: `float32`
- **描述**: Scale to apply to vectors in the noise field.

### NoiseMax
- **类型**: `float32`
- **描述**: The maximum magnitude of noise vectors to apply.

### bLoop
- **类型**: `bool`

