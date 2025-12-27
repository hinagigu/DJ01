# UCommonUserSubsystem

**继承自**: `UGameInstanceSubsystem`

Game subsystem that handles queries and changes to user identity and login status.
One subsystem is created for each game instance and can be accessed from blueprints or C++ code.
If a game-specific subclass exists, this base subsystem will not be created.

## 属性

### OnUserInitializeComplete
- **类型**: `FCommonUserOnInitializeCompleteMulticast`

### OnHandleSystemMessage
- **类型**: `FCommonUserHandleSystemMessageDelegate`

### OnUserPrivilegeChanged
- **类型**: `FCommonUserAvailabilityChangedDelegate`

## 方法

### CancelUserInitialization
```angelscript
bool CancelUserInitialization(int LocalPlayerIndex)
```
Attempts to cancel an in-progress initialization attempt, this may not work on all platforms but will disable callbacks

### GetLocalPlayerInitializationState
```angelscript
ECommonUserInitializationState GetLocalPlayerInitializationState(int LocalPlayerIndex)
```
Returns the state of initializing the specified local player

### GetMaxLocalPlayers
```angelscript
int GetMaxLocalPlayers()
```
Gets the maximum number of local players

### GetNumLocalPlayers
```angelscript
int GetNumLocalPlayers()
```
Gets the current number of local players, will always be at least 1

### GetUserInfoForControllerId
```angelscript
const UCommonUserInfo GetUserInfoForControllerId(int ControllerId)
```
Deprecated, use InputDeviceId when available

### GetUserInfoForInputDevice
```angelscript
const UCommonUserInfo GetUserInfoForInputDevice(FInputDeviceId InputDevice)
```
Returns the user info for a given input device. Can return null

### GetUserInfoForLocalPlayerIndex
```angelscript
const UCommonUserInfo GetUserInfoForLocalPlayerIndex(int LocalPlayerIndex)
```
Returns the user info for a given local player index in game instance, 0 is always valid in a running game

### GetUserInfoForPlatformUser
```angelscript
const UCommonUserInfo GetUserInfoForPlatformUser(FPlatformUserId PlatformUser)
```
Returns the primary user info for a given platform user index. Can return null

### GetUserInfoForPlatformUserIndex
```angelscript
const UCommonUserInfo GetUserInfoForPlatformUserIndex(int PlatformUserIndex)
```
Deprecated, use PlatformUserId when available

### GetUserInfoForUniqueNetId
```angelscript
const UCommonUserInfo GetUserInfoForUniqueNetId(FUniqueNetIdRepl NetId)
```
Returns the user info for a unique net id. Can return null

### HasTraitTag
```angelscript
bool HasTraitTag(FGameplayTag TraitTag)
```
Checks if a specific platform/feature tag is enabled

### ListenForLoginKeyInput
```angelscript
void ListenForLoginKeyInput(TArray<FKey> AnyUserKeys, TArray<FKey> NewUserKeys, FCommonUserInitializeParams Params)
```
Starts the process of listening for user input for new and existing controllers and logging them.
This will insert a key input handler on the active GameViewportClient and is turned off by calling again with empty key arrays.

@param AnyUserKeys           Listen for these keys for any user, even the default user. Set this for an initial press start screen or empty to disable
@param NewUserKeys           Listen for these keys for a new user without a player controller. Set this for splitscreen/local multiplayer or empty to disable
@param Params                        Params passed to TryToInitializeUser after detecting key input

### ResetUserState
```angelscript
void ResetUserState()
```
Resets the login and initialization state when returning to the main menu after an error

### SendSystemMessage
```angelscript
void SendSystemMessage(FGameplayTag MessageType, FText TitleText, FText BodyText)
```
Send a system message via OnHandleSystemMessage

### SetMaxLocalPlayers
```angelscript
void SetMaxLocalPlayers(int InMaxLocalPLayers)
```
Sets the maximum number of local players, will not destroy existing ones

### ShouldWaitForStartInput
```angelscript
bool ShouldWaitForStartInput()
```
Checks to see if we should display a press start/input confirmation screen at startup. Games can call this or check the trait tags directly

### TryToInitializeForLocalPlay
```angelscript
bool TryToInitializeForLocalPlay(int LocalPlayerIndex, FInputDeviceId PrimaryInputDevice, bool bCanUseGuestLogin)
```
Tries to start the process of creating or updating a local player, including logging in and creating a player controller.
When the process has succeeded or failed, it will broadcast the OnUserInitializeComplete delegate.

@param LocalPlayerIndex      Desired index of LocalPlayer in Game Instance, 0 will be primary player and 1+ for local multiplayer
@param PrimaryInputDevice The physical controller that should be mapped to this user, will use the default device if invalid
@param bCanUseGuestLogin     If true, this player can be a guest without a real Unique Net Id

@returns true if the process was started, false if it failed before properly starting

### TryToInitializeUser
```angelscript
bool TryToInitializeUser(FCommonUserInitializeParams Params)
```
Starts a general user login and initialization process, using the params structure to determine what to log in to.
When the process has succeeded or failed, it will broadcast the OnUserInitializeComplete delegate.
AsyncAction_CommonUserInitialize provides several wrapper functions for using this in an Event graph.

@returns true if the process was started, false if it failed before properly starting

### TryToLoginForOnlinePlay
```angelscript
bool TryToLoginForOnlinePlay(int LocalPlayerIndex)
```
Starts the process of taking a locally logged in user and doing a full online login including account permission checks.
When the process has succeeded or failed, it will broadcast the OnUserInitializeComplete delegate.

@param LocalPlayerIndex      Index of existing LocalPlayer in Game Instance

@returns true if the process was started, false if it failed before properly starting

### TryToLogOutUser
```angelscript
bool TryToLogOutUser(int LocalPlayerIndex, bool bDestroyPlayer)
```
Logs a player out of any online systems, and optionally destroys the player entirely if it's not the first one

