# FCommonUserInitializeParams

Parameter struct for initialize functions, this would normally be filled in by wrapper functions like async nodes

## 属性

### LocalPlayerIndex
- **类型**: `int`

### ControllerId
- **类型**: `int`

### PrimaryInputDevice
- **类型**: `FInputDeviceId`
- **描述**: Primary controller input device for this user, they could also have additional secondary devices

### PlatformUser
- **类型**: `FPlatformUserId`
- **描述**: Specifies the logical user on the local platform

### RequestedPrivilege
- **类型**: `ECommonUserPrivilege`

### OnlineContext
- **类型**: `ECommonUserOnlineContext`

### bCanCreateNewLocalPlayer
- **类型**: `bool`

### bCanUseGuestLogin
- **类型**: `bool`

### bSuppressLoginErrors
- **类型**: `bool`

### OnUserInitializeComplete
- **类型**: `FCommonUserOnInitializeComplete`

## 方法

### opAssign
```angelscript
FCommonUserInitializeParams& opAssign(FCommonUserInitializeParams Other)
```

