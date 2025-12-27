# UMovieSceneAudioSection

**继承自**: `UMovieSceneSection`

Audio section, for use in the audio track, or by attached audio objects

## 属性

### StartFrameOffset
- **类型**: `FFrameNumber`
- **描述**: The offset into the beginning of the audio clip

### bLooping
- **类型**: `bool`
- **描述**: Allow looping if the section length is greater than the sound duration

### bSuppressSubtitles
- **类型**: `bool`

### bOverrideAttenuation
- **类型**: `bool`
- **描述**: Should the attenuation settings on this section be used.

## 方法

### GetAttenuationSettings
```angelscript
USoundAttenuation GetAttenuationSettings()
```
@return The attenuation settings

### GetLooping
```angelscript
bool GetLooping()
```
@return Whether to allow looping if the section length is greater than the sound duration

### GetOverrideAttenuation
```angelscript
bool GetOverrideAttenuation()
```
@return Whether override settings on this section should be used

### GetSound
```angelscript
USoundBase GetSound()
```
Gets the sound for this section

### GetStartOffset
```angelscript
FFrameNumber GetStartOffset()
```
Get the offset into the beginning of the audio clip

### GetSuppressSubtitles
```angelscript
bool GetSuppressSubtitles()
```
@return Whether subtitles should be suppressed

### SetAttenuationSettings
```angelscript
void SetAttenuationSettings(USoundAttenuation InAttenuationSettings)
```
Set the attenuation settings for this audio section

### SetLooping
```angelscript
void SetLooping(bool bInLooping)
```
Set whether the sound should be looped

### SetOverrideAttenuation
```angelscript
void SetOverrideAttenuation(bool bInOverrideAttenuation)
```
Set whether the attentuation should be overriden

### SetSound
```angelscript
void SetSound(USoundBase InSound)
```
Sets this section's sound

### SetStartOffset
```angelscript
void SetStartOffset(FFrameNumber InStartOffset)
```
Set the offset into the beginning of the audio clip

### SetSuppressSubtitles
```angelscript
void SetSuppressSubtitles(bool bInSuppressSubtitles)
```
Set whether subtitles should be suppressed

