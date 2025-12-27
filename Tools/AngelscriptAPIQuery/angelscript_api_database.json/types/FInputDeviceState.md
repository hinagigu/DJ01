# FInputDeviceState

Current state of physical input devices at a point in time.
Assumption is that the state refers to a single physical input device,
ie InputDevice field is a single value of EInputDevices and not a combination.

## 属性

### InputDevice
- **类型**: `EInputDevices`
- **描述**: Which InputDevice member is valid in this state

### bShiftKeyDown
- **类型**: `bool`
- **描述**: Is they keyboard SHIFT modifier key currently pressed down

### bAltKeyDown
- **类型**: `bool`
- **描述**: Is they keyboard ALT modifier key currently pressed down

### bCtrlKeyDown
- **类型**: `bool`
- **描述**: Is they keyboard CTRL modifier key currently pressed down

### bCmdKeyDown
- **类型**: `bool`
- **描述**: Is they keyboard CMD modifier key currently pressed down (only on Apple devices)

### Keyboard
- **类型**: `FKeyboardInputDeviceState`
- **描述**: Current state of Keyboard device, if InputDevice == EInputDevices::Keyboard

### Mouse
- **类型**: `FMouseInputDeviceState`
- **描述**: Current state of Mouse device, if InputDevice == EInputDevices::Mouse

## 方法

### opAssign
```angelscript
FInputDeviceState& opAssign(FInputDeviceState Other)
```

