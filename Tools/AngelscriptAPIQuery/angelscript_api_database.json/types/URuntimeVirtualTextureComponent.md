# URuntimeVirtualTextureComponent

**继承自**: `USceneComponent`

Component used to place a URuntimeVirtualTexture in the world.

## 属性

### BoundsAlignActor
- **类型**: `TSoftObjectPtr<AActor>`
- **描述**: Actor to align rotation to. If set this actor is always included in the bounds calculation.

### bSnapBoundsToLandscape
- **类型**: `bool`
- **描述**: If the Bounds Align Actor is a Landscape then this will snap the bounds so that virtual texture texels align with landscape vertex positions.

### ExpandBounds
- **类型**: `float32`
- **描述**: Amount to expand the Bounds during calculation.

### VirtualTexture
- **类型**: `URuntimeVirtualTexture`

### EnableInGamePerPlatform
- **类型**: `FPerPlatformBool`
- **描述**: Per platform overrides for enabling the virtual texture. Only affects In-Game and PIE.

### bEnableForNaniteOnly
- **类型**: `bool`
- **描述**: Enable the virtual texture only when Nanite is enabled. Can be used for a Displacement virtual texture with Nanite tessellation.

### bEnableScalability
- **类型**: `bool`
- **描述**: Set to true to enable scalability settings for the virtual texture.

### ScalabilityGroup
- **类型**: `uint`
- **描述**: Group index of the scalability settings to use for the virtual texture.

### bHidePrimitives
- **类型**: `bool`
- **描述**: Hide primitives in the main pass. Hidden primitives will be those that draw to this virtual texture with 'Draw in Main Pass' set to 'From Virtual Texture'.

### StreamingTexture
- **类型**: `UVirtualTextureBuilder`

### StreamLowMips
- **类型**: `int`
- **描述**: Number of streaming low mips to build for the virtual texture.

### LossyCompressionAmount
- **类型**: `ETextureLossyCompressionAmount`

### bUseStreamingMipsFixedColor
- **类型**: `bool`

### StreamingMipsFixedColor
- **类型**: `FLinearColor`

### bUseStreamingLowMipsInEditor
- **类型**: `bool`
- **描述**: Use streaming low mips when rendering in editor. Set true to view and debug the baked streaming low mips.

## 方法

### Invalidate
```angelscript
void Invalidate(FBoxSphereBounds WorldBounds)
```
This function marks an area of the runtime virtual texture as dirty.
@param WorldBounds : The world space bounds of the pages to invalidate.

