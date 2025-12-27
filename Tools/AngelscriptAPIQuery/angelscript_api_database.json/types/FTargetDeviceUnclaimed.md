# FTargetDeviceUnclaimed

Implements a message that is sent when a device is no longer claimed.

@see FTargetDeviceClaimDenied, FTargetDeviceClaimRequest

## 属性

### DeviceName
- **类型**: `FString`
- **描述**: Holds the identifier of the device that is no longer claimed.

### HostName
- **类型**: `FString`
- **描述**: Holds the name of the host computer that had claimed the device.

### HostUser
- **类型**: `FString`
- **描述**: Holds the name of the user that had claimed the device.

## 方法

### opAssign
```angelscript
FTargetDeviceUnclaimed& opAssign(FTargetDeviceUnclaimed Other)
```

