# __ULocalPlayerSaveGame

## 方法

### AsyncLoadOrCreateSaveGameForLocalPlayer
```angelscript
bool AsyncLoadOrCreateSaveGameForLocalPlayer(TSubclassOf<ULocalPlayerSaveGame> SaveGameClass, APlayerController LocalPlayerController, FString SlotName, FOnLocalPlayerSaveGameLoaded Delegate)
```
Asynchronously loads a save game object in the specified slot for the local player, if this returns true the delegate will get called later.
False means the load was never scheduled, otherwise it will create and initialize a new instance before calling the delegate if loading failed.

### LoadOrCreateSaveGameForLocalPlayer
```angelscript
ULocalPlayerSaveGame LoadOrCreateSaveGameForLocalPlayer(TSubclassOf<ULocalPlayerSaveGame> SaveGameClass, APlayerController LocalPlayerController, FString SlotName)
```
Synchronously loads a save game object in the specified slot for the local player, stalling the main thread until it completes.
This will return null for invalid parameters, but will create a new instance if the parameters are valid but loading fails.

### StaticClass
```angelscript
UClass StaticClass()
```

