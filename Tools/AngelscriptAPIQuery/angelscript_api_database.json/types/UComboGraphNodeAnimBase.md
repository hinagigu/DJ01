# UComboGraphNodeAnimBase

**继承自**: `UComboGraphNodeBase`

Base Class for all Anim related Combo Graph nodes (montage or sequence)

Holds runtime properties for animation and effects / cues containers.

## 属性

### MontagePlayRate
- **类型**: `float32`

### RootMotionScale
- **类型**: `float32`

### bStopAnimationWhenAbilityEnds
- **类型**: `bool`

### DamageHandlingMethod
- **类型**: `EComboGraphDamageHandlingMethod`

### EffectsContainerMap
- **类型**: `TMap<FGameplayTag,FComboGraphGameplayEffectContainer>`

### DamagesContainerMap
- **类型**: `TMap<FGameplayTag,FComboGraphDamageSystemContainer>`

### CostGameplayEffect
- **类型**: `TSubclassOf<UGameplayEffect>`

### EventTags
- **类型**: `FGameplayTagContainer`

### CuesContainerMap
- **类型**: `TMap<FGameplayTag,FComboGraphCueContainer>`

### NotifyStatesOverrides
- **类型**: `TMap<TSoftClassPtr<UAnimNotifyState>,FComboGraphNotifyStateAutoSetup>`

## 方法

### GetAvatarActor
```angelscript
AActor GetAvatarActor()
```
Returns the direct parent node that this node was transitioned from.

### GetAvatarAsCharacter
```angelscript
ACharacter GetAvatarAsCharacter()
```
Returns the direct parent node that this node was transitioned from.

### GetAvatarAsPawn
```angelscript
APawn GetAvatarAsPawn()
```
Returns the direct parent node that this node was transitioned from.

### GetMagnitudeForContainer
```angelscript
float32 GetMagnitudeForContainer(float OriginalMagnitude, float ElapsedSeconds, float TriggeredSeconds, float AnimationLength, float MontagePlayTime, float InputMagnitude, FGameplayTag ContainerTag)
```
Used by Combo Graph Task to calculate Damage Container damage to apply or Effect Container set by caller magnitudes before being applied via Effects.

Can be overridden in Blueprint, and should return the new computed magnitude value (default native implementation simply return the Container Magnitude value)

@param OriginalMagnitude Original magnitude or base damage value defined in Combo Node for the Effect or Damage Container (depends on DamageHandlingMethod)
@param ElapsedSeconds Time in seconds returned by the Enhanced Input system. Total time the action has been evaluating triggering (Ongoing & Triggered)
@param TriggeredSeconds Time in seconds returned by the Enhanced Input system. Time the action has been actively triggered (Triggered only)
@param AnimationLength Total animation play time with section time defined by StartSection on montage node subtracted from the result. If no StartSection is defined (None), total animation play time is used
@param MontagePlayTime Actual Play time in seconds for the montage at the time the container is applied
@param InputMagnitude Normalized magnitude value ranging from 0 to 1 based on Enhanced Input Elapsed Time and Animation Length (1 means Elapsed Time is at or above the total animation length)
@param ContainerTag Gameplay Tag key for the Effect or Damage container (depends on DamageHandlingMethod). Can be used to get back original container from DamagesContainerMap or EffectsContainerMap
@return New adjusted magnitude value

### GetOwnerActor
```angelscript
AActor GetOwnerActor()
```
Returns the direct parent node that this node was transitioned from.

### CanActivateNode
```angelscript
bool CanActivateNode()
```
Returns true if this node can be activated right now. Has no side effects.

### GetAnimationAsset
```angelscript
UAnimSequenceBase GetAnimationAsset()
```
Returns the animation asset defined in editor for the node. Can be either a sequence or montage.

### GetAnimationClass
```angelscript
UClass GetAnimationClass()
```
Returns the type as text of underlying animation asset for the node. Can be either a sequence or montage.

Effectively just calling AnimationAsset->GetClass();

### GetChildren
```angelscript
TArray<UComboGraphNodeAnimBase> GetChildren()
```
Returns the list of children nodes for this node, that is direct descendant in the graph hierarchy.

### GetNodeTitle
```angelscript
FText GetNodeTitle()
```
Returns title for the node as displayed in the editor (either name of the animation asset or if defined the NodeTitle property)

### GetOwningAbility
```angelscript
UGameplayAbility GetOwningAbility()
```
Returns the owning gameplay ability this node currently being played in. Should only return valid instance if the ability is currently active / running.

### GetOwningGraph
```angelscript
UComboGraph GetOwningGraph()
```
Returns the ComboGraph UObject this node is part of.

### GetOwningTask
```angelscript
UComboGraphAbilityTask_StartGraph GetOwningTask()
```
Returns the owning ability task this node currently being played in. Should only return valid instance if the task is currently active / running.

### GetPreviousNode
```angelscript
UComboGraphNodeAnimBase GetPreviousNode()
```
Returns the direct parent node that this node was transitioned from.

### OnActivated
```angelscript
void OnActivated()
```
Event triggered when the node is activated and transitioned to in the owning graph.

This only triggers if checks (CanActivateNode / Cost commit) have been successful and not preventing execution.

### OnDeactivated
```angelscript
void OnDeactivated()
```
Event triggered when the node is ending and owning graph is transitioning to the next node (or ending the graph).

### OnEventReceived
```angelscript
void OnEventReceived(FGameplayTag EventTag, FGameplayEventData EventData)
```
Event triggered when the actor owning the combo graph this node is part of is receiving a gameplay event this node listens to
(either with the EventTags property or if it is defining Gameplay Effects or Cues Containers).

### OnInitialized
```angelscript
void OnInitialized()
```
Event triggered when the node is activated and transitioned to in the owning graph, before CanActivateNode checks / cost commit and activation.

### OnMontagePlay
```angelscript
void OnMontagePlay(UAnimMontage Montage)
```
Event triggered when the animation asset for this node is played as an anim montage in the owning ability task and gameplay ability.

