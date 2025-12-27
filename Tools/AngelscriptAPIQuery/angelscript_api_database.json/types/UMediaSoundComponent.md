# UMediaSoundComponent

**继承自**: `USynthComponent`

Implements a sound component for playing a media player's audio output.

## 属性

### Channels
- **类型**: `EMediaSoundChannels`
- **描述**: Media sound channel type.

### DynamicRateAdjustment
- **类型**: `bool`
- **描述**: Dynamically adjust the sample rate if audio and media clock desynchronize.

### RateAdjustmentFactor
- **类型**: `float32`
- **描述**: Factor for calculating the sample rate adjustment.

If dynamic rate adjustment is enabled, this number is multiplied with the drift
between the audio and media clock (in 100ns ticks) to determine the adjustment.
that is to be multiplied into the current playrate.

### RateAdjustmentRange
- **类型**: `FFloatRange`
- **描述**: The allowed range of dynamic rate adjustment.

If dynamic rate adjustment is enabled, and the necessary adjustment
falls outside of this range, audio samples will be dropped.

## 方法

### GetAttenuationSettingsToApply
```angelscript
bool GetAttenuationSettingsToApply(FSoundAttenuationSettings& OutAttenuationSettings)
```
Get the attenuation settings based on the current component settings.

@param OutAttenuationSettings Will contain the attenuation settings, if available.
@return true if attenuation settings were returned, false if attenuation is disabled.

### GetEnvelopeValue
```angelscript
float32 GetEnvelopeValue()
```
Retrieves the current amplitude envelope.

### GetMediaPlayer
```angelscript
UMediaPlayer GetMediaPlayer()
```
Get the media player that provides the audio samples.

@return The component's media player, or nullptr if not set.
@see SetMediaPlayer

### GetNormalizedSpectralData
```angelscript
TArray<FMediaSoundComponentSpectralData> GetNormalizedSpectralData()
```
Retrieves and normalizes the spectral data if spectral analysis is enabled.

### GetSpectralData
```angelscript
TArray<FMediaSoundComponentSpectralData> GetSpectralData()
```
Retrieves the spectral data if spectral analysis is enabled.

### SetEnableEnvelopeFollowing
```angelscript
void SetEnableEnvelopeFollowing(bool bInEnvelopeFollowing)
```
Turns on amplitude envelope following the audio in the media sound component.

### SetEnableSpectralAnalysis
```angelscript
void SetEnableSpectralAnalysis(bool bInSpectralAnalysisEnabled)
```
Turns on spectral analysis of the audio generated in the media sound component.

### SetEnvelopeFollowingsettings
```angelscript
void SetEnvelopeFollowingsettings(int AttackTimeMsec, int ReleaseTimeMsec)
```
Sets the envelope attack and release times (in ms).

### SetMediaPlayer
```angelscript
void SetMediaPlayer(UMediaPlayer NewMediaPlayer)
```
Set the media player that provides the audio samples.

@param NewMediaPlayer The player to set.
@see GetMediaPlayer

### SetSpectralAnalysisSettings
```angelscript
void SetSpectralAnalysisSettings(TArray<float32> InFrequenciesToAnalyze, EMediaSoundComponentFFTSize InFFTSize)
```
Sets the settings to use for spectral analysis.

