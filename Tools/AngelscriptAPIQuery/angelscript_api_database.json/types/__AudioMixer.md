# __AudioMixer

## 方法

### AddMasterSubmixEffect
```angelscript
void AddMasterSubmixEffect(USoundEffectSubmixPreset SubmixEffectPreset)
```
Adds a submix effect preset to the master submix.

### AddSourceEffectToPresetChain
```angelscript
void AddSourceEffectToPresetChain(USoundEffectSourcePresetChain PresetChain, FSourceEffectChainEntry Entry)
```
Adds source effect entry to preset chain. Only effects the instance of the preset chain

### AddSubmixEffect
```angelscript
int AddSubmixEffect(USoundSubmix SoundSubmix, USoundEffectSubmixPreset SubmixEffectPreset)
```
Adds a submix effect preset to the given submix at the end of its submix effect chain. Returns the number of submix effects.

### ClearMasterSubmixEffects
```angelscript
void ClearMasterSubmixEffects()
```
Clears all master submix effects.

### ClearSubmixEffectChainOverride
```angelscript
void ClearSubmixEffectChainOverride(USoundSubmix SoundSubmix, float32 FadeTimeSec)
```
Clears all submix effect overrides on the given submix and returns it to the default effect chain.

### ClearSubmixEffects
```angelscript
void ClearSubmixEffects(USoundSubmix SoundSubmix)
```
Clears all submix effects on the given submix.

### Conv_AudioOutputDeviceInfoToString
```angelscript
FString Conv_AudioOutputDeviceInfoToString(FAudioOutputDeviceInfo Info)
```
Returns the device info in a human readable format
@param info - The audio device data to print
@return The data in a string format

### GetAvailableAudioOutputDevices
```angelscript
void GetAvailableAudioOutputDevices(FOnAudioOutputDevicesObtained OnObtainDevicesEvent)
```
Gets information about all audio output devices available in the system
@param OnObtainDevicesEvent - the event to fire when the audio endpoint devices have been retrieved

### GetCurrentAudioOutputDeviceName
```angelscript
void GetCurrentAudioOutputDeviceName(FOnMainAudioOutputDeviceObtained OnObtainCurrentDeviceEvent)
```
Gets information about the currently used audio output device
@param OnObtainCurrentDeviceEvent - the event to fire when the audio endpoint devices have been retrieved

### GetMagnitudeForFrequencies
```angelscript
void GetMagnitudeForFrequencies(TArray<float32> Frequencies, TArray<float32>& Magnitudes, USoundSubmix SubmixToAnalyze)
```
Retrieve the magnitudes for the given frequencies.

### GetNumberOfEntriesInSourceEffectChain
```angelscript
int GetNumberOfEntriesInSourceEffectChain(USoundEffectSourcePresetChain PresetChain)
```
Returns the number of effect chain entries in the given source effect chain.

### GetPhaseForFrequencies
```angelscript
void GetPhaseForFrequencies(TArray<float32> Frequencies, TArray<float32>& Phases, USoundSubmix SubmixToAnalyze)
```
Retrieve the phases for the given frequencies.

### IsAudioBusActive
```angelscript
bool IsAudioBusActive(UAudioBus AudioBus)
```
Queries if the given audio bus is active (and audio can be mixed to it).

### MakeFullSpectrumSpectralAnalysisBandSettings
```angelscript
TArray<FSoundSubmixSpectralAnalysisBandSettings> MakeFullSpectrumSpectralAnalysisBandSettings(int InNumBands, float32 InMinimumFrequency, float32 InMaximumFrequency, int InAttackTimeMsec, int InReleaseTimeMsec)
```
Make an array of logarithmically spaced bands.

@param InNumBands - The number of bands to used to represent the spectrum.
@param InMinimumFrequency - The center frequency of the first band.
@param InMaximumFrequency - The center frequency of the last band.
@param InAttackTimeMsec - The attack time (in milliseconds) to apply to each band's envelope tracker.
@param InReleaseTimeMsec - The release time (in milliseconds) to apply to each band's envelope tracker.

### MakeMusicalSpectralAnalysisBandSettings
```angelscript
TArray<FSoundSubmixSpectralAnalysisBandSettings> MakeMusicalSpectralAnalysisBandSettings(int InNumSemitones, EMusicalNoteName InStartingMusicalNote, int InStartingOctave, int InAttackTimeMsec, int InReleaseTimeMsec)
```
Make an array of musically spaced bands with ascending frequency.

@param InNumSemitones - The number of semitones to represent.
@param InStartingMuiscalNote - The name of the first note in the array.
@param InStartingOctave - The octave of the first note in the array.
@param InAttackTimeMsec - The attack time (in milliseconds) to apply to each band's envelope tracker.
@param InReleaseTimeMsec - The release time (in milliseconds) to apply to each band's envelope tracker.

### MakePresetSpectralAnalysisBandSettings
```angelscript
TArray<FSoundSubmixSpectralAnalysisBandSettings> MakePresetSpectralAnalysisBandSettings(EAudioSpectrumBandPresetType InBandPresetType, int InNumBands, int InAttackTimeMsec, int InReleaseTimeMsec)
```
Make an array of bands which span the frequency range of a given EAudioSpectrumBandPresetType.

@param InBandPresetType - The type audio content which the bands encompass.
@param InNumBands - The number of bands used to represent the spectrum.
@param InAttackTimeMsec - The attack time (in milliseconds) to apply to each band's envelope tracker.
@param InReleaseTimeMsec - The release time (in milliseconds) to apply to each band's envelope tracker.

### PauseRecordingOutput
```angelscript
void PauseRecordingOutput(USoundSubmix SubmixToPause)
```
Pause recording audio, without finalizing the recording to disk. By leaving the Submix To Record field blank, you can record the master output of the game.

### PrimeSoundCueForPlayback
```angelscript
void PrimeSoundCueForPlayback(USoundCue SoundCue)
```
Begin loading any sounds referenced by a sound cue into the cache so that it can be played immediately.

### PrimeSoundForPlayback
```angelscript
void PrimeSoundForPlayback(USoundWave SoundWave, FOnSoundLoadComplete OnLoadCompletion)
```
Begin loading a sound into the cache so that it can be played immediately.

### RegisterAudioBusToSubmix
```angelscript
void RegisterAudioBusToSubmix(USoundSubmix SoundSubmix, UAudioBus AudioBus)
```
Registers an audio bus to a submix so the submix output can be routed to the audiobus.

### RemoveMasterSubmixEffect
```angelscript
void RemoveMasterSubmixEffect(USoundEffectSubmixPreset SubmixEffectPreset)
```
Removes a submix effect preset from the master submix.

### RemoveSourceEffectFromPresetChain
```angelscript
void RemoveSourceEffectFromPresetChain(USoundEffectSourcePresetChain PresetChain, int EntryIndex)
```
Removes source effect entry from preset chain. Only affects the instance of preset chain.

### RemoveSubmixEffect
```angelscript
void RemoveSubmixEffect(USoundSubmix SoundSubmix, USoundEffectSubmixPreset SubmixEffectPreset)
```
Removes all instances of a submix effect preset from the given submix.

### RemoveSubmixEffectAtIndex
```angelscript
void RemoveSubmixEffectAtIndex(USoundSubmix SoundSubmix, int SubmixChainIndex)
```
Removes the submix effect at the given submix chain index, if there is a submix effect at that index.

### ReplaceSubmixEffect
```angelscript
void ReplaceSubmixEffect(USoundSubmix InSoundSubmix, int SubmixChainIndex, USoundEffectSubmixPreset SubmixEffectPreset)
```
Replaces the submix effect at the given submix chain index, adds the effect if there is none at that index.

### ResumeRecordingOutput
```angelscript
void ResumeRecordingOutput(USoundSubmix SubmixToPause)
```
Resume recording audio after pausing. By leaving the Submix To Pause field blank, you can record the master output of the game.

### SetBypassSourceEffectChainEntry
```angelscript
void SetBypassSourceEffectChainEntry(USoundEffectSourcePresetChain PresetChain, int EntryIndex, bool bBypassed)
```
Set whether or not to bypass the effect at the source effect chain index.

### SetSubmixEffectChainOverride
```angelscript
void SetSubmixEffectChainOverride(USoundSubmix SoundSubmix, TArray<USoundEffectSubmixPreset> SubmixEffectPresetChain, float32 FadeTimeSec)
```
Sets a submix effect chain override on the given submix. The effect chain will cross fade from the base effect chain or current override to the new override.

### StartAnalyzingOutput
```angelscript
void StartAnalyzingOutput(USoundSubmix SubmixToAnalyze, EFFTSize FFTSize, EFFTPeakInterpolationMethod InterpolationMethod, EFFTWindowType WindowType, float32 HopSize, EAudioSpectrumType SpectrumType)
```
Start spectrum analysis of the audio output. By leaving the Submix To Analyze blank, you can analyze the master output of the game.

### StartAudioBus
```angelscript
void StartAudioBus(UAudioBus AudioBus)
```
Starts the given audio bus.

### StartRecordingOutput
```angelscript
void StartRecordingOutput(float32 ExpectedDuration, USoundSubmix SubmixToRecord)
```
Start recording audio. By leaving the Submix To Record field blank, you can record the master output of the game.

### StopAnalyzingOutput
```angelscript
void StopAnalyzingOutput(USoundSubmix SubmixToStopAnalyzing)
```
Stop spectrum analysis.

### StopAudioBus
```angelscript
void StopAudioBus(UAudioBus AudioBus)
```
Stops the given audio bus.

### StopRecordingOutput
```angelscript
USoundWave StopRecordingOutput(EAudioRecordingExportType ExportType, FString Name, FString Path, USoundSubmix SubmixToRecord, USoundWave ExistingSoundWaveToOverwrite)
```
Stop recording audio. Path can be absolute, or relative (to the /Saved/BouncedWavFiles folder). By leaving the Submix To Record field blank, you can record the master output of the game.

### SwapAudioOutputDevice
```angelscript
void SwapAudioOutputDevice(FString NewDeviceId, FOnCompletedDeviceSwap OnCompletedDeviceSwap)
```
Hotswaps to the requested audio output device
@param NewDeviceId - the device Id to swap to
@param OnCompletedDeviceSwap - the event to fire when the audio endpoint devices have been retrieved

### TrimAudioCache
```angelscript
float32 TrimAudioCache(float32 InMegabytesToFree)
```
Trim memory used by the audio cache. Returns the number of megabytes freed.

### UnregisterAudioBusFromSubmix
```angelscript
void UnregisterAudioBusFromSubmix(USoundSubmix SoundSubmix, UAudioBus AudioBus)
```
Unregisters an audio bus that could have been registered to a submix.

