# UChaosDestructionListener

**继承自**: `USceneComponent`

Object allowing for retrieving Chaos Destruction data.

## 属性

### ChaosSolverActors
- **类型**: `TSet<TObjectPtr<AChaosSolverActor>>`

### GeometryCollectionActors
- **类型**: `TSet<TObjectPtr<AGeometryCollectionActor>>`

### OnCollisionEvents
- **类型**: `FOnChaosCollisionEvents`

### OnBreakingEvents
- **类型**: `FOnChaosBreakingEvents`

### OnTrailingEvents
- **类型**: `FOnChaosTrailingEvents`

### OnRemovalEvents
- **类型**: `FOnChaosRemovalEvents`

### bIsCollisionEventListeningEnabled
- **类型**: `bool`

### bIsBreakingEventListeningEnabled
- **类型**: `bool`

### bIsTrailingEventListeningEnabled
- **类型**: `bool`

### bIsRemovalEventListeningEnabled
- **类型**: `bool`

### CollisionEventRequestSettings
- **类型**: `FChaosCollisionEventRequestSettings`

### BreakingEventRequestSettings
- **类型**: `FChaosBreakingEventRequestSettings`

### TrailingEventRequestSettings
- **类型**: `FChaosTrailingEventRequestSettings`

### RemovalEventRequestSettings
- **类型**: `FChaosRemovalEventRequestSettings`

## 方法

### AddChaosSolverActor
```angelscript
void AddChaosSolverActor(AChaosSolverActor ChaosSolverActor)
```
Dynamically adds a chaos solver to the listener

### AddGeometryCollectionActor
```angelscript
void AddGeometryCollectionActor(AGeometryCollectionActor GeometryCollectionActor)
```
Dynamically adds a chaos solver to the listener

### IsEventListening
```angelscript
bool IsEventListening()
```
Returns if the destruction listener is listening to any events

### RemoveChaosSolverActor
```angelscript
void RemoveChaosSolverActor(AChaosSolverActor ChaosSolverActor)
```
Dynamically removes a chaos solver from the listener

### RemoveGeometryCollectionActor
```angelscript
void RemoveGeometryCollectionActor(AGeometryCollectionActor GeometryCollectionActor)
```
Dynamically removes a chaos solver from the listener

### SetBreakingEventEnabled
```angelscript
void SetBreakingEventEnabled(bool bIsEnabled)
```
Enables or disables breaking event listening

### SetBreakingEventRequestSettings
```angelscript
void SetBreakingEventRequestSettings(FChaosBreakingEventRequestSettings InSettings)
```
Sets breaking event request settings dynamically

### SetCollisionEventEnabled
```angelscript
void SetCollisionEventEnabled(bool bIsEnabled)
```
Enables or disables collision event listening

### SetCollisionEventRequestSettings
```angelscript
void SetCollisionEventRequestSettings(FChaosCollisionEventRequestSettings InSettings)
```
Sets collision event request settings dynamically

### SetRemovalEventEnabled
```angelscript
void SetRemovalEventEnabled(bool bIsEnabled)
```
Enables or disables removal event listening

### SetRemovalEventRequestSettings
```angelscript
void SetRemovalEventRequestSettings(FChaosRemovalEventRequestSettings InSettings)
```
Sets removal event request settings dynamically

### SetTrailingEventEnabled
```angelscript
void SetTrailingEventEnabled(bool bIsEnabled)
```
Enables or disables trailing event listening

### SetTrailingEventRequestSettings
```angelscript
void SetTrailingEventRequestSettings(FChaosTrailingEventRequestSettings InSettings)
```
Sets trailing event request settings dynamically

### SortBreakingEvents
```angelscript
void SortBreakingEvents(TArray<FChaosBreakingEventData>& BreakingEvents, EChaosBreakingSortMethod SortMethod)
```
Sorts breaking events according to the given sort method

### SortCollisionEvents
```angelscript
void SortCollisionEvents(TArray<FChaosCollisionEventData>& CollisionEvents, EChaosCollisionSortMethod SortMethod)
```
Sorts collision events according to the given sort method

### SortRemovalEvents
```angelscript
void SortRemovalEvents(TArray<FChaosRemovalEventData>& RemovalEvents, EChaosRemovalSortMethod SortMethod)
```
Sorts removal events according to the given sort method

### SortTrailingEvents
```angelscript
void SortTrailingEvents(TArray<FChaosTrailingEventData>& TrailingEvents, EChaosTrailingSortMethod SortMethod)
```
Sorts trailing events according to the given sort method

