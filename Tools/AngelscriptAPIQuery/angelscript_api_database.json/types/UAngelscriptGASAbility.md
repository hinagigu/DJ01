# UAngelscriptGASAbility

**继承自**: `UGameplayAbility`

## 方法

### AddGameplayCue_Actor
```angelscript
void AddGameplayCue_Actor(TSubclassOf<AGameplayCueNotify_Actor> GameplayCue, FGameplayEffectContextHandle Context, bool bRemoveOnAbilityEnd)
```
Adds a persistent gameplay cue to the ability owner. Optionally will remove if ability ends

### AddGameplayCue_Static
```angelscript
void AddGameplayCue_Static(TSubclassOf<UGameplayCueNotify_Static> GameplayCue, FGameplayEffectContextHandle Context, bool bRemoveOnAbilityEnd)
```
Adds a persistent gameplay cue to the ability owner. Optionally will remove if ability ends

### AddGameplayCueWithParams_Actor
```angelscript
void AddGameplayCueWithParams_Actor(TSubclassOf<AGameplayCueNotify_Actor> GameplayCue, FGameplayCueParameters GameplayCueParameter, bool bRemoveOnAbilityEnd)
```
Adds a persistent gameplay cue to the ability owner. Optionally will remove if ability ends

### AddGameplayCueWithParams_Static
```angelscript
void AddGameplayCueWithParams_Static(TSubclassOf<UGameplayCueNotify_Static> GameplayCue, FGameplayCueParameters GameplayCueParameter, bool bRemoveOnAbilityEnd)
```
Adds a persistent gameplay cue to the ability owner. Optionally will remove if ability ends

### ExecuteGameplayCue_Actor
```angelscript
void ExecuteGameplayCue_Actor(TSubclassOf<AGameplayCueNotify_Actor> GameplayCue, FGameplayEffectContextHandle Context)
```
Invoke a gameplay cue on the ability owner

### ExecuteGameplayCue_Static
```angelscript
void ExecuteGameplayCue_Static(TSubclassOf<UGameplayCueNotify_Static> GameplayCue, FGameplayEffectContextHandle Context)
```
Invoke a gameplay cue on the ability owner

### ExecuteGameplayCueWithParams_Actor
```angelscript
void ExecuteGameplayCueWithParams_Actor(TSubclassOf<AGameplayCueNotify_Actor> GameplayCue, FGameplayCueParameters GameplayCueParameters)
```
Invoke a gameplay cue on the ability owner, with extra parameters

### ExecuteGameplayCueWithParams_Static
```angelscript
void ExecuteGameplayCueWithParams_Static(TSubclassOf<UGameplayCueNotify_Static> GameplayCue, FGameplayCueParameters GameplayCueParameters)
```
Invoke a gameplay cue on the ability owner, with extra parameters

### RemoveGameplayCue_Actor
```angelscript
void RemoveGameplayCue_Actor(TSubclassOf<AGameplayCueNotify_Actor> GameplayCue)
```
Removes a persistent gameplay cue from the ability owner

### RemoveGameplayCue_Static
```angelscript
void RemoveGameplayCue_Static(TSubclassOf<UGameplayCueNotify_Static> GameplayCue)
```
Removes a persistent gameplay cue from the ability owner

