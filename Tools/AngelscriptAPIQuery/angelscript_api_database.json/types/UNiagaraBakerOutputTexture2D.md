# UNiagaraBakerOutputTexture2D

**继承自**: `UNiagaraBakerOutput`

## 属性

### SourceBinding
- **类型**: `FNiagaraBakerTextureSource`
- **描述**: Source visualization we should capture, i.e. Scene Color, World Normal, etc

### FrameSize
- **类型**: `FIntPoint`
- **描述**: Size of each frame we generate.

### AtlasTextureSize
- **类型**: `FIntPoint`
- **描述**: Size of the atlas texture when generating an atlas.

### TextureAddressX
- **类型**: `TextureAddress`
- **描述**: After baking sets the texture address mode to use on the X axis.

### TextureAddressY
- **类型**: `TextureAddress`
- **描述**: After baking sets the texture address mode to use on the Y axis.

### AtlasAssetPathFormat
- **类型**: `FString`
- **描述**: When enabled a texture atlas is created

### FramesAssetPathFormat
- **类型**: `FString`
- **描述**: When enabled each frame will create an asset.

### FramesExportPathFormat
- **类型**: `FString`
- **描述**: When enabled each frame will be exported to the output path using the format extension.

### bGenerateAtlas
- **类型**: `bool`

### bGenerateFrames
- **类型**: `bool`

### bExportFrames
- **类型**: `bool`

### bSetTextureAddressX
- **类型**: `bool`

### bSetTextureAddressY
- **类型**: `bool`

