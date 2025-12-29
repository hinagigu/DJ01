# __AngelscriptAbilityAsync

## 方法

### WaitForAttributeChanged
```angelscript
UAbilityAsync_WaitAttributeChanged WaitForAttributeChanged(AActor TargetActor, FGameplayAttribute Attribute, bool bTriggerOnce)
```

### WaitGameplayEventToActor
```angelscript
UAbilityAsync_WaitGameplayEvent WaitGameplayEventToActor(AActor TargetActor, FGameplayTag Tag, bool bTriggerOnce, bool bMatchExact)
```

### WaitGameplayTagAddToActor
```angelscript
UAbilityAsync_WaitGameplayTagAdded WaitGameplayTagAddToActor(AActor TargetActor, FGameplayTag Tag, bool bTriggerOnce)
```

### WaitGameplayTagQueryOnActor
```angelscript
UAbilityAsync_WaitGameplayTagQuery WaitGameplayTagQueryOnActor(AActor TargetActor, FGameplayTagQuery Query, EWaitGameplayTagQueryTriggerCondition TriggerCondition, bool bTriggerOnce)
```

### WaitGameplayTagRemoveFromActor
```angelscript
UAbilityAsync_WaitGameplayTagRemoved WaitGameplayTagRemoveFromActor(AActor TargetActor, FGameplayTag Tag, bool bTriggerOnce)
```

