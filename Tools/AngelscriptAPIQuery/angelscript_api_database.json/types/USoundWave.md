# USoundWave

**继承自**: `USoundBase`

## 属性

### CompressionQuality
- **类型**: `int`
- **描述**: Platform agnostic compression quality. 1..100 with 1 being best compression and 100 being best quality. ADPCM and PCM sound asset compression types ignore this parameter.

### SampleRateQuality
- **类型**: `ESoundwaveSampleRateSettings`
- **描述**: Determines the max sample rate to use if the platform enables "Resampling For Device" in project settings.
     For example, if the platform enables Resampling For Device and specifies 32000 for High, then setting High here will
     force the sound wave to be _at most_ 32000. Does nothing if Resampling For Device is disabled.

### SoundGroup
- **类型**: `ESoundGroup`

### OverrideSoundToUseForAnalysis
- **类型**: `USoundWave`
- **描述**: Specify a sound to use for the baked analysis. Will default to this USoundWave if not set.

### FFTSize
- **类型**: `ESoundWaveFFTSize`
- **描述**: The FFT window size to use for fft analysis.

### FFTAnalysisFrameSize
- **类型**: `int`
- **描述**: How many audio frames analyze at a time.

### FFTAnalysisAttackTime
- **类型**: `int`
- **描述**: Attack time in milliseconds of the spectral envelope follower.

### FFTAnalysisReleaseTime
- **类型**: `int`
- **描述**: Release time in milliseconds of the spectral envelope follower.

### EnvelopeFollowerFrameSize
- **类型**: `int`
- **描述**: How many audio frames to average a new envelope value. Larger values use less memory for audio envelope data but will result in lower envelope accuracy.

### EnvelopeFollowerAttackTime
- **类型**: `int`
- **描述**: The attack time in milliseconds. Describes how quickly the envelope analyzer responds to increasing amplitudes.

### EnvelopeFollowerReleaseTime
- **类型**: `int`
- **描述**: The release time in milliseconds. Describes how quickly the envelope analyzer responds to decreasing amplitudes.

### ModulationSettings
- **类型**: `FSoundModulationDefaultRoutingSettings`

### FrequenciesToAnalyze
- **类型**: `TArray<float32>`
- **描述**: The frequencies (in hz) to analyze when doing baked FFT analysis.

### LoadingBehavior
- **类型**: `ESoundWaveLoadingBehavior`
- **描述**: Specifies how and when compressed audio data is loaded for asset if stream caching is enabled.

### SizeOfFirstAudioChunkInSeconds
- **类型**: `FPerPlatformFloat`
- **描述**: How much audio to add to First Audio Chunk (in seconds)

### SubtitlePriority
- **类型**: `float32`

### Volume
- **类型**: `float32`
- **描述**: Playback volume of sound 0 to 1 - Default is 1.0.

### Pitch
- **类型**: `float32`
- **描述**: Playback pitch for sound.

### Subtitles
- **类型**: `TArray<FSubtitleCue>`

### Comment
- **类型**: `FString`
- **描述**: Provides contextual information for the sound to the translator.

### AssetImportData
- **类型**: `UAssetImportData`

### Curves
- **类型**: `UCurveTable`
- **描述**: Curves associated with this sound wave

### PlatformSettings
- **类型**: `TMap<FGuid,FSoundWaveCloudStreamingPlatformSettings>`
- **描述**: Optionally disables cloud streaming per platform

### Transformations
- **类型**: `TArray<TObjectPtr<UWaveformTransformationBase>>`
- **描述**: Waveform edits to be applied to this SoundWave on cook (editing transformations will trigger a cook)

### bLooping
- **类型**: `bool`

### TreatFileAsLoopingForAnalysis
- **类型**: `bool`

### bEnableBakedFFTAnalysis
- **类型**: `bool`

### bEnableAmplitudeEnvelopeAnalysis
- **类型**: `bool`

### bMature
- **类型**: `bool`

### bManualWordWrap
- **类型**: `bool`

### bSingleLine
- **类型**: `bool`

### bIsAmbisonics
- **类型**: `bool`

### bEnableCloudStreaming
- **类型**: `bool`

## 方法

### GetCuePoints
```angelscript
TArray<FSoundWaveCuePoint> GetCuePoints()
```
Filters for the cue points that are _not_ loop regions and returns those as a new array

### GetLoopRegions
```angelscript
TArray<FSoundWaveCuePoint> GetLoopRegions()
```
Filters for the cue points that _are_ loop regions and returns those as a new array

### GetSoundAssetCompressionType
```angelscript
ESoundAssetCompressionType GetSoundAssetCompressionType()
```
Returns the sound's asset compression type.

### SetSoundAssetCompressionType
```angelscript
void SetSoundAssetCompressionType(ESoundAssetCompressionType InSoundAssetCompressionType, bool bMarkDirty)
```
Procedurally set the compression type.

