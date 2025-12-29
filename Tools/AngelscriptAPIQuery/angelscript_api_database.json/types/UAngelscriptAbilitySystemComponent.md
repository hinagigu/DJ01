# UAngelscriptAbilitySystemComponent

**继承自**: `UAbilitySystemComponent`

## 属性

### OnInitAbilityActorInfo
- **类型**: `FInitAbilityActorInfoDelegate`

### OnAbilityGiven
- **类型**: `FAbilityGivenDelegate`

### OnAbilityRemoved
- **类型**: `FAbilityRemovedDelegate`

### OnAttributeChanged
- **类型**: `FAttributeChangedDelegate`

### OnOwnedTagUpdated
- **类型**: `FOwnedTagUpdatedDelegate`

## 方法

### ActivateAbilitiesUsingTags
```angelscript
bool ActivateAbilitiesUsingTags(FGameplayTagContainer GameplayTagContainer, bool bAllowRemoteActivation)
```

### BindInput
```angelscript
void BindInput(UInputComponent InputComponent, FAngelscriptInputBindData BindData)
```

### GiveAbility
```angelscript
FGameplayAbilitySpecHandle GiveAbility(TSubclassOf<UGameplayAbility> InAbilityClass, int Level, int OptionalInputID, UObject OptionalSourceObject)
```
Ability functions

### GiveAbilityAndActivateOnce
```angelscript
FGameplayAbilitySpecHandle GiveAbilityAndActivateOnce(TSubclassOf<UGameplayAbility> InAbilityClass, int Level, int OptionalInputID, UObject OptionalSourceObject)
```

### InitAbilityActorInfo
```angelscript
void InitAbilityActorInfo(AActor InOwnerActor, AActor InAvatarActor)
```

### SetRemoveAbilityOnEnd
```angelscript
void SetRemoveAbilityOnEnd(FGameplayAbilitySpecHandle AbilitySpecHandle)
```

### CanActivateAbilityByClass
```angelscript
bool CanActivateAbilityByClass(TSubclassOf<UGameplayAbility> InAbilityToActivate)
```
Check if ability of class can be activated

### CanActivateAbilitySpec
```angelscript
bool CanActivateAbilitySpec(FGameplayAbilitySpecHandle AbilitySpecHandle)
```
Check if ability can be activated

### CancelAbilitiesByTags
```angelscript
void CancelAbilitiesByTags(FGameplayTagContainer WithTags, FGameplayTagContainer WithoutTags, UGameplayAbility Ignore)
```

### CancelAbility
```angelscript
void CancelAbility(TSubclassOf<UGameplayAbility> InAbilityClass)
```

### CancelAbilityByHandle
```angelscript
void CancelAbilityByHandle(FGameplayAbilitySpecHandle AbilityHandle)
```

### GetAbilityActorInfo
```angelscript
FGameplayAbilityActorInfo& GetAbilityActorInfo()
```

### GetAbilitySpecSourceObject
```angelscript
UObject GetAbilitySpecSourceObject(FGameplayAbilitySpecHandle AbilitySpecHandle)
```

### GetActiveAbilitiesWithTags
```angelscript
void GetActiveAbilitiesWithTags(FGameplayTagContainer GameplayTagContainer, TArray<UGameplayAbility>& ActiveAbilities)
```

### GetAndRegisterAttributeChangedCallback
```angelscript
void GetAndRegisterAttributeChangedCallback(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass, FName AttributeName, UObject CallbackObject, FName CallbackFunctionName_FAngelscriptAttributeChangedData, float32& OutCurrentValue)
```

### GetAndRegisterCallbackForAttribute
```angelscript
void GetAndRegisterCallbackForAttribute(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass, FName AttributeName, float32& OutCurrentValue)
```

### GetAttributeBaseValue
```angelscript
float32 GetAttributeBaseValue(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass, FName AttributeName, float32 DefaultValue)
```
If attribute doesn't exist will return DefaultValue(which is by default 0.f)

### GetAttributeBaseValueChecked
```angelscript
float32 GetAttributeBaseValueChecked(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass, FName AttributeName)
```

### GetAttributeCurrentValue
```angelscript
float32 GetAttributeCurrentValue(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass, FName AttributeName, float32 DefaultValue)
```
If attribute doesn't exist will return DefaultValue(which is by default 0.f)

### GetAttributeCurrentValueChecked
```angelscript
float32 GetAttributeCurrentValueChecked(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass, FName AttributeName)
```

### GetAvatar
```angelscript
AActor GetAvatar()
```

### GetCooldownTimeRemaining
```angelscript
float32 GetCooldownTimeRemaining(TSubclassOf<UGameplayAbility> InAbilityClass)
```

### GetPlayerController
```angelscript
APlayerController GetPlayerController()
```

### HasAbility
```angelscript
bool HasAbility(TSubclassOf<UGameplayAbility> InAbilityClass)
```

### HasAllGameplayTags
```angelscript
bool HasAllGameplayTags(FGameplayTagContainer TagContainer)
```
HasAllMatchingGameplayTags, but cannot have the same name so adding "Owned"

### HasAnyGameplayTags
```angelscript
bool HasAnyGameplayTags(FGameplayTagContainer TagContainer)
```
HasAnyMatchingGameplayTags, but cannot have the same name so adding "Owned"

### HasGameplayTag
```angelscript
bool HasGameplayTag(FGameplayTag TagToCheck)
```
Tag functions

### IsAbilityActive
```angelscript
bool IsAbilityActive(TSubclassOf<UGameplayAbility> InAbilityClass)
```

### ModAttributeUnsafe
```angelscript
void ModAttributeUnsafe(FGameplayAttribute GameplayAttribute, EGameplayModOp ModifierOp, float32 ModifierMagnitude)
```
This function will apply an attribute change without invoking all the callbacks! Do not use unless you have to and know what you are doing! It can be useful for clamping attribute values to max values for example. For all other scenarios, use the SetAttribute set of functions!

### OnAttributeSetRegistered
```angelscript
void OnAttributeSetRegistered(UObject InObject, FName InFunctionName)
```
This could be called multiple times if we register attribute sets late. This needs to be a function so we can handle late adds.

### RegisterAttributeChangedCallback
```angelscript
void RegisterAttributeChangedCallback(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass, FName AttributeName, UObject CallbackObject, FName CallbackFunctionName_FAngelscriptAttributeChangedData)
```
Use these to register callbacks to individual attributes. As the CallbackFunctionName_FAngelscriptAttributeChangedData parameter name suggests, the callback function should take a single FAngelscriptAttributeChangedData as its parameter to bind correctly.

### RegisterAttributeSet
```angelscript
UAngelscriptAttributeSet RegisterAttributeSet(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass)
```
Adds the attribute set type to the actor that owns this component. Ensures that attribute sets are never added twice.

### RegisterCallbackForAttribute
```angelscript
void RegisterCallbackForAttribute(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass, FName AttributeName)
```

### SetAbilitySpecSourceObject
```angelscript
void SetAbilitySpecSourceObject(FGameplayAbilitySpecHandle AbilitySpecHandle, UObject NewSourceObject)
```

### SetAttributeBaseValue
```angelscript
void SetAttributeBaseValue(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass, FName AttributeName, float32 NewBaseValue)
```
Requires the attribute to actually exist

### TryActivateAbilitySpec
```angelscript
bool TryActivateAbilitySpec(FGameplayAbilitySpecHandle Handle, bool bAllowRemoteActivation)
```

### TryGetAttributeBaseValue
```angelscript
bool TryGetAttributeBaseValue(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass, FName AttributeName, float32& OutBaseValue)
```

### TryGetAttributeCurrentValue
```angelscript
bool TryGetAttributeCurrentValue(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass, FName AttributeName, float32& OutCurrentValue)
```

### TrySetAttributeBaseValue
```angelscript
bool TrySetAttributeBaseValue(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass, FName AttributeName, float32 NewBaseValue)
```
Use these functions when you are not sure if the attribute exists

