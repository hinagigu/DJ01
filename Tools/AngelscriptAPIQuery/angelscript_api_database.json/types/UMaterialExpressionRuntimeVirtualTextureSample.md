# UMaterialExpressionRuntimeVirtualTextureSample

**继承自**: `UMaterialExpression`

Material expression for sampling from a runtime virtual texture.

## 属性

### VirtualTexture
- **类型**: `URuntimeVirtualTexture`
- **描述**: The virtual texture object to sample.

### MaterialType
- **类型**: `ERuntimeVirtualTextureMaterialType`
- **描述**: How to interpret the virtual texture contents. Note that the bound Virtual Texture should have the same setting for sampling to work correctly.

### bSinglePhysicalSpace
- **类型**: `bool`
- **描述**: Enable page table channel packing. Note that the bound Virtual Texture should have the same setting for sampling to work correctly.

### bAdaptive
- **类型**: `bool`
- **描述**: Enable sparse adaptive page tables. Note that the bound Virtual Texture should have valid adaptive virtual texture settings for sampling to work correctly.

### bEnableFeedback
- **类型**: `bool`
- **描述**: Enable virtual texture feedback.
Disabling this can result in the virtual texture not reaching the correct mip level.
It should only be used in cases where we don't care about the correct mip level being resident, or some other process is maintaining the correct level.

### WorldPositionOriginType
- **类型**: `EPositionOrigin`
- **描述**: Defines the reference space for the WorldPosition input.

### MipValueMode
- **类型**: `ERuntimeVirtualTextureMipValueMode`
- **描述**: Defines how the mip level is calculated for the virtual texture lookup.

### TextureAddressMode
- **类型**: `ERuntimeVirtualTextureTextureAddressMode`
- **描述**: Defines the texture addressing mode.

