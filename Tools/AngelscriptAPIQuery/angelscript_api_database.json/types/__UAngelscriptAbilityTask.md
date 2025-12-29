# __UAngelscriptAbilityTask

## 方法

### CreateAbilityTask
```angelscript
UAngelscriptAbilityTask CreateAbilityTask(TSubclassOf<UAngelscriptAbilityTask> TaskType, UGameplayAbility ThisAbility, FName NewInstanceName)
```
If you create a task using this function from AS, you must start it manually using ReadyForActivation. This is useful if you want to set up properties on the task before you run it.

### CreateAbilityTaskAndRunIt
```angelscript
UAngelscriptAbilityTask CreateAbilityTaskAndRunIt(TSubclassOf<UAngelscriptAbilityTask> TaskType, UGameplayAbility ThisAbility, FName NewInstanceName)
```
This method will both create the task and call ReadyForActivation on it for you immediately.

### StaticClass
```angelscript
UClass StaticClass()
```

