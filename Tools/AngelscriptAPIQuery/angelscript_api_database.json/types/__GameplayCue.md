# __GameplayCue

## 方法

### AddGameplayCueOnActor
```angelscript
void AddGameplayCueOnActor(AActor Target, FGameplayTag GameplayCueTag, FGameplayCueParameters Parameters)
```
Invoke the added event for a gameplay cue on the target actor. This should be paired with a RemoveGameplayCueOnActor call.
* If the actor has an ability system, the event will fire on authority only and will be replicated.
* If the actor does not have an ability system, the event will only be fired locally.

### ExecuteGameplayCueOnActor
```angelscript
void ExecuteGameplayCueOnActor(AActor Target, FGameplayTag GameplayCueTag, FGameplayCueParameters Parameters)
```
Invoke a one time "instant" execute event for a gameplay cue on the target actor.
* If the actor has an ability system, the event will fire on authority only and will be replicated.
* If the actor does not have an ability system, the event will only be fired locally.

### MakeGameplayCueParametersFromHitResult
```angelscript
FGameplayCueParameters MakeGameplayCueParametersFromHitResult(FHitResult HitResult)
```
Builds gameplay cue parameters using data from a hit result.

### RemoveGameplayCueOnActor
```angelscript
void RemoveGameplayCueOnActor(AActor Target, FGameplayTag GameplayCueTag, FGameplayCueParameters Parameters)
```
Invoke the removed event for a gameplay cue on the target actor. This should be paired with an AddGameplayCueOnActor call.
* If the actor has an ability system, the event will fire on authority only and will be replicated.
* If the actor does not have an ability system, the event will only be fired locally.

