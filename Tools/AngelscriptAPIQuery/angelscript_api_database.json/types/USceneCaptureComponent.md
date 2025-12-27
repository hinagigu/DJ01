# USceneCaptureComponent

**继承自**: `USceneComponent`

-> will be exported to EngineDecalClasses.h

## 属性

### PrimitiveRenderMode
- **类型**: `ESceneCapturePrimitiveRenderMode`

### CaptureSource
- **类型**: `ESceneCaptureSource`

### bAlwaysPersistRenderingState
- **类型**: `bool`

### HiddenActors
- **类型**: `TArray<TObjectPtr<AActor>>`

### ShowOnlyActors
- **类型**: `TArray<TObjectPtr<AActor>>`

### LODDistanceFactor
- **类型**: `float32`
- **描述**: Scales the distance used by LOD. Set to values greater than 1 to cause the scene capture to use lower LODs than the main view to speed up the scene capture pass.

### MaxViewDistanceOverride
- **类型**: `float32`

### bUseRayTracingIfEnabled
- **类型**: `bool`

### ShowFlagSettings
- **类型**: `TArray<FEngineShowFlagsSetting>`

### ProfilingEventName
- **类型**: `FString`

### bCaptureEveryFrame
- **类型**: `bool`

### bCaptureOnMovement
- **类型**: `bool`

### CaptureSortPriority
- **类型**: `int`

## 方法

### ClearHiddenComponents
```angelscript
void ClearHiddenComponents()
```
Clears the hidden list.

### ClearShowOnlyComponents
```angelscript
void ClearShowOnlyComponents()
```
Clears the Show Only list.

### HideActorComponents
```angelscript
void HideActorComponents(AActor InActor, bool bIncludeFromChildActors)
```
Adds all primitive components in the actor to our list of hidden components.
@param bIncludeFromChildActors Whether to include the components from child actors

### HideComponent
```angelscript
void HideComponent(UPrimitiveComponent InComponent)
```
Adds the component to our list of hidden components.

### RemoveShowOnlyActorComponents
```angelscript
void RemoveShowOnlyActorComponents(AActor InActor, bool bIncludeFromChildActors)
```
Removes an actor's components from the Show Only list.
@param bIncludeFromChildActors Whether to remove the components from child actors

### RemoveShowOnlyComponent
```angelscript
void RemoveShowOnlyComponent(UPrimitiveComponent InComponent)
```
Removes a component from the Show Only list.

### SetCaptureSortPriority
```angelscript
void SetCaptureSortPriority(int NewCaptureSortPriority)
```
Changes the value of TranslucentSortPriority.

### ShowOnlyActorComponents
```angelscript
void ShowOnlyActorComponents(AActor InActor, bool bIncludeFromChildActors)
```
Adds all primitive components in the actor to our list of show-only components.
@param bIncludeFromChildActors Whether to include the components from child actors

### ShowOnlyComponent
```angelscript
void ShowOnlyComponent(UPrimitiveComponent InComponent)
```
Adds the component to our list of show-only components.

