# UMaterialExpressionMaterialXTextureSampleParameterBlur

**继承自**: `UMaterialExpressionTextureSampleParameter2D`

## 属性

### KernelSize
- **类型**: `EMAterialXTextureSampleBlurKernel`
- **描述**: The size of the blur kernel, relative to 0-1 UV space.

### FilterSize
- **类型**: `float32`
- **描述**: Size of the filter when we sample a texture coordinate

### FilterOffset
- **类型**: `float32`
- **描述**: Offset of the filter when we sample a texture coordinate

### Filter
- **类型**: `EMaterialXTextureSampleBlurFilter`
- **描述**: Filter to use when we blur a Texture: Gaussian or Box Linear filter

