# UMaterialExpressionTextureSample

**继承自**: `UMaterialExpressionTextureBase`

## 属性

### MipValueMode
- **类型**: `ETextureMipValueMode`
- **描述**: Defines how the MipValue property is applied to the texture lookup

### SamplerSource
- **类型**: `ESamplerSourceMode`
- **描述**: Controls where the sampler for this texture lookup will come from.
Choose 'from texture asset' to make use of the UTexture addressing settings,
Otherwise use one of the global samplers, which will not consume a sampler slot.
This allows materials to use more than 16 unique textures on SM5 platforms.

### ConstCoordinate
- **类型**: `uint8`
- **描述**: only used if Coordinates is not hooked up

### ConstMipValue
- **类型**: `int`
- **描述**: only used if MipValue is not hooked up

### AutomaticViewMipBias
- **类型**: `bool`

