# FAudioOutputDeviceInfo

Platform audio output device info, in a Blueprint-readable format

## 属性

### Name
- **类型**: `FString`
- **描述**: The name of the audio device

### DeviceId
- **类型**: `FString`
- **描述**: ID of the device.

### NumChannels
- **类型**: `int`
- **描述**: The number of channels supported by the audio device

### SampleRate
- **类型**: `int`
- **描述**: The sample rate of the audio device

### Format
- **类型**: `EAudioMixerStreamDataFormatType`
- **描述**: The data format of the audio stream

### OutputChannelArray
- **类型**: `TArray<EAudioMixerChannelType>`
- **描述**: The output channel array of the audio device

### bIsSystemDefault
- **类型**: `bool`

### bIsCurrentDevice
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FAudioOutputDeviceInfo& opAssign(FAudioOutputDeviceInfo Other)
```

