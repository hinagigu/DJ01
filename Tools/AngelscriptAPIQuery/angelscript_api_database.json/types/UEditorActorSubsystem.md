# UEditorActorSubsystem

**继承自**: `UEditorSubsystem`

UEditorActorUtilitiesSubsystem
Subsystem for exposing actor related utilities to scripts,

## 属性

### OnNewActorsDropped
- **类型**: `FOnEditNewActorsDropped`

### OnNewActorsPlaced
- **类型**: `FOnEditNewActorsPlaced`

### OnEditCutActorsBegin
- **类型**: `FOnEditCutActorsBegin`

### OnEditCutActorsEnd
- **类型**: `FOnEditCutActorsEnd`

### OnEditCopyActorsBegin
- **类型**: `FOnEditCopyActorsBegin`

### OnEditCopyActorsEnd
- **类型**: `FOnEditCopyActorsEnd`

### OnEditPasteActorsBegin
- **类型**: `FOnEditPasteActorsBegin`

### OnEditPasteActorsEnd
- **类型**: `FOnEditPasteActorsEnd`

### OnDuplicateActorsBegin
- **类型**: `FOnEditCutActorsBegin`

### OnDuplicateActorsEnd
- **类型**: `FOnDuplicateActorsEnd`

### OnDeleteActorsBegin
- **类型**: `FOnDeleteActorsBegin`

### OnDeleteActorsEnd
- **类型**: `FOnDeleteActorsEnd`

## 方法

### ClearActorSelectionSet
```angelscript
void ClearActorSelectionSet()
```
Remove all actors from the selection set

### ConvertActors
```angelscript
TArray<AActor> ConvertActors(TArray<AActor> Actors, TSubclassOf<AActor> ActorClass, FString StaticMeshPackagePath)
```
Replace in the level all Actors provided with a new actor of type ActorClass. Destroy all Actors provided.
@param       Actors                                  List of Actors to replace.
@param       ActorClass                              Class/Blueprint of the new actor that will be spawn.
@param       StaticMeshPackagePath   If the list contains Brushes and it is requested to change them to StaticMesh, StaticMeshPackagePath is the package path to where the StaticMesh will be created. ie. /Game/MyFolder/

### DeleteSelectedActors
```angelscript
void DeleteSelectedActors(UWorld InWorld)
```
Delete all the selected actors in the given world
@param       InWorld         The world the actors are selected in.

### DestroyActor
```angelscript
bool DestroyActor(AActor ActorToDestroy)
```
Destroy the actor from the world editor. Notify the Editor that the actor got destroyed.
@param       ActorToDestroy  Actor to destroy.
@return      True if the operation succeeds.

### DestroyActors
```angelscript
bool DestroyActors(TArray<AActor> ActorsToDestroy)
```
Destroy the actors from the world editor. Notify the Editor that the actor got destroyed.
@param        ActorsToDestroy         Actors to destroy.
@return       True if the operation succeeds.

### DuplicateActor
```angelscript
AActor DuplicateActor(AActor ActorToDuplicate, UWorld ToWorld, FVector Offset)
```
Duplicate an actor from the world editor.
@param       ActorToDuplicate        Actor to duplicate.
@param       ToWorld                         World to place the duplicated actor in.
@param       Offset                          Translation to offset duplicated actor by.
@return      The duplicated actor, or none if it didn't succeed

### DuplicateActors
```angelscript
TArray<AActor> DuplicateActors(TArray<AActor> ActorsToDuplicate, UWorld ToWorld, FVector Offset)
```
Duplicate actors from the world editor.
@param       ActorsToDuplicate       Actors to duplicate.
@param       ToWorld                         World to place the duplicated actors in.
* @param     Offset                          Translation to offset duplicated actors by.
@return      The duplicated actors, or empty if it didn't succeed

### DuplicateSelectedActors
```angelscript
void DuplicateSelectedActors(UWorld InWorld)
```
Duplicate all the selected actors in the given world
@param       InWorld         The world the actors are selected in.

### GetActorReference
```angelscript
AActor GetActorReference(FString PathToActor)
```
Attempts to find the actor specified by PathToActor in the current editor world
@param        PathToActor     The path to the actor (e.g. PersistentLevel.PlayerStart)
@return       A reference to the actor, or none if it wasn't found

### GetAllLevelActors
```angelscript
TArray<AActor> GetAllLevelActors()
```
Find all loaded Actors in the world editor. Exclude actor that are pending kill, in PIE, PreviewEditor, ...
@return      List of found Actors

### GetAllLevelActorsComponents
```angelscript
TArray<UActorComponent> GetAllLevelActorsComponents()
```
Find all loaded ActorComponent own by an actor in the world editor. Exclude actor that are pending kill, in PIE, PreviewEditor, ...
@return      List of found ActorComponent

### GetSelectedLevelActors
```angelscript
TArray<AActor> GetSelectedLevelActors()
```
Find all loaded Actors that are selected in the world editor. Exclude actor that are pending kill, in PIE, PreviewEditor, ...
@param       ActorClass      Actor Class to find.
@return      List of found Actors

### InvertSelection
```angelscript
void InvertSelection(UWorld InWorld)
```
Invert the selection in the given world
@param       InWorld         The world the selection is in.

### SelectAll
```angelscript
void SelectAll(UWorld InWorld)
```
Select all actors and BSP models in the given world, except those which are hidden
 @param       InWorld         The world the actors are to be selected in.

### SelectAllChildren
```angelscript
void SelectAllChildren(bool bRecurseChildren)
```
Select all children actors of the current selection.

@param   bRecurseChildren    True to recurse through all descendants of the children

### SelectNothing
```angelscript
void SelectNothing()
```
Selects nothing in the editor (another way to clear the selection)

### SetActorSelectionState
```angelscript
void SetActorSelectionState(AActor Actor, bool bShouldBeSelected)
```
Set the selection state for the selected actor

### SetActorTransform
```angelscript
bool SetActorTransform(AActor InActor, FTransform InWorldTransform)
```
Sets the world transform of the given actor, if possible.
@returns false if the world transform could not be set.

### SetComponentTransform
```angelscript
bool SetComponentTransform(USceneComponent InSceneComponent, FTransform InWorldTransform)
```
Sets the world transform of the given component, if possible.
@returns false if the world transform could not be set.

### SetSelectedLevelActors
```angelscript
void SetSelectedLevelActors(TArray<AActor> ActorsToSelect)
```
Clear the current world editor selection and select the provided actors. Exclude actor that are pending kill, in PIE, PreviewEditor, ...
@param       ActorsToSelect  Actor that should be selected in the world editor.

### SpawnActorFromClass
```angelscript
AActor SpawnActorFromClass(TSubclassOf<AActor> ActorClass, FVector Location, FRotator Rotation, bool bTransient)
```
Create an actor and place it in the world editor. Can be created from a Blueprint or a Class.
The actor will be created in the current level and will be selected.
@param       ActorClass              Asset to attempt to use for an actor to place.
@param       Location                Location of the new actor.
@return      The created actor.

### SpawnActorFromObject
```angelscript
AActor SpawnActorFromObject(UObject ObjectToUse, FVector Location, FRotator Rotation, bool bTransient)
```
Create an actor and place it in the world editor. The Actor can be created from a Factory, Archetype, Blueprint, Class or an Asset.
The actor will be created in the current level and will be selected.
@param       ObjectToUse             Asset to attempt to use for an actor to place.
@param       Location                Location of the new actor.
@return      The created actor.

