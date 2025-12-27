# ULocalPlayer

**继承自**: `UPlayer`

Each player that is active on the current client/listen server has a LocalPlayer.
It stays active across maps, and there may be several spawned in the case of splitscreen/coop.
There will be 0 spawned on dedicated servers.

## 方法

### GetWorld
```angelscript
UWorld GetWorld()
```

### GetGameInstance
```angelscript
UGameInstance GetGameInstance()
```

### GetControllerId
```angelscript
int GetControllerId()
```

