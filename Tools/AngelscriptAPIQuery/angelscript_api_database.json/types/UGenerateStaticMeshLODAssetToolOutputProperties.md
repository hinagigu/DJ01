# UGenerateStaticMeshLODAssetToolOutputProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### OutputMode
- **类型**: `EGenerateLODAssetOutputMode`
- **描述**: Whether to modify the static mesh in place or create a new one.

### NewAssetName
- **类型**: `FString`
- **描述**: Base name for newly-generated asset

### bSaveInputAsHiResSource
- **类型**: `bool`
- **描述**: If the Asset doesn't already have a HiRes source, store the input mesh as the HiRes source

### GeneratedSuffix
- **类型**: `FString`
- **描述**: Suffix to append to newly-generated Asset (Meshes, Textures, Materials, etc)

