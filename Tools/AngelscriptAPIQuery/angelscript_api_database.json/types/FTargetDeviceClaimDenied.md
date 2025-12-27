# FTargetDeviceClaimDenied

Implements a message that is sent when a device is already claimed by someone else.

@see FTargetDeviceClaimDropped
@see FTargetDeviceClaimRequest

## 属性

### DeviceName
- **类型**: `FString`
- **描述**: Holds the identifier of the device that is already claimed.

### HostName
- **类型**: `FString`
- **描述**: Holds the name of the host computer that claimed the device.

### HostUser
- **类型**: `FString`
- **描述**: Holds the name of the user that claimed the device.

## 方法

### opAssign
```angelscript
FTargetDeviceClaimDenied& opAssign(FTargetDeviceClaimDenied Other)
```

