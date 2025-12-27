# UDJ01GameplayAbility

**继承自**: `UGameplayAbility`

UDJ01GameplayAbility

    The base gameplay ability class used by this project.

## 属性

### ActivationPolicy
- **类型**: `EDJ01AbilityActivationPolicy`

### ActivationGroup
- **类型**: `EDJ01AbilityActivationGroup`

### AdditionalCosts
- **类型**: `TArray<TObjectPtr<UDJ01AbilityCost>>`
- **描述**: Additional costs that must be paid to activate this ability

### FailureTagToUserFacingMessages
- **类型**: `TMap<FGameplayTag,FText>`
- **描述**: Map of failure tags to simple error messages

### FailureTagToAnimMontage
- **类型**: `TMap<FGameplayTag,TObjectPtr<UAnimMontage>>`
- **描述**: Map of failure tags to anim montages that should be played with them

### bLogCancelation
- **类型**: `bool`
- **描述**: If true, extra information should be logged when this ability is canceled. This is temporary, used for tracking a bug.

## 方法

### CanChangeActivationGroup
```angelscript
bool CanChangeActivationGroup(EDJ01AbilityActivationGroup NewGroup)
```
Returns true if the requested activation group is a valid transition.

### ChangeActivationGroup
```angelscript
bool ChangeActivationGroup(EDJ01AbilityActivationGroup NewGroup)
```
Tries to change the activation group.  Returns true if it successfully changed.

### ClearCameraMode
```angelscript
void ClearCameraMode()
```
Clears the ability's camera mode.  Automatically called if needed when the ability ends.

### GetControllerFromActorInfo
```angelscript
AController GetControllerFromActorInfo()
```

### GetDJ01AbilitySystemComponentFromActorInfo
```angelscript
UDJ01AbilitySystemComponent GetDJ01AbilitySystemComponentFromActorInfo()
```

### GetDJ01CharacterFromActorInfo
```angelscript
ADJ01Character GetDJ01CharacterFromActorInfo()
```

### GetDJ01PlayerControllerFromActorInfo
```angelscript
ADJ01PlayerController GetDJ01PlayerControllerFromActorInfo()
```

### GetHeroComponentFromActorInfo
```angelscript
UDJ01HeroComponent GetHeroComponentFromActorInfo()
```

### OnAbilityAdded
```angelscript
void OnAbilityAdded()
```
Called when this ability is granted to the ability system component.

### OnAbilityRemoved
```angelscript
void OnAbilityRemoved()
```
Called when this ability is removed from the ability system component.

### OnPawnAvatarSet
```angelscript
void OnPawnAvatarSet()
```
Called when the ability system is initialized with a pawn avatar.

### ScriptOnAbilityFailedToActivate
```angelscript
void ScriptOnAbilityFailedToActivate(FGameplayTagContainer FailedReason)
```
Called when the ability fails to activate

### SetCameraMode
```angelscript
void SetCameraMode(TSubclassOf<UDJ01CameraMode> CameraMode)
```
Sets the ability's camera mode.

