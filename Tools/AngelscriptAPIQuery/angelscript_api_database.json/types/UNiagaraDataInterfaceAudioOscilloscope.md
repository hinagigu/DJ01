# UNiagaraDataInterfaceAudioOscilloscope

**继承自**: `UNiagaraDataInterface`

Data Interface allowing sampling of recent audio data.

## 属性

### Submix
- **类型**: `USoundSubmix`

### Resolution
- **类型**: `int`
- **描述**: The number of samples of audio to pass to the GPU. Audio will be resampled to fit this resolution.
Increasing this number will increase the resolution of the waveform, but will also increase usage of the GPU memory bus,
potentially causing issues across the application.

### ScopeInMilliseconds
- **类型**: `float32`
- **描述**: The number of milliseconds of audio to show.

