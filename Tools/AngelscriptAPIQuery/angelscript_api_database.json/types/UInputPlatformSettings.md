# UInputPlatformSettings

**继承自**: `UPlatformSettings`

Per-Platform input options

## 属性

### MaxTriggerFeedbackPosition
- **类型**: `int`
- **描述**: The maximum position that a trigger can be set to

@see UInputDeviceTriggerFeedbackProperty

### MaxTriggerFeedbackStrength
- **类型**: `int`
- **描述**: The maximum strength that trigger feedback can be set to

@see UInputDeviceTriggerFeedbackProperty

### MaxTriggerVibrationTriggerPosition
- **类型**: `int`
- **描述**: The max position that a vibration trigger effect can be set to.

@see UInputDeviceTriggerVibrationProperty::GetTriggerPositionValue

### MaxTriggerVibrationFrequency
- **类型**: `int`
- **描述**: The max frequency that a trigger vibration can occur

@see UInputDeviceTriggerVibrationProperty::GetVibrationFrequencyValue

### MaxTriggerVibrationAmplitude
- **类型**: `int`
- **描述**: The maximum amplitude that can be set on trigger vibrations

@see UInputDeviceTriggerVibrationProperty::GetVibrationAmplitudeValue

### HardwareDevices
- **类型**: `TArray<FHardwareDeviceIdentifier>`
- **描述**: A list of identifiable hardware devices available on this platform

