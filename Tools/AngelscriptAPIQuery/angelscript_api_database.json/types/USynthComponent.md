# USynthComponent

**继承自**: `USceneComponent`

## 属性

### AttenuationSettings
- **类型**: `USoundAttenuation`

### AttenuationOverrides
- **类型**: `FSoundAttenuationSettings`

### ConcurrencySet
- **类型**: `TSet<TObjectPtr<USoundConcurrency>>`

### SoundClass
- **类型**: `USoundClass`
- **描述**: Sound class this sound belongs to

### SourceEffectChain
- **类型**: `USoundEffectSourcePresetChain`
- **描述**: The source effect chain to use for this sound.

### SoundSubmix
- **类型**: `USoundSubmixBase`
- **描述**: Submix this sound belongs to

### SoundSubmixSends
- **类型**: `TArray<FSoundSubmixSendInfo>`

### BusSends
- **类型**: `TArray<FSoundSourceBusSendInfo>`

### PreEffectBusSends
- **类型**: `TArray<FSoundSourceBusSendInfo>`

### EnvelopeFollowerAttackTime
- **类型**: `int`

### EnvelopeFollowerReleaseTime
- **类型**: `int`

### OnAudioEnvelopeValue
- **类型**: `FOnSynthEnvelopeValue`

### bAllowSpatialization
- **类型**: `bool`

### bOverrideAttenuation
- **类型**: `bool`

### bEnableBusSends
- **类型**: `bool`

### bEnableBaseSubmix
- **类型**: `bool`

### bEnableSubmixSends
- **类型**: `bool`

### ModulationRouting
- **类型**: `FSoundModulationDefaultRoutingSettings`

### bIsUISound
- **类型**: `bool`

## 方法

### AdjustVolume
```angelscript
void AdjustVolume(float32 AdjustVolumeDuration, float32 AdjustVolumeLevel, EAudioFaderCurve FadeCurve)
```
This function allows designers to trigger an adjustment to the sound instance’s playback Volume with options for smoothly applying a curve over time.
@param AdjustVolumeDuration The length of time in which to interpolate between the initial volume and the new volume.
@param AdjustVolumeLevel The new volume to set the Audio Component to.
@param FadeCurve The curve used when interpolating between the old and new volume.

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

### GetModulators
```angelscript
TSet<USoundModulatorBase> GetModulators(EModulationDestination Destination)
```
Gets the set of currently active modulators for a given Modulation Destination.
@param Destination The Destination to retrieve the Modulators from.
@return The set of of Modulators applied to this component for the given Destination.

### IsPlaying
```angelscript
bool IsPlaying()
```
Returns true if this component is currently playing.

### SetAudioBusSendPostEffect
```angelscript
void SetAudioBusSendPostEffect(UAudioBus AudioBus, float32 AudioBusSendLevel)
```
Sets how much audio the sound should send to the given AudioBus (post effect).

### SetAudioBusSendPreEffect
```angelscript
void SetAudioBusSendPreEffect(UAudioBus AudioBus, float32 AudioBusSendLevel)
```
Sets how much audio the sound should send to the given AudioBus (pre effect).

### SetLowPassFilterEnabled
```angelscript
void SetLowPassFilterEnabled(bool InLowPassFilterEnabled)
```
Sets whether or not the low pass filter is enabled on the audio component.

### SetLowPassFilterFrequency
```angelscript
void SetLowPassFilterFrequency(float32 InLowPassFilterFrequency)
```
Sets lowpass filter frequency of the audio component.

### SetModulationRouting
```angelscript
void SetModulationRouting(TSet<USoundModulatorBase> Modulators, EModulationDestination Destination, EModulationRouting RoutingMethod)
```
Sets the routing for one of the given Synth component's Modulation Destinations.
@param Modulators The set of modulators to apply to the given destination on the component.
@param Destination The destination to assign the modulators to.
@param RoutingMethod The routing method to use for the given modulator.

### SetOutputToBusOnly
```angelscript
void SetOutputToBusOnly(bool bInOutputToBusOnly)
```
Sets whether or not the synth component outputs its audio to any source or audio buses.

### SetSourceBusSendPostEffect
```angelscript
void SetSourceBusSendPostEffect(USoundSourceBus SoundSourceBus, float32 SourceBusSendLevel)
```
Sets how much audio the sound should send to the given SourceBus (post effect).

### SetSourceBusSendPreEffect
```angelscript
void SetSourceBusSendPreEffect(USoundSourceBus SoundSourceBus, float32 SourceBusSendLevel)
```
Sets how much audio the sound should send to the given SourceBus (pre effect).

### SetSubmixSend
```angelscript
void SetSubmixSend(USoundSubmixBase Submix, float32 SendLevel)
```
Sets how much audio the sound should send to the given submix.

### SetVolumeMultiplier
```angelscript
void SetVolumeMultiplier(float32 VolumeMultiplier)
```
Set a new volume multiplier

### Start
```angelscript
void Start()
```
Starts the synth generating audio.

### Stop
```angelscript
void Stop()
```
Stops the synth generating audio.

