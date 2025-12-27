# UVirtualTextureBuilder

**继承自**: `UObject`

Container for a UVirtualTexture2D that can be built from a FVirtualTextureBuildDesc description.
This has a simple BuildTexture() interface but we may want to extend in the future to support partial builds
or other more blueprint driven approaches for data generation.

## 属性

### Texture
- **类型**: `UVirtualTexture2D`
- **描述**: The UTexture object.

### TextureMobile
- **类型**: `UVirtualTexture2D`
- **描述**: The UTexture object for Mobile rendering.

### bSeparateTextureForMobile
- **类型**: `bool`
- **描述**: Whether to use a separate texture for Mobile rendering. A separate texure will be built using mobile preview editor mode

### EnableCookPerPlatform
- **类型**: `FPerPlatformBool`
- **描述**: Per platform overrides for cooking the virtual texture.

