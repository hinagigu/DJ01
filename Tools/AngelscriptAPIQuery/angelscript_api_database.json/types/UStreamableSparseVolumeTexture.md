# UStreamableSparseVolumeTexture

**继承自**: `USparseVolumeTexture`

Represents a streamable SparseVolumeTexture asset and serves as base class for UStaticSparseVolumeTexture and UAnimatedSparseVolumeTexture. It has an array of USparseVolumeTextureFrame.

## 属性

### AddressX
- **类型**: `TextureAddress`

### AddressY
- **类型**: `TextureAddress`

### AddressZ
- **类型**: `TextureAddress`

### bLocalDDCOnly
- **类型**: `bool`

### StreamingPoolSizeFactor
- **类型**: `float32`
- **描述**: The SVT streaming pool is sized such that it can hold the largest frame multiplied by this value. There should be some slack to allow for prefetching frames.

### NumberOfPrefetchFrames
- **类型**: `int`
- **描述**: When using non-blocking streaming requests, upcoming frames are loaded into memory in advance. This property controls how many frames to prefetch.

### PrefetchPercentageStepSize
- **类型**: `float32`
- **描述**: When using non-blocking streaming requests, upcoming frames are loaded into memory in advance. This property controls the size reduction in percent of each additional prefetched frames.
A value of 20.0 would prefetch frame N+1 at 80%, N+2 at 60%, N+3 at 40% etc.

### PrefetchPercentageBias
- **类型**: `float32`
- **描述**: When using non-blocking streaming requests, upcoming frames are loaded into memory in advance. This property applies a bias in percent to how much data is prefetched for every frame.
A value of 20.0 adds 20% to all prefetch percentages. So if PrefetchPercentageStepSize is set to 20.0, frame N+1 is prefetched at 80% + 20% = 100%, frame N+2 at 60% + 20% = 80%, N+3 at 40% + 20% = 60% etc.

### AssetImportData
- **类型**: `UAssetImportData`

### AssetUserData
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

