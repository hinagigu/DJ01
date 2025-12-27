# USoundSubmix

**继承自**: `USoundSubmixWithParentBase`

Sound Submix class meant for applying an effect to the downmixed sum of multiple audio sources.

## 属性

### SubmixEffectChain
- **类型**: `TArray<TObjectPtr<USoundEffectSubmixPreset>>`

### AmbisonicsPluginSettings
- **类型**: `USoundfieldEncodingSettingsBase`

### EnvelopeFollowerAttackTime
- **类型**: `int`

### EnvelopeFollowerReleaseTime
- **类型**: `int`

### OutputVolumeModulation
- **类型**: `FSoundModulationDestinationSettings`

### WetLevelModulation
- **类型**: `FSoundModulationDestinationSettings`

### DryLevelModulation
- **类型**: `FSoundModulationDestinationSettings`

### AudioLinkSettings
- **类型**: `UAudioLinkSettingsAbstract`

### OnSubmixRecordedFileDone
- **类型**: `FOnSubmixRecordedFileDone`

### bMuteWhenBackgrounded
- **类型**: `bool`

### bSendToAudioLink
- **类型**: `bool`

## 方法

### AddEnvelopeFollowerDelegate
```angelscript
void AddEnvelopeFollowerDelegate(FOnSubmixEnvelopeBP OnSubmixEnvelopeBP)
```
Adds an envelope follower delegate to the submix when envelope following is enabled on this submix.
@param  OnSubmixEnvelopeBP      Event to fire when new envelope data is available.

### AddSpectralAnalysisDelegate
```angelscript
void AddSpectralAnalysisDelegate(TArray<FSoundSubmixSpectralAnalysisBandSettings> InBandSettings, FOnSubmixSpectralAnalysisBP OnSubmixSpectralAnalysisBP, float32 UpdateRate, float32 DecibelNoiseFloor, bool bDoNormalize, bool bDoAutoRange, float32 AutoRangeAttackTime, float32 AutoRangeReleaseTime)
```
Adds a spectral analysis delegate to receive notifications when this submix has spectrum analysis enabled.
@param  InBandsettings                                  The frequency bands to analyze and their envelope-following settings.
@param  OnSubmixSpectralAnalysisBP          Event to fire when new spectral data is available.
@param  UpdateRate                                              How often to retrieve the data from the spectral analyzer and broadcast the event. Max is 30 times per second.
@param  InterpMethod                    Method to used for band peak calculation.
@param  SpectrumType                    Metric to use when returning spectrum values.
@param  DecibelNoiseFloor               Decibel Noise Floor to consider as silence when using a Decibel Spectrum Type.
@param  bDoNormalize                    If true, output band values will be normalized between zero and one.
@param  bDoAutoRange                    If true, output band values will have their ranges automatically adjusted to the minimum and maximum values in the audio. Output band values will be normalized between zero and one.
@param  AutoRangeAttackTime             The time (in seconds) it takes for the range to expand to 90% of a larger range.
@param  AutoRangeReleaseTime            The time (in seconds) it takes for the range to shrink to 90% of a smaller range.

### RemoveSpectralAnalysisDelegate
```angelscript
void RemoveSpectralAnalysisDelegate(FOnSubmixSpectralAnalysisBP OnSubmixSpectralAnalysisBP)
```
Remove a spectral analysis delegate.
@param  OnSubmixSpectralAnalysisBP          The event delegate to remove.

### SetSubmixDryLevel
```angelscript
void SetSubmixDryLevel(float32 InDryLevel)
```
Sets the output volume of the submix in linear gain. This dynamic level acts as a multiplier on the DryLevel property of this submix.

### SetSubmixOutputVolume
```angelscript
void SetSubmixOutputVolume(float32 InOutputVolume)
```
Sets the output volume of the submix in linear gain. This dynamic volume acts as a multiplier on the OutputVolume property of this submix.

### SetSubmixWetLevel
```angelscript
void SetSubmixWetLevel(float32 InWetLevel)
```
Sets the output volume of the submix in linear gain. This dynamic level acts as a multiplier on the WetLevel property of this submix.

### StartEnvelopeFollowing
```angelscript
void StartEnvelopeFollowing()
```
Start envelope following the submix output. Register with OnSubmixEnvelope to receive envelope follower data in BP.

### StartRecordingOutput
```angelscript
void StartRecordingOutput(float32 ExpectedDuration)
```
Start recording the audio from this submix.

### StartSpectralAnalysis
```angelscript
void StartSpectralAnalysis(EFFTSize FFTSize, EFFTPeakInterpolationMethod InterpolationMethod, EFFTWindowType WindowType, float32 HopSize, EAudioSpectrumType SpectrumType)
```
Start spectrum analysis of the audio output.

### StopEnvelopeFollowing
```angelscript
void StopEnvelopeFollowing()
```
Start envelope following the submix output. Register with OnSubmixEnvelope to receive envelope follower data in BP.

### StopRecordingOutput
```angelscript
void StopRecordingOutput(EAudioRecordingExportType ExportType, FString Name, FString Path, USoundWave ExistingSoundWaveToOverwrite)
```
Finish recording the audio from this submix and export it as a wav file or a USoundWave.

### StopSpectralAnalysis
```angelscript
void StopSpectralAnalysis()
```
Stop spectrum analysis of the audio output.

