# ULevelStreaming

**继承自**: `UObject`

Abstract base class of container object encapsulating data required for streaming and providing
interface for when a level should be streamed in and out of memory.

## 属性

### WorldAsset
- **类型**: `TSoftObjectPtr<UWorld>`
- **描述**: The reference to the world containing the level to load

### LevelTransform
- **类型**: `FTransform`

### LevelColor
- **类型**: `FLinearColor`
- **描述**: The level color used for visualization. (Show -> Advanced -> Level Coloration)

### EditorStreamingVolumes
- **类型**: `TArray<TObjectPtr<ALevelStreamingVolume>>`
- **描述**: The level streaming volumes bound to this level.

### MinTimeBetweenVolumeUnloadRequests
- **类型**: `float32`
- **描述**: Cooldown time in seconds between volume-based unload requests.  Used in preventing spurious unload requests.

### OnLevelLoaded
- **类型**: `FLevelStreamingLoadedStatus`

### OnLevelUnloaded
- **类型**: `FLevelStreamingLoadedStatus`

### OnLevelShown
- **类型**: `FLevelStreamingVisibilityStatus`

### OnLevelHidden
- **类型**: `FLevelStreamingVisibilityStatus`

### StreamingPriority
- **类型**: `int`

### bShouldBeVisible
- **类型**: `bool`

### bShouldBeLoaded
- **类型**: `bool`

### LevelLODIndex
- **类型**: `int`

### bIsStatic
- **类型**: `bool`

### bShouldBlockOnLoad
- **类型**: `bool`

### bShouldBlockOnUnload
- **类型**: `bool`

### bDisableDistanceStreaming
- **类型**: `bool`

### bDrawOnLevelStatusMap
- **类型**: `bool`

## 方法

### CreateInstance
```angelscript
ULevelStreaming CreateInstance(FString UniqueInstanceName)
```
Creates a new instance of this streaming level with a provided unique instance name

### GetIsRequestingUnloadAndRemoval
```angelscript
bool GetIsRequestingUnloadAndRemoval()
```
Returns if the streaming level has requested to be unloaded and removed.

### GetLoadedLevel
```angelscript
ULevel GetLoadedLevel()
```
Gets a pointer to the LoadedLevel value

### GetWorldAssetPackageFName
```angelscript
FName GetWorldAssetPackageFName()
```
Gets the package name for the world asset referred to by this level streaming as an FName

### IsLevelLoaded
```angelscript
bool IsLevelLoaded()
```
Returns whether streaming level is loaded

### IsLevelVisible
```angelscript
bool IsLevelVisible()
```
Returns whether streaming level is visible

### IsStreamingStatePending
```angelscript
bool IsStreamingStatePending()
```
Returns whether level has streaming state change pending

### SetIsRequestingUnloadAndRemoval
```angelscript
void SetIsRequestingUnloadAndRemoval(bool bInIsRequestingUnloadAndRemoval)
```
Sets if the streaming level should be unloaded and removed.

### SetLevelLODIndex
```angelscript
void SetLevelLODIndex(int LODIndex)
```
Sets the world composition level LOD index and marks the streaming level as requiring consideration.

### SetPriority
```angelscript
void SetPriority(int NewPriority)
```
Sets the relative priority of considering the streaming level. Changing the priority will not interrupt the currently considered level, but will affect the next time a level is being selected for evaluation.

### SetShouldBeLoaded
```angelscript
void SetShouldBeLoaded(bool bInShouldBeLoaded)
```
Virtual that can be overridden to change whether a streaming level should be loaded.
Doesn't do anything at the base level as should be loaded defaults to true

### SetShouldBeVisible
```angelscript
void SetShouldBeVisible(bool bInShouldBeVisible)
```
Sets the should be visible flag and marks the streaming level as requiring consideration.

### ShouldBeLoaded
```angelscript
bool ShouldBeLoaded()
```
Return whether this level should be present in memory which in turn tells the
streaming code to stream it in. Please note that a change in value from false
to true only tells the streaming code that it needs to START streaming it in
so the code needs to return true an appropriate amount of time before it is
needed.

@return true if level should be loaded/ streamed in, false otherwise

