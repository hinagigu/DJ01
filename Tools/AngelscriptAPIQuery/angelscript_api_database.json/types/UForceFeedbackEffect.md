# UForceFeedbackEffect

**继承自**: `UObject`

A predefined force-feedback effect to be played on a controller

## 属性

### ChannelDetails
- **类型**: `TArray<FForceFeedbackChannelDetails>`

### PerDeviceOverrides
- **类型**: `TMap<FName,FForceFeedbackEffectOverridenChannelDetails>`
- **描述**: A map of platform name -> ForceFeedback channel details

### DeviceProperties
- **类型**: `TArray<TObjectPtr<UInputDeviceProperty>>`
- **描述**: A map of input device properties that we want to set while this effect is playing

### Duration
- **类型**: `float32`
- **描述**: Duration of force feedback pattern in seconds.

