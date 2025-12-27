# ULoudnessAnalyzer

**继承自**: `UAudioAnalyzer`

ULoudnessAnalyzer

ULoudnessAnalyzer calculates the temporal evolution of perceptual loudness for a given
audio bus in real-time. Loudness is available for individual channels or the overall audio bus. Normalized
loudness values convert the range to 0.0 to 1.0 where 0.0 is the noise floor and 1.0 is the
maximum loudness of the particular sound.

## 属性

### Settings
- **类型**: `ULoudnessSettings`

### OnOverallLoudnessResults
- **类型**: `FOnOverallLoudnessResults`

### OnPerChannelLoudnessResults
- **类型**: `FOnPerChannelLoudnessResults`

### OnLatestOverallLoudnessResults
- **类型**: `FOnLatestOverallLoudnessResults`

### OnLatestPerChannelLoudnessResults
- **类型**: `FOnLatestPerChannelLoudnessResults`

