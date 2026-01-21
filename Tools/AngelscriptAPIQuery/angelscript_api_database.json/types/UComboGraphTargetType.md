# UComboGraphTargetType

**继承自**: `UObject`

Class that is used to determine targeting for abilities

It is meant to be blueprinted to run target logic

This does not subclass GameplayAbilityTargetActor because this class is never instanced into the world

This can be used as a basis for a game-specific targeting blueprint. If your targeting is more complicated
you may need to instance into the world once or as a pooled actor

## 方法

### GetTargets
```angelscript
void GetTargets(AActor TargetingActor, FGameplayEventData EventData, TArray<FHitResult>& OutHitResults, TArray<AActor>& OutActors)
```
Called to determine targets to apply gameplay effects to

