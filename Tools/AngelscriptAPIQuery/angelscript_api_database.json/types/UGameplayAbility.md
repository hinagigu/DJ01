# UGameplayAbility

**继承自**: `UObject`

Abilities define custom gameplay logic that can be activated by players or external game logic

## 属性

### AbilityTags
- **类型**: `FGameplayTagContainer`
- **描述**: This ability has these tags

### bReplicateInputDirectly
- **类型**: `bool`
- **描述**: If true, this ability will always replicate input press/release events to the server.

### ReplicationPolicy
- **类型**: `EGameplayAbilityReplicationPolicy`
- **描述**: How an ability replicates state/events to everyone on the network. Replication is not required for NetExecutionPolicy.

### InstancingPolicy
- **类型**: `EGameplayAbilityInstancingPolicy`
- **描述**: How the ability is instanced when executed. This limits what an ability can do in its implementation.

### bServerRespectsRemoteAbilityCancellation
- **类型**: `bool`
- **描述**: If this is set, the server-side version of the ability can be canceled by the client-side version. The client-side version can always be canceled by the server.

### bRetriggerInstancedAbility
- **类型**: `bool`
- **描述**: if true, and trying to activate an already active instanced ability, end it and re-trigger it.

### CurrentActivationInfo
- **类型**: `FGameplayAbilityActivationInfo`
- **描述**: This is information specific to this instance of the ability. E.g, whether it is predicting, authoring, confirmed, etc.

### CurrentEventData
- **类型**: `FGameplayEventData`
- **描述**: Information specific to this instance of the ability, if it was activated by an event

### NetExecutionPolicy
- **类型**: `EGameplayAbilityNetExecutionPolicy`
- **描述**: How does an ability execute on the network. Does a client "ask and predict", "ask and wait", "don't ask (just do it)".

### NetSecurityPolicy
- **类型**: `EGameplayAbilityNetSecurityPolicy`
- **描述**: What protections does this ability have? Should the client be allowed to request changes to the execution of the ability?

### CostGameplayEffectClass
- **类型**: `TSubclassOf<UGameplayEffect>`
- **描述**: This GameplayEffect represents the cost (mana, stamina, etc) of the ability. It will be applied when the ability is committed.

### AbilityTriggers
- **类型**: `TArray<FAbilityTriggerData>`
- **描述**: Triggers to determine if this ability should execute in response to an event

### CooldownGameplayEffectClass
- **类型**: `TSubclassOf<UGameplayEffect>`
- **描述**: This GameplayEffect represents the cooldown. It will be applied when the ability is committed and the ability cannot be used again until it is expired.

### CancelAbilitiesWithTag
- **类型**: `FGameplayTagContainer`
- **描述**: Abilities with these tags are cancelled when this ability is executed

### BlockAbilitiesWithTag
- **类型**: `FGameplayTagContainer`
- **描述**: Abilities with these tags are blocked while this ability is active

### ActivationOwnedTags
- **类型**: `FGameplayTagContainer`
- **描述**: Tags to apply to activating owner while this ability is active. These are replicated if ReplicateActivationOwnedTags is enabled in AbilitySystemGlobals.

### ActivationRequiredTags
- **类型**: `FGameplayTagContainer`
- **描述**: This ability can only be activated if the activating actor/component has all of these tags

### ActivationBlockedTags
- **类型**: `FGameplayTagContainer`
- **描述**: This ability is blocked if the activating actor/component has any of these tags

### SourceRequiredTags
- **类型**: `FGameplayTagContainer`
- **描述**: This ability can only be activated if the source actor/component has all of these tags

### SourceBlockedTags
- **类型**: `FGameplayTagContainer`
- **描述**: This ability is blocked if the source actor/component has any of these tags

### TargetRequiredTags
- **类型**: `FGameplayTagContainer`
- **描述**: This ability can only be activated if the target actor/component has all of these tags

### TargetBlockedTags
- **类型**: `FGameplayTagContainer`
- **描述**: This ability is blocked if the target actor/component has any of these tags

## 方法

### ApplyGameplayEffectToOwner
```angelscript
FActiveGameplayEffectHandle ApplyGameplayEffectToOwner(TSubclassOf<UGameplayEffect> GameplayEffectClass, int GameplayEffectLevel, int Stacks)
```
Apply a gameplay effect to the owner of this ability

### ApplyGameplayEffectToTarget
```angelscript
TArray<FActiveGameplayEffectHandle> ApplyGameplayEffectToTarget(FGameplayAbilityTargetDataHandle TargetData, TSubclassOf<UGameplayEffect> GameplayEffectClass, int GameplayEffectLevel, int Stacks)
```
Apply a gameplay effect to a Target

### RemoveGameplayEffectFromOwnerWithAssetTags
```angelscript
void RemoveGameplayEffectFromOwnerWithAssetTags(FGameplayTagContainer WithAssetTags, int StacksToRemove)
```
Removes GameplayEffects from owner which match the given asset level tags

### RemoveGameplayEffectFromOwnerWithGrantedTags
```angelscript
void RemoveGameplayEffectFromOwnerWithGrantedTags(FGameplayTagContainer WithGrantedTags, int StacksToRemove)
```
Removes GameplayEffects from owner which grant the given tags

### RemoveGameplayEffectFromOwnerWithHandle
```angelscript
void RemoveGameplayEffectFromOwnerWithHandle(FActiveGameplayEffectHandle Handle, int StacksToRemove)
```
Removes GameplayEffect from owner that match the given handle

### CancelTaskByInstanceName
```angelscript
void CancelTaskByInstanceName(FName InstanceName)
```
Add any task with this instance name to a list to be canceled (not ended) next frame.  See also EndTaskByInstanceName.

### ConfirmTaskByInstanceName
```angelscript
void ConfirmTaskByInstanceName(FName InstanceName, bool bEndTask)
```
Finds all currently active tasks named InstanceName and confirms them. What this means depends on the individual task. By default, this does nothing other than ending if bEndTask is true.

### EndAbilityState
```angelscript
void EndAbilityState(FName OptionalStateNameToEnd)
```
Ends any active ability state task with the given name. If name is 'None' all active states will be ended (in an arbitrary order).

### EndTaskByInstanceName
```angelscript
void EndTaskByInstanceName(FName InstanceName)
```
Add any task with this instance name to a list to be ended (not canceled) next frame.  See also CancelTaskByInstanceName.

### GetAbilityLevel
```angelscript
int GetAbilityLevel()
```
Returns current level of the Ability

### GetAbilityLevel_BP
```angelscript
int GetAbilityLevel_BP(FGameplayAbilitySpecHandle Handle, FGameplayAbilityActorInfo ActorInfo)
```
Returns current ability level for non instanced abilities. You must call this version in these contexts!

### GetAbilitySystemComponentFromActorInfo
```angelscript
UAbilitySystemComponent GetAbilitySystemComponentFromActorInfo()
```
Returns the AbilitySystemComponent that is activating this ability

### GetActorInfo
```angelscript
FGameplayAbilityActorInfo GetActorInfo()
```
Returns the actor info associated with this ability, has cached pointers to useful objects

### GetAvatarActorFromActorInfo
```angelscript
AActor GetAvatarActorFromActorInfo()
```
Returns the physical actor that is executing this ability. May be null

### GetContextFromOwner
```angelscript
FGameplayEffectContextHandle GetContextFromOwner(FGameplayAbilityTargetDataHandle OptionalTargetData)
```
Generates a GameplayEffectContextHandle from our owner and an optional TargetData.

### GetCooldownTimeRemaining
```angelscript
float32 GetCooldownTimeRemaining()
```
Returns the time in seconds remaining on the currently active cooldown.

### GetCurrentMontage
```angelscript
UAnimMontage GetCurrentMontage()
```
Returns the currently playing montage for this ability, if any

### GetCurrentSourceObject
```angelscript
UObject GetCurrentSourceObject()
```
Retrieves the SourceObject associated with this ability. Can only be called on instanced abilities.

### GetGrantedByEffectContext
```angelscript
FGameplayEffectContextHandle GetGrantedByEffectContext()
```
Retrieves the EffectContext of the GameplayEffect that granted this ability. Can only be called on instanced abilities.

### GetOwningActorFromActorInfo
```angelscript
AActor GetOwningActorFromActorInfo()
```
Returns the actor that owns this ability, which may not have a physical location

### GetOwningComponentFromActorInfo
```angelscript
USkeletalMeshComponent GetOwningComponentFromActorInfo()
```
Convenience method for abilities to get skeletal mesh component - useful for aiming abilities

### GetSourceObject_BP
```angelscript
UObject GetSourceObject_BP(FGameplayAbilitySpecHandle Handle, FGameplayAbilityActorInfo ActorInfo)
```
Retrieves the SourceObject associated with this ability. Callable on non instanced

### InvalidateClientPredictionKey
```angelscript
void InvalidateClientPredictionKey()
```
Invalidates the current prediction key. This should be used in cases where there is a valid prediction window, but the server is doing logic that only it can do, and afterwards performs an action that the client could predict (had the client been able to run the server-only code prior).
This returns instantly and has no other side effects other than clearing the current prediction key.

### IsLocallyControlled
```angelscript
bool IsLocallyControlled()
```
True if the owning actor is locally controlled, true in single player

### ActivateAbility
```angelscript
void ActivateAbility()
```
The main function that defines what an ability does.
 -Child classes will want to override this
 -This function graph should call CommitAbility
 -This function graph should call EndAbility

 Latent/async actions are ok in this graph. Note that Commit and EndAbility calling requirements speak to the K2_ActivateAbility graph.
 In C++, the call to K2_ActivateAbility() may return without CommitAbility or EndAbility having been called. But it is expected that this
 will only occur when latent/async actions are pending. When K2_ActivateAbility logically finishes, then we will expect Commit/End to have been called.

### ActivateAbilityFromEvent
```angelscript
void ActivateAbilityFromEvent(FGameplayEventData EventData)
```

### AddGameplayCue
```angelscript
void AddGameplayCue(FGameplayTag GameplayCueTag, FGameplayEffectContextHandle Context, bool bRemoveOnAbilityEnd)
```
Adds a persistent gameplay cue to the ability owner. Optionally will remove if ability ends

### AddGameplayCueWithParams
```angelscript
void AddGameplayCueWithParams(FGameplayTag GameplayCueTag, FGameplayCueParameters GameplayCueParameter, bool bRemoveOnAbilityEnd)
```
Adds a persistent gameplay cue to the ability owner. Optionally will remove if ability ends

### ApplyGameplayEffectSpecToOwner
```angelscript
FActiveGameplayEffectHandle ApplyGameplayEffectSpecToOwner(FGameplayEffectSpecHandle EffectSpecHandle)
```
Apply a previously created gameplay effect spec to the owner of this ability

### ApplyGameplayEffectSpecToTarget
```angelscript
TArray<FActiveGameplayEffectHandle> ApplyGameplayEffectSpecToTarget(FGameplayEffectSpecHandle EffectSpecHandle, FGameplayAbilityTargetDataHandle TargetData)
```
Apply a previously created gameplay effect spec to a target

### CanActivateAbility
```angelscript
bool CanActivateAbility(FGameplayAbilityActorInfo ActorInfo, FGameplayAbilitySpecHandle Handle, FGameplayTagContainer& RelevantTags)
```
Returns true if this ability can be activated right now. Has no side effects

### CancelAbility
```angelscript
void CancelAbility()
```
Call from Blueprint to cancel the ability naturally

### CheckAbilityCooldown
```angelscript
bool CheckAbilityCooldown()
```
Checks the ability's cooldown, but does not apply it.

### CheckAbilityCost
```angelscript
bool CheckAbilityCost()
```
Checks the ability's cost, but does not apply it.

### CommitAbility
```angelscript
bool CommitAbility()
```
Attempts to commit the ability (spend resources, etc). This our last chance to fail. Child classes that override ActivateAbility must call this themselves!

### CommitAbilityCooldown
```angelscript
bool CommitAbilityCooldown(bool BroadcastCommitEvent, bool ForceCooldown)
```
Attempts to commit the ability's cooldown only. If BroadcastCommitEvent is true, it will broadcast the commit event that tasks like WaitAbilityCommit are listening for.

### CommitAbilityCost
```angelscript
bool CommitAbilityCost(bool BroadcastCommitEvent)
```
Attempts to commit the ability's cost only. If BroadcastCommitEvent is true, it will broadcast the commit event that tasks like WaitAbilityCommit are listening for.

### CommitExecute
```angelscript
void CommitExecute()
```
BP event called from CommitAbility

### EndAbility
```angelscript
void EndAbility()
```
Call from blueprints to forcibly end the ability without canceling it. This will replicate the end ability to the client or server which can interrupt tasks

### EndAbilityLocally
```angelscript
void EndAbilityLocally()
```
Call from blueprints to end the ability naturally. This will only end predicted abilities locally, allowing it end naturally on the client or server

### ExecuteGameplayCue
```angelscript
void ExecuteGameplayCue(FGameplayTag GameplayCueTag, FGameplayEffectContextHandle Context)
```
Invoke a gameplay cue on the ability owner

### ExecuteGameplayCueWithParams
```angelscript
void ExecuteGameplayCueWithParams(FGameplayTag GameplayCueTag, FGameplayCueParameters GameplayCueParameters)
```
Invoke a gameplay cue on the ability owner, with extra parameters

### HasAuthority
```angelscript
bool HasAuthority()
```

### OnEndAbility
```angelscript
void OnEndAbility(bool bWasCancelled)
```
Blueprint event, will be called if an ability ends normally or abnormally

### RemoveGameplayCue
```angelscript
void RemoveGameplayCue(FGameplayTag GameplayCueTag)
```
Removes a persistent gameplay cue from the ability owner

### ShouldAbilityRespondToEvent
```angelscript
bool ShouldAbilityRespondToEvent(FGameplayAbilityActorInfo ActorInfo, FGameplayEventData Payload)
```
Returns true if this ability can be activated right now. Has no side effects

### MakeOutgoingGameplayEffectSpec
```angelscript
FGameplayEffectSpecHandle MakeOutgoingGameplayEffectSpec(TSubclassOf<UGameplayEffect> GameplayEffectClass, float32 Level)
```
Convenience method for abilities to get outgoing gameplay effect specs (for example, to pass on to projectiles to apply to whoever they hit)

### MakeTargetLocationInfoFromOwnerActor
```angelscript
FGameplayAbilityTargetingLocationInfo MakeTargetLocationInfoFromOwnerActor()
```
Creates a target location from where the owner avatar is

### MakeTargetLocationInfoFromOwnerSkeletalMeshComponent
```angelscript
FGameplayAbilityTargetingLocationInfo MakeTargetLocationInfoFromOwnerSkeletalMeshComponent(FName SocketName)
```
Creates a target location from a socket on the owner avatar's skeletal mesh

### MontageJumpToSection
```angelscript
void MontageJumpToSection(FName SectionName)
```
Immediately jumps the active montage to a section

### MontageSetNextSectionName
```angelscript
void MontageSetNextSectionName(FName FromSectionName, FName ToSectionName)
```
Sets pending section on active montage

### MontageStop
```angelscript
void MontageStop(float32 OverrideBlendOutTime)
```
Stops the current animation montage.

@param OverrideBlendTime If >= 0, will override the BlendOutTime parameter on the AnimMontage instance

### RemoveGrantedByEffect
```angelscript
void RemoveGrantedByEffect()
```
Removes the GameplayEffect that granted this ability. Can only be called on instanced abilities.

### SendGameplayEvent
```angelscript
void SendGameplayEvent(FGameplayTag EventTag, FGameplayEventData Payload)
```
Sends a gameplay event, also creates a prediction window

### SetCanBeCanceled
```angelscript
void SetCanBeCanceled(bool bCanBeCanceled)
```
Sets whether the ability should ignore cancel requests. Only valid on instanced abilities

### SetShouldBlockOtherAbilities
```angelscript
void SetShouldBlockOtherAbilities(bool bShouldBlockAbilities)
```
Sets rather ability block flags are enabled or disabled. Only valid on instanced abilities

### GetSourceObject
```angelscript
UObject GetSourceObject(FGameplayAbilitySpecHandle Handle, FGameplayAbilityActorInfo ActorInfo)
```

