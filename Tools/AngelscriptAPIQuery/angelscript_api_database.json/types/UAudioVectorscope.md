# UAudioVectorscope

**继承自**: `UWidget`

A vectorscope UMG widget.

Supports displaying waveforms in 2D (Left channel X axis, Right channel Y axis) from incoming audio samples.

## 属性

### VectorscopeStyle
- **类型**: `FAudioVectorscopePanelStyle`

### AudioBus
- **类型**: `UAudioBus`

### bShowGrid
- **类型**: `bool`

### GridDivisions
- **类型**: `int`

### DisplayPersistenceMs
- **类型**: `float32`

### Scale
- **类型**: `float32`

### PanelLayoutType
- **类型**: `EAudioPanelLayoutType`

## 方法

### StartProcessing
```angelscript
void StartProcessing()
```
Starts the vectorscope processing.

### StopProcessing
```angelscript
void StopProcessing()
```
Stops the vectorscope processing.

