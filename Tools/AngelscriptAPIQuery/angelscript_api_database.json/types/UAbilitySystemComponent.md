# UAbilitySystemComponent

**继承自**: `UGameplayTasksComponent`

The core ActorComponent for interfacing with the GameplayAbilities System

## 属性

### DefaultStartingData
- **类型**: `TArray<FAttributeDefaults>`

### AffectedAnimInstanceTag
- **类型**: `FName`

### ActivatableAbilities
- **类型**: `FGameplayAbilitySpecContainer`
- **描述**: The abilities we can activate.
        -This will include CDOs for non instanced abilities and per-execution instanced abilities.
        -Actor-instanced abilities will be the actual instance (not CDO)

This array is not vital for things to work. It is a convenience thing for 'giving abilities to the actor'. But abilities could also work on things
without an AbilitySystemComponent. For example an ability could be written to execute on a StaticMeshActor. As long as the ability doesn't require
instancing or anything else that the AbilitySystemComponent would provide, then it doesn't need the component to function.

## 方法

### ApplyGameplayEffectSpecToSelf
```angelscript
FActiveGameplayEffectHandle ApplyGameplayEffectSpecToSelf(FGameplayEffectSpecHandle SpecHandle)
```
Applies a previously created gameplay effect spec to this component

### ApplyGameplayEffectSpecToTarget
```angelscript
FActiveGameplayEffectHandle ApplyGameplayEffectSpecToTarget(FGameplayEffectSpecHandle SpecHandle, UAbilitySystemComponent Target)
```
Applies a previously created gameplay effect spec to a target

### ApplyGameplayEffectToSelf
```angelscript
FActiveGameplayEffectHandle ApplyGameplayEffectToSelf(TSubclassOf<UGameplayEffect> GameplayEffectClass, float32 Level, FGameplayEffectContextHandle EffectContext)
```
Apply a gameplay effect to self

### ApplyGameplayEffectToTarget
```angelscript
FActiveGameplayEffectHandle ApplyGameplayEffectToTarget(TSubclassOf<UGameplayEffect> GameplayEffectClass, UAbilitySystemComponent Target, float32 Level, FGameplayEffectContextHandle Context)
```
Apply a gameplay effect to passed in target

### ClearAbility
```angelscript
void ClearAbility(FGameplayAbilitySpecHandle Handle)
```
Removes the specified ability.
This will be ignored if the actor is not authoritative.

@param Handle Ability Spec Handle of the ability we want to remove

### ClearAllAbilities
```angelscript
void ClearAllAbilities()
```
Wipes all 'given' abilities. This will be ignored if the actor is not authoritative.

### ClearAllAbilitiesWithInputID
```angelscript
void ClearAllAbilitiesWithInputID(int InputID)
```
Clears all abilities bound to a given Input ID
This will be ignored if the actor is not authoritative

@param InputID The numeric Input ID of the abilities to remove

### ClientActivateAbilityFailed
```angelscript
void ClientActivateAbilityFailed(FGameplayAbilitySpecHandle AbilityToActivate, int16 PredictionKey)
```

### ClientCancelAbility
```angelscript
void ClientCancelAbility(FGameplayAbilitySpecHandle AbilityToCancel, FGameplayAbilityActivationInfo ActivationInfo)
```

### ClientEndAbility
```angelscript
void ClientEndAbility(FGameplayAbilitySpecHandle AbilityToEnd, FGameplayAbilityActivationInfo ActivationInfo)
```

### ClientPrintDebug_Response
```angelscript
void ClientPrintDebug_Response(TArray<FString> Strings, int GameFlags)
```

### ClientTryActivateAbility
```angelscript
void ClientTryActivateAbility(FGameplayAbilitySpecHandle AbilityToActivate)
```

### FindAllAbilitiesMatchingQuery
```angelscript
void FindAllAbilitiesMatchingQuery(TArray<FGameplayAbilitySpecHandle>& OutAbilityHandles, FGameplayTagQuery Query)
```
Returns an array with all abilities that match the provided Gameplay Tag Query

@param OutAbilityHandles This array will be filled with matching Ability Spec Handles
@param Query Gameplay Tag Query to match

### FindAllAbilitiesWithInputID
```angelscript
void FindAllAbilitiesWithInputID(TArray<FGameplayAbilitySpecHandle>& OutAbilityHandles, int InputID)
```
Returns an array with all abilities bound to an Input ID value

@param OutAbilityHandles This array will be filled with matching Ability Spec Handles
@param InputID The Input ID to match

### FindAllAbilitiesWithTags
```angelscript
void FindAllAbilitiesWithTags(TArray<FGameplayAbilitySpecHandle>& OutAbilityHandles, FGameplayTagContainer Tags, bool bExactMatch)
```
Returns an array with all abilities that match the provided tags

@param OutAbilityHandles This array will be filled with matching Ability Spec Handles
@param Tags Gameplay Tags to match
@param bExactMatch If true, tags must be matched exactly. Otherwise, abilities matching any of the tags will be returned

### GetActiveEffects
```angelscript
TArray<FActiveGameplayEffectHandle> GetActiveEffects(FGameplayEffectQuery Query)
```
Returns list of active effects, for a query

### GetActiveEffectsWithAllTags
```angelscript
TArray<FActiveGameplayEffectHandle> GetActiveEffectsWithAllTags(FGameplayTagContainer Tags)
```
Returns list of active effects that have all of the passed in tags

### GetAllAbilities
```angelscript
void GetAllAbilities(TArray<FGameplayAbilitySpecHandle>& OutAbilityHandles)
```
Returns an array with all granted ability handles
NOTE: currently this doesn't include abilities that are mid-activation

@param OutAbilityHandles This array will be filled with the granted Ability Spec Handles

### GetAllAttributes
```angelscript
void GetAllAttributes(TArray<FGameplayAttribute>& OutAttributes)
```
Returns a list of all attributes for this abilty system component

### GetAttributeSet
```angelscript
const UAttributeSet GetAttributeSet(TSubclassOf<UAttributeSet> AttributeSetClass)
```
Returns a reference to the Attribute Set instance, if one exists in this component

@param AttributeSetClass The type of attribute set to look for
@param bFound Set to true if an instance of the Attribute Set exists

### GetGameplayAttributeValue
```angelscript
float32 GetGameplayAttributeValue(FGameplayAttribute Attribute, bool& bFound)
```
Returns the current value of the given gameplay attribute, or zero if the attribute is not found.
NOTE: This doesn't take predicted gameplay effect modifiers into consideration, so the value may not be accurate on clients at all times.

@param Attribute The gameplay attribute to query
@param bFound Set to true if the attribute exists in this component

### GetGameplayEffectCount
```angelscript
int GetGameplayEffectCount(TSubclassOf<UGameplayEffect> SourceGameplayEffect, UAbilitySystemComponent OptionalInstigatorFilterComponent, bool bEnforceOnGoingCheck)
```
Get the count of the specified source effect on the ability system component. For non-stacking effects, this is the sum of all active instances.
For stacking effects, this is the sum of all valid stack counts. If an instigator is specified, only effects from that instigator are counted.

@param SourceGameplayEffect                                  Effect to get the count of
@param OptionalInstigatorFilterComponent             If specified, only count effects applied by this ability system component

@return Count of the specified source effect

### GetGameplayEffectCount_IfLoaded
```angelscript
int GetGameplayEffectCount_IfLoaded(TSoftClassPtr<UGameplayEffect> SoftSourceGameplayEffect, UAbilitySystemComponent OptionalInstigatorFilterComponent, bool bEnforceOnGoingCheck)
```
Get the count of the specified source effect on the ability system component. For non-stacking effects, this is the sum of all active instances.
For stacking effects, this is the sum of all valid stack counts. If an instigator is specified, only effects from that instigator are counted.

@param SoftSourceGameplayEffect                              Effect to get the count of. If this is not currently loaded, the count is 0
@param OptionalInstigatorFilterComponent             If specified, only count effects applied by this ability system component

@return Count of the specified source effect

### GetGameplayEffectMagnitude
```angelscript
float32 GetGameplayEffectMagnitude(FActiveGameplayEffectHandle Handle, FGameplayAttribute Attribute)
```
Raw accessor to ask the magnitude of a gameplay effect, not necessarily always correct. How should outside code (UI, etc) ask things like 'how much is this gameplay effect modifying my damage by'
(most likely we want to catch this on the backend - when damage is applied we can get a full dump/history of how the number got to where it is. But still we may need polling methods like below (how much would my damage be)

### GetGameplayTagCount
```angelscript
int GetGameplayTagCount(FGameplayTag GameplayTag)
```
Returns the current count of the given gameplay tag.
This includes both loose tags, and tags granted by gameplay effects and abilities.
This function can be called on the client, but it may not display the most current count on the server.

@param GameplayTag The gameplay tag to query

### GetUserAbilityActivationInhibited
```angelscript
bool GetUserAbilityActivationInhibited()
```
This is meant to be used to inhibit activating an ability from an input perspective. (E.g., the menu is pulled up, another game mechanism is consuming all input, etc)
This should only be called on locally owned players.
This should not be used to game mechanics like silences or disables. Those should be done through gameplay effects.

### InputCancel
```angelscript
void InputCancel()
```
Sends a local player Input Cancel event, notifying abilities

### InputConfirm
```angelscript
void InputConfirm()
```
Sends a local player Input Confirm event, notifying abilities

### IsGameplayCueActive
```angelscript
bool IsGameplayCueActive(FGameplayTag GameplayCueTag)
```
Allows polling to see if a GameplayCue is active. We expect most GameplayCue handling to be event based, but some cases we may need to check if a GameplayCue is active (Animation Blueprint for example)

### GiveAbility
```angelscript
FGameplayAbilitySpecHandle GiveAbility(TSubclassOf<UGameplayAbility> AbilityClass, int Level, int InputID)
```
Grants a Gameplay Ability and returns its handle.
This will be ignored if the actor is not authoritative.

@param AbilityClass Type of ability to grant
@param Level Level to grant the ability at
@param InputID Input ID value to bind ability activation to.

### GiveAbilityAndActivateOnce
```angelscript
FGameplayAbilitySpecHandle GiveAbilityAndActivateOnce(TSubclassOf<UGameplayAbility> AbilityClass, int Level, int InputID)
```
Grants a Gameplay Ability, activates it once, and removes it.
This will be ignored if the actor is not authoritative.

@param AbilityClass Type of ability to grant
@param Level Level to grant the ability at
@param InputID Input ID value to bind ability activation to.

### InitStats
```angelscript
void InitStats(TSubclassOf<UAttributeSet> Attributes, const UDataTable DataTable)
```

### MakeEffectContext
```angelscript
FGameplayEffectContextHandle MakeEffectContext()
```
Create an EffectContext for the owner of this AbilitySystemComponent

### MakeOutgoingSpec
```angelscript
FGameplayEffectSpecHandle MakeOutgoingSpec(TSubclassOf<UGameplayEffect> GameplayEffectClass, float32 Level, FGameplayEffectContextHandle Context)
```
Get an outgoing GameplayEffectSpec that is ready to be applied to other things.

### PressInputID
```angelscript
void PressInputID(int InputID)
```
* Sends a local player Input Pressed event with the provided Input ID, notifying any bound abilities
*
* @param InputID The Input ID to match

### ReleaseInputID
```angelscript
void ReleaseInputID(int InputID)
```
Sends a local player Input Released event with the provided Input ID, notifying any bound abilities
@param InputID The Input ID to match

### RemoveActiveEffectsWithAppliedTags
```angelscript
int RemoveActiveEffectsWithAppliedTags(FGameplayTagContainer Tags)
```
Removes all active effects that apply any of the tags in Tags

### RemoveActiveEffectsWithGrantedTags
```angelscript
int RemoveActiveEffectsWithGrantedTags(FGameplayTagContainer Tags)
```
Removes all active effects that grant any of the tags in Tags

### RemoveActiveEffectsWithSourceTags
```angelscript
int RemoveActiveEffectsWithSourceTags(FGameplayTagContainer Tags)
```
Removes all active effects with captured source tags that contain any of the tags in Tags

### RemoveActiveEffectsWithTags
```angelscript
int RemoveActiveEffectsWithTags(FGameplayTagContainer Tags)
```
Removes all active effects that contain any of the tags in Tags

### RemoveActiveGameplayEffect
```angelscript
bool RemoveActiveGameplayEffect(FActiveGameplayEffectHandle Handle, int StacksToRemove)
```
Removes GameplayEffect by Handle. StacksToRemove=-1 will remove all stacks.

### RemoveActiveGameplayEffectBySourceEffect
```angelscript
void RemoveActiveGameplayEffectBySourceEffect(TSubclassOf<UGameplayEffect> GameplayEffect, UAbilitySystemComponent InstigatorAbilitySystemComponent, int StacksToRemove)
```
Remove active gameplay effects whose backing definition are the specified gameplay effect class

@param GameplayEffect                                        Class of gameplay effect to remove; Does nothing if left null
@param InstigatorAbilitySystemComponent      If specified, will only remove gameplay effects applied from this instigator ability system component
@param StacksToRemove                                        Number of stacks to remove, -1 means remove all

### ServerCancelAbility
```angelscript
void ServerCancelAbility(FGameplayAbilitySpecHandle AbilityToCancel, FGameplayAbilityActivationInfo ActivationInfo)
```

### ServerCurrentMontageJumpToSectionName
```angelscript
void ServerCurrentMontageJumpToSectionName(UAnimSequenceBase ClientAnimation, FName SectionName)
```
RPC function called from CurrentMontageJumpToSection, replicates to other clients

### ServerCurrentMontageSetNextSectionName
```angelscript
void ServerCurrentMontageSetNextSectionName(UAnimSequenceBase ClientAnimation, float32 ClientPosition, FName SectionName, FName NextSectionName)
```
RPC function called from CurrentMontageSetNextSectionName, replicates to other clients

### ServerCurrentMontageSetPlayRate
```angelscript
void ServerCurrentMontageSetPlayRate(UAnimSequenceBase ClientAnimation, float32 InPlayRate)
```
RPC function called from CurrentMontageSetPlayRate, replicates to other clients

### ServerPrintDebug_Request
```angelscript
void ServerPrintDebug_Request()
```
Ask the server to send ability system debug information back to the client, via ClientPrintDebug_Response

### ServerPrintDebug_RequestWithStrings
```angelscript
void ServerPrintDebug_RequestWithStrings(TArray<FString> Strings)
```
Same as ServerPrintDebug_Request but this includes the client debug strings so that the server can embed them in replays

### ServerSetInputPressed
```angelscript
void ServerSetInputPressed(FGameplayAbilitySpecHandle AbilityHandle)
```
Direct Input state replication. These will be called if bReplicateInputDirectly is true on the ability and is generally not a good thing to use. (Instead, prefer to use Generic Replicated Events).

### ServerSetInputReleased
```angelscript
void ServerSetInputReleased(FGameplayAbilitySpecHandle AbilityHandle)
```

### SetActiveGameplayEffectLevel
```angelscript
void SetActiveGameplayEffectLevel(FActiveGameplayEffectHandle ActiveHandle, int NewLevel)
```
Updates the level of an already applied gameplay effect. The intention is that this is 'seemless' and doesnt behave like removing/reapplying

### SetActiveGameplayEffectLevelUsingQuery
```angelscript
void SetActiveGameplayEffectLevelUsingQuery(FGameplayEffectQuery Query, int NewLevel)
```
Updates the level of an already applied gameplay effect. The intention is that this is 'seemless' and doesnt behave like removing/reapplying

### SetUserAbilityActivationInhibited
```angelscript
void SetUserAbilityActivationInhibited(bool NewInhibit)
```
Disable or Enable a local user from being able to activate abilities. This should only be used for input/UI etc related inhibition. Do not use for game mechanics.

### TargetCancel
```angelscript
void TargetCancel()
```
Any active targeting actors will be stopped and canceled, not returning any targeting data

### TargetConfirm
```angelscript
void TargetConfirm()
```
Any active targeting actors will be told to stop and return current targeting data

### TryActivateAbilitiesByTag
```angelscript
bool TryActivateAbilitiesByTag(FGameplayTagContainer GameplayTagContainer, bool bAllowRemoteActivation)
```
Attempts to activate every gameplay ability that matches the given tag and DoesAbilitySatisfyTagRequirements().
Returns true if anything attempts to activate. Can activate more than one ability and the ability may fail later.
If bAllowRemoteActivation is true, it will remotely activate local/server abilities, if false it will only try to locally activate abilities.

### TryActivateAbility
```angelscript
bool TryActivateAbility(FGameplayAbilitySpecHandle AbilityToActivate, bool bAllowRemoteActivation)
```
Attempts to activate the given ability, will check costs and requirements before doing so.
Returns true if it thinks it activated, but it may return false positives due to failure later in activation.
If bAllowRemoteActivation is true, it will remotely activate local/server abilities, if false it will only try to locally activate the ability

### TryActivateAbilityByClass
```angelscript
bool TryActivateAbilityByClass(TSubclassOf<UGameplayAbility> InAbilityToActivate, bool bAllowRemoteActivation)
```
Attempts to activate the ability that is passed in. This will check costs and requirements before doing so.
Returns true if it thinks it activated, but it may return false positives due to failure later in activation.
If bAllowRemoteActivation is true, it will remotely activate local/server abilities, if false it will only try to locally activate the ability

### UpdateActiveGameplayEffectSetByCallerMagnitude
```angelscript
void UpdateActiveGameplayEffectSetByCallerMagnitude(FActiveGameplayEffectHandle ActiveHandle, FGameplayTag SetByCallerTag, float32 NewValue)
```
Dynamically update the set-by-caller magnitude for an active gameplay effect

### UpdateActiveGameplayEffectSetByCallerMagnitudes
```angelscript
void UpdateActiveGameplayEffectSetByCallerMagnitudes(FActiveGameplayEffectHandle ActiveHandle, TMap<FGameplayTag,float32> NewSetByCallerValues)
```
Dynamically update multiple set-by-caller magnitudes for an active gameplay effect

