// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "Abilities/GameplayAbility.h"
#include "DJ01AbilityEffect.h"
#include "DJ01AbilityPhase.h"
#include "DJ01AbilityPhaseStateMachine.h"

#include "DJ01GameplayAbility.generated.h"


struct FGameplayAbilityActivationInfo;
struct FGameplayAbilitySpec;
struct FGameplayAbilitySpecHandle;

class AActor;
class AController;
class ADJ01Character;
class ADJ01PlayerController;
class APlayerController;
class FText;
class IDJ01AbilitySourceInterface;
class UAnimMontage;
class UDJ01AbilityCost;
class UDJ01AbilitySystemComponent;
class UDJ01CameraMode;
class UDJ01HeroComponent;
class UObject;
struct FFrame;
struct FGameplayAbilityActorInfo;
struct FGameplayEffectSpec;
struct FGameplayEventData;

/**
 * EDJ01AbilityActivationPolicy
 *
 *	Defines how an ability is meant to activate.
 */
UENUM(BlueprintType)
enum class EDJ01AbilityActivationPolicy : uint8
{
	// Try to activate the ability when the input is triggered.
	OnInputTriggered,

	// Continually try to activate the ability while the input is active.
	WhileInputActive,

	// Try to activate the ability when an avatar is assigned.
	OnSpawn
};


/**
 * EDJ01AbilityActivationGroup
 *
 *	Defines how an ability activates in relation to other abilities.
 */
UENUM(BlueprintType)
enum class EDJ01AbilityActivationGroup : uint8
{
	// Ability runs independently of all other abilities.
	Independent,

	// Ability is canceled and replaced by other exclusive abilities.
	Exclusive_Replaceable,

	// Ability blocks all other exclusive abilities from activating.
	Exclusive_Blocking,

	MAX	UMETA(Hidden)
};

/** Failure reason that can be used to play an animation montage when a failure occurs */
USTRUCT(BlueprintType)
struct FDJ01AbilityMontageFailureMessage
{
	GENERATED_BODY()

public:
	
	UPROPERTY(BlueprintReadWrite)
	TObjectPtr<APlayerController> PlayerController = nullptr;

	// All the reasons why this ability has failed
	UPROPERTY(BlueprintReadWrite)
	FGameplayTagContainer FailureTags;

	UPROPERTY(BlueprintReadWrite)
	TObjectPtr<UAnimMontage> FailureMontage = nullptr;
};

/**
 * UDJ01GameplayAbility
 *
 *	The base gameplay ability class used by this project.
 */
UCLASS(Abstract, HideCategories = Input, Meta = (ShortTooltip = "The base gameplay ability class used by this project."))
class DJ01_API UDJ01GameplayAbility : public UGameplayAbility
{
	GENERATED_BODY()
	friend class UDJ01AbilitySystemComponent;

public:

	UDJ01GameplayAbility(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

	UFUNCTION(BlueprintCallable, Category = "DJ01|Ability")
	UDJ01AbilitySystemComponent* GetDJ01AbilitySystemComponentFromActorInfo() const;

	UFUNCTION(BlueprintCallable, Category = "DJ01|Ability")
	ADJ01PlayerController* GetDJ01PlayerControllerFromActorInfo() const;

	UFUNCTION(BlueprintCallable, Category = "DJ01|Ability")
	AController* GetControllerFromActorInfo() const;

	UFUNCTION(BlueprintCallable, Category = "DJ01|Ability")
	ADJ01Character* GetDJ01CharacterFromActorInfo() const;

	UFUNCTION(BlueprintCallable, Category = "DJ01|Ability")
	UDJ01HeroComponent* GetHeroComponentFromActorInfo() const;

	EDJ01AbilityActivationPolicy GetActivationPolicy() const { return ActivationPolicy; }
	EDJ01AbilityActivationGroup GetActivationGroup() const { return ActivationGroup; }

	void TryActivateAbilityOnSpawn(const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilitySpec& Spec) const;

	// Returns true if the requested activation group is a valid transition.
	UFUNCTION(BlueprintCallable, BlueprintPure = false, Category = "DJ01|Ability", Meta = (ExpandBoolAsExecs = "ReturnValue"))
	bool CanChangeActivationGroup(EDJ01AbilityActivationGroup NewGroup) const;

	// Tries to change the activation group.  Returns true if it successfully changed.
	UFUNCTION(BlueprintCallable, BlueprintPure = false, Category = "DJ01|Ability", Meta = (ExpandBoolAsExecs = "ReturnValue"))
	bool ChangeActivationGroup(EDJ01AbilityActivationGroup NewGroup);

	// Sets the ability's camera mode.
	UFUNCTION(BlueprintCallable, Category = "DJ01|Ability")
	void SetCameraMode(TSubclassOf<UDJ01CameraMode> CameraMode);

	// Clears the ability's camera mode.  Automatically called if needed when the ability ends.
	UFUNCTION(BlueprintCallable, Category = "DJ01|Ability")
	void ClearCameraMode();

	void OnAbilityFailedToActivate(const FGameplayTagContainer& FailedReason) const
	{
		NativeOnAbilityFailedToActivate(FailedReason);
		ScriptOnAbilityFailedToActivate(FailedReason);
	}

protected:

	// Called when the ability fails to activate
	virtual void NativeOnAbilityFailedToActivate(const FGameplayTagContainer& FailedReason) const;

	// Called when the ability fails to activate
	UFUNCTION(BlueprintImplementableEvent)
	void ScriptOnAbilityFailedToActivate(const FGameplayTagContainer& FailedReason) const;

	//~UGameplayAbility interface
	virtual bool CanActivateAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, const FGameplayTagContainer* SourceTags, const FGameplayTagContainer* TargetTags, FGameplayTagContainer* OptionalRelevantTags) const override;
	virtual void SetCanBeCanceled(bool bCanBeCanceled) override;
	virtual void OnGiveAbility(const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilitySpec& Spec) override;
	virtual void OnRemoveAbility(const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilitySpec& Spec) override;
	virtual void ActivateAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilityActivationInfo ActivationInfo, const FGameplayEventData* TriggerEventData) override;
	virtual void EndAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilityActivationInfo ActivationInfo, bool bReplicateEndAbility, bool bWasCancelled) override;
	virtual bool CheckCost(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, OUT FGameplayTagContainer* OptionalRelevantTags = nullptr) const override;
	virtual void ApplyCost(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilityActivationInfo ActivationInfo) const override;
	virtual FGameplayEffectContextHandle MakeEffectContext(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo) const override;
	virtual void ApplyAbilityTagsToGameplayEffectSpec(FGameplayEffectSpec& Spec, FGameplayAbilitySpec* AbilitySpec) const override;
	virtual bool DoesAbilitySatisfyTagRequirements(const UAbilitySystemComponent& AbilitySystemComponent, const FGameplayTagContainer* SourceTags = nullptr, const FGameplayTagContainer* TargetTags = nullptr, OUT FGameplayTagContainer* OptionalRelevantTags = nullptr) const override;
	//~End of UGameplayAbility interface

	virtual void OnPawnAvatarSet();

	virtual void GetAbilitySource(FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, float& OutSourceLevel, const IDJ01AbilitySourceInterface*& OutAbilitySource, AActor*& OutEffectCauser) const;

	/** Called when this ability is granted to the ability system component. */
	UFUNCTION(BlueprintImplementableEvent, Category = Ability, DisplayName = "OnAbilityAdded")
	void K2_OnAbilityAdded();

	/** Called when this ability is removed from the ability system component. */
	UFUNCTION(BlueprintImplementableEvent, Category = Ability, DisplayName = "OnAbilityRemoved")
	void K2_OnAbilityRemoved();

	/** Called when the ability system is initialized with a pawn avatar. */
	UFUNCTION(BlueprintImplementableEvent, Category = Ability, DisplayName = "OnPawnAvatarSet")
	void K2_OnPawnAvatarSet();

protected:

	// Defines how this ability is meant to activate.
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DJ01|Ability Activation")
	EDJ01AbilityActivationPolicy ActivationPolicy;

	// Defines the relationship between this ability activating and other abilities activating.
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DJ01|Ability Activation")
	EDJ01AbilityActivationGroup ActivationGroup;

	// Additional costs that must be paid to activate this ability
	UPROPERTY(EditDefaultsOnly, Instanced, Category = Costs)
	TArray<TObjectPtr<UDJ01AbilityCost>> AdditionalCosts;

	// Map of failure tags to simple error messages
	UPROPERTY(EditDefaultsOnly, Category = "Advanced")
	TMap<FGameplayTag, FText> FailureTagToUserFacingMessages;

	// Map of failure tags to anim montages that should be played with them
	UPROPERTY(EditDefaultsOnly, Category = "Advanced")
	TMap<FGameplayTag, TObjectPtr<UAnimMontage>> FailureTagToAnimMontage;

	// If true, extra information should be logged when this ability is canceled. This is temporary, used for tracking a bug.
	UPROPERTY(EditDefaultsOnly, Category = "Advanced")
	bool bLogCancelation;

	// Current camera mode set by the ability.
	TSubclassOf<UDJ01CameraMode> ActiveCameraMode;

	// ========== 阶段状态机 ==========

	/** 是否使用阶段状态机（禁用后需要手动管理阶段） */
	UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "DJ01|Phase")
	bool bUsePhaseStateMachine = true;

	/** 阶段配置 */
	UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "DJ01|Phase", 
		meta = (EditCondition = "bUsePhaseStateMachine"))
	FDJ01AbilityPhaseConfig PhaseConfig;

	/** 阶段状态机实例 */
	UPROPERTY(Transient)
	TObjectPtr<UDJ01AbilityPhaseStateMachine> PhaseStateMachine;

public:
	// ========== 阶段控制方法 ==========

	/** 获取阶段状态机 */
	UFUNCTION(BlueprintCallable, BlueprintPure, Category = "DJ01|Phase")
	UDJ01AbilityPhaseStateMachine* GetPhaseStateMachine() const { return PhaseStateMachine; }

	/** 获取当前阶段 */
	UFUNCTION(BlueprintCallable, BlueprintPure, Category = "DJ01|Phase")
	EDJ01AbilityPhase GetCurrentPhase() const;

	/** 切换到指定阶段 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Phase")
	bool TransitionToPhase(EDJ01AbilityPhase NewPhase, bool bForce = false);

	/** 当前阶段是否可被打断 */
	UFUNCTION(BlueprintCallable, BlueprintPure, Category = "DJ01|Phase")
	bool CanCurrentPhaseBeInterrupted() const;

	/** 当前阶段是否可取消到其他技能 */
	UFUNCTION(BlueprintCallable, BlueprintPure, Category = "DJ01|Phase")
	bool CanCurrentPhaseCancelInto() const;

	/** 跳过当前阶段（立即进入下一阶段） */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Phase")
	void SkipCurrentPhase();

	/** 获取当前阶段剩余时间 */
	UFUNCTION(BlueprintCallable, BlueprintPure, Category = "DJ01|Phase")
	float GetCurrentPhaseRemainingTime() const;

protected:
	/** 创建状态机实例 */
	virtual void CreatePhaseStateMachine();

	/** 播放阶段对应的 Montage (如果配置了) */
	void PlayPhaseMontage(const FDJ01AbilityPhaseInfo& PhaseInfo);

	/** 状态机阶段进入回调 */
	UFUNCTION()
	void HandleStateMachinePhaseEnter(EDJ01AbilityPhase Phase);

	/** 状态机阶段退出回调 */
	UFUNCTION()
	void HandleStateMachinePhaseExit(EDJ01AbilityPhase Phase);

	/** 状态机完成回调 */
	UFUNCTION()
	void HandleStateMachineFinished();

	/** 阶段进入回调 - 子类可重写 */
	UFUNCTION(BlueprintNativeEvent, Category = "DJ01|Phase")
	void OnPhaseEnter(EDJ01AbilityPhase Phase);
	virtual void OnPhaseEnter_Implementation(EDJ01AbilityPhase Phase);

	/** 阶段退出回调 - 子类可重写 */
	UFUNCTION(BlueprintNativeEvent, Category = "DJ01|Phase")
	void OnPhaseExit(EDJ01AbilityPhase Phase);
	virtual void OnPhaseExit_Implementation(EDJ01AbilityPhase Phase);

	/** 将阶段映射到效果触发阶段 */
	EDJ01EffectPhase MapPhaseToEffectPhase(EDJ01AbilityPhase Phase) const;

	// ========== 效果系统 ==========

	/** 
	 * 效果列表
	 * 每个效果绑定到特定的触发阶段
	 */
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DJ01|Effects", 
		meta = (TitleProperty = "Phase: {Phase} - {Effect}"))
	TArray<FDJ01AbilityEffectEntry> Effects;

public:
	// ========== 效果触发方法 ==========

	/**
	 * 触发指定阶段的所有效果
	 * @param Phase - 触发阶段
	 * @param Targets - 目标 Actor 列表
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Effects")
	void TriggerEffects(EDJ01EffectPhase Phase, const TArray<AActor*>& Targets);

	/**
	 * 触发动画事件效果
	 * @param EventTag - 动画事件 Tag
	 * @param Targets - 目标 Actor 列表
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Effects")
	void TriggerEffectsByEvent(FGameplayTag EventTag, const TArray<AActor*>& Targets);

	/**
	 * 触发效果（内部使用）
	 */
	void TriggerEffectsInternal(EDJ01EffectPhase Phase, const FGameplayTag& EventTag, const TArray<AActor*>& Targets);

protected:
	/** 构建效果执行上下文 */
	FDJ01EffectContext BuildEffectContext(const TArray<AActor*>& Targets) const;
};

