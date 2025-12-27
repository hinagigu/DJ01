# ULoudnessNRT

**继承自**: `UAudioSynesthesiaNRT`

ULoudnessNRT

ULoudnessNRT calculates the temporal evolution of perceptual loudness for a given
sound. Loudness is available for individual channels or the overall sound asset. Normalized
loudness values convert the range to 0.0 to 1.0 where 0.0 is the noise floor and 1.0 is the
maximum loudness of the particular sound.

## 属性

### Settings
- **类型**: `ULoudnessNRTSettings`

## 方法

### GetChannelLoudnessAtTime
```angelscript
void GetChannelLoudnessAtTime(float32 InSeconds, int InChannel, float32& OutLoudness)
```
Get a specific channel loudness of the analyzed sound at a given time.

### GetLoudnessAtTime
```angelscript
void GetLoudnessAtTime(float32 InSeconds, float32& OutLoudness)
```
Get the overall loudness of the analyzed sound at a given time.

### GetNormalizedChannelLoudnessAtTime
```angelscript
void GetNormalizedChannelLoudnessAtTime(float32 InSeconds, int InChannel, float32& OutLoudness)
```
Get a specific channel normalized loudness of the analyzed sound at a given time. Normalized
loudness is always between 0.0 to 1.0. 0.0 refers to the noise floor while 1.0 refers to the
maximum loudness in the sound.

### GetNormalizedLoudnessAtTime
```angelscript
void GetNormalizedLoudnessAtTime(float32 InSeconds, float32& OutLoudness)
```
Get the normalized overall loudness of the analyzed sound at a given time. Normalized loudness
is always between 0.0 to 1.0. 0.0 refers to the noise floor while 1.0 refers to the maximum
loudness in the sound.

