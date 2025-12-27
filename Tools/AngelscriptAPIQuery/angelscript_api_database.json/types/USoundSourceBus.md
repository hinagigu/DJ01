# USoundSourceBus

**继承自**: `USoundWave`

A source bus is a type of USoundBase and can be "played" like any sound.

## 属性

### SourceBusChannels
- **类型**: `ESourceBusChannels`
- **描述**: How many channels to use for the source bus if the audio bus is not specified, otherwise it will use the audio bus object's channel count.

### SourceBusDuration
- **类型**: `float32`
- **描述**: The duration (in seconds) to use for the source bus. A duration of 0.0 indicates to play the source bus indefinitely.

### AudioBus
- **类型**: `UAudioBus`
- **描述**: Audio bus to use as audio for this source bus. This source bus will sonify the audio from the audio bus.

