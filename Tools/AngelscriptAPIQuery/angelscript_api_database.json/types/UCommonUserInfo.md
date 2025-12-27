# UCommonUserInfo

**继承自**: `UObject`

Logical representation of an individual user, one of these will exist for all initialized local players

## 属性

### PrimaryInputDevice
- **类型**: `FInputDeviceId`
- **描述**: Primary controller input device for this user, they could also have additional secondary devices

### PlatformUser
- **类型**: `FPlatformUserId`
- **描述**: Specifies the logical user on the local platform, guest users will point to the primary user

### LocalPlayerIndex
- **类型**: `int`
- **描述**: If this user is assigned a LocalPlayer, this will match the index in the GameInstance localplayers array once it is fully created

### bCanBeGuest
- **类型**: `bool`
- **描述**: If true, this user is allowed to be a guest

### bIsGuest
- **类型**: `bool`
- **描述**: If true, this is a guest user attached to primary user 0

### InitializationState
- **类型**: `ECommonUserInitializationState`
- **描述**: Overall state of the user's initialization process

## 方法

### GetCachedPrivilegeResult
```angelscript
ECommonUserPrivilegeResult GetCachedPrivilegeResult(ECommonUserPrivilege Privilege, ECommonUserOnlineContext Context)
```
Returns the most recently queries result for a specific privilege, will return unknown if never queried

### GetDebugString
```angelscript
FString GetDebugString()
```
Returns an internal debug string for this player

### GetNetId
```angelscript
FUniqueNetIdRepl GetNetId(ECommonUserOnlineContext Context)
```
Returns the net id for the given context

### GetNickname
```angelscript
FString GetNickname()
```
Returns the user's human readable nickname

### GetPrivilegeAvailability
```angelscript
ECommonUserAvailability GetPrivilegeAvailability(ECommonUserPrivilege Privilege)
```
Ask about the general availability of a feature, this combines cached results with state

### IsDoingLogin
```angelscript
bool IsDoingLogin()
```
Returns true if this user is in the middle of logging in

### IsLoggedIn
```angelscript
bool IsLoggedIn()
```
Returns true if this user has successfully logged in

