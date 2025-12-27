# UConstantQNRT

**继承自**: `UAudioSynesthesiaNRT`

UConstantQNRT

UConstantQNRT calculates the temporal evolution of constant q transform for a given
sound. ConstantQ is available for individual channels or the overall sound asset.

## 属性

### Settings
- **类型**: `UConstantQNRTSettings`

## 方法

### GetChannelConstantQAtTime
```angelscript
void GetChannelConstantQAtTime(float32 InSeconds, int InChannel, TArray<float32>& OutConstantQ)
```
Get a specific channel cqt of the analyzed sound at a given time.

### GetNormalizedChannelConstantQAtTime
```angelscript
void GetNormalizedChannelConstantQAtTime(float32 InSeconds, int InChannel, TArray<float32>& OutConstantQ)
```
Get a specific channel cqt of the analyzed sound at a given time.

