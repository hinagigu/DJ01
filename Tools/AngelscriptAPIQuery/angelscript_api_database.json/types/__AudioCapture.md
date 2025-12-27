# __AudioCapture

## 方法

### CreateAudioCapture
```angelscript
UAudioCapture CreateAudioCapture()
```

### Conv_AudioInputDeviceInfoToString
```angelscript
FString Conv_AudioInputDeviceInfoToString(FAudioInputDeviceInfo info)
```
Returns the device info in a human readable format
@param info - The audio device data to print
@return The data in a string format

### GetAvailableAudioInputDevices
```angelscript
void GetAvailableAudioInputDevices(FOnAudioInputDevicesObtained OnObtainDevicesEvent)
```
Gets information about all audio output devices available in the system
@param OnObtainDevicesEvent - the event to fire when the audio endpoint devices have been retrieved

