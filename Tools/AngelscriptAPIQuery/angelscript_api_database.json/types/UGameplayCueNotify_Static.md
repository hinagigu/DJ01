# UGameplayCueNotify_Static

**继承自**: `UObject`

A non instantiated UObject that acts as a handler for a GameplayCue. These are useful for one-off "burst" effects.

## 属性

### GameplayCueTag
- **类型**: `FGameplayTag`
- **描述**: Tag this notify is activated by

### IsOverride
- **类型**: `bool`
- **描述**: Does this Cue override other cues, or is it called in addition to them? E.g., If this is Damage.Physical.Slash, we wont call Damage.Physical afer we run this cue.

## 方法

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

