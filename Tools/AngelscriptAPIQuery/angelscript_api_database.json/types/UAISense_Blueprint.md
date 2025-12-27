# UAISense_Blueprint

**继承自**: `UAISense`

## 属性

### ListenerDataType
- **类型**: `TSubclassOf<UUserDefinedStruct>`

### ListenerContainer
- **类型**: `TArray<TObjectPtr<UAIPerceptionComponent>>`

## 方法

### GetAllListenerActors
```angelscript
void GetAllListenerActors(TArray<AActor>& ListenerActors)
```

### GetAllListenerComponents
```angelscript
void GetAllListenerComponents(TArray<UAIPerceptionComponent>& ListenerComponents)
```

### OnNewPawn
```angelscript
void OnNewPawn(APawn NewPawn)
```
called when sense's instance gets notified about new pawn that has just been spawned

### OnListenerRegistered
```angelscript
void OnListenerRegistered(AActor ActorListener, UAIPerceptionComponent PerceptionComponent)
```
@param PerceptionComponent is ActorListener's AIPerceptionComponent instance

### OnListenerUnregistered
```angelscript
void OnListenerUnregistered(AActor ActorListener, UAIPerceptionComponent PerceptionComponent)
```
called when a listener unregistered from this sense. Most often this is called due to actor's death
    @param PerceptionComponent is ActorListener's AIPerceptionComponent instance

### OnListenerUpdated
```angelscript
void OnListenerUpdated(AActor ActorListener, UAIPerceptionComponent PerceptionComponent)
```
@param PerceptionComponent is ActorListener's AIPerceptionComponent instance

### OnUpdate
```angelscript
float32 OnUpdate(TArray<UAISenseEvent> EventsToProcess)
```
returns requested amount of time to pass until next frame.
    Return 0 to get update every frame (WARNING: hits performance)

