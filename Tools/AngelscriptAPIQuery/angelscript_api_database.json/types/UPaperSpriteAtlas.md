# UPaperSpriteAtlas

**继承自**: `UObject`

Groups together a set of sprites that will try to share the same texture atlas (allowing them to be combined into a single draw call)

## 属性

### AtlasDescription
- **类型**: `FString`
- **描述**: Description of this atlas, which shows up in the content browser tooltip

### MaxWidth
- **类型**: `int`
- **描述**: Maximum atlas page width (single pages might be smaller)

### MaxHeight
- **类型**: `int`
- **描述**: Maximum atlas page height (single pages might be smaller)

### MipCount
- **类型**: `int`
- **描述**: Maximum atlas page height (single pages might be smaller)

### PaddingType
- **类型**: `EPaperSpriteAtlasPadding`
- **描述**: The type of padding performed on this atlas

### Padding
- **类型**: `int`
- **描述**: The number of pixels of padding

### CompressionSettings
- **类型**: `TextureCompressionSettings`
- **描述**: Compression settings to use on atlas texture

### Filter
- **类型**: `TextureFilter`
- **描述**: Texture filtering mode when sampling these textures

### bRebuildAtlas
- **类型**: `bool`
- **描述**: Slots in the atlas

