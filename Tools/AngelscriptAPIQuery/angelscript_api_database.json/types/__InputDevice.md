# __InputDevice

## 方法

### EqualEqual_InputDeviceId
```angelscript
bool EqualEqual_InputDeviceId(FInputDeviceId A, FInputDeviceId B)
```
Returns true if InputDeviceId A is equal to InputDeviceId B (A == B)

### EqualEqual_PlatformUserId
```angelscript
bool EqualEqual_PlatformUserId(FPlatformUserId A, FPlatformUserId B)
```
Returns true if PlatformUserId A is equal to PlatformUserId B (A == B)

### GetAllActiveUsers
```angelscript
int GetAllActiveUsers(TArray<FPlatformUserId>& OutUsers)
```
Get all currently active platform ids, anyone who has a mapped input device

@param OutUsers              Array that will be populated with the platform users.
@return                              The number of active platform users

### GetAllConnectedInputDevices
```angelscript
int GetAllConnectedInputDevices(TArray<FInputDeviceId>& OutInputDevices)
```
Gather all currently connected input devices

@param OutInputDevices       Array of input devices to populate
@return                                      The number of connected input devices

### GetAllInputDevices
```angelscript
int GetAllInputDevices(TArray<FInputDeviceId>& OutInputDevices)
```
Get all mapped input devices on this platform regardless of their connection state.

@param OutInputDevices       Array of input devices to populate
@return                                      The number of connected input devices

### GetAllInputDevicesForUser
```angelscript
int GetAllInputDevicesForUser(FPlatformUserId UserId, TArray<FInputDeviceId>& OutInputDevices)
```
Populates the OutInputDevices array with any InputDeviceID's that are mapped to the given platform user

@param UserId                                The Platform User to gather the input devices of.
@param OutInputDevices               Array of input device ID's that will be populated with the mapped devices.
@return                                              The number of mapped devices, INDEX_NONE if the user was not found.

### GetDefaultInputDevice
```angelscript
FInputDeviceId GetDefaultInputDevice()
```
Returns the default device id used for things like keyboard/mouse input

### GetInputDeviceConnectionState
```angelscript
EInputDeviceConnectionState GetInputDeviceConnectionState(FInputDeviceId DeviceId)
```
Gets the connection state of the given input device.

@param DeviceId              The device to get the connection state of
@return                              The connection state of the given device. EInputDeviceConnectionState::Unknown if the device is not mapped

### GetPlayerControllerFromInputDevice
```angelscript
APlayerController GetPlayerControllerFromInputDevice(FInputDeviceId DeviceId)
```
Get the player controller who owns the given input device id

### GetPlayerControllerFromPlatformUser
```angelscript
APlayerController GetPlayerControllerFromPlatformUser(FPlatformUserId UserId)
```
Get the player controller who has the given Platform User ID.

### GetPrimaryInputDeviceForUser
```angelscript
FInputDeviceId GetPrimaryInputDeviceForUser(FPlatformUserId UserId)
```
Returns the primary input device used by a specific player, or INPUTDEVICEID_NONE if invalid

### GetPrimaryPlatformUser
```angelscript
FPlatformUserId GetPrimaryPlatformUser()
```
Returns the 'Primary' Platform user for this platform.
This typically has an internal ID of '0' and is used as the default platform user to
map devices such as the keyboard and mouse that don't get assigned unique ID's from their
owning platform code.

### GetUserForInputDevice
```angelscript
FPlatformUserId GetUserForInputDevice(FInputDeviceId DeviceId)
```
Returns the platform user attached to this input device, or PLATFORMUSERID_NONE if invalid

### GetUserForUnpairedInputDevices
```angelscript
FPlatformUserId GetUserForUnpairedInputDevices()
```
Returns the platform user id that is being used for unmapped input devices.
Will be PLATFORMUSERID_NONE if platform does not support this (this is the default behavior)

### InputDeviceId_None
```angelscript
FInputDeviceId InputDeviceId_None()
```
Static invalid input device

### IsDevicePropertyHandleValid
```angelscript
bool IsDevicePropertyHandleValid(FInputDevicePropertyHandle InHandle)
```
Returns true if the given handle is valid

### IsInputDeviceMappedToUnpairedUser
```angelscript
bool IsInputDeviceMappedToUnpairedUser(FInputDeviceId InputDevice)
```
Returns true if the given input device is mapped to the unpaired platform user id.

### IsUnpairedUserId
```angelscript
bool IsUnpairedUserId(FPlatformUserId PlatformId)
```
Returns true if the given Platform User Id is the user for unpaired input devices on this platform.

### IsValidInputDevice
```angelscript
bool IsValidInputDevice(FInputDeviceId DeviceId)
```
Check if the given input device is valid

@return      True if the given input device is valid (it has been assigned an ID by the PlatformInputDeviceMapper)

### IsValidPlatformId
```angelscript
bool IsValidPlatformId(FPlatformUserId UserId)
```
Check if the given platform ID is valid

@return      True if the platform ID is valid (it has been assigned by the PlatformInputDeviceMapper)

### NotEqual_InputDeviceId
```angelscript
bool NotEqual_InputDeviceId(FInputDeviceId A, FInputDeviceId B)
```
Returns true if InputDeviceId A is not equal to InputDeviceId B (A != B)

### NotEqual_PlatformUserId
```angelscript
bool NotEqual_PlatformUserId(FPlatformUserId A, FPlatformUserId B)
```
Returns true if PlatformUserId A is not equal to PlatformUserId B (A != B)

### PlatformUserId_None
```angelscript
FPlatformUserId PlatformUserId_None()
```
Static invalid platform user

