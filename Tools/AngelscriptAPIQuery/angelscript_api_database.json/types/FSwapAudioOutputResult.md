# FSwapAudioOutputResult

Out structure for use with AudioMixerBlueprintLibrary::SwapAudioOutputDevice

## 属性

### CurrentDeviceId
- **类型**: `FString`
- **描述**: ID of the currently set device.  This is the device at the time of the call, NOT the resulting deviceId

### RequestedDeviceId
- **类型**: `FString`
- **描述**: ID of the requested device.

### Result
- **类型**: `ESwapAudioOutputDeviceResultState`
- **描述**: Result of the call

## 方法

### opAssign
```angelscript
FSwapAudioOutputResult& opAssign(FSwapAudioOutputResult Other)
```

