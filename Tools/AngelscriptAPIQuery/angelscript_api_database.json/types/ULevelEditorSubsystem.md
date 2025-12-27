# ULevelEditorSubsystem

**继承自**: `UEditorSubsystem`

ULevelEditorSubsystem
Subsystem for exposing Level Editor related functionality to scripts

## 属性

### OnPreSaveWorld
- **类型**: `FOnLevelEditorPreSaveWorld`

### OnPostSaveWorld
- **类型**: `FOnLevelEditorPostSaveWorld`

### OnEditorCameraMoved
- **类型**: `FOnLevelEditorEditorCameraMoved`

### OnMapChanged
- **类型**: `FOnLevelEditorMapChanged`

### OnMapOpened
- **类型**: `FOnLevelEditorMapOpened`

## 方法

### BuildLightMaps
```angelscript
bool BuildLightMaps(ELightingBuildQuality Quality, bool bWithReflectionCaptures)
```
Build Light Maps and optionally the reflection captures.
@param       Quality One of the enum LightingBuildQuality value. Default is Quality_Production.
@param       bWithReflectionCaptures Build the related reflection captures after building the light maps.
@return      True if build was successful.

### EditorGetGameView
```angelscript
bool EditorGetGameView(FName ViewportConfigKey)
```

### EditorInvalidateViewports
```angelscript
void EditorInvalidateViewports()
```

### EditorPlaySimulate
```angelscript
void EditorPlaySimulate()
```

### EditorRequestEndPlay
```angelscript
void EditorRequestEndPlay()
```

### EditorSetGameView
```angelscript
void EditorSetGameView(bool bGameView, FName ViewportConfigKey)
```

### EjectPilotLevelActor
```angelscript
void EjectPilotLevelActor(FName ViewportConfigKey)
```

### GetActiveViewportConfigKey
```angelscript
FName GetActiveViewportConfigKey()
```

### GetAllowsCinematicControl
```angelscript
bool GetAllowsCinematicControl(FName ViewportConfigKey)
```

### GetCurrentLevel
```angelscript
ULevel GetCurrentLevel()
```
Get the current level used by the world editor.
@return       The current level

### GetPilotLevelActor
```angelscript
AActor GetPilotLevelActor(FName ViewportConfigKey)
```

### GetSelectionSet
```angelscript
UTypedElementSelectionSet GetSelectionSet()
```
Get the selection set for the current world, you can use this to track
and create changes to the level editor's selection

### GetViewportConfigKeys
```angelscript
TArray<FName> GetViewportConfigKeys()
```

### IsInPlayInEditor
```angelscript
bool IsInPlayInEditor()
```

### LoadLevel
```angelscript
bool LoadLevel(FString AssetPath)
```
Close the current Persistent Level (without saving it). Loads the specified level.
@param       AssetPath                               Asset Path of the level to be loaded.
             ie. /Game/MyFolder/MyAsset
@return      True if the operation succeeds.

### NewLevel
```angelscript
bool NewLevel(FString AssetPath, bool bIsPartitionedWorld)
```
Close the current Persistent Level (without saving it). Create a new blank Level and save it. Load the new created level.
@param       AssetPath               Asset Path of where the level will be saved.
             ie. /Game/MyFolder/MyAsset
@param   bIsPartitionedWorld If true, new map is partitioned.
@return      True if the operation succeeds.

### NewLevelFromTemplate
```angelscript
bool NewLevelFromTemplate(FString AssetPath, FString TemplateAssetPath)
```
Close the current Persistent Level (without saving it). Create a new Level base on another level and save it. Load the new created level.
@param       AssetPath                               Asset Path of where the level will be saved.
             ie. /Game/MyFolder/MyAsset
@param       TemplateAssetPath               Level to be used as Template.
             ie. /Game/MyFolder/MyAsset
@return      True if the operation succeeds.

### PilotLevelActor
```angelscript
void PilotLevelActor(AActor ActorToPilot, FName ViewportConfigKey)
```

### SaveAllDirtyLevels
```angelscript
bool SaveAllDirtyLevels()
```
Saves all Level currently loaded by the World Editor.
@return      True if the operation succeeds.

### SaveCurrentLevel
```angelscript
bool SaveCurrentLevel()
```
Saves the specified Level. Must already be saved at lease once to have a valid path.
@return      True if the operation succeeds.

### SetAllowsCinematicControl
```angelscript
void SetAllowsCinematicControl(bool bAllow, FName ViewportConfigKey)
```

### SetCurrentLevelByName
```angelscript
bool SetCurrentLevelByName(FName LevelName)
```
Set the current level used by the world editor.
If more than one level shares the same name, the first one encounter of that level name will be used.
@param       LevelName       The name of the Level the actor belongs to (same name as in the ContentBrowser).
@return      True if the operation succeeds.

