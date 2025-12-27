# UTextureImportSettings

**继承自**: `UDeveloperSettings`

## 属性

### AutoVTSize
- **类型**: `int`
- **描述**: Automatically enable the 'Virtual Texture Streaming' texture setting for textures larger than or equal to this size. This setting will not affect existing textures in the project.

### bEnableNormalizeNormals
- **类型**: `bool`
- **描述**: NormalizeNormals makes more correct normals in mip maps; it is recommended, but can be turned off to maintain legacy behavior. This setting is applied to newly imported textures, it does not affect existing textures in the project.

### bEnableFastMipFilter
- **类型**: `bool`
- **描述**: Use the fast mip filter on new textures; it is recommended, but can be turned off to maintain legacy behavior. This setting is applied to newly imported textures, it does not affect existing textures in the project.

### CompressedFormatForFloatTextures
- **类型**: `ETextureImportFloatingPointFormat`
- **描述**: Optionally use HDRCompressed (BC6H), or 32-bit adaptively, instead of HDR (RGBA16F) for floating point textures.  This setting is applied to newly imported textures, it does not affect existing textures in the project.

### PNGInfill
- **类型**: `ETextureImportPNGInfill`
- **描述**: Default behavior is to infill only for binary transparency; this setting may change that to always or never.  Will check TextureImporter/FillPNGZeroAlpha if this is not changed from Default.  This setting is applied to newly imported textures, it does not affect existing textures in the project.

