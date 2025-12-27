# FHardwareDeviceIdentifier

An identifier that can be used to determine what input devices are available based on the FInputDeviceScope.
These mappings should match a FInputDeviceScope that is used by an IInputDevice

## 属性

### InputClassName
- **类型**: `FName`

### HardwareDeviceIdentifier
- **类型**: `FName`

### PrimaryDeviceType
- **类型**: `EHardwareDevicePrimaryType`

### SupportedFeaturesMask
- **类型**: `int`

## 方法

### opAssign
```angelscript
FHardwareDeviceIdentifier& opAssign(FHardwareDeviceIdentifier Other)
```

