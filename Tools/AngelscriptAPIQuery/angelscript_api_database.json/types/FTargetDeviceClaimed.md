# FTargetDeviceClaimed

Implements a message that is sent when a service claimed a device.

@see FTargetDeviceClaimDenied
@see FTargetDeviceClaimDropped

## 属性

### DeviceName
- **类型**: `FString`
- **描述**: Holds the identifier of the device that is being claimed.

### HostName
- **类型**: `FString`
- **描述**: Holds the name of the host computer that is claiming the device.

### HostUser
- **类型**: `FString`
- **描述**: Holds the name of the user that is claiming the device.

## 方法

### opAssign
```angelscript
FTargetDeviceClaimed& opAssign(FTargetDeviceClaimed Other)
```

