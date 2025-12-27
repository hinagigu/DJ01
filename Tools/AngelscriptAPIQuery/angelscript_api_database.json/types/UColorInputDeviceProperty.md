# UColorInputDeviceProperty

**继承自**: `UInputDeviceProperty`

Set the color of an Input Device to a static color. This will NOT reset the device color when the property
is done evaluating. You can think of this as a "One Shot" effect, where you set the device property color.

NOTE: This property has platform specific implementations and may behave differently per platform.
See the docs for more details on each platform.

## 属性

### ColorData
- **类型**: `FDeviceColorData`

### DeviceOverrideData
- **类型**: `TMap<FName,FDeviceColorData>`

