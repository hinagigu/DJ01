# UWorld

**继承自**: `UObject`

The World is the top level object representing a map or a sandbox in which Actors and Components will exist and be rendered.

A World can be a single Persistent Level with an optional list of streaming levels that are loaded and unloaded via volumes and blueprint functions
or it can be a collection of levels organized with a World Composition.

In a standalone game, generally only a single World exists except during seamless area transitions when both a destination and current world exists.
In the editor many Worlds exist: The level being edited, each PIE instance, each editor tool which has an interactive rendered viewport, and many more.

## 属性

### WorldType
- **类型**: `EWorldType`

### ThumbnailInfo
- **类型**: `UThumbnailInfo`
- **描述**: Information for thumbnail rendering

## 方法

### IsGameWorld
```angelscript
bool IsGameWorld()
```

### IsEditorWorld
```angelscript
bool IsEditorWorld()
```

### IsPreviewWorld
```angelscript
bool IsPreviewWorld()
```

### ServerTravel
```angelscript
bool ServerTravel(FString FURL, bool bAbsolute, bool bShouldSkipGameNotify)
```

### GetNetMode
```angelscript
ENetMode GetNetMode()
```

### GetGameState
```angelscript
AGameStateBase GetGameState()
```

### GetTimeSeconds
```angelscript
float GetTimeSeconds()
```

### GetUnpausedTimeSeconds
```angelscript
float GetUnpausedTimeSeconds()
```

### GetRealTimeSeconds
```angelscript
float GetRealTimeSeconds()
```

### GetAudioTimeSeconds
```angelscript
float GetAudioTimeSeconds()
```

### GetDeltaSeconds
```angelscript
float32 GetDeltaSeconds()
```

### IsStartingUp
```angelscript
bool IsStartingUp()
```

### IsTearingDown
```angelscript
bool IsTearingDown()
```

### SetGameInstance
```angelscript
void SetGameInstance(UGameInstance NewGI)
```

### GetGameInstance
```angelscript
UGameInstance GetGameInstance()
```

### GetLevelScriptActor
```angelscript
ALevelScriptActor GetLevelScriptActor()
```

### GetPersistentLevel
```angelscript
ULevel GetPersistentLevel()
```

### GetDataLayerManager
```angelscript
UDataLayerManager GetDataLayerManager()
```
Returns the UDataLayerManager associated with this world.

@return UDataLayerManager object associated with this world

### GetWorldSettings
```angelscript
AWorldSettings GetWorldSettings()
```
Returns the AWorldSettings actor associated with this world.

@return AWorldSettings actor associated with this world

### GetStreamingLevels
```angelscript
TArray<ULevelStreaming> GetStreamingLevels()
```

