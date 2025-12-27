# ULayersSubsystem

**继承自**: `UEditorSubsystem`

## 方法

### AddActorsToLayer
```angelscript
bool AddActorsToLayer(TArray<AActor> Actors, FName LayerName)
```
Add the actors to the named layer

@param       Actors          The actors to add to the named layer
@param       LayerName       The name of the layer to add to
@return                              true if at least one actor was added to the layer.  false is returned if all the actors already belonged to the layer.

### AddActorsToLayers
```angelscript
bool AddActorsToLayers(TArray<AActor> Actors, TArray<FName> LayerNames)
```
Add the actors to the named layers

@param       Actors          The actors to add to the named layers
@param       LayerNames      A valid list of layer names.
@return                              true if at least one actor was added to at least one layer.  false is returned if all the actors already belonged to all specified layers.

### AddActorToLayer
```angelscript
bool AddActorToLayer(AActor Actor, FName LayerName)
```
Adds the actor to the named layer.

@param       Actor           The actor to add to the named layer
@param       LayerName       The name of the layer to add the actor to
@return                              true if the actor was added.  false is returned if the actor already belongs to the layer.

### AddActorToLayers
```angelscript
bool AddActorToLayers(AActor Actor, TArray<FName> LayerNames)
```
Adds the provided actor to the named layers.

@param       Actor           The actor to add to the provided layers
@param       LayerNames      A valid list of layer names.
@return                              true if the actor was added to at least one of the provided layers.

### AddAllLayerNamesTo
```angelscript
void AddAllLayerNamesTo(TArray<FName>& OutLayerNames)
```
Gets all known layers and appends their names to the provide array

@param OutLayers[OUT] Output array to store all known layers

### AddAllLayersTo
```angelscript
void AddAllLayersTo(TArray<ULayer>& OutLayers)
```
Gets all known layers and appends them to the provided array

@param OutLayers[OUT] Output array to store all known layers

### AddLevelLayerInformation
```angelscript
void AddLevelLayerInformation(ULevel Level)
```
Aggregates any information regarding layers associated with the level and it contents

@param  Level   The process

### AddSelectedActorsToLayer
```angelscript
bool AddSelectedActorsToLayer(FName LayerName)
```
Adds selected actors to the named layer.

@param       LayerName       A layer name.
@return                              true if at least one actor was added.  false is returned if all selected actors already belong to the named layer.

### AddSelectedActorsToLayers
```angelscript
bool AddSelectedActorsToLayers(TArray<FName> LayerNames)
```
Adds selected actors to the named layers.

@param       LayerNames      A valid list of layer names.
@return                              true if at least one actor was added.  false is returned if all selected actors already belong to the named layers.

### AppendActorsFromLayer
```angelscript
void AppendActorsFromLayer(FName LayerName, TArray<AActor>& InOutActors)
```
Appends all the actors associated with the specified layer.

@param  LayerName                       The layer to find actors for.
@param  InOutActors                     The list to append the found actors to.

### AppendActorsFromLayers
```angelscript
void AppendActorsFromLayers(TArray<FName> LayerNames, TArray<AActor>& InOutActors)
```
Appends all the actors associated with ANY of the specified layers.

@param  LayerNames                      The layers to find actors for.
@param  InOutActors                     The list to append the found actors to.

### CreateLayer
```angelscript
ULayer CreateLayer(FName LayerName)
```
Creates a ULayer Object for the named layer

@param       LayerName       The name of the layer to create
@return                              The newly created ULayer Object for the named layer

### DeleteLayer
```angelscript
void DeleteLayer(FName LayerToDelete)
```
Deletes the provided layer, disassociating all actors from them

@param LayerToDelete         A valid layer name

### DeleteLayers
```angelscript
void DeleteLayers(TArray<FName> LayersToDelete)
```
Deletes all of the provided layers, disassociating all actors from them

@param LayersToDelete        A valid list of layer names.

### DisassociateActorFromLayers
```angelscript
bool DisassociateActorFromLayers(AActor Actor)
```
Disassociates an Actor's layers from the layer system, general used before deleting the Actor

@param  Actor   The actor to disassociate from the layer system

### DisassociateActorsFromLayers
```angelscript
bool DisassociateActorsFromLayers(TArray<AActor> Actors)
```
Disassociates actors from the layer system, generally used before deleting the Actors

@param  Actors  The actors to disassociate from the layer system

### EditorMapChange
```angelscript
void EditorMapChange()
```
Delegate handler for FEditorDelegates::MapChange. It internally calls LayersChanged.Broadcast.

### EditorRefreshLayerBrowser
```angelscript
void EditorRefreshLayerBrowser()
```
Delegate handler for FEditorDelegates::RefreshLayerBrowser. It internally calls UpdateAllActorsVisibility to refresh the actors of each layer.

### GetActorsFromLayer
```angelscript
TArray<AActor> GetActorsFromLayer(FName LayerName)
```
Gets all the actors associated with the specified layer. Analog to AppendActorsFromLayer but it returns rather than appends the actors.

@param  LayerName                       The layer to find actors for.
@return                                         The list to assign the found actors to.

### GetActorsFromLayers
```angelscript
TArray<AActor> GetActorsFromLayers(TArray<FName> LayerNames)
```
Gets all the actors associated with ANY of the specified layers. Analog to AppendActorsFromLayers but it returns rather than appends the actors.

@param  LayerNames                      The layers to find actors for.
@return                                         The list to assign the found actors to.

### GetLayer
```angelscript
ULayer GetLayer(FName LayerName)
```
Gets the ULayer Object of the named layer

@param       LayerName       The name of the layer whose ULayer Object is returned
@return                              The ULayer Object of the provided layer name

### GetSelectedActors
```angelscript
TArray<AActor> GetSelectedActors()
```
Find and return the selected actors.

@return                              The selected AActor's as a TArray.

### GetWorld
```angelscript
UWorld GetWorld()
```
Get the current UWorld object.

@return                                              The UWorld* object

### InitializeNewActorLayers
```angelscript
bool InitializeNewActorLayers(AActor Actor)
```
Synchronizes an newly created Actor's layers with the layer system

@param  Actor   The actor to initialize

### IsActorValidForLayer
```angelscript
bool IsActorValidForLayer(AActor Actor)
```
Checks to see if the specified actor is in an appropriate state to interact with layers

@param  Actor   The actor to validate

### IsLayer
```angelscript
bool IsLayer(FName LayerName)
```
Checks whether the ULayer Object of the provided layer name exists.

@param       LayerName               The name of the layer whose ULayer Object to retrieve
@return                                      If true a valid ULayer Object was found; if false, a valid ULayer object was not found

### MakeAllLayersVisible
```angelscript
void MakeAllLayersVisible()
```
Set the visibility of all layers to true

### RemoveActorFromLayer
```angelscript
bool RemoveActorFromLayer(AActor Actor, FName LayerToRemove, bool bUpdateStats)
```
Removes an actor from the specified layer.

@param       Actor                   The actor to remove from the provided layer
@param       LayerToRemove   The name of the layer to remove the actor from
@return                                      true if the actor was removed from the layer.  false is returned if the actor already belonged to the layer.

### RemoveActorFromLayers
```angelscript
bool RemoveActorFromLayers(AActor Actor, TArray<FName> LayerNames, bool bUpdateStats)
```
Removes the provided actor from the named layers.

@param       Actor           The actor to remove from the provided layers
@param       LayerNames      A valid list of layer names.
@return                              true if the actor was removed from at least one of the provided layers.

### RemoveActorsFromLayer
```angelscript
bool RemoveActorsFromLayer(TArray<AActor> Actors, FName LayerName, bool bUpdateStats)
```
Removes the actors from the specified layer.

@param       Actors                  The actors to remove from the provided layer
@param       LayerToRemove   The name of the layer to remove the actors from
@return                                      true if at least one actor was removed from the layer.  false is returned if all the actors already belonged to the layer.

### RemoveActorsFromLayers
```angelscript
bool RemoveActorsFromLayers(TArray<AActor> Actors, TArray<FName> LayerNames, bool bUpdateStats)
```
Remove the actors to the named layers

@param       Actors          The actors to remove to the named layers
@param       LayerNames      A valid list of layer names.
@return                              true if at least one actor was removed from at least one layer.  false is returned if none of the actors belonged to any of the specified layers.

### RemoveLevelLayerInformation
```angelscript
void RemoveLevelLayerInformation(ULevel Level)
```
Purges any information regarding layers associated with the level and it contents

@param  Level   The process

### RemoveSelectedActorsFromLayer
```angelscript
bool RemoveSelectedActorsFromLayer(FName LayerName)
```
Removes the selected actors from the named layer.

@param       LayerName       A layer name.
@return                              true if at least one actor was added.  false is returned if all selected actors already belong to the named layer.

### RemoveSelectedActorsFromLayers
```angelscript
bool RemoveSelectedActorsFromLayers(TArray<FName> LayerNames)
```
Removes selected actors from the named layers.

@param       LayerNames      A valid list of layer names.
@return                              true if at least one actor was removed.

### RenameLayer
```angelscript
bool RenameLayer(FName OriginalLayerName, FName NewLayerName)
```
Renames the provided originally named layer to the provided new name

@param       OriginalLayerName       The name of the layer to be renamed
@param       NewLayerName            The new name for the layer to be renamed

### SelectActorsInLayer
```angelscript
bool SelectActorsInLayer(FName LayerName, bool bSelect, bool bNotify, bool bSelectEvenIfHidden)
```
Selects/de-selects actors belonging to the named layer.

@param       LayerName                                               A valid layer name.
@param       bSelect                                                 If true actors are selected; if false, actors are deselected.
@param       bNotify                                                 If true the Editor is notified of the selection change; if false, the Editor will not be notified.
@param       bSelectEvenIfHidden     [optional]      If true even hidden actors will be selected; if false, hidden actors won't be selected.
@return                                                                      true if at least one actor was selected/deselected.

### SelectActorsInLayers
```angelscript
bool SelectActorsInLayers(TArray<FName> LayerNames, bool bSelect, bool bNotify, bool bSelectEvenIfHidden)
```
Selects/de-selects actors belonging to the named layers.

@param       LayerNames                                              A valid list of layer names.
@param       bSelect                                                 If true actors are selected; if false, actors are deselected.
@param       bNotify                                                 If true the Editor is notified of the selection change; if false, the Editor will not be notified
@param       bSelectEvenIfHidden     [optional]      If true even hidden actors will be selected; if false, hidden actors won't be selected.
@return                                                                      true if at least one actor was selected/deselected.

### SetLayersVisibility
```angelscript
void SetLayersVisibility(TArray<FName> LayerNames, bool bIsVisible)
```
Changes visibility of the named layers to the provided state

@param       LayerNames      The names of the layers to affect
@param       bIsVisible      If true the layers will be visible; if false, the layers will not be visible

### SetLayerVisibility
```angelscript
void SetLayerVisibility(FName LayerName, bool bIsVisible)
```
Changes the named layer's visibility to the provided state

@param       LayerName       The name of the layer to affect.
@param       bIsVisible      If true the layer will be visible; if false, the layer will not be visible.

### ToggleLayersVisibility
```angelscript
void ToggleLayersVisibility(TArray<FName> LayerNames)
```
Toggles the visibility of all of the named layers

@param       LayerNames      The names of the layers to affect

### ToggleLayerVisibility
```angelscript
void ToggleLayerVisibility(FName LayerName)
```
Toggles the named layer's visibility

@param LayerName     The name of the layer to affect

### TryGetLayer
```angelscript
bool TryGetLayer(FName LayerName, ULayer& OutLayer)
```
Attempts to get the ULayer Object of the provided layer name.

@param       LayerName               The name of the layer whose ULayer Object to retrieve
@param       OutLayer[OUT]   Set to the ULayer Object of the named layer. Set to Invalid if no ULayer Object exists.
@return                                      If true a valid ULayer Object was found and set to OutLayer; if false, a valid ULayer object was not found and invalid set to OutLayer

### UpdateActorAllViewsVisibility
```angelscript
void UpdateActorAllViewsVisibility(AActor Actor)
```
Updates per-view visibility for the given actor for all views

@param Actor         Actor to update

### UpdateActorVisibility
```angelscript
bool UpdateActorVisibility(AActor Actor, bool& bOutSelectionChanged, bool& bOutActorModified, bool bNotifySelectionChange, bool bRedrawViewports)
```
Updates the provided actors visibility in the viewports

@param       Actor                                           Actor to update
@param       bOutSelectionChanged [OUT]      Whether the Editors selection changed
@param       bOutActorModified [OUT]         Whether the actor was modified
@param       bNotifySelectionChange          If true the Editor is notified of the selection change; if false, the Editor will not be notified
@param       bRedrawViewports                        If true the viewports will be redrawn; if false, they will not

### UpdateAllActorsVisibility
```angelscript
bool UpdateAllActorsVisibility(bool bNotifySelectionChange, bool bRedrawViewports)
```
Updates the visibility of all actors in the viewports

@param       bNotifySelectionChange          If true the Editor is notified of the selection change; if false, the Editor will not be notified
@param       bRedrawViewports                        If true the viewports will be redrawn; if false, they will not

### UpdateAllViewVisibility
```angelscript
void UpdateAllViewVisibility(FName LayerThatChanged)
```
Updates the visibility for all actors for all views.

@param LayerThatChanged  If one layer was changed (toggled in view pop-up, etc), then we only need to modify actors that use that layer.

