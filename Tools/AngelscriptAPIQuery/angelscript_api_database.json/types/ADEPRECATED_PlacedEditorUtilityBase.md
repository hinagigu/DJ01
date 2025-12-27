# ADEPRECATED_PlacedEditorUtilityBase

**继承自**: `AActor`

## 属性

### HelpText
- **类型**: `FString`

## 方法

### ClearActorSelectionSet
```angelscript
void ClearActorSelectionSet()
```
Remove all actors from the selection set

### GetActorReference
```angelscript
AActor GetActorReference(FString PathToActor)
```
Attempts to find the actor specified by PathToActor in the current editor world
@param        PathToActor     The path to the actor (e.g. PersistentLevel.PlayerStart)
@return       A reference to the actor, or none if it wasn't found

### GetLevelViewportCameraInfo
```angelscript
bool GetLevelViewportCameraInfo(FVector& CameraLocation, FRotator& CameraRotation)
```
Gets information about the camera position for the primary level editor viewport.  In non-editor builds, these will be zeroed

@param       CameraLocation  (out) Current location of the level editing viewport camera, or zero if none found
@param       CameraRotation  (out) Current rotation of the level editing viewport camera, or zero if none found
@return      Whether or not we were able to get a camera for a level editing viewport

### GetSelectionSet
```angelscript
TArray<AActor> GetSelectionSet()
```
Returns the current selection set in the editor.  Note that for non-editor builds, this will return an empty array

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

### SetLevelViewportCameraInfo
```angelscript
void SetLevelViewportCameraInfo(FVector CameraLocation, FRotator CameraRotation)
```
Sets information about the camera position for the primary level editor viewport.

@param        CameraLocation  Location the camera will be moved to.
@param        CameraRotation  Rotation the camera will be set to.

