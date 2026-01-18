// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/AbilitySystem/Abilities/Public/DJ01GameplayAbility.h"
#include "DJ01/System/Public/DJ01LogChannels.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"
#include "AbilitySystemLog.h"
#include "DJ01/Player/Public/DJ01PlayerController.h"
#include "DJ01/Character/Public/DJ01Character.h"
#include "DJ01/System/Public/DJ01GameplayTags.h"
#include "DJ01/AbilitySystem/Abilities/Public/DJ01AbilityCost.h"
#include "DJ01/Character/Public/DJ01HeroComponent.h"
#include "AbilitySystemBlueprintLibrary.h"
#include "AbilitySystemGlobals.h"
#include "DJ01/AbilitySystem/Abilities/Public/DJ01AbilitySimpleFailureMessage.h"
#include "GameFramework/GameplayMessageSubsystem.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilitySourceInterface.h"
#include "DJ01/AbilitySystem/Public/DJ01GameplayEffectContext.h"
#include "DJ01/Physics//PhysicalMaterialWithTags.h"
#include "GameFramework/PlayerState.h"
#include "DJ01/Camera/Public/DJ01CameraMode.h"
#include "ClassGenerator/ASClass.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01GameplayAbility)

#define ENSURE_ABILITY_IS_INSTANTIATED_OR_RETURN(FunctionName, ReturnValue)																				\
{																																						\
	if (!ensure(IsInstantiated()))																														\
	{																																					\
		ABILITY_LOG(Error, TEXT("%s: " #FunctionName " cannot be called on a non-instanced ability. Check the instancing policy."), *GetPathName());	\
		return ReturnValue;																																\
	}																																					\
}

UE_DEFINE_GAMEPLAY_TAG(TAG_ABILITY_SIMPLE_FAILURE_MESSAGE, "Ability.UserFacingSimpleActivateFail.Message");
UE_DEFINE_GAMEPLAY_TAG(TAG_ABILITY_PLAY_MONTAGE_FAILURE_MESSAGE, "A bility.PlayMontageOnActivateFail.Message");

UDJ01GameplayAbility::UDJ01GameplayAbility(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
	ReplicationPolicy = EGameplayAbilityReplicationPolicy::ReplicateNo;
	InstancingPolicy = EGameplayAbilityInstancingPolicy::InstancedPerActor;
	NetExecutionPolicy = EGameplayAbilityNetExecutionPolicy::LocalPredicted;
	NetSecurityPolicy = EGameplayAbilityNetSecurityPolicy::ClientOrServer;

	ActivationPolicy = EDJ01AbilityActivationPolicy::OnInputTriggered;
	ActivationGroup = EDJ01AbilityActivationGroup::Independent;

	bLogCancelation = false;

	ActiveCameraMode = nullptr;

	// AngelScript 集成：检测 AS 类是否覆盖了 K2_ 开头的蓝图事件
	// 这段逻辑来自 UAngelscriptGASAbility，确保 AS 能力能够正确激活
	auto ImplementedInAS = [](const UFunction* Func) -> bool {
		return Func && ensure(Func->GetOuter()) && Func->GetOuter()->IsA(UASClass::StaticClass());
	};

	if (!bHasBlueprintShouldAbilityRespondToEvent)
	{		
		static FName FuncName = FName(TEXT("K2_ShouldAbilityRespondToEvent"));
		UFunction* ShouldRespondFunction = GetClass()->FindFunctionByName(FuncName);
		bHasBlueprintShouldAbilityRespondToEvent = ImplementedInAS(ShouldRespondFunction);
	}

	if (!bHasBlueprintCanUse)
	{
		static FName FuncName = FName(TEXT("K2_CanActivateAbility"));
		UFunction* CanActivateFunction = GetClass()->FindFunctionByName(FuncName);
		bHasBlueprintCanUse = ImplementedInAS(CanActivateFunction);
	}

	if (!bHasBlueprintActivate)
	{
		static FName FuncName = FName(TEXT("K2_ActivateAbility"));
		UFunction* ActivateFunction = GetClass()->FindFunctionByName(FuncName);
		// 与 UAngelscriptGASAbility 相同的安全检查
		if (ActivateFunction && (HasAnyFlags(RF_ClassDefaultObject) || ActivateFunction->IsValidLowLevelFast()))
		{
			bHasBlueprintActivate = ImplementedInAS(ActivateFunction);
		}
	}

	if (!bHasBlueprintActivateFromEvent)
	{
		static FName FuncName = FName(TEXT("K2_ActivateAbilityFromEvent"));
		UFunction* ActivateFunction = GetClass()->FindFunctionByName(FuncName);
		bHasBlueprintActivateFromEvent = ImplementedInAS(ActivateFunction);
	}
}

UDJ01AbilitySystemComponent* UDJ01GameplayAbility::GetDJ01AbilitySystemComponentFromActorInfo() const
{
	return (CurrentActorInfo ? Cast<UDJ01AbilitySystemComponent>(CurrentActorInfo->AbilitySystemComponent.Get()) : nullptr);
}

ADJ01PlayerController* UDJ01GameplayAbility::GetDJ01PlayerControllerFromActorInfo() const
{
	return (CurrentActorInfo ? Cast<ADJ01PlayerController>(CurrentActorInfo->PlayerController.Get()) : nullptr);
}

AController* UDJ01GameplayAbility::GetControllerFromActorInfo() const
{
	if (CurrentActorInfo)
	{
		if (AController* PC = CurrentActorInfo->PlayerController.Get())
		{
			return PC;
		}

		// Look for a player controller or pawn in the owner chain.
		AActor* TestActor = CurrentActorInfo->OwnerActor.Get();
		while (TestActor)
		{
			if (AController* C = Cast<AController>(TestActor))
			{
				return C;
			}

			if (APawn* Pawn = Cast<APawn>(TestActor))
			{
				return Pawn->GetController();
			}

			TestActor = TestActor->GetOwner();
		}
	}

	return nullptr;
}

ADJ01Character* UDJ01GameplayAbility::GetDJ01CharacterFromActorInfo() const
{
	return (CurrentActorInfo ? Cast<ADJ01Character>(CurrentActorInfo->AvatarActor.Get()) : nullptr);
}

UDJ01HeroComponent* UDJ01GameplayAbility::GetHeroComponentFromActorInfo() const
{
	return (CurrentActorInfo ? UDJ01HeroComponent::FindHeroComponent(CurrentActorInfo->AvatarActor.Get()) : nullptr);
}

void UDJ01GameplayAbility::NativeOnAbilityFailedToActivate(const FGameplayTagContainer& FailedReason) const
{
	bool bSimpleFailureFound = false;
	for (FGameplayTag Reason : FailedReason)
	{
		if (!bSimpleFailureFound)
		{
			if (const FText* pUserFacingMessage = FailureTagToUserFacingMessages.Find(Reason))
			{
				FDJ01AbilitySimpleFailureMessage Message;
				Message.PlayerController = GetActorInfo().PlayerController.Get();
				Message.FailureTags = FailedReason;
				Message.UserFacingReason = *pUserFacingMessage;

				UGameplayMessageSubsystem& MessageSystem = UGameplayMessageSubsystem::Get(GetWorld());
				MessageSystem.BroadcastMessage(TAG_ABILITY_SIMPLE_FAILURE_MESSAGE, Message);
				bSimpleFailureFound = true;
			}
		}
		
		if (UAnimMontage* pMontage = FailureTagToAnimMontage.FindRef(Reason))
		{
			FDJ01AbilityMontageFailureMessage Message;
			Message.PlayerController = GetActorInfo().PlayerController.Get();
			Message.FailureTags = FailedReason;
			Message.FailureMontage = pMontage;

			UGameplayMessageSubsystem& MessageSystem = UGameplayMessageSubsystem::Get(GetWorld());
			MessageSystem.BroadcastMessage(TAG_ABILITY_PLAY_MONTAGE_FAILURE_MESSAGE, Message);
		}
	}
}

bool UDJ01GameplayAbility::CanActivateAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, const FGameplayTagContainer* SourceTags, const FGameplayTagContainer* TargetTags, FGameplayTagContainer* OptionalRelevantTags) const
{
	if (!ActorInfo || !ActorInfo->AbilitySystemComponent.IsValid())
	{
		return false;
	}

	if (!Super::CanActivateAbility(Handle, ActorInfo, SourceTags, TargetTags, OptionalRelevantTags))
	{
		return false;
	}

	//@TODO Possibly remove after setting up tag relationships
	UDJ01AbilitySystemComponent* DJ01ASC = CastChecked<UDJ01AbilitySystemComponent>(ActorInfo->AbilitySystemComponent.Get());
	
	// 调试日志
	const bool bIsBlocked = DJ01ASC->IsActivationGroupBlocked(ActivationGroup);
	UE_LOG(LogTemp, Warning, TEXT("[GAS] CanActivateAbility - %s, ActivationGroup: %d, IsBlocked: %s"), 
		*GetName(), (int32)ActivationGroup, bIsBlocked ? TEXT("YES") : TEXT("NO"));
	
	if (bIsBlocked)
	{
		UE_LOG(LogTemp, Warning, TEXT("[GAS] CanActivateAbility - %s BLOCKED!"), *GetName());
		if (OptionalRelevantTags)
		{
			OptionalRelevantTags->AddTag(DJ01GameplayTags::Ability_ActivateFail_ActivationGroup);
		}
		return false;
	}

	return true;
}

void UDJ01GameplayAbility::SetCanBeCanceled(bool bCanBeCanceled)
{
	// The ability can not block canceling if it's replaceable.
	if (!bCanBeCanceled && (ActivationGroup == EDJ01AbilityActivationGroup::Exclusive_Replaceable))
	{
		UE_LOG(LogDJ01AbilitySystem, Error, TEXT("SetCanBeCanceled: Ability [%s] can not block canceling because its activation group is replaceable."), *GetName());
		return;
	}

	Super::SetCanBeCanceled(bCanBeCanceled);
}

void UDJ01GameplayAbility::OnGiveAbility(const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilitySpec& Spec)
{
	Super::OnGiveAbility(ActorInfo, Spec);

	K2_OnAbilityAdded();

	TryActivateAbilityOnSpawn(ActorInfo, Spec);
}

void UDJ01GameplayAbility::OnRemoveAbility(const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilitySpec& Spec)
{
	K2_OnAbilityRemoved();

	Super::OnRemoveAbility(ActorInfo, Spec);
}

void UDJ01GameplayAbility::ActivateAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilityActivationInfo ActivationInfo, const FGameplayEventData* TriggerEventData)
{
	Super::ActivateAbility(Handle, ActorInfo, ActivationInfo, TriggerEventData);

	// ========== 启动阶段状态机 ==========
	if (bUsePhaseStateMachine)
	{
		CreatePhaseStateMachine();
		
		if (PhaseStateMachine)
		{
			PhaseStateMachine->Start();
		}
	}
}

void UDJ01GameplayAbility::EndAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilityActivationInfo ActivationInfo, bool bReplicateEndAbility, bool bWasCancelled)
{
	// ========== 清理阶段状态机 ==========
	if (PhaseStateMachine)
	{
		// 如果尚未结束，触发结束阶段
		EDJ01AbilityPhase CurrentPhase = PhaseStateMachine->GetCurrentPhase();
		if (CurrentPhase != EDJ01AbilityPhase::Ended && CurrentPhase != EDJ01AbilityPhase::None)
		{
			PhaseStateMachine->TransitionToPhase(EDJ01AbilityPhase::Ended, true);
		}
		
		PhaseStateMachine->Shutdown();
		PhaseStateMachine = nullptr;
	}

	ClearCameraMode();

	Super::EndAbility(Handle, ActorInfo, ActivationInfo, bReplicateEndAbility, bWasCancelled);
}

bool UDJ01GameplayAbility::CheckCost(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, OUT FGameplayTagContainer* OptionalRelevantTags) const
{
	if (!Super::CheckCost(Handle, ActorInfo, OptionalRelevantTags) || !ActorInfo)
	{
		return false;
	}

	// Verify we can afford any additional costs
	for (const TObjectPtr<UDJ01AbilityCost>& AdditionalCost : AdditionalCosts)
	{
		if (AdditionalCost != nullptr)
		{
			if (!AdditionalCost->CheckCost(this, Handle, ActorInfo, /*inout*/ OptionalRelevantTags))
			{
				return false;
			}
		}
	}

	return true;
}

void UDJ01GameplayAbility::ApplyCost(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilityActivationInfo ActivationInfo) const
{
	Super::ApplyCost(Handle, ActorInfo, ActivationInfo);

	check(ActorInfo);

	// 效果触发现在由阶段状态机管理（OnPhaseEnter）

	// Used to determine if the ability actually hit a target (as some costs are only spent on successful attempts)
	auto DetermineIfAbilityHitTarget = [&]()
	{
		if (ActorInfo->IsNetAuthority())
		{
			if (UDJ01AbilitySystemComponent* ASC = Cast<UDJ01AbilitySystemComponent>(ActorInfo->AbilitySystemComponent.Get()))
			{
				FGameplayAbilityTargetDataHandle TargetData;
				ASC->GetAbilityTargetData(Handle, ActivationInfo, TargetData);
				for (int32 TargetDataIdx = 0; TargetDataIdx < TargetData.Data.Num(); ++TargetDataIdx)
				{
					if (UAbilitySystemBlueprintLibrary::TargetDataHasHitResult(TargetData, TargetDataIdx))
					{
						return true;
					}
				}
			}
		}

		return false;
	};

	// Pay any additional costs
	bool bAbilityHitTarget = false;
	bool bHasDeterminedIfAbilityHitTarget = false;
	for (const TObjectPtr<UDJ01AbilityCost>& AdditionalCost : AdditionalCosts)
	{
		if (AdditionalCost != nullptr)
		{
			if (AdditionalCost->ShouldOnlyApplyCostOnHit())
			{
				if (!bHasDeterminedIfAbilityHitTarget)
				{
					bAbilityHitTarget = DetermineIfAbilityHitTarget();
					bHasDeterminedIfAbilityHitTarget = true;
				}

				if (!bAbilityHitTarget)
				{
					continue;
				}
			}

			AdditionalCost->ApplyCost(this, Handle, ActorInfo, ActivationInfo);
		}
	}
}

FGameplayEffectContextHandle UDJ01GameplayAbility::MakeEffectContext(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo) const
{
	FGameplayEffectContextHandle ContextHandle = Super::MakeEffectContext(Handle, ActorInfo);

	FDJ01GameplayEffectContext* EffectContext = FDJ01GameplayEffectContext::ExtractEffectContext(ContextHandle);
	check(EffectContext);

	check(ActorInfo);

	AActor* EffectCauser = nullptr;
	const IDJ01AbilitySourceInterface* AbilitySource = nullptr;
	float SourceLevel = 0.0f;
	GetAbilitySource(Handle, ActorInfo, /*out*/ SourceLevel, /*out*/ AbilitySource, /*out*/ EffectCauser);

	UObject* SourceObject = GetSourceObject(Handle, ActorInfo);

	AActor* Instigator = ActorInfo ? ActorInfo->OwnerActor.Get() : nullptr;

	EffectContext->SetAbilitySource(AbilitySource, SourceLevel);
	EffectContext->AddInstigator(Instigator, EffectCauser);
	EffectContext->AddSourceObject(SourceObject);

	return ContextHandle;
}

void UDJ01GameplayAbility::ApplyAbilityTagsToGameplayEffectSpec(FGameplayEffectSpec& Spec, FGameplayAbilitySpec* AbilitySpec) const
{
	Super::ApplyAbilityTagsToGameplayEffectSpec(Spec, AbilitySpec);

	if (const FHitResult* HitResult = Spec.GetContext().GetHitResult())
	{
		if (const UPhysicalMaterialWithTags* PhysMatWithTags = Cast<const UPhysicalMaterialWithTags>(HitResult->PhysMaterial.Get()))
		{
			Spec.CapturedTargetTags.GetSpecTags().AppendTags(PhysMatWithTags->Tags);
		}
	}
}

bool UDJ01GameplayAbility::DoesAbilitySatisfyTagRequirements(const UAbilitySystemComponent& AbilitySystemComponent, const FGameplayTagContainer* SourceTags, const FGameplayTagContainer* TargetTags, OUT FGameplayTagContainer* OptionalRelevantTags) const
{
	// Specialized version to handle death exclusion and AbilityTags expansion via ASC

	bool bBlocked = false;
	bool bMissing = false;

	UAbilitySystemGlobals& AbilitySystemGlobals = UAbilitySystemGlobals::Get();
	const FGameplayTag& BlockedTag = AbilitySystemGlobals.ActivateFailTagsBlockedTag;
	const FGameplayTag& MissingTag = AbilitySystemGlobals.ActivateFailTagsMissingTag;

	// Check if any of this ability's tags are currently blocked
	if (AbilitySystemComponent.AreAbilityTagsBlocked(AbilityTags))
	{
		bBlocked = true;
	}

	const UDJ01AbilitySystemComponent* DJ01ASC = Cast<UDJ01AbilitySystemComponent>(&AbilitySystemComponent);
	static FGameplayTagContainer AllRequiredTags;
	static FGameplayTagContainer AllBlockedTags;

	AllRequiredTags = ActivationRequiredTags;
	AllBlockedTags = ActivationBlockedTags;

	// Expand our ability tags to add additional required/blocked tags
	if (DJ01ASC)
	{
		DJ01ASC->GetAdditionalActivationTagRequirements(AbilityTags, AllRequiredTags, AllBlockedTags);
	}

	// Check to see the required/blocked tags for this ability
	if (AllBlockedTags.Num() || AllRequiredTags.Num())
	{
		static FGameplayTagContainer AbilitySystemComponentTags;
		
		AbilitySystemComponentTags.Reset();
		AbilitySystemComponent.GetOwnedGameplayTags(AbilitySystemComponentTags);

		if (AbilitySystemComponentTags.HasAny(AllBlockedTags))
		{
			if (OptionalRelevantTags && AbilitySystemComponentTags.HasTag(DJ01GameplayTags::Status_Death))
			{
				// If player is dead and was rejected due to blocking tags, give that feedback
				OptionalRelevantTags->AddTag(DJ01GameplayTags::Ability_ActivateFail_IsDead);
			}

			bBlocked = true;
		}

		if (!AbilitySystemComponentTags.HasAll(AllRequiredTags))
		{
			bMissing = true;
		}
	}

	if (SourceTags != nullptr)
	{
		if (SourceBlockedTags.Num() || SourceRequiredTags.Num())
		{
			if (SourceTags->HasAny(SourceBlockedTags))
			{
				bBlocked = true;
			}

			if (!SourceTags->HasAll(SourceRequiredTags))
			{
				bMissing = true;
			}
		}
	}

	if (TargetTags != nullptr)
	{
		if (TargetBlockedTags.Num() || TargetRequiredTags.Num())
		{
			if (TargetTags->HasAny(TargetBlockedTags))
			{
				bBlocked = true;
			}

			if (!TargetTags->HasAll(TargetRequiredTags))
			{
				bMissing = true;
			}
		}
	}

	if (bBlocked)
	{
		if (OptionalRelevantTags && BlockedTag.IsValid())
		{
			OptionalRelevantTags->AddTag(BlockedTag);
		}
		return false;
	}
	if (bMissing)
	{
		if (OptionalRelevantTags && MissingTag.IsValid())
		{
			OptionalRelevantTags->AddTag(MissingTag);
		}
		return false;
	}

	return true;
}

void UDJ01GameplayAbility::OnPawnAvatarSet()
{
	K2_OnPawnAvatarSet();
}

void UDJ01GameplayAbility::GetAbilitySource(FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, float& OutSourceLevel, const IDJ01AbilitySourceInterface*& OutAbilitySource, AActor*& OutEffectCauser) const
{
	OutSourceLevel = 0.0f;
	OutAbilitySource = nullptr;
	OutEffectCauser = nullptr;

	OutEffectCauser = ActorInfo->AvatarActor.Get();

	// If we were added by something that's an ability info source, use it
	UObject* SourceObject = GetSourceObject(Handle, ActorInfo);

	OutAbilitySource = Cast<IDJ01AbilitySourceInterface>(SourceObject);
}

void UDJ01GameplayAbility::TryActivateAbilityOnSpawn(const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilitySpec& Spec) const
{
	const bool bIsPredicting = (Spec.ActivationInfo.ActivationMode == EGameplayAbilityActivationMode::Predicting);

	// Try to activate if activation policy is on spawn.
	if (ActorInfo && !Spec.IsActive() && !bIsPredicting && (ActivationPolicy == EDJ01AbilityActivationPolicy::OnSpawn))
	{
		UAbilitySystemComponent* ASC = ActorInfo->AbilitySystemComponent.Get();
		const AActor* AvatarActor = ActorInfo->AvatarActor.Get();

		// If avatar actor is torn off or about to die, don't try to activate until we get the new one.
		if (ASC && AvatarActor && !AvatarActor->GetTearOff() && (AvatarActor->GetLifeSpan() <= 0.0f))
		{
			const bool bIsLocalExecution = (NetExecutionPolicy == EGameplayAbilityNetExecutionPolicy::LocalPredicted) || (NetExecutionPolicy == EGameplayAbilityNetExecutionPolicy::LocalOnly);
			const bool bIsServerExecution = (NetExecutionPolicy == EGameplayAbilityNetExecutionPolicy::ServerOnly) || (NetExecutionPolicy == EGameplayAbilityNetExecutionPolicy::ServerInitiated);

			const bool bClientShouldActivate = ActorInfo->IsLocallyControlled() && bIsLocalExecution;
			const bool bServerShouldActivate = ActorInfo->IsNetAuthority() && bIsServerExecution;

			if (bClientShouldActivate || bServerShouldActivate)
			{
				ASC->TryActivateAbility(Spec.Handle);
			}
		}
	}
}

bool UDJ01GameplayAbility::CanChangeActivationGroup(EDJ01AbilityActivationGroup NewGroup) const
{
	if (!IsInstantiated() || !IsActive())
	{
		return false;
	}

	if (ActivationGroup == NewGroup)
	{
		return true;
	}

	UDJ01AbilitySystemComponent* DJ01ASC = GetDJ01AbilitySystemComponentFromActorInfo();
	check(DJ01ASC);

	if ((ActivationGroup != EDJ01AbilityActivationGroup::Exclusive_Blocking) && DJ01ASC->IsActivationGroupBlocked(NewGroup))
	{
		// This ability can't change groups if it's blocked (unless it is the one doing the blocking).
		return false;
	}

	if ((NewGroup == EDJ01AbilityActivationGroup::Exclusive_Replaceable) && !CanBeCanceled())
	{
		// This ability can't become replaceable if it can't be canceled.
		return false;
	}

	return true;
}

bool UDJ01GameplayAbility::ChangeActivationGroup(EDJ01AbilityActivationGroup NewGroup)
{
	ENSURE_ABILITY_IS_INSTANTIATED_OR_RETURN(ChangeActivationGroup, false);

	if (!CanChangeActivationGroup(NewGroup))
	{
		return false;
	}

	if (ActivationGroup != NewGroup)
	{
		UDJ01AbilitySystemComponent* DJ01ASC = GetDJ01AbilitySystemComponentFromActorInfo();
		check(DJ01ASC);

		DJ01ASC->RemoveAbilityFromActivationGroup(ActivationGroup, this);
		DJ01ASC->AddAbilityToActivationGroup(NewGroup, this);

		ActivationGroup = NewGroup;
	}

	return true;
}

void UDJ01GameplayAbility::SetCameraMode(TSubclassOf<UDJ01CameraMode> CameraMode)
{
	ENSURE_ABILITY_IS_INSTANTIATED_OR_RETURN(SetCameraMode, );

	if (UDJ01HeroComponent* HeroComponent = GetHeroComponentFromActorInfo())
	{
		HeroComponent->SetAbilityCameraMode(CameraMode, CurrentSpecHandle);
		ActiveCameraMode = CameraMode;
	}
}

void UDJ01GameplayAbility::ClearCameraMode()
{
	ENSURE_ABILITY_IS_INSTANTIATED_OR_RETURN(ClearCameraMode, );

	if (ActiveCameraMode)
	{
		if (UDJ01HeroComponent* HeroComponent = GetHeroComponentFromActorInfo())
		{
			HeroComponent->ClearAbilityCameraMode(CurrentSpecHandle);
		}

		ActiveCameraMode = nullptr;
	}
}

// ========== 阶段状态机实现 ==========

void UDJ01GameplayAbility::CreatePhaseStateMachine()
{
	// 如果已经存在，先清理
	if (PhaseStateMachine)
	{
		PhaseStateMachine->Shutdown();
		PhaseStateMachine = nullptr;
	}

	// 创建状态机实例
	PhaseStateMachine = NewObject<UDJ01AbilityPhaseStateMachine>(this);
	PhaseStateMachine->Initialize(this, PhaseConfig);

	// 绑定委托
	PhaseStateMachine->OnPhaseEnter.AddDynamic(this, &UDJ01GameplayAbility::HandleStateMachinePhaseEnter);
	PhaseStateMachine->OnPhaseExit.AddDynamic(this, &UDJ01GameplayAbility::HandleStateMachinePhaseExit);
	PhaseStateMachine->OnFinished.AddDynamic(this, &UDJ01GameplayAbility::HandleStateMachineFinished);

	UE_LOG(LogDJ01AbilitySystem, Verbose, 
		TEXT("Ability [%s]: Created phase state machine"), *GetName());
}

EDJ01AbilityPhase UDJ01GameplayAbility::GetCurrentPhase() const
{
	if (PhaseStateMachine)
	{
		return PhaseStateMachine->GetCurrentPhase();
	}
	return EDJ01AbilityPhase::None;
}

bool UDJ01GameplayAbility::TransitionToPhase(EDJ01AbilityPhase NewPhase, bool bForce)
{
	if (!PhaseStateMachine)
	{
		UE_LOG(LogDJ01AbilitySystem, Warning, 
			TEXT("Ability [%s]: Cannot transition phase - state machine not created"), *GetName());
		return false;
	}

	return PhaseStateMachine->TransitionToPhase(NewPhase, bForce);
}

bool UDJ01GameplayAbility::CanCurrentPhaseBeInterrupted() const
{
	if (PhaseStateMachine)
	{
		return PhaseStateMachine->CanCurrentPhaseBeInterrupted();
	}
	return true; // 默认可打断
}

bool UDJ01GameplayAbility::CanCurrentPhaseCancelInto() const
{
	if (PhaseStateMachine)
	{
		return PhaseStateMachine->CanCurrentPhaseCancelInto();
	}
	return false; // 默认不可取消到其他技能
}

void UDJ01GameplayAbility::SkipCurrentPhase()
{
	if (PhaseStateMachine)
	{
		PhaseStateMachine->SkipCurrentPhase();
	}
}

float UDJ01GameplayAbility::GetCurrentPhaseRemainingTime() const
{
	if (PhaseStateMachine)
	{
		return PhaseStateMachine->GetCurrentPhaseRemainingTime();
	}
	return 0.0f;
}

void UDJ01GameplayAbility::HandleStateMachinePhaseEnter(EDJ01AbilityPhase Phase)
{
	// 自动播放阶段对应的 Montage
	const FDJ01AbilityPhaseInfo* PhaseInfo = PhaseConfig.GetPhaseInfo(Phase);
	if (PhaseInfo && PhaseInfo->HasMontage())
	{
		PlayPhaseMontage(*PhaseInfo);
	}

	// 调用可重写的蓝图事件
	OnPhaseEnter(Phase);
}

void UDJ01GameplayAbility::PlayPhaseMontage(const FDJ01AbilityPhaseInfo& PhaseInfo)
{
	if (!PhaseInfo.Montage)
	{
		return;
	}

	// 获取角色
	ADJ01Character* Character = GetDJ01CharacterFromActorInfo();
	if (!Character)
	{
		UE_LOG(LogDJ01AbilitySystem, Warning, 
			TEXT("Ability [%s]: Cannot play phase montage - no character"), *GetName());
		return;
	}

	// 获取 Mesh 和 AnimInstance
	USkeletalMeshComponent* MeshComp = Character->GetMesh();
	if (!MeshComp)
	{
		return;
	}

	UAnimInstance* AnimInstance = MeshComp->GetAnimInstance();
	if (!AnimInstance)
	{
		return;
	}

	// 播放 Montage
	const float PlayRate = FMath::Max(PhaseInfo.MontagePlayRate, 0.1f);
	AnimInstance->Montage_Play(PhaseInfo.Montage, PlayRate);

	// 如果指定了起始 Section，跳转到该 Section
	if (PhaseInfo.MontageStartSection != NAME_None)
	{
		AnimInstance->Montage_JumpToSection(PhaseInfo.MontageStartSection, PhaseInfo.Montage);
	}

	UE_LOG(LogDJ01AbilitySystem, Verbose, 
		TEXT("Ability [%s]: Playing phase montage [%s] at rate %.2f"), 
		*GetName(), *PhaseInfo.Montage->GetName(), PlayRate);
}

void UDJ01GameplayAbility::HandleStateMachinePhaseExit(EDJ01AbilityPhase Phase)
{
	// 调用可重写的蓝图事件
	OnPhaseExit(Phase);
}

void UDJ01GameplayAbility::HandleStateMachineFinished()
{
	// 状态机完成，结束技能
	UE_LOG(LogDJ01AbilitySystem, Verbose, 
		TEXT("Ability [%s]: Phase state machine finished, ending ability"), *GetName());
	
	K2_EndAbility();
}

void UDJ01GameplayAbility::OnPhaseEnter_Implementation(EDJ01AbilityPhase Phase)
{
	UE_LOG(LogDJ01AbilitySystem, Verbose, 
		TEXT("Ability [%s]: Entered phase %s"), *GetName(), *GetAbilityPhaseName(Phase));

	// ========== 触发对应阶段的 Effects ==========
	EDJ01EffectPhase EffectPhase = MapPhaseToEffectPhase(Phase);
	// OnAnimEvent 由动画事件触发, Manual 由代码手动触发
	if (EffectPhase != EDJ01EffectPhase::OnAnimEvent && EffectPhase != EDJ01EffectPhase::Manual)
	{
		TriggerEffects(EffectPhase, TArray<AActor*>());
	}
}

void UDJ01GameplayAbility::OnPhaseExit_Implementation(EDJ01AbilityPhase Phase)
{
	UE_LOG(LogDJ01AbilitySystem, Verbose, 
		TEXT("Ability [%s]: Exited phase %s"), *GetName(), *GetAbilityPhaseName(Phase));
	
	// Tag 管理已由状态机处理，此处无需额外逻辑
}

EDJ01EffectPhase UDJ01GameplayAbility::MapPhaseToEffectPhase(EDJ01AbilityPhase Phase) const
{
	switch (Phase)
	{
	case EDJ01AbilityPhase::Startup:
		return EDJ01EffectPhase::OnActivate; // 前摇触发 OnActivate 效果
	case EDJ01AbilityPhase::Active:
		return EDJ01EffectPhase::OnCommit;   // 激活阶段触发 OnCommit 效果
	case EDJ01AbilityPhase::Ended:
		return EDJ01EffectPhase::OnEnd;      // 仅结束阶段触发 OnEnd 效果
	case EDJ01AbilityPhase::Recovery:
	default:
		return EDJ01EffectPhase::Manual;     // Recovery 和其他阶段不自动触发
	}
}

// ========== 效果系统实现 ==========

void UDJ01GameplayAbility::TriggerEffects(EDJ01EffectPhase Phase, const TArray<AActor*>& Targets)
{
	TriggerEffectsInternal(Phase, FGameplayTag(), Targets);
}

void UDJ01GameplayAbility::TriggerEffectsByEvent(FGameplayTag EventTag, const TArray<AActor*>& Targets)
{
	TriggerEffectsInternal(EDJ01EffectPhase::OnAnimEvent, EventTag, Targets);
}

void UDJ01GameplayAbility::TriggerEffectsInternal(EDJ01EffectPhase Phase, const FGameplayTag& EventTag, const TArray<AActor*>& Targets)
{
	if (Effects.Num() == 0)
	{
		return;
	}

	// 构建执行上下文
	FDJ01EffectContext Context = BuildEffectContext(Targets);
	Context.EventTag = EventTag;

	// 遍历所有效果条目，触发匹配的效果
	for (const FDJ01AbilityEffectEntry& Entry : Effects)
	{
		if (Entry.ShouldTrigger(Phase, EventTag))
		{
			if (Entry.Effect)
			{
				Entry.Effect->Execute(Context);
			}
		}
	}
}

FDJ01EffectContext UDJ01GameplayAbility::BuildEffectContext(const TArray<AActor*>& Targets) const
{
	FDJ01EffectContext Context;

	// 设置施法者 ASC
	if (CurrentActorInfo && CurrentActorInfo->AbilitySystemComponent.IsValid())
	{
		Context.InstigatorASC = CurrentActorInfo->AbilitySystemComponent.Get();
	}

	// 设置技能等级
	Context.AbilityLevel = GetAbilityLevel();

	// 设置技能实例
	Context.SourceAbility = const_cast<UDJ01GameplayAbility*>(this);

	// 收集目标 ASC
	for (AActor* TargetActor : Targets)
	{
		if (TargetActor)
		{
			if (UAbilitySystemComponent* TargetASC = UAbilitySystemBlueprintLibrary::GetAbilitySystemComponent(TargetActor))
			{
				Context.TargetASCs.Add(TargetASC);
			}
		}
	}

	return Context;
}