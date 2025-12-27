# AGameplayCueNotify_Actor

**继承自**: `AActor`

An instantiated Actor that acts as a handler of a GameplayCue. Since they are instantiated, they can maintain state and tick/update every frame if necessary.

## 属性

### bAutoDestroyOnRemove
- **类型**: `bool`
- **描述**: We will auto destroy (recycle) this GameplayCueActor when the OnRemove event fires (after OnRemove is called).

### AutoDestroyDelay
- **类型**: `float32`
- **描述**: If bAutoDestroyOnRemove is true, the actor will stay alive for this many seconds before being auto destroyed.

### WarnIfTimelineIsStillRunning
- **类型**: `bool`
- **描述**: Warn if we have a timeline running when we cleanup this gameplay cue (we will kill the timeline either way)

### WarnIfLatentActionIsStillRunning
- **类型**: `bool`
- **描述**: Warn if we have a latent action (delay, etc) running when we cleanup this gameplay cue (we will kill the latent action either way)

### GameplayCueTag
- **类型**: `FGameplayTag`
- **描述**: Tag this notify is activated by

### bAutoAttachToOwner
- **类型**: `bool`
- **描述**: If true, attach this GameplayCue Actor to the target actor while it is active. Attaching is slightly more expensive than not attaching, so only enable when you need to.

### IsOverride
- **类型**: `bool`
- **描述**: Does this Cue override other cues, or is it called in addition to them? E.g., If this is Damage.Physical.Slash, we wont call Damage.Physical afer we run this cue.

### bUniqueInstancePerInstigator
- **类型**: `bool`
- **描述**: Does this cue get a new instance for each instigator? For example if two instigators apply a GC to the same source, do we create two of these GameplayCue Notify actors or just one?
If the notify is simply playing FX or sounds on the source, it should not need unique instances. If this Notify is attaching a beam from the instigator to the target, it does need a unique instance per instigator.

### bUniqueInstancePerSourceObject
- **类型**: `bool`
- **描述**: Does this cue get a new instance for each source object? For example if two source objects apply a GC to the same source, do we create two of these GameplayCue Notify actors or just one?
If the notify is simply playing FX or sounds on the source, it should not need unique instances. If this Notify is attaching a beam from the source object to the target, it does need a unique instance per instigator.

### bAllowMultipleOnActiveEvents
- **类型**: `bool`
- **描述**: Does this cue trigger its OnActive event if it's already been triggered?
This can occur when the associated tag is triggered by multiple sources and there is no unique instancing.

### bAllowMultipleWhileActiveEvents
- **类型**: `bool`
- **描述**: Does this cue trigger its WhileActive event if it's already been triggered?
This can occur when the associated tag is triggered by multiple sources and there is no unique instancing.

### NumPreallocatedInstances
- **类型**: `int`
- **描述**: How many instances of the gameplay cue to preallocate

## 方法

### EndGameplayCue
```angelscript
void EndGameplayCue()
```
Ends the gameplay cue: either destroying it or recycling it. You must call this manually only if you do not use bAutoDestroyOnRemove/AutoDestroyDelay

### HandleGameplayCue
```angelscript
void HandleGameplayCue(AActor MyTarget, EGameplayCueEvent EventType, FGameplayCueParameters Parameters)
```
Generic Event Graph event that will get called for every event type

### OnActive
```angelscript
bool OnActive(AActor MyTarget, FGameplayCueParameters Parameters)
```
Called when a GameplayCue with duration is first activated, this will only be called if the client witnessed the activation

### OnExecute
```angelscript
bool OnExecute(AActor MyTarget, FGameplayCueParameters Parameters)
```
Called when a GameplayCue is executed, this is used for instant effects or periodic ticks

### OnRemove
```angelscript
bool OnRemove(AActor MyTarget, FGameplayCueParameters Parameters)
```
Called when a GameplayCue with duration is removed

### WhileActive
```angelscript
bool WhileActive(AActor MyTarget, FGameplayCueParameters Parameters)
```
Called when a GameplayCue with duration is first seen as active, even if it wasn't actually just applied (Join in progress, etc)

