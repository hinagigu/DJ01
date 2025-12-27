# UAudioAnalyzerNRT

**继承自**: `UAudioAnalyzerAssetBase`

UAudioAnalyzerNRT

UAudioAnalyzerNRT applies an analyzer to a sound using specific settings, stores the
results and exposes them via blueprints.

Subclasses of UAudioAnalyzerNRT must implement GetAnalyzerNRTFactoryName() to associate
the UAudioAnalyzerNRT with an IAudioAnalyzerNRTFactory implementation.

To support blueprint access, subclasses can implement UFUNCTIONs to expose the data
returned by GetResult().

## 属性

### Sound
- **类型**: `USoundWave`

### DurationInSeconds
- **类型**: `float32`
- **描述**: The duration of the analyzed audio in seconds.

