# UMaterialExpressionSpriteTextureSampler

**继承自**: `UMaterialExpressionTextureSampleParameter2D`

This is a texture sampler 2D with a special automatically defined parameter name. The texture specified here will be replaced by the SourceTexture or an AdditionalSourceTextures entry of a Paper2D sprite if this material is used on a sprite.

## 属性

### bSampleAdditionalTextures
- **类型**: `bool`
- **描述**: Is this a sampler for the default SourceTexture or the AdditionalSourceTextures list?

### AdditionalSlotIndex
- **类型**: `int`
- **描述**: This is the slot index into the AdditionalSourceTextures array

### SlotDisplayName
- **类型**: `FText`
- **描述**: Friendly label for the texture slot, displayed in the Sprite Editor if not empty

