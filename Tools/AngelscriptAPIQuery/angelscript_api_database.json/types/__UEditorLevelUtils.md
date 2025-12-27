# __UEditorLevelUtils

## 方法

### CreateNewStreamingLevel
```angelscript
ULevelStreaming CreateNewStreamingLevel(TSubclassOf<ULevelStreaming> LevelStreamingClass, FString NewLevelPath, bool bMoveSelectedActorsIntoNewLevel)
```
Creates a new streaming level in the current world

@param       LevelStreamingClass                                     The streaming class type instead to use for the level.
@param       NewLevelPath                                            Optional path to the level package path format ("e.g /Game/MyLevel").  If empty, the user will be prompted during the save process.
@param       bMoveSelectedActorsIntoNewLevel         If true, move any selected actors into the new level.

@return      Returns the newly created level, or NULL on failure

### GetLevels
```angelscript
TArray<ULevel> GetLevels(UWorld World)
```
Returns all levels for a world.

@param       World                           World containing levels
@return                                              Set of all levels

### AddLevelToWorld
```angelscript
ULevelStreaming AddLevelToWorld(UWorld World, FString LevelPackageName, TSubclassOf<ULevelStreaming> LevelStreamingClass)
```
Adds the named level package to the world.  Does nothing if the level already exists in the world.

@param       InWorld                         World in which to add the level.
@param       LevelPackageName        The package name ("e.g /Game/MyLevel") of the level package to add.
@param       LevelStreamingClass     The streaming class type to use for the level.

@return                                                              The new level, or NULL if the level couldn't added.

### AddLevelToWorldWithTransform
```angelscript
ULevelStreaming AddLevelToWorldWithTransform(UWorld World, FString LevelPackageName, TSubclassOf<ULevelStreaming> LevelStreamingClass, FTransform LevelTransform)
```
Adds the named level package to the world at the given position.  Does nothing if the level already exists in the world.

@param       InWorld                         World in which to add the level.
@param       LevelPackageName        The package name ("e.g /Game/MyLevel") of the level package to add.
@param       LevelStreamingClass     The streaming class type to use for the level.
@param       LevelTransform          The origin of the new level in the world.

@return                                                              The new level, or NULL if the level couldn't added.

### RemoveLevelFromWorld
```angelscript
bool RemoveLevelFromWorld(ULevel InLevel, bool bClearSelection, bool bResetTransactionBuffer)
```
Removes given level from the world. Note, this will only work for sub-levels in the main level.

@param       InLevel                             Level asset to remove from the world.
@param       bClearSelection                 If true, it will clear the editor selection.
@param       bResetTransactionBuffer If true, it will reset the transaction buffer (i.e. clear undo history)

@return                                                      True if the level was successfully removed.

### MakeLevelCurrent
```angelscript
void MakeLevelCurrent(ULevelStreaming InStreamingLevel)
```
Makes the specified streaming level the current level for editing.
The current level is where actors are spawned to when calling SpawnActor

@return      true    If a level was removed.

### MoveActorsToLevel
```angelscript
int MoveActorsToLevel(TArray<AActor> ActorsToMove, ULevelStreaming DestStreamingLevel, bool bWarnAboutReferences, bool bWarnAboutRenaming)
```
Moves the specified list of actors to the specified streaming level. The new actors will be selected

@param       ActorsToMove                    List of actors to move
@param       DestStreamingLevel              The destination streaming level of the current world to move the actors to
@param       bWarnAboutReferences    Whether or not to show a modal warning about referenced actors that may no longer function after being moved
@return                                                      The number of actors that were successfully moved to the new level

### MoveSelectedActorsToLevel
```angelscript
int MoveSelectedActorsToLevel(ULevelStreaming DestLevel, bool bWarnAboutReferences)
```
Moves the currently selected actors to the specified streaming level. The new actors will be selected

@param       DestStreamingLevel              The destination streaming level of the current world to move the actors to
@param       bWarnAboutReferences    Whether or not to show a modal warning about referenced actors that may no longer function after being moved
@return                                                      The number of actors that were successfully moved to the new level

### SetLevelsVisibility
```angelscript
void SetLevelsVisibility(TArray<ULevel> Levels, TArray<bool> bShouldBeVisible, bool bForceLayersVisible, ELevelVisibilityDirtyMode ModifyMode)
```
Sets a level's visibility in the editor. More efficient than SetLevelsVisibility when changing the visibility of multiple levels simultaneously.

@param       Levels                                  The levels to modify.
@param       bShouldBeVisible                The level's new visibility state for each level.
@param       bForceLayersVisible             If true and the level is visible, force the level's layers to be visible.
@param       ModifyMode                              ELevelVisibilityDirtyMode mode value.

### SetLevelVisibility
```angelscript
void SetLevelVisibility(ULevel Level, bool bShouldBeVisible, bool bForceLayersVisible, ELevelVisibilityDirtyMode ModifyMode)
```
Sets a level's visibility in the editor. Less efficient than SetLevelsVisibility when changing the visibility of multiple levels simultaneously.

@param       Level                                   The level to modify.
@param       bShouldBeVisible                The level's new visibility state.
@param       bForceLayersVisible             If true and the level is visible, force the level's layers to be visible.
@param       ModifyMode                              ELevelVisibilityDirtyMode mode value.

### StaticClass
```angelscript
UClass StaticClass()
```

