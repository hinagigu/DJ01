# UPaperImporterSettings

**继承自**: `UObject`

Implements the settings for imported Paper2D assets, such as sprite sheet textures.

## 属性

### bPickBestMaterialWhenCreatingSprites
- **类型**: `bool`
- **描述**: Should the source texture be scanned when creating new sprites to determine the appropriate material? (if false, the Default Masked Material is always used)

### bPickBestMaterialWhenCreatingTileMaps
- **类型**: `bool`
- **描述**: Should the source texture be scanned when creating new tile maps (from a tile set or via importing) to determine the appropriate material? (if false, the Default Masked Material is always used)

### bAnalysisCanUseOpaque
- **类型**: `bool`
- **描述**: Can opaque materials be applied as part of the 'best material' analysis?

### DefaultPixelsPerUnrealUnit
- **类型**: `float32`
- **描述**: The default scaling factor between pixels and Unreal units (cm) to use for newly created sprite assets (e.g., 0.64 would make a 64 pixel wide sprite take up 100 cm)

### NormalMapTextureSuffixes
- **类型**: `TArray<FString>`
- **描述**: A list of default suffixes to use when looking for associated normal maps while importing sprites or creating sprites from textures

### BaseMapTextureSuffixes
- **类型**: `TArray<FString>`
- **描述**: The default suffix to remove (if present) from a texture name before looking for an associated normal map using NormalMapTextureSuffixes

### DefaultSpriteTextureGroup
- **类型**: `TextureGroup`
- **描述**: The default texture group for imported sprite textures, tile sheets, etc... (typically set to UI for 'modern 2D' or 2D pixels for 'retro 2D')

### bOverrideTextureCompression
- **类型**: `bool`
- **描述**: Should texture compression settings be overridden on imported sprite textures, tile sheets, etc...?

### DefaultSpriteTextureCompression
- **类型**: `TextureCompressionSettings`
- **描述**: Compression settings to use when building the texture.
The default texture group for imported sprite textures, tile sheets, etc... (typically set to UI for 'modern 2D' or 2D pixels for 'retro 2D')

### UnlitDefaultMaskedMaterialName
- **类型**: `FSoftObjectPath`
- **描述**: The unlit default masked material for newly created sprites (masked means binary opacity: things are either opaque or see-thru, with nothing in between)

### UnlitDefaultTranslucentMaterialName
- **类型**: `FSoftObjectPath`
- **描述**: The unlit default translucent material for newly created sprites (translucent means smooth opacity which can vary continuously from 0..1, but translucent rendering is more expensive that opaque or masked rendering and has different sorting rules)

### UnlitDefaultOpaqueMaterialName
- **类型**: `FSoftObjectPath`
- **描述**: The unlit default opaque material for newly created sprites

### LitDefaultMaskedMaterialName
- **类型**: `FSoftObjectPath`
- **描述**: The lit default masked material for newly created sprites (masked means binary opacity: things are either opaque or see-thru, with nothing in between)

### LitDefaultTranslucentMaterialName
- **类型**: `FSoftObjectPath`
- **描述**: The lit default translucent material for newly created sprites (translucent means smooth opacity which can vary continuously from 0..1, but translucent rendering is more expensive that opaque or masked rendering and has different sorting rules)

### LitDefaultOpaqueMaterialName
- **类型**: `FSoftObjectPath`
- **描述**: The lit default opaque material for newly created sprites

