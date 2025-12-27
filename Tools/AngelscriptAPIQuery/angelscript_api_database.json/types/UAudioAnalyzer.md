# UAudioAnalyzer

**继承自**: `UObject`

UAudioAnalyzer

UAudioAnalyzer performs analysis on an audio bus using specific settings and exposes the results via blueprints.

Subclasses of UAudioAnalyzer must implement GetAnalyzerFactoryName() to associate
the UAudioAnalyzer asset with an IAudioAnalyzerFactory implementation.

To support blueprint access, subclasses can implement UFUNCTIONs to expose the data
returned by GetResult().

## 方法

### StartAnalyzing
```angelscript
void StartAnalyzing(UAudioBus AudioBusToAnalyze)
```
Starts analyzing audio from the given audio bus. Optionally override the audio bus desired to analyze.

### StopAnalyzing
```angelscript
void StopAnalyzing()
```
Stops analyzing audio.

