# UMaterialExpressionSparseVolumeTextureSample

**继承自**: `UMaterialExpressionSparseVolumeTextureBase`

Material expression for sampling from a runtime virtual texture.

## 属性

### SamplerSource
- **类型**: `ESamplerSourceMode`
- **描述**: Controls where the sampler for this texture lookup will come from.
Choose 'from texture asset' to make use of the USparseVolumeTexture addressing settings,
Otherwise use one of the global samplers, which will not consume a sampler slot.
This allows materials to use more than 16 unique textures on SM5 platforms.

