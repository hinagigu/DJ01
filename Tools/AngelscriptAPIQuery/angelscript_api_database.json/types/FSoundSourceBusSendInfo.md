# FSoundSourceBusSendInfo

## 属性

### SourceBusSendLevelControlMethod
- **类型**: `ESourceBusSendLevelControlMethod`
- **描述**: Manual: Use Send Level only
Linear: Interpolate between Min and Max Send Levels based on listener distance (between Distance Min and Distance Max)
Custom Curve: Use the float curve to map Send Level to distance (0.0-1.0 on curve maps to Distance Min - Distance Max)

### SoundSourceBus
- **类型**: `USoundSourceBus`
- **描述**: A source Bus to send the audio to. Source buses sonify (make audible) the audio sent to it and are themselves sounds which take up a voice slot in the audio engine.

### AudioBus
- **类型**: `UAudioBus`
- **描述**: An audio bus to send the audio to. Audio buses can be used to route audio to DSP effects or other purposes. E.g. side-chaining, analysis, etc. Audio buses are not audible unless hooked up to a source bus.

### SendLevel
- **类型**: `float32`
- **描述**: The amount of audio to send to the bus.

### MinSendLevel
- **类型**: `float32`

### MaxSendLevel
- **类型**: `float32`

### MinSendDistance
- **类型**: `float32`

### MaxSendDistance
- **类型**: `float32`

### CustomSendLevelCurve
- **类型**: `FRuntimeFloatCurve`

## 方法

### opAssign
```angelscript
FSoundSourceBusSendInfo& opAssign(FSoundSourceBusSendInfo Other)
```

