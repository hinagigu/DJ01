# FSubmixEffectMultibandCompressorSettings

A submix dynamics processor

## 属性

### DynamicsProcessorType
- **类型**: `ESubmixEffectDynamicsProcessorType`

### PeakMode
- **类型**: `ESubmixEffectDynamicsPeakMode`

### LinkMode
- **类型**: `ESubmixEffectDynamicsChannelLinkMode`

### LookAheadMsec
- **类型**: `float32`

### bAnalogMode
- **类型**: `bool`

### bFourPole
- **类型**: `bool`

### bBypass
- **类型**: `bool`

### KeySource
- **类型**: `ESubmixEffectDynamicsKeySource`

### ExternalAudioBus
- **类型**: `UAudioBus`

### ExternalSubmix
- **类型**: `USoundSubmix`

### KeyGainDb
- **类型**: `float32`

### bKeyAudition
- **类型**: `bool`

### Bands
- **类型**: `TArray<FDynamicsBandSettings>`

## 方法

### opAssign
```angelscript
FSubmixEffectMultibandCompressorSettings& opAssign(FSubmixEffectMultibandCompressorSettings Other)
```

