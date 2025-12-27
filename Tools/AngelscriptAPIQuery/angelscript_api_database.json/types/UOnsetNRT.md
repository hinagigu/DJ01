# UOnsetNRT

**继承自**: `UAudioSynesthesiaNRT`

UOnsetNRT

UOnsetNRT calculates the temporal evolution of constant q transform for a given
sound. Onset is available for individual channels or the overall sound asset.

## 属性

### Settings
- **类型**: `UOnsetNRTSettings`

## 方法

### GetChannelOnsetsBetweenTimes
```angelscript
void GetChannelOnsetsBetweenTimes(float32 InStartSeconds, float32 InEndSeconds, int InChannel, TArray<float32>& OutOnsetTimestamps, TArray<float32>& OutOnsetStrengths)
```
Returns onsets which occured between start and end timestamps.

### GetNormalizedChannelOnsetsBetweenTimes
```angelscript
void GetNormalizedChannelOnsetsBetweenTimes(float32 InStartSeconds, float32 InEndSeconds, int InChannel, TArray<float32>& OutOnsetTimestamps, TArray<float32>& OutOnsetStrengths)
```
Get a specific channel cqt of the analyzed sound at a given time.

