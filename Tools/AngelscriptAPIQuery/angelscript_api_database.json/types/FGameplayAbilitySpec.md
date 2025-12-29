# FGameplayAbilitySpec

An activatable ability spec, hosted on the ability system component. This defines both what the ability is (what class, what level, input binding etc)
and also holds runtime state that must be kept outside of the ability being instanced/activated.

## 属性

### Handle
- **类型**: `FGameplayAbilitySpecHandle`

### Ability
- **类型**: `UGameplayAbility`

### Level
- **类型**: `int`

### InputID
- **类型**: `int`

### SourceObject
- **类型**: `TWeakObjectPtr<UObject>`

### ActiveCount
- **类型**: `uint8`

### ActivationInfo
- **类型**: `FGameplayAbilityActivationInfo`

### DynamicAbilityTags
- **类型**: `FGameplayTagContainer`

### NonReplicatedInstances
- **类型**: `TArray<TObjectPtr<UGameplayAbility>>`

### ReplicatedInstances
- **类型**: `TArray<TObjectPtr<UGameplayAbility>>`

### GameplayEffectHandle
- **类型**: `FActiveGameplayEffectHandle`

### SetByCallerTagMagnitudes
- **类型**: `TMap<FGameplayTag,float32>`

## 方法

### GetbInputPressed
```angelscript
bool GetbInputPressed()
```

### SetbInputPressed
```angelscript
void SetbInputPressed(bool bValue)
```

### GetbRemoveAfterActivation
```angelscript
bool GetbRemoveAfterActivation()
```

### SetbRemoveAfterActivation
```angelscript
void SetbRemoveAfterActivation(bool bValue)
```

### GetbPendingRemove
```angelscript
bool GetbPendingRemove()
```

### SetbPendingRemove
```angelscript
void SetbPendingRemove(bool bValue)
```

### GetbActivateOnce
```angelscript
bool GetbActivateOnce()
```

### SetbActivateOnce
```angelscript
void SetbActivateOnce(bool bValue)
```

### GetPrimaryInstance
```angelscript
UGameplayAbility GetPrimaryInstance()
```

### ShouldReplicateAbilitySpec
```angelscript
bool ShouldReplicateAbilitySpec()
```

### GetAbilityInstances
```angelscript
TArray<UGameplayAbility> GetAbilityInstances()
```

### IsActive
```angelscript
bool IsActive()
```

### PreReplicatedRemoved
```angelscript
void PreReplicatedRemoved(FGameplayAbilitySpecContainer InArraySerializer)
```

### PostReplicatedAdd
```angelscript
void PostReplicatedAdd(FGameplayAbilitySpecContainer InArraySerializer)
```

### GetDebugString
```angelscript
FString GetDebugString()
```

### opAssign
```angelscript
FGameplayAbilitySpec& opAssign(FGameplayAbilitySpec Other)
```

