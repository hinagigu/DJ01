# FAudioInputDeviceInfoProperty

Encapsulates audio device properties which are utilized by UI facing classes such as FAudioInputDeviceProperty.

## 属性

### DeviceName
- **类型**: `FString`
- **描述**: User friendly name of the audio device

### DeviceId
- **类型**: `FString`
- **描述**: The unique id used to identify the device

### InputChannels
- **类型**: `int`
- **描述**: The number input channels this device supports

### PreferredSampleRate
- **类型**: `int`
- **描述**: The preferred sample rate for this audio device

### bIsDefaultDevice
- **类型**: `bool`
- **描述**: Boolean indicating if this device is the currently the system selected input device

## 方法

### opAssign
```angelscript
FAudioInputDeviceInfoProperty& opAssign(FAudioInputDeviceInfoProperty Other)
```

