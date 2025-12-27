# UAudioComponent

**继承自**: `USceneComponent`

AudioComponent is used to play a Sound

@see https://docs.unrealengine.com/WorkingWithAudio/Overview
@see USoundBase

## 属性

### DefaultParameters
- **类型**: `TArray<FAudioParameter>`

### SoundClassOverride
- **类型**: `USoundClass`
- **描述**: SoundClass that overrides that set on the referenced SoundBase when component is played.

### PitchModulationMin
- **类型**: `float32`

### PitchModulationMax
- **类型**: `float32`

### VolumeModulationMin
- **类型**: `float32`

### VolumeModulationMax
- **类型**: `float32`

### EnvelopeFollowerAttackTime
- **类型**: `int`

### EnvelopeFollowerReleaseTime
- **类型**: `int`

### Priority
- **类型**: `float32`

### SubtitlePriority
- **类型**: `float32`

### SourceEffectChain
- **类型**: `USoundEffectSourcePresetChain`

### ConcurrencySet
- **类型**: `TSet<TObjectPtr<USoundConcurrency>>`

### AutoAttachLocationRule
- **类型**: `EAttachmentRule`

### AutoAttachRotationRule
- **类型**: `EAttachmentRule`

### AutoAttachScaleRule
- **类型**: `EAttachmentRule`

### OnAudioPlayStateChanged
- **类型**: `FOnAudioPlayStateChanged`

### OnAudioVirtualizationChanged
- **类型**: `FOnAudioVirtualizationChanged`

### OnAudioFinished
- **类型**: `FOnAudioFinished`

### OnAudioPlaybackPercent
- **类型**: `FOnAudioPlaybackPercent`

### OnAudioSingleEnvelopeValue
- **类型**: `FOnAudioSingleEnvelopeValue`

### OnAudioMultiEnvelopeValue
- **类型**: `FOnAudioMultiEnvelopeValue`

### AutoAttachParent
- **类型**: `TWeakObjectPtr<USceneComponent>`

### AutoAttachSocketName
- **类型**: `FName`

### bOverrideAttenuation
- **类型**: `bool`

### Sound
- **类型**: `USoundBase`

### bAllowSpatialization
- **类型**: `bool`

### bOverrideSubtitlePriority
- **类型**: `bool`

### bIsUISound
- **类型**: `bool`

### bEnableLowPassFilter
- **类型**: `bool`

### bOverridePriority
- **类型**: `bool`

### bSuppressSubtitles
- **类型**: `bool`

### bCanPlayMultipleInstances
- **类型**: `bool`

### bDisableParameterUpdatesWhilePlaying
- **类型**: `bool`

### bAutoManageAttachment
- **类型**: `bool`

### VolumeMultiplier
- **类型**: `float32`

### PitchMultiplier
- **类型**: `float32`

### LowPassFilterFrequency
- **类型**: `float32`

### AttenuationSettings
- **类型**: `USoundAttenuation`

### AttenuationOverrides
- **类型**: `FSoundAttenuationSettings`

### ModulationRouting
- **类型**: `FSoundModulationDefaultRoutingSettings`

## 方法

### AdjustAttenuation
```angelscript
void AdjustAttenuation(FSoundAttenuationSettings InAttenuationSettings)
```
This function is used to modify the Attenuation Settings on the targeted Audio Component instance. It is worth noting that Attenuation Settings are only passed to new Active Sounds on start, so modified Attenuation data should be set before sound playback.

### AdjustVolume
```angelscript
void AdjustVolume(float32 AdjustVolumeDuration, float32 AdjustVolumeLevel, EAudioFaderCurve FadeCurve)
```
This function allows designers to trigger an adjustment to the sound instance’s playback Volume with options for smoothly applying a curve over time.
@param AdjustVolumeDuration The length of time in which to interpolate between the initial volume and the new volume.
@param AdjustVolumeLevel The new volume to set the Audio Component to.
@param FadeCurve The curve used when interpolating between the old and new volume.

### GetAttenuationSettingsToApply
```angelscript
bool GetAttenuationSettingsToApply(FSoundAttenuationSettings& OutAttenuationSettings)
```
Retrieves Attenuation Settings data on the targeted Audio Component. Returns FALSE if no settings were found.
Because the Attenuation Settings data structure is copied, FALSE returns will return default values.

### FadeIn
```angelscript
void FadeIn(float32 FadeInDuration, float32 FadeVolumeLevel, float32 StartTime, EAudioFaderCurve FadeCurve)
```
This function allows designers to call Play on an Audio Component instance while applying a volume curve over time.
Parameters allow designers to indicate the duration of the fade, the curve shape, and the start time if seeking into the sound.

@param FadeInDuration How long it should take to reach the FadeVolumeLevel
@param FadeVolumeLevel The percentage of the AudioComponents's calculated volume to fade to
@param FadeCurve The curve to use when interpolating between the old and new volume

### FadeOut
```angelscript
void FadeOut(float32 FadeOutDuration, float32 FadeVolumeLevel, EAudioFaderCurve FadeCurve)
```
This function allows designers to call a delayed Stop on an Audio Component instance while applying a
volume curve over time. Parameters allow designers to indicate the duration of the fade and the curve shape.

@param FadeOutDuration how long it should take to reach the FadeVolumeLevel
@param FadeVolumeLevel the percentage of the AudioComponents's calculated volume in which to fade to
@param FadeCurve The curve to use when interpolating between the old and new volume

### GetCookedEnvelopeData
```angelscript
bool GetCookedEnvelopeData(float32& OutEnvelopeData)
```
Retrieves Cooked Amplitude Envelope Data at the current playback time. If there are multiple
SoundWaves playing, data is interpolated and averaged across all playing sound waves.
Returns FALSE if no data was found.

### GetCookedEnvelopeDataForAllPlayingSounds
```angelscript
bool GetCookedEnvelopeDataForAllPlayingSounds(TArray<FSoundWaveEnvelopeDataPerSound>& OutEnvelopeData)
```
Retrieves the current-time amplitude envelope data of the sounds playing on the audio component.
Envelope data is not averaged or interpolated. Instead an array of data with all playing sound waves with cooked data is returned.
Returns true if there is data and the audio component is playing.

### GetCookedFFTData
```angelscript
bool GetCookedFFTData(TArray<float32> FrequenciesToGet, TArray<FSoundWaveSpectralData>& OutSoundWaveSpectralData)
```
Retrieves the current-time cooked spectral data of the sounds playing on the audio component.
Spectral data is averaged and interpolated for all playing sounds on this audio component.
Returns true if there is data and the audio component is playing.

### GetCookedFFTDataForAllPlayingSounds
```angelscript
bool GetCookedFFTDataForAllPlayingSounds(TArray<FSoundWaveSpectralDataPerSound>& OutSoundWaveSpectralData)
```
Retrieves the current-time cooked spectral data of the sounds playing on the audio component.
Spectral data is not averaged or interpolated. Instead an array of data with all playing sound waves with cooked data is returned.
Returns true if there is data and the audio component is playing.

### GetModulators
```angelscript
TSet<USoundModulatorBase> GetModulators(EModulationDestination Destination)
```
Gets the set of currently active modulators for a given Modulation Destination.
@param Destination The Destination to retrieve the Modulators from.
@return The set of of Modulators applied to this component for the given Destination.

### GetPlayState
```angelscript
EAudioComponentPlayState GetPlayState()
```
Returns the enumerated play states of the audio component.

### HasCookedAmplitudeEnvelopeData
```angelscript
bool HasCookedAmplitudeEnvelopeData()
```
Queries whether or not the targeted Audio Component instance’s sound has Amplitude Envelope Data, returns FALSE if none found.

### HasCookedFFTData
```angelscript
bool HasCookedFFTData()
```
Queries if the sound wave playing in this audio component has cooked FFT data, returns FALSE if none found.

### IsPlaying
```angelscript
bool IsPlaying()
```
Returns TRUE if the targeted Audio Component’s sound is playing.
Doesn't indicate if the sound is paused or fading in/out. Use GetPlayState() to get the full play state.

### IsVirtualized
```angelscript
bool IsVirtualized()
```
Returns if the sound is virtualized.

### Play
```angelscript
void Play(float32 StartTime)
```
Begins playing the targeted Audio Component's sound at the designated Start Time, seeking into a sound.
@param StartTime The offset, in seconds, to begin reading the sound at

### PlayQuantized
```angelscript
void PlayQuantized(UQuartzClockHandle& InClockHandle, FQuartzQuantizationBoundary& InQuantizationBoundary, FOnQuartzCommandEventBP InDelegate, float32 InStartTime, float32 InFadeInDuration, float32 InFadeVolumeLevel, EAudioFaderCurve InFadeCurve)
```
Start a sound playing on an audio component on a given quantization boundary with the handle to an existing clock

### SetAttenuationOverrides
```angelscript
void SetAttenuationOverrides(FSoundAttenuationSettings InAttenuationOverrides)
```

### SetAttenuationSettings
```angelscript
void SetAttenuationSettings(USoundAttenuation InAttenuationSettings)
```

### SetAudioBusSendPostEffect
```angelscript
void SetAudioBusSendPostEffect(UAudioBus AudioBus, float32 AudioBusSendLevel)
```
Sets how much audio the sound should send to the given Audio Bus (POST Source Effects).
if the Audio Bus Send doesn't already exist, it will be added to the overrides on the active sound.
@param AudioBus The Bus to send the signal to
@param AudioBusSendLevel The scalar used to alter the volume of the copied signal

### SetAudioBusSendPreEffect
```angelscript
void SetAudioBusSendPreEffect(UAudioBus AudioBus, float32 AudioBusSendLevel)
```
Sets how much audio the sound should send to the given Audio Bus (PRE Source Effects).
if the Bus Send doesn't already exist, it will be added to the overrides on the active sound.
@param AudioBus The Bus to send the signal to
@param AudioBusSendLevel The scalar used to alter the volume of the copied signal

### SetBoolParameter
```angelscript
void SetBoolParameter(FName InName, bool InBool)
```
Sets a named Boolean

### SetFloatParameter
```angelscript
void SetFloatParameter(FName InName, float32 InFloat)
```
Sets a named Float

### SetIntParameter
```angelscript
void SetIntParameter(FName InName, int InInt)
```
Sets a named Int32

### SetLowPassFilterEnabled
```angelscript
void SetLowPassFilterEnabled(bool InLowPassFilterEnabled)
```
When set to TRUE, enables an additional Low Pass Filter Frequency to be calculated in with the
sound instance’s LPF total, allowing designers to set filter settings for the targeted Audio Component’s
sound instance.

### SetLowPassFilterFrequency
```angelscript
void SetLowPassFilterFrequency(float32 InLowPassFilterFrequency)
```
Sets a cutoff frequency, in Hz, for the targeted Audio Component’s sound’s Low Pass Filter calculation.
The lowest cutoff frequency from all of the sound instance’s possible LPF calculations wins.

### SetModulationRouting
```angelscript
void SetModulationRouting(TSet<USoundModulatorBase> Modulators, EModulationDestination Destination, EModulationRouting RoutingMethod)
```
Sets the routing for one of the given Audio component's Modulation Destinations.
@param Modulators The set of modulators to apply to the given destination on the component.
@param Destination The destination to assign the modulators to.
@param RoutingMethod The routing method to use for the given modulator.

### SetOutputToBusOnly
```angelscript
void SetOutputToBusOnly(bool bInOutputToBusOnly)
```
Sets whether or not to output the audio to bus only.

### SetOverrideAttenuation
```angelscript
void SetOverrideAttenuation(bool bInOverrideAttenuation)
```

### SetPaused
```angelscript
void SetPaused(bool bPause)
```
Pause an audio component playing its sound cue, issue any delegates if needed

### SetPitchMultiplier
```angelscript
void SetPitchMultiplier(float32 NewPitchMultiplier)
```
Set a new pitch multiplier

### SetSound
```angelscript
void SetSound(USoundBase NewSound)
```
Set what sound is played by this component

### SetSourceBusSendPostEffect
```angelscript
void SetSourceBusSendPostEffect(USoundSourceBus SoundSourceBus, float32 SourceBusSendLevel)
```
Allows designers to target a specific Audio Component instance’s sound and set the send level (volume of sound copied)
to the indicated Source Bus. If the Source Bus is not already part of the sound’s sends, the reference will be added to
this instance’s Override sends. This particular send occurs after the Source Effect processing chain.
@param SoundSourceBus The Bus to send the signal to
@param SourceBusSendLevel The scalar used to alter the volume of the copied signal

### SetSourceBusSendPreEffect
```angelscript
void SetSourceBusSendPreEffect(USoundSourceBus SoundSourceBus, float32 SourceBusSendLevel)
```
Allows designers to target a specific Audio Component instance’s sound and set the send level (volume of sound copied)
to the indicated Source Bus. If the Source Bus is not already part of the sound’s sends, the reference will be added to
this instance’s Override sends. This particular send occurs before the Source Effect processing chain.
@param SoundSourceBus The Bus to send the signal to.
@param SourceBusSendLevel The scalar used to alter the volume of the copied signal.

### SetSubmixSend
```angelscript
void SetSubmixSend(USoundSubmixBase Submix, float32 SendLevel)
```
Allows designers to target a specific Audio Component instance’s sound set the send level (volume of sound copied) to the indicated Submix.
@param Submix The Submix to send the signal to.
@param SendLevel The scalar used to alter the volume of the copied signal.

### SetUISound
```angelscript
void SetUISound(bool bInUISound)
```
Set whether sounds generated by this audio component should be considered UI sounds

### SetVolumeMultiplier
```angelscript
void SetVolumeMultiplier(float32 NewVolumeMultiplier)
```
Set a new volume multiplier

### SetWaveParameter
```angelscript
void SetWaveParameter(FName InName, USoundWave InWave)
```
Sets the parameter matching the name indicated to the provided Wave. Provided for convenience/backward compatibility
with SoundCues (The parameter interface supports any object and is up to the system querying it to determine whether
it is a valid type).
@param InName The name of the parameter to assign the wave to.
@param InWave The wave value to set.

### Stop
```angelscript
void Stop()
```
Stop an audio component's sound, issue any delegates if needed

### StopDelayed
```angelscript
void StopDelayed(float32 DelayTime)
```
Cues request to stop sound after the provided delay (in seconds), stopping immediately if delay is zero or negative

