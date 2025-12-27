# UAudioOscilloscope

**继承自**: `UWidget`

An oscilloscope UMG widget.

Supports displaying waveforms from incoming audio samples.

## 属性

### OscilloscopeStyle
- **类型**: `FAudioOscilloscopePanelStyle`

### AudioBus
- **类型**: `UAudioBus`

### TimeWindowMs
- **类型**: `float32`

### AnalysisPeriodMs
- **类型**: `float32`

### bShowTimeGrid
- **类型**: `bool`

### TimeGridLabelsUnit
- **类型**: `EXAxisLabelsUnit`

### bShowAmplitudeGrid
- **类型**: `bool`

### bShowAmplitudeLabels
- **类型**: `bool`

### AmplitudeGridLabelsUnit
- **类型**: `EYAxisLabelsUnit`

### bShowTriggerThresholdLine
- **类型**: `bool`

### TriggerThreshold
- **类型**: `float32`

### PanelLayoutType
- **类型**: `EAudioPanelLayoutType`

## 方法

### StartProcessing
```angelscript
void StartProcessing()
```
Starts the oscilloscope processing.

### StopProcessing
```angelscript
void StopProcessing()
```
Stops the oscilloscope processing.

