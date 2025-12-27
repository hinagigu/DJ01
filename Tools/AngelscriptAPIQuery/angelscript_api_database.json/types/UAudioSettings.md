# UAudioSettings

**继承自**: `UDeveloperSettings`

Audio settings.

## 属性

### DefaultSoundClassName
- **类型**: `FSoftObjectPath`
- **描述**: The SoundClass assigned to newly created sounds

### DefaultMediaSoundClassName
- **类型**: `FSoftObjectPath`
- **描述**: The SoundClass assigned to media player assets

### DefaultSoundConcurrencyName
- **类型**: `FSoftObjectPath`
- **描述**: The SoundConcurrency assigned to newly created sounds

### DefaultBaseSoundMix
- **类型**: `FSoftObjectPath`
- **描述**: The SoundMix to use as base when no other system has specified a Base SoundMix

### VoiPSoundClass
- **类型**: `FSoftObjectPath`
- **描述**: Sound class to be used for the VOIP audio component

### MasterSubmix
- **类型**: `FSoftObjectPath`
- **描述**: The default submix through which all sounds are routed to. The root submix that outputs to audio hardware.

### BaseDefaultSubmix
- **类型**: `FSoftObjectPath`
- **描述**: The default submix to use for implicit submix sends (i.e. if the base submix send is null or if a submix parent is null)

### ReverbSubmix
- **类型**: `FSoftObjectPath`
- **描述**: The submix through which all sounds set to use reverb are routed

### EQSubmix
- **类型**: `FSoftObjectPath`
- **描述**: The submix through which all sounds set to use legacy EQ system are routed

### VoiPSampleRate
- **类型**: `EVoiceSampleRate`
- **描述**: Sample rate used for voice over IP. VOIP audio is resampled to the application's sample rate on the receiver side.

### DefaultAudioCompressionType
- **类型**: `EDefaultAudioCompressionType`
- **描述**: Default audio compression type to use for audio assets.

### DefaultCompressionQuality
- **类型**: `int`
- **描述**: The default compression quality (e.g. for new SoundWaves)

### MaximumConcurrentStreams
- **类型**: `int`
- **描述**: How many streaming sounds can be played at the same time (if more are played they will be sorted by priority)

### GlobalMinPitchScale
- **类型**: `float32`
- **描述**: The value to use to clamp the min pitch scale

### GlobalMaxPitchScale
- **类型**: `float32`
- **描述**: The value to use to clamp the max pitch scale

### QualityLevels
- **类型**: `TArray<FAudioQualitySettings>`

### NumStoppingSources
- **类型**: `uint`
- **描述**: The max number of sources to reserve for "stopping" sounds. A "stopping" sound applies a fast fade in the DSP
render to prevent discontinuities when stopping sources.

### PanningMethod
- **类型**: `EPanningMethod`
- **描述**: The method to use when doing non-binaural or object-based panning.

### MonoChannelUpmixMethod
- **类型**: `EMonoChannelUpmixMethod`
- **描述**: The upmixing method for mono sound sources. Defines how mono channels are up-mixed to stereo channels.

### DialogueFilenameFormat
- **类型**: `FString`
- **描述**: The format string to use when generating the filename for contexts within dialogue waves. This must generate unique names for your project.
Available format markers:
  * {DialogueGuid} - The GUID of the dialogue wave. Guaranteed to be unique and stable against asset renames.
  * {DialogueHash} - The hash of the dialogue wave. Not guaranteed to be unique or stable against asset renames, however may be unique enough if combined with the dialogue name.
  * {DialogueName} - The name of the dialogue wave. Not guaranteed to be unique or stable against asset renames, however may be unique enough if combined with the dialogue hash.
  * {ContextId}    - The ID of the context. Guaranteed to be unique within its dialogue wave. Not guaranteed to be stable against changes to the context.
  * {ContextIndex} - The index of the context within its parent dialogue wave. Guaranteed to be unique within its dialogue wave. Not guaranteed to be stable against contexts being removed.

### DebugSounds
- **类型**: `TArray<FSoundDebugEntry>`
- **描述**: Sounds only packaged in non-shipped builds for debugging.

### DefaultAudioBuses
- **类型**: `TArray<FDefaultAudioBusSettings>`
- **描述**: Array of AudioBuses that are automatically initialized when the AudioEngine is initialized

### bAllowPlayWhenSilent
- **类型**: `bool`

### bDisableMasterEQ
- **类型**: `bool`

### bAllowCenterChannel3DPanning
- **类型**: `bool`

