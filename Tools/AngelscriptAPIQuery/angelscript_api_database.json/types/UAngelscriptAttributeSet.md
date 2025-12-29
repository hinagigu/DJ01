# UAngelscriptAttributeSet

**继承自**: `UAttributeSet`

## 属性

### ReplicatedAttributeBlackList
- **类型**: `TArray<FName>`

## 方法

### GetActorInfo
```angelscript
FGameplayAbilityActorInfo& GetActorInfo()
```

### GetOwningAbilitySystemComponent
```angelscript
UAngelscriptAbilitySystemComponent GetOwningAbilitySystemComponent()
```

### GetOwningActor
```angelscript
AActor GetOwningActor()
```

### OnInitFromMetaDataTable
```angelscript
bool OnInitFromMetaDataTable(const UDataTable DataTable)
```
Return true if you could load the data. False if you want to use the default loading function

### PostAttributeBaseChange
```angelscript
void PostAttributeBaseChange(FGameplayAttribute Attribute, float OldValue, float NewValue)
```

### PostAttributeChange
```angelscript
void PostAttributeChange(FGameplayAttribute Attribute, float OldValue, float NewValue)
```

### PostGameplayEffectExecute
```angelscript
void PostGameplayEffectExecute(FGameplayEffectSpec EffectSpec, FGameplayModifierEvaluatedData& EvaluatedData, UAngelscriptAbilitySystemComponent AbilitySystemComponent)
```

### PreAttributeBaseChange
```angelscript
void PreAttributeBaseChange(FGameplayAttribute Attribute, float32& NewValue)
```

### PreAttributeChange
```angelscript
void PreAttributeChange(FGameplayAttribute Attribute, float32& NewValue)
```

### PreGameplayEffectExecute
```angelscript
bool PreGameplayEffectExecute(FGameplayEffectSpec EffectSpec, FGameplayModifierEvaluatedData& EvaluatedData, UAngelscriptAbilitySystemComponent AbilitySystemComponent)
```
Return true if you want to allow the effect to execute

### InitFromMetaDataTable
```angelscript
void InitFromMetaDataTable(const UDataTable DataTable)
```

### OnRep_Attribute
```angelscript
void OnRep_Attribute(FAngelscriptGameplayAttributeData& OldAttributeData)
```

### TryGetAttributeBaseValue
```angelscript
bool TryGetAttributeBaseValue(FName AttributeName, float32& OutBaseValue)
```

### TryGetAttributeCurrentValue
```angelscript
bool TryGetAttributeCurrentValue(FName AttributeName, float32& OutCurrentValue)
```

### TrySetAttributeBaseValue
```angelscript
bool TrySetAttributeBaseValue(FName AttributeName, float32 NewBaseValue)
```
Use these functions when you are not sure if the attribute you are trying to manipulate will exist on the set.

