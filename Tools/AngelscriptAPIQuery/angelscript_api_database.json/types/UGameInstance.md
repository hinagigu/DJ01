# UGameInstance

**继承自**: `UObject`

GameInstance: high-level manager object for an instance of the running game.
Spawned at game creation and not destroyed until game instance is shut down.
Running as a standalone game, there will be one of these.
Running in PIE (play-in-editor) will generate one of these per PIE instance.

## 属性

### OnPawnControllerChangedDelegates
- **类型**: `FOnPawnControllerChanged`

### OnInputDeviceConnectionChange
- **类型**: `FOnUserInputDeviceConnectionChange`

### OnUserInputDevicePairingChange
- **类型**: `FOnUserInputDevicePairingChange`

## 方法

### CreateInitialPlayer
```angelscript
ULocalPlayer CreateInitialPlayer(FString& OutError)
```

### CreateLocalPlayer
```angelscript
ULocalPlayer CreateLocalPlayer(int ControllerId, FString& OutError, bool bSpawnPlayerController)
```

### CreateLocalPlayer
```angelscript
ULocalPlayer CreateLocalPlayer(FPlatformUserId UserId, FString& OutError, bool bSpawnPlayerController)
```

### AddLocalPlayer
```angelscript
int AddLocalPlayer(ULocalPlayer NewPlayer, FPlatformUserId UserId)
```

### RemoveLocalPlayer
```angelscript
bool RemoveLocalPlayer(ULocalPlayer ExistingPlayer)
```

### GetNumLocalPlayers
```angelscript
int GetNumLocalPlayers()
```

### GetLocalPlayerByIndex
```angelscript
ULocalPlayer GetLocalPlayerByIndex(int Index)
```

### GetFirstLocalPlayerController
```angelscript
APlayerController GetFirstLocalPlayerController(const UWorld World)
```

### FindLocalPlayerFromControllerId
```angelscript
ULocalPlayer FindLocalPlayerFromControllerId(int ControllerId)
```

### FindLocalPlayerFromUniqueNetId
```angelscript
ULocalPlayer FindLocalPlayerFromUniqueNetId(FUniqueNetIdRepl UniqueNetId)
```

### GetFirstGamePlayer
```angelscript
ULocalPlayer GetFirstGamePlayer()
```

### HandleNetworkError
```angelscript
void HandleNetworkError(ENetworkFailure FailureType, bool bIsServer)
```
Opportunity for blueprints to handle network errors.

### HandleTravelError
```angelscript
void HandleTravelError(ETravelFailure FailureType)
```
Opportunity for blueprints to handle travel errors.

### Init
```angelscript
void Init()
```
Opportunity for blueprints to handle the game instance being initialized.

### Shutdown
```angelscript
void Shutdown()
```
Opportunity for blueprints to handle the game instance being shutdown.

