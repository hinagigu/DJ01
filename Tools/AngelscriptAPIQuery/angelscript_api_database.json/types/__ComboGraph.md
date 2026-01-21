# __ComboGraph

## 方法

### GetComboGraphGameplayTasksComponent
```angelscript
UComboGraphGameplayTasksComponent GetComboGraphGameplayTasksComponent(const AActor Actor)
```
Searches the passed in actor for a Combo Graph gameplay tasks component, will use component search

### GetCueParamsObjectsFromContext
```angelscript
TArray<UObject> GetCueParamsObjectsFromContext(FGameplayEffectContextHandle EffectContext)
```
Extracts Cue Params resolved Objects (set in a combo graph node) from Gameplay Effect Context

### GetCueParamsObjectsPathsFromContext
```angelscript
TArray<FSoftObjectPath> GetCueParamsObjectsPathsFromContext(FGameplayEffectContextHandle EffectContext)
```
Extracts Cue Params Soft Object Paths (set in a combo graph node) from Gameplay Effect Context

### HasCueParamsObjectsFromContext
```angelscript
bool HasCueParamsObjectsFromContext(FGameplayEffectContextHandle EffectContext)
```
Checks if Gameplay Effect Context has any Cue Params resolved Objects (set in a combo graph node)

### HasCueParamsObjectsPathsFromContext
```angelscript
bool HasCueParamsObjectsPathsFromContext(FGameplayEffectContextHandle EffectContext)
```
Checks if Gameplay Effect Context has any Cue Params Soft Object Paths (set in a combo graph node)

### SendGameplayEventToActor
```angelscript
void SendGameplayEventToActor(AActor Actor, FGameplayTag EventTag, FGameplayEventData Payload)
```
This function is functionally the same as SendGameplayEventToActor (from Ability System Blueprint Library),
except it can be used on actors that do not implement IAbilitySystemInterface. In ue5, this custom version
won't be necessary anymore.

This function can be used to trigger an ability on the actor in question with useful payload data.
NOTE: GetAbilitySystemComponent is called on the actor to find a good component, and if the component isn't
found, the event will not be sent.

### SimulateComboInput
```angelscript
void SimulateComboInput(AActor Actor, UInputAction InputAction)
```
Simulate user input for the passed in actor running a combo graph.

This will send a gameplay event with relevant gameplay event data.

