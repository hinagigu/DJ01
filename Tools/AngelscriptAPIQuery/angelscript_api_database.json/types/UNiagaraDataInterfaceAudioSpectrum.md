# UNiagaraDataInterfaceAudioSpectrum

**继承自**: `UNiagaraDataInterfaceAudioSubmix`

Data Interface allowing sampling of recent audio spectrum.

## 属性

### Resolution
- **类型**: `int`
- **描述**: The number of spectrum samples to pass to the GPU

### MinimumFrequency
- **类型**: `float32`
- **描述**: The minimum frequency represented in the spectrum.

### MaximumFrequency
- **类型**: `float32`
- **描述**: The maximum frequency represented in the spectrum.

### NoiseFloorDb
- **类型**: `float32`
- **描述**: The decibel level considered as silence. This is used to scale the output of the spectrum.

