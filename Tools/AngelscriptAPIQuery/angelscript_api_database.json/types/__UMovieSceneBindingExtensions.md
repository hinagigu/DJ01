# __UMovieSceneBindingExtensions

## 方法

### AddTrack
```angelscript
UMovieSceneTrack AddTrack(FMovieSceneBindingProxy InBinding, TSubclassOf<UMovieSceneTrack> TrackType)
```
Add a new track to the specified binding

@param InBinding     The binding to add tracks to
@param TrackType     A UMovieSceneTrack class type specifying the type of track to create
@return The newly created track, if successful

### FindTracksByExactType
```angelscript
TArray<UMovieSceneTrack> FindTracksByExactType(FMovieSceneBindingProxy InBinding, TSubclassOf<UMovieSceneTrack> TrackType)
```
Find all tracks within a given binding of the specified type, not allowing sub-classed types

@param InBinding     The binding to find tracks in
@param TrackType     A UMovieSceneTrack class type specifying the exact types of track to return
@return An array containing any tracks that are exactly the same as the type specified

### FindTracksByType
```angelscript
TArray<UMovieSceneTrack> FindTracksByType(FMovieSceneBindingProxy InBinding, TSubclassOf<UMovieSceneTrack> TrackType)
```
Find all tracks within a given binding of the specified type

@param InBinding     The binding to find tracks in
@param TrackType     A UMovieSceneTrack class type specifying which types of track to return
@return An array containing any tracks that match the type specified

### GetChildPossessables
```angelscript
TArray<FMovieSceneBindingProxy> GetChildPossessables(FMovieSceneBindingProxy InBinding)
```
Get all the children of this binding

@param InBinding     The binding to to get children of
@return An array containing all the binding's children

### GetDisplayName
```angelscript
FText GetDisplayName(FMovieSceneBindingProxy InBinding)
```
Get this binding's name

@param InBinding     The binding to get the name of
@return The display name of the binding

### GetId
```angelscript
FGuid GetId(FMovieSceneBindingProxy InBinding)
```
Get this binding's ID

@param InBinding     The binding to get the ID of
@return The guid that uniquely represents this binding

### GetName
```angelscript
FString GetName(FMovieSceneBindingProxy InBinding)
```
Get this binding's object non-display name

@param InBinding     The binding to get the name of
@return The name of the binding

### GetObjectTemplate
```angelscript
UObject GetObjectTemplate(FMovieSceneBindingProxy InBinding)
```
Get this binding's object template

@param InBinding     The binding to get the object template of
@return The object template of the binding

### GetParent
```angelscript
FMovieSceneBindingProxy GetParent(FMovieSceneBindingProxy InBinding)
```
Get the parent of this binding

@param InBinding     The binding to get the parent of
@return The binding's parent

### GetPossessedObjectClass
```angelscript
UClass GetPossessedObjectClass(FMovieSceneBindingProxy InBinding)
```
Get this binding's possessed object class

@param InBinding     The binding to get the possessed object class of
@return The possessed object class of the binding

### GetSortingOrder
```angelscript
int GetSortingOrder(FMovieSceneBindingProxy InBinding)
```
Get the sorting order for this binding

@param InBinding        The binding to get the sorting order from
@return The sorting order of the requested binding

### GetTracks
```angelscript
TArray<UMovieSceneTrack> GetTracks(FMovieSceneBindingProxy InBinding)
```
Get all the tracks stored within this binding

@param InBinding     The binding to find tracks in
@return An array containing all the binding's tracks

### IsValid
```angelscript
bool IsValid(FMovieSceneBindingProxy InBinding)
```
Check whether the specified binding is valid

### MoveBindingContents
```angelscript
void MoveBindingContents(FMovieSceneBindingProxy SourceBindingId, FMovieSceneBindingProxy DestinationBindingId)
```
Move all the contents (tracks, child bindings) of the specified binding ID onto another

@param SourceBindingId The identifier of the binding ID to move all tracks and children from
@param DestinationBindingId The identifier of the binding ID to move the contents to

### Remove
```angelscript
void Remove(FMovieSceneBindingProxy InBinding)
```
Remove the specified binding

@param InBinding     The binding to remove the track from

### RemoveTrack
```angelscript
void RemoveTrack(FMovieSceneBindingProxy InBinding, UMovieSceneTrack TrackToRemove)
```
Remove the specified track from this binding

@param InBinding     The binding to remove the track from
@param TrackToRemove The track to remove

### SetDisplayName
```angelscript
void SetDisplayName(FMovieSceneBindingProxy InBinding, FText InDisplayName)
```
Set this binding's name

@param InBinding     The binding to get the name of
@param InName The display name of the binding

### SetName
```angelscript
void SetName(FMovieSceneBindingProxy InBinding, FString InName)
```
Set this binding's object non-display name

@param InBinding     The binding to get the name of
@param InName The name of the binding

### SetParent
```angelscript
void SetParent(FMovieSceneBindingProxy InBinding, FMovieSceneBindingProxy InParentBinding)
```
Set the parent to this binding

@param InBinding     The binding to set
@param InParentBinding     The parent to set the InBinding to

### SetSortingOrder
```angelscript
void SetSortingOrder(FMovieSceneBindingProxy InBinding, int SortingOrder)
```
Set the sorting order for this binding

@param InBinding        The binding to get the sorting order from
@param SortingOrder The sorting order to set

### SetSpawnableBindingID
```angelscript
void SetSpawnableBindingID(FMovieSceneBindingProxy InBinding, FMovieSceneObjectBindingID SpawnableBindingID)
```
Set the spawnable id that the possessable binding should possess

@param InBinding     The binding to set
@param SpawnableBindingID The spawnable's binding id

### StaticClass
```angelscript
UClass StaticClass()
```

