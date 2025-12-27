# FAudioInputDeviceInfo

Platform audio input device info, in a Blueprint-readable format

## 属性

### DeviceName
- **类型**: `FString`
- **描述**: The name of the audio device

### DeviceId
- **类型**: `FString`
- **描述**: ID of the device.

### InputChannels
- **类型**: `int`
- **描述**: The number of channels supported by the audio device

### PreferredSampleRate
- **类型**: `int`
- **描述**: The preferred sample rate of the audio device

### bSupportsHardwareAEC
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FAudioInputDeviceInfo& opAssign(FAudioInputDeviceInfo Other)
```

