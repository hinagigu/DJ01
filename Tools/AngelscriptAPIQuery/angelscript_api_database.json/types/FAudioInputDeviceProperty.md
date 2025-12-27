# FAudioInputDeviceProperty

Encapsulates the array of audio input devices which is populated by UTakeRecorderMicrophoneAudioManager and
utilized by the audio input device list in FAudioInputDevicePropertyCustomization.

## 属性

### bUseSystemDefaultAudioDevice
- **类型**: `bool`

### DeviceInfoArray
- **类型**: `TArray<FAudioInputDeviceInfoProperty>`
- **描述**: Holds device information for each of the audio devices available on this system.

### DeviceId
- **类型**: `FString`

### AudioInputBufferSize
- **类型**: `int`

## 方法

### opAssign
```angelscript
FAudioInputDeviceProperty& opAssign(FAudioInputDeviceProperty Other)
```

