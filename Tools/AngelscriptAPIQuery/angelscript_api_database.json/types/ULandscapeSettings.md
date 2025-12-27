# ULandscapeSettings

**继承自**: `UDeveloperSettings`

## 属性

### MaxNumberOfLayers
- **类型**: `int`
- **描述**: This option controls the maximum editing layers that can be added to a Landscape

### MaxComponents
- **类型**: `int`
- **描述**: Maximum Dimension of Landscape in Components

### MaxImageImportCacheSizeMegaBytes
- **类型**: `uint`
- **描述**: Maximum Size of Import Image Cache in MB

### PaintStrengthGamma
- **类型**: `float32`
- **描述**: Exponent for the Paint Tool Strength

### bDisablePaintingStartupSlowdown
- **类型**: `bool`
- **描述**: Disable Painting Startup Slowdown

### LandscapeDirtyingMode
- **类型**: `ELandscapeDirtyingMode`

### DefaultLandscapeMaterial
- **类型**: `TSoftObjectPtr<UMaterialInterface>`
- **描述**: Default Landscape Material will be prefilled when creating a new landscape.

### DefaultLayerInfoObject
- **类型**: `TSoftObjectPtr<ULandscapeLayerInfoObject>`
- **描述**: Default Layer Info Object

### BrushSizeUIMax
- **类型**: `float32`
- **描述**: Maximum size that can be set via the slider for the landscape sculpt/paint brushes

### BrushSizeClampMax
- **类型**: `float32`
- **描述**: Maximum size that can be set manually for the landscape sculpt/paint brushes

### HLODMaxTextureSize
- **类型**: `int`
- **描述**: Maximum size of the textures generated for landscape HLODs

