# FTargetDeviceServicePong

Implements a message that is sent in response to target device service discovery messages.

## 属性

### Connected
- **类型**: `bool`
- **描述**: Holds a flag indicating whether the device is currently connected.

### Authorized
- **类型**: `bool`
- **描述**: Holds a flag indicating whether the device is authorized.

### HostName
- **类型**: `FString`
- **描述**: Holds the name of the host computer that the device is attached to.

### HostUser
- **类型**: `FString`
- **描述**: Holds the name of the user under which the host computer is running.

### Make
- **类型**: `FString`
- **描述**: Holds the make of the device, i.e. Microsoft or Sony.

### Model
- **类型**: `FString`
- **描述**: Holds the model of the device.

### Name
- **类型**: `FString`
- **描述**: Holds the human readable name of the device, i.e "Bob's XBox'.

### DeviceUser
- **类型**: `FString`
- **描述**: Holds the name of the user that we log in to remote device as, i.e "root".

### DeviceUserPassword
- **类型**: `FString`
- **描述**: Holds the password of the user that we log in to remote device as, i.e "12345".

### Shared
- **类型**: `bool`
- **描述**: Holds a flag indicating whether this device is shared with other users on the network.

### SupportsMultiLaunch
- **类型**: `bool`
- **描述**: Holds a flag indicating whether the device supports running multiple application instances in parallel.

### SupportsPowerOff
- **类型**: `bool`
- **描述**: Holds a flag indicating whether the device can be powered off.

### SupportsPowerOn
- **类型**: `bool`
- **描述**: Holds a flag indicating whether the device can be powered on.

### SupportsReboot
- **类型**: `bool`
- **描述**: Holds a flag indicating whether the device can be rebooted.

### SupportsVariants
- **类型**: `bool`
- **描述**: Holds a flag indicating whether the device's target platform supports variants.

### Type
- **类型**: `FString`
- **描述**: Holds the device type.

### OSVersion
- **类型**: `FString`
- **描述**: Holds the device OS Version.

### ConnectionType
- **类型**: `FString`
- **描述**: Holds the connection type.

### DefaultVariant
- **类型**: `FName`
- **描述**: Holds the variant name of the default device.

### Variants
- **类型**: `TArray<FTargetDeviceVariant>`
- **描述**: List of the Flavors this service supports

### Aggregated
- **类型**: `bool`
- **描述**: Flag for the "All devices" proxy.

### AllDevicesName
- **类型**: `FString`
- **描述**: Holds the name of "All devices" proxy.

### AllDevicesDefaultVariant
- **类型**: `FName`
- **描述**: Holds the default variant name of "All devices" proxy.

## 方法

### opAssign
```angelscript
FTargetDeviceServicePong& opAssign(FTargetDeviceServicePong Other)
```

