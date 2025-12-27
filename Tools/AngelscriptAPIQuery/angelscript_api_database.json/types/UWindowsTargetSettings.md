# UWindowsTargetSettings

**继承自**: `UObject`

Implements the settings for the Windows target platform. The first instance of this class is initialized in
WindowsTargetPlatform, really early during the startup sequence before the CDO has been constructed, so its config
settings are read manually from there.

## 属性

### DefaultGraphicsRHI
- **类型**: `EDefaultGraphicsRHI`
- **描述**: Select which RHI to use. Make sure its also selected as a Targeted RHI. Requires Editor restart.

### D3D12TargetedShaderFormats
- **类型**: `TArray<FString>`

### D3D11TargetedShaderFormats
- **类型**: `TArray<FString>`

### VulkanTargetedShaderFormats
- **类型**: `TArray<FString>`

### Compiler
- **类型**: `ECompilerVersion`
- **描述**: The compiler version to use for this project. May be different to the chosen IDE.

### AudioSampleRate
- **类型**: `int`
- **描述**: Sample rate to run the audio mixer with.

### AudioCallbackBufferFrameSize
- **类型**: `int`
- **描述**: The amount of audio to compute each callback block. Lower values decrease latency but may increase CPU cost.

### AudioNumBuffersToEnqueue
- **类型**: `int`
- **描述**: The number of buffers to keep enqueued. More buffers increases latency, but can compensate for variable compute availability in audio callbacks on some platforms.

### AudioMaxChannels
- **类型**: `int`
- **描述**: The max number of channels (voices) to limit for this platform. The max channels used will be the minimum of this value and the global audio quality settings. A value of 0 will not apply a platform channel count max.

### AudioNumSourceWorkers
- **类型**: `int`
- **描述**: The number of workers to use to compute source audio. Will only use up to the max number of sources. Will evenly divide sources to each source worker.

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

### CompressionOverrides
- **类型**: `FPlatformRuntimeAudioCompressionOverrides`
- **描述**: Various overrides for how this platform should handle compression and decompression

### CacheSizeKB
- **类型**: `int`
- **描述**: This determines the max amount of memory that should be used for the cache at any given time. If set low (<= 8 MB), it lowers the size of individual chunks of audio during cook.

### MaxChunkSizeOverrideKB
- **类型**: `int`
- **描述**: This overrides the default max chunk size used when chunking audio for stream caching (ignored if < 0)

### bResampleForDevice
- **类型**: `bool`

### MaxSampleRate
- **类型**: `float32`
- **描述**: Mapping of which sample rates are used for each sample rate quality for a specific platform.

### HighSampleRate
- **类型**: `float32`

### MedSampleRate
- **类型**: `float32`

### LowSampleRate
- **类型**: `float32`

### MinSampleRate
- **类型**: `float32`

### CompressionQualityModifier
- **类型**: `float32`
- **描述**: Scales all compression qualities when cooking to this platform. For example, 0.5 will halve all compression qualities, and 1.0 will leave them unchanged.

### SoundCueCookQualityIndex
- **类型**: `int`
- **描述**: Quality Level to COOK SoundCues at (if set, all other levels will be stripped by the cooker).

