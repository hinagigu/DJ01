# UWaveTableBank

**继承自**: `UObject`

## 属性

### SampleMode
- **类型**: `EWaveTableSamplingMode`
- **描述**: Sampling mode used for the bank.

### Resolution
- **类型**: `EWaveTableResolution`
- **描述**: Number of samples cached for each entry in the given bank.

### SampleRate
- **类型**: `int`
- **描述**: Number of samples cached for each entry in the given bank.

### bBipolar
- **类型**: `bool`
- **描述**: Determines if output from curve/wavetable are to be clamped between
[-1.0f, 1.0f] (i.e. for waveform generation, oscillation, etc.)
or [0.0f, 1.0f] (i.e. for enveloping) when sampling curve/wavetable

### Entries
- **类型**: `TArray<FWaveTableBankEntry>`

