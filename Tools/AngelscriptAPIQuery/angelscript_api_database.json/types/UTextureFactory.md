# UTextureFactory

**继承自**: `UFactory`

## 属性

### CompressionSettings
- **类型**: `TextureCompressionSettings`
- **描述**: Compression settings for the texture

### Blending
- **类型**: `EBlendMode`
- **描述**: The blend mode of the created material

### ShadingModel
- **类型**: `EMaterialShadingModel`
- **描述**: The shading model of the created material

### MipGenSettings
- **类型**: `TextureMipGenSettings`
- **描述**: The mip-map generation settings for the texture; Allows customization of the content of the mip-map chain

### LODGroup
- **类型**: `TextureGroup`
- **描述**: The group the texture belongs to

### bDoScaleMipsForAlphaCoverage
- **类型**: `bool`
- **描述**: Whether mip RGBA should be scaled to preserve the number of pixels with Value >= AlphaCoverageThresholds

### bUseNewMipFilter
- **类型**: `bool`
- **描述**: Whether to use newer & faster mip generation filter

### AlphaCoverageThresholds
- **类型**: `FVector4`
- **描述**: Channel values to compare to when preserving alpha coverage from a mask for mips

### NoAlpha
- **类型**: `bool`

### bDeferCompression
- **类型**: `bool`

### bCreateMaterial
- **类型**: `bool`

### bRGBToBaseColor
- **类型**: `bool`

### bRGBToEmissive
- **类型**: `bool`

### bAlphaToRoughness
- **类型**: `bool`

### bAlphaToEmissive
- **类型**: `bool`

### bAlphaToOpacity
- **类型**: `bool`

### bAlphaToOpacityMask
- **类型**: `bool`

### bTwoSided
- **类型**: `bool`

### bPreserveBorder
- **类型**: `bool`

### bFlipNormalMapGreenChannel
- **类型**: `bool`

