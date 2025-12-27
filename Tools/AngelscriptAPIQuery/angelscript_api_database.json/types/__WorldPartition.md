# __WorldPartition

## 方法

### GetActorDescs
```angelscript
bool GetActorDescs(TArray<FActorDesc>& OutActorDescs)
```
Gets all the actor descriptors into the provided array, recursing into actor containers.
@return True if the operation was successful.

### GetActorDescsForActors
```angelscript
bool GetActorDescsForActors(TArray<AActor> InActors, TArray<FActorDesc>& OutActorDescs)
```
Gets all the actor descriptors from the provided actor pointers, which represents descriptors on disk, e.g. will not
reflect properties of unsaved actors.
@return True if the operation was successful.

### GetDataLayerManager
```angelscript
UDataLayerManager GetDataLayerManager()
```
Returns the Data Layer Manager for this object.

### GetEditorWorldBounds
```angelscript
FBox GetEditorWorldBounds()
```
Gets the editor world bounds, which includes all actor descriptors.
@return The editor world bounds.

### GetIntersectingActorDescs
```angelscript
bool GetIntersectingActorDescs(FBox InBox, TArray<FActorDesc>& OutActorDescs)
```
Gets all the actor descriptors intersecting the provided box into the provided array, recursing into actor containers.
@return True if the operation was successful.

### GetRuntimeWorldBounds
```angelscript
FBox GetRuntimeWorldBounds()
```
Gets the runtime world bounds, which only includes actor descriptors that aren't editor only.
@return The runtime world bounds.

### LoadActors
```angelscript
void LoadActors(TArray<FGuid> InActorsToLoad)
```
Load actors

### PinActors
```angelscript
void PinActors(TArray<FGuid> InActorsToPin)
```
Pin actors

### UnloadActors
```angelscript
void UnloadActors(TArray<FGuid> InActorsToUnload)
```
Unload actors

### UnpinActors
```angelscript
void UnpinActors(TArray<FGuid> InActorsToUnpin)
```
Unpin actors

