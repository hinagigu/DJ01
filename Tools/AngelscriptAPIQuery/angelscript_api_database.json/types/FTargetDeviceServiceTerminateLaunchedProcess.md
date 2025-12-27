# FTargetDeviceServiceTerminateLaunchedProcess

Implements a message for terminating an application running on the device.

@see FTargetDeviceServiceTerminateLaunchedProcess

## 属性

### Variant
- **类型**: `FName`
- **描述**: Holds the variant identifier of the target device to use.

### AppID
- **类型**: `FString`
- **描述**: Holds the identifier of the application to launch.

The semantics of this identifier are target platform specific. In some cases it may be
a GUID, in other cases it may be the path to the application or some other means of
identifying the application. Application identifiers are returned from target device
services as result of successful deployment transactions.

## 方法

### opAssign
```angelscript
FTargetDeviceServiceTerminateLaunchedProcess& opAssign(FTargetDeviceServiceTerminateLaunchedProcess Other)
```

