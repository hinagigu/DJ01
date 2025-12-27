# FTargetDeviceServicePowerOff

Implements a message for powering on a target device.

## 属性

### Force
- **类型**: `bool`
- **描述**: Holds a flag indicating whether the power-off should be enforced.

If powering off is not enforced, if may fail if some running application prevents it.

### Operator
- **类型**: `FString`
- **描述**: Holds the name of the user that wishes to power off the device.

## 方法

### opAssign
```angelscript
FTargetDeviceServicePowerOff& opAssign(FTargetDeviceServicePowerOff Other)
```

