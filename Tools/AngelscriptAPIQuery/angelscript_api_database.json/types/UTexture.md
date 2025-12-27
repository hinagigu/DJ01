# UTexture

**继承自**: `UStreamableRenderAsset`

## 属性

### AssetImportData
- **类型**: `UAssetImportData`

### AdjustBrightness
- **类型**: `float32`

### AdjustBrightnessCurve
- **类型**: `float32`

### AdjustVibrance
- **类型**: `float32`

### AdjustSaturation
- **类型**: `float32`

### AdjustRGBCurve
- **类型**: `float32`

### AdjustHue
- **类型**: `float32`

### AdjustMinAlpha
- **类型**: `float32`

### AdjustMaxAlpha
- **类型**: `float32`

### LossyCompressionAmount
- **类型**: `ETextureLossyCompressionAmount`

### OodleTextureSdkVersion
- **类型**: `FName`

### MaxTextureSize
- **类型**: `int`

### CompressionQuality
- **类型**: `ETextureCompressionQuality`

### CompressionCacheId
- **类型**: `FGuid`
- **描述**: Change this optional ID to force the texture to be recompressed by changing its cache key.

### bDoScaleMipsForAlphaCoverage
- **类型**: `bool`

### AlphaCoverageThresholds
- **类型**: `FVector4`

### bUseNewMipFilter
- **类型**: `bool`

### PowerOfTwoMode
- **类型**: `ETexturePowerOfTwoSetting`

### PaddingColor
- **类型**: `FColor`

### bPadWithBorderColor
- **类型**: `bool`

### ResizeDuringBuildX
- **类型**: `int`

### ResizeDuringBuildY
- **类型**: `int`

### bChromaKeyTexture
- **类型**: `bool`

### ChromaKeyThreshold
- **类型**: `float32`

### ChromaKeyColor
- **类型**: `FColor`

### MipGenSettings
- **类型**: `TextureMipGenSettings`

### CompositeTexture
- **类型**: `UTexture`

### CompositeTextureMode
- **类型**: `ECompositeTextureMode`

### CompositePower
- **类型**: `float32`

### LODBias
- **类型**: `int`

### CompressionSettings
- **类型**: `TextureCompressionSettings`

### Filter
- **类型**: `TextureFilter`

### MipLoadOptions
- **类型**: `ETextureMipLoadOptions`

### CookPlatformTilingSettings
- **类型**: `TextureCookPlatformTilingSettings`

### bOodlePreserveExtremes
- **类型**: `bool`

### LODGroup
- **类型**: `TextureGroup`

### Downscale
- **类型**: `FPerPlatformFloat`
- **描述**: Downscale source texture, applied only to 2d textures without mips
< 1.0 - use scale value from texture group
1.0 - do not scale texture
> 1.0 - scale texure

### DownscaleOptions
- **类型**: `ETextureDownscaleOptions`
- **描述**: Texture downscaling options

### Availability
- **类型**: `ETextureAvailability`

### SourceColorSettings
- **类型**: `FTextureSourceColorSettings`

### AssetUserData
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

### CompressionNoAlpha
- **类型**: `bool`

### CompressFinal
- **类型**: `bool`

### DeferCompression
- **类型**: `bool`

### bPreserveBorder
- **类型**: `bool`

### bFlipGreenChannel
- **类型**: `bool`

### SRGB
- **类型**: `bool`

### bNormalizeNormals
- **类型**: `bool`

### bUseLegacyGamma
- **类型**: `bool`

### VirtualTextureStreaming
- **类型**: `bool`

## 方法

### Blueprint_GetMemorySize
```angelscript
int64 Blueprint_GetMemorySize()
```
Gets the memory size of the texture, in bytes.
This is the size in GPU memory of the built platformdata, accounting for LODBias, etc.
Returns zero for error.

### Blueprint_GetTextureSourceDiskAndMemorySize
```angelscript
void Blueprint_GetTextureSourceDiskAndMemorySize(int64& OutDiskSize, int64& OutMemorySize)
```
Gets the memory size of the texture source top mip, in bytes, and the size on disk of the asset, which may be compressed.
Uses texture source, not available in runtime games.
Does not cause texture source to be loaded, queries cached values.
Returns zero for error.

### ComputeTextureSourceChannelMinMax
```angelscript
bool ComputeTextureSourceChannelMinMax(FLinearColor& OutColorMin, FLinearColor& OutColorMax)
```
Scan the texture source pixels to compute the min & max values of the RGBA channels.
Uses texture source, not available in runtime games.
Causes texture source data to be loaded, is computed by scanning pixels when called.
Will set Min=Max=zero and return false on failure

