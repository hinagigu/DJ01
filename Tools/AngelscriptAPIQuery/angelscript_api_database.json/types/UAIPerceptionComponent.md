# UAIPerceptionComponent

**继承自**: `UActorComponent`

AIPerceptionComponent is used to register as stimuli listener in AIPerceptionSystem
and gathers registered stimuli. UpdatePerception is called when component gets new stimuli (batched)

## 属性

### SensesConfig
- **类型**: `TArray<TObjectPtr<UAISenseConfig>>`

### DominantSense
- **类型**: `TSubclassOf<UAISense>`
- **描述**: Indicated sense that takes precedence over other senses when determining sensed actor's location.
    Should be set to one of the senses configured in SensesConfig, or None.

### OnPerceptionUpdated
- **类型**: `FPerceptionUpdatedDelegate`

### OnTargetPerceptionForgotten
- **类型**: `FActorPerceptionForgetUpdatedDelegate`

### OnTargetPerceptionUpdated
- **类型**: `FActorPerceptionUpdatedDelegate`

### OnTargetPerceptionInfoUpdated
- **类型**: `FActorPerceptionInfoUpdatedDelegate`

## 方法

### ForgetAll
```angelscript
void ForgetAll()
```
basically cleans up PerceptualData, resulting in loss of all previous perception

### GetActorsPerception
```angelscript
bool GetActorsPerception(AActor Actor, FActorPerceptionBlueprintInfo& Info)
```
Retrieves whatever has been sensed about given actor

### GetCurrentlyPerceivedActors
```angelscript
void GetCurrentlyPerceivedActors(TSubclassOf<UAISense> SenseToUse, TArray<AActor>& OutActors)
```
If SenseToUse is none all actors currently perceived in any way will get fetched

### GetKnownPerceivedActors
```angelscript
void GetKnownPerceivedActors(TSubclassOf<UAISense> SenseToUse, TArray<AActor>& OutActors)
```
If SenseToUse is none all actors ever perceived in any way (and not forgotten yet) will get fetched

### GetPerceivedHostileActors
```angelscript
void GetPerceivedHostileActors(TArray<AActor>& OutActors)
```
blueprint interface

### GetPerceivedHostileActorsBySense
```angelscript
void GetPerceivedHostileActorsBySense(TSubclassOf<UAISense> SenseToUse, TArray<AActor>& OutActors)
```

### IsSenseEnabled
```angelscript
bool IsSenseEnabled(TSubclassOf<UAISense> SenseClass)
```
Returns if a sense is active. Note that this works only if given sense has been
     already configured for this component instance

### RequestStimuliListenerUpdate
```angelscript
void RequestStimuliListenerUpdate()
```
Notifies AIPerceptionSystem to update properties for this "stimuli listener"

### SetSenseEnabled
```angelscript
void SetSenseEnabled(TSubclassOf<UAISense> SenseClass, bool bEnable)
```
Note that this works only if given sense has been already configured for
    this component instance

