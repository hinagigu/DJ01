# UAIPerceptionStimuliSourceComponent

**继承自**: `UActorComponent`

Gives owning actor a way to auto-register as perception system's sense stimuli source

## 属性

### RegisterAsSourceForSenses
- **类型**: `TArray<TSubclassOf<UAISense>>`

### bAutoRegisterAsSource
- **类型**: `bool`

## 方法

### RegisterForSense
```angelscript
void RegisterForSense(TSubclassOf<UAISense> SenseClass)
```
Registers owning actor as source for specified sense class

### RegisterWithPerceptionSystem
```angelscript
void RegisterWithPerceptionSystem()
```
Registers owning actor as source of stimuli for senses specified in RegisterAsSourceForSenses.
    Note that you don't have to do it if bAutoRegisterAsSource == true

### UnregisterFromPerceptionSystem
```angelscript
void UnregisterFromPerceptionSystem()
```
Unregister owning actor from being a source of sense stimuli

### UnregisterFromSense
```angelscript
void UnregisterFromSense(TSubclassOf<UAISense> SenseClass)
```
Unregisters owning actor from sources list of a specified sense class

