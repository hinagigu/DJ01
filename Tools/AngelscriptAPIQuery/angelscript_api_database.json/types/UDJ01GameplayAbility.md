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

### bUsePhaseStateMachine
- **类型**: `bool`

### PhaseConfig
- **类型**: `FDJ01AbilityPhaseConfig`

### Effects
- **类型**: `TArray<FDJ01AbilityEffectEntry>`

## 方法

### CanChangeActivationGroup
```angelscript
bool CanChangeActivationGroup(EDJ01AbilityActivationGroup NewGroup)
```
Returns true if the requested activation group is a valid transition.

### CanCurrentPhaseBeInterrupted
```angelscript
bool CanCurrentPhaseBeInterrupted()
```
当前阶段是否可被打断

### CanCurrentPhaseCancelInto
```angelscript
bool CanCurrentPhaseCancelInto()
```
当前阶段是否可取消到其他技能

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

### GetCurrentPhase
```angelscript
EDJ01AbilityPhase GetCurrentPhase()
```
获取当前阶段

### GetCurrentPhaseRemainingTime
```angelscript
float32 GetCurrentPhaseRemainingTime()
```
获取当前阶段剩余时间

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

### GetPhaseStateMachine
```angelscript
UDJ01AbilityPhaseStateMachine GetPhaseStateMachine()
```
获取阶段状态机

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

### OnPhaseEnter
```angelscript
void OnPhaseEnter(EDJ01AbilityPhase Phase)
```
阶段进入回调 - 子类可重写

### OnPhaseExit
```angelscript
void OnPhaseExit(EDJ01AbilityPhase Phase)
```
阶段退出回调 - 子类可重写

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

### SkipCurrentPhase
```angelscript
void SkipCurrentPhase()
```
跳过当前阶段（立即进入下一阶段）

### TransitionToPhase
```angelscript
bool TransitionToPhase(EDJ01AbilityPhase NewPhase, bool bForce)
```
切换到指定阶段

### TriggerEffects
```angelscript
void TriggerEffects(EDJ01EffectPhase Phase, TArray<AActor> Targets)
```
触发指定阶段的所有效果
@param Phase - 触发阶段
@param Targets - 目标 Actor 列表

### TriggerEffectsByEvent
```angelscript
void TriggerEffectsByEvent(FGameplayTag EventTag, TArray<AActor> Targets)
```
触发动画事件效果
@param EventTag - 动画事件 Tag
@param Targets - 目标 Actor 列表

