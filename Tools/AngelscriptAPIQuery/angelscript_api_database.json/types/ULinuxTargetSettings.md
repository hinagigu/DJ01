# ULinuxTargetSettings

**继承自**: `UObject`

Implements the settings for the Linux target platform.

## 属性

### SpatializationPlugin
- **类型**: `FString`
- **描述**: Which of the currently enabled spatialization plugins to use.

### SourceDataOverridePlugin
- **类型**: `FString`
- **描述**: Which of the currently enabled source data override plugins to use.

### ReverbPlugin
- **类型**: `FString`
- **描述**: Which of the currently enabled reverb plugins to use.

### OcclusionPlugin
- **类型**: `FString`
- **描述**: Which of the currently enabled occlusion plugins to use.

### SoundCueCookQualityIndex
- **类型**: `int`
- **描述**: Quality Level to COOK SoundCues at (if set, all other levels will be stripped by the cooker).

### TargetedRHIs
- **类型**: `TArray<FString>`
- **描述**: The collection of RHI's we want to support on this platform.
This is not always the full list of RHI we can support.

