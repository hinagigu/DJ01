# UDEPRECATED_GlobalEditorUtilityBase

**继承自**: `UObject`

## 属性

### HelpText
- **类型**: `FString`

### bAutoRunDefaultAction
- **类型**: `bool`

### OnEachSelectedActor
- **类型**: `FForEachActorIteratorSignature`

### OnEachSelectedAsset
- **类型**: `FForEachAssetIteratorSignature`

## 方法

### ClearActorSelectionSet
```angelscript
void ClearActorSelectionSet()
```
Remove all actors from the selection set

### ForEachSelectedActor
```angelscript
void ForEachSelectedActor()
```
Calls OnEachSelectedActor for each selected actor

### ForEachSelectedAsset
```angelscript
void ForEachSelectedAsset()
```
Calls OnEachSelectedAsset for each selected asset

### GetActorReference
```angelscript
AActor GetActorReference(FString PathToActor)
```
Attempts to find the actor specified by PathToActor in the current editor world
@param       PathToActor     The path to the actor (e.g. PersistentLevel.PlayerStart)
@return      A reference to the actor, or none if it wasn't found

### GetEditorUserSettings
```angelscript
UEditorPerProjectUserSettings GetEditorUserSettings()
```

### GetSelectedAssets
```angelscript
TArray<UObject> GetSelectedAssets()
```
Gets the set of currently selected assets

### GetSelectionBounds
```angelscript
void GetSelectionBounds(FVector& Origin, FVector& BoxExtent, float32& SphereRadius)
```

### GetSelectionSet
```angelscript
TArray<AActor> GetSelectionSet()
```

### OnDefaultActionClicked
```angelscript
void OnDefaultActionClicked()
```
The default action called when the blutility is invoked if bAutoRunDefaultAction=true (it is never called otherwise)

### RenameAsset
```angelscript
void RenameAsset(UObject Asset, FString NewName)
```
Renames an asset (cannot move folders)

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

