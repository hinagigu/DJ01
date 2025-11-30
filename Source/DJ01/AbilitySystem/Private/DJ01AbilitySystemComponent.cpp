// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"

#include "DJ01/AbilitySystem/Abilities/Public/DJ01GameplayAbility.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilityTagRelationshipMapping.h"
#include "DJ01/Animation/DJ01AnimInstance.h"
#include "Engine/World.h"
#include "GameFramework/Pawn.h"
#include "DJ01/AbilitySystem/Public/DJ01GlobalAbilitySystem.h"
#include "DJ01/System/Public/DJ01LogChannels.h"
#include "DJ01/System/Public/DJ01AssetManager.h"
#include "DJ01/System/Public/DJ01GameData.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01AbilitySystemComponent)

UE_DEFINE_GAMEPLAY_TAG(TAG_Gameplay_AbilityInputBlocked, "Gameplay.AbilityInputBlocked");

UDJ01AbilitySystemComponent::UDJ01AbilitySystemComponent(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
	InputPressedSpecHandles.Reset();
	InputReleasedSpecHandles.Reset();
	InputHeldSpecHandles.Reset();

	FMemory::Memset(ActivationGroupCounts, 0, sizeof(ActivationGroupCounts));
}

void UDJ01AbilitySystemComponent::EndPlay(const EEndPlayReason::Type EndPlayReason)
{
	if (UDJ01GlobalAbilitySystem* GlobalAbilitySystem = UWorld::GetSubsystem<UDJ01GlobalAbilitySystem>(GetWorld()))
	{
		GlobalAbilitySystem->UnregisterASC(this);
	}

	Super::EndPlay(EndPlayReason);
}

void UDJ01AbilitySystemComponent::InitAbilityActorInfo(AActor* InOwnerActor, AActor* InAvatarActor)
{
	FGameplayAbilityActorInfo* ActorInfo = AbilityActorInfo.Get();
	check(ActorInfo);
	check(InOwnerActor);

	const bool bHasNewPawnAvatar = Cast<APawn>(InAvatarActor) && (InAvatarActor != ActorInfo->AvatarActor);

	Super::InitAbilityActorInfo(InOwnerActor, InAvatarActor);

	if (bHasNewPawnAvatar)
	{
		// Notify all abilities that a new pawn avatar has been set
		for (const FGameplayAbilitySpec& AbilitySpec : ActivatableAbilities.Items)
		{
			UDJ01GameplayAbility* DJ01AbilityCDO = Cast<UDJ01GameplayAbility>(AbilitySpec.Ability);
			if (!DJ01AbilityCDO)
			{
				continue;
			}

			if (DJ01AbilityCDO->GetInstancingPolicy() != EGameplayAbilityInstancingPolicy::NonInstanced)
			{
				TArray<UGameplayAbility*> Instances = AbilitySpec.GetAbilityInstances();
				for (UGameplayAbility* AbilityInstance : Instances)
				{
					UDJ01GameplayAbility* DJ01AbilityInstance = Cast<UDJ01GameplayAbility>(AbilityInstance);
					if (DJ01AbilityInstance)
					{
						// Ability instances may be missing for replays
						DJ01AbilityInstance->OnPawnAvatarSet();
					}
				}
			}
			else
			{
				DJ01AbilityCDO->OnPawnAvatarSet();
			}
		}

		// Register with the global system once we actually have a pawn avatar. We wait until this time since some globally-applied effects may require an avatar.
		if (UDJ01GlobalAbilitySystem* GlobalAbilitySystem = UWorld::GetSubsystem<UDJ01GlobalAbilitySystem>(GetWorld()))
		{
			GlobalAbilitySystem->RegisterASC(this);
		}

		if (UDJ01AnimInstance* DJ01AnimInst = Cast<UDJ01AnimInstance>(ActorInfo->GetAnimInstance()))
		{
			DJ01AnimInst->InitializeWithAbilitySystem(this);
		}

		TryActivateAbilitiesOnSpawn();
	}
}

void UDJ01AbilitySystemComponent::TryActivateAbilitiesOnSpawn()
{
	ABILITYLIST_SCOPE_LOCK();
	for (const FGameplayAbilitySpec& AbilitySpec : ActivatableAbilities.Items)
	{
		if (const UDJ01GameplayAbility* DJ01AbilityCDO = Cast<UDJ01GameplayAbility>(AbilitySpec.Ability))
		{
			DJ01AbilityCDO->TryActivateAbilityOnSpawn(AbilityActorInfo.Get(), AbilitySpec);
		}
	}
}

void UDJ01AbilitySystemComponent::CancelAbilitiesByFunc(TShouldCancelAbilityFunc ShouldCancelFunc, bool bReplicateCancelAbility)
{
	ABILITYLIST_SCOPE_LOCK();
	for (const FGameplayAbilitySpec& AbilitySpec : ActivatableAbilities.Items)
	{
		if (!AbilitySpec.IsActive())
		{
			continue;
		}

		UDJ01GameplayAbility* DJ01AbilityCDO = Cast<UDJ01GameplayAbility>(AbilitySpec.Ability);
		if (!DJ01AbilityCDO)
		{
			UE_LOG(LogDJ01AbilitySystem, Error, TEXT("CancelAbilitiesByFunc: Non-DJ01GameplayAbility %s was Granted to ASC. Skipping."), *AbilitySpec.Ability.GetName());
			continue;
		}

		if (DJ01AbilityCDO->GetInstancingPolicy() != EGameplayAbilityInstancingPolicy::NonInstanced)
		{
			// Cancel all the spawned instances, not the CDO.
			TArray<UGameplayAbility*> Instances = AbilitySpec.GetAbilityInstances();
			for (UGameplayAbility* AbilityInstance : Instances)
			{
				UDJ01GameplayAbility* DJ01AbilityInstance = CastChecked<UDJ01GameplayAbility>(AbilityInstance);

				if (ShouldCancelFunc(DJ01AbilityInstance, AbilitySpec.Handle))
				{
					if (DJ01AbilityInstance->CanBeCanceled())
					{
						DJ01AbilityInstance->CancelAbility(AbilitySpec.Handle, AbilityActorInfo.Get(), DJ01AbilityInstance->GetCurrentActivationInfo(), bReplicateCancelAbility);
					}
					else
					{
						UE_LOG(LogDJ01AbilitySystem, Error, TEXT("CancelAbilitiesByFunc: Can't cancel ability [%s] because CanBeCanceled is false."), *DJ01AbilityInstance->GetName());
					}
				}
			}
		}
		else
		{
			// Cancel the non-instanced ability CDO.
			if (ShouldCancelFunc(DJ01AbilityCDO, AbilitySpec.Handle))
			{
				// Non-instanced abilities can always be canceled.
				check(DJ01AbilityCDO->CanBeCanceled());
				DJ01AbilityCDO->CancelAbility(AbilitySpec.Handle, AbilityActorInfo.Get(), FGameplayAbilityActivationInfo(), bReplicateCancelAbility);
			}
		}
	}
}

void UDJ01AbilitySystemComponent::CancelInputActivatedAbilities(bool bReplicateCancelAbility)
{
	auto ShouldCancelFunc = [this](const UDJ01GameplayAbility* DJ01Ability, FGameplayAbilitySpecHandle Handle)
	{
		const EDJ01AbilityActivationPolicy ActivationPolicy = DJ01Ability->GetActivationPolicy();
		return ((ActivationPolicy == EDJ01AbilityActivationPolicy::OnInputTriggered) || (ActivationPolicy == EDJ01AbilityActivationPolicy::WhileInputActive));
	};

	CancelAbilitiesByFunc(ShouldCancelFunc, bReplicateCancelAbility);
}

void UDJ01AbilitySystemComponent::AbilitySpecInputPressed(FGameplayAbilitySpec& Spec)
{
	Super::AbilitySpecInputPressed(Spec);

	// We don't support UGameplayAbility::bReplicateInputDirectly.
	// Use replicated events instead so that the WaitInputPress ability task works.
	if (Spec.IsActive())
	{
		// Invoke the InputPressed event. This is not replicated here. If someone is listening, they may replicate the InputPressed event to the server.
		InvokeReplicatedEvent(EAbilityGenericReplicatedEvent::InputPressed, Spec.Handle, Spec.ActivationInfo.GetActivationPredictionKey());
	}
}

void UDJ01AbilitySystemComponent::AbilitySpecInputReleased(FGameplayAbilitySpec& Spec)
{
	Super::AbilitySpecInputReleased(Spec);

	// We don't support UGameplayAbility::bReplicateInputDirectly.
	// Use replicated events instead so that the WaitInputRelease ability task works.
	if (Spec.IsActive())
	{
		// Invoke the InputReleased event. This is not replicated here. If someone is listening, they may replicate the InputReleased event to the server.
		InvokeReplicatedEvent(EAbilityGenericReplicatedEvent::InputReleased, Spec.Handle, Spec.ActivationInfo.GetActivationPredictionKey());
	}
}

void UDJ01AbilitySystemComponent::AbilityInputTagPressed(const FGameplayTag& InputTag)
{
	if (InputTag.IsValid())
	{
		for (const FGameplayAbilitySpec& AbilitySpec : ActivatableAbilities.Items)
		{
			if (AbilitySpec.Ability && (AbilitySpec.DynamicAbilityTags.HasTagExact(InputTag)))
			{
				InputPressedSpecHandles.AddUnique(AbilitySpec.Handle);
				InputHeldSpecHandles.AddUnique(AbilitySpec.Handle);
			}
		}
	}
}

void UDJ01AbilitySystemComponent::AbilityInputTagReleased(const FGameplayTag& InputTag)
{
	if (InputTag.IsValid())
	{
		for (const FGameplayAbilitySpec& AbilitySpec : ActivatableAbilities.Items)
		{
			if (AbilitySpec.Ability && (AbilitySpec.DynamicAbilityTags.HasTagExact(InputTag)))
			{
				InputReleasedSpecHandles.AddUnique(AbilitySpec.Handle);
				InputHeldSpecHandles.Remove(AbilitySpec.Handle);
			}
		}
	}
}

void UDJ01AbilitySystemComponent::ProcessAbilityInput(float DeltaTime, bool bGamePaused)
{
	if (HasMatchingGameplayTag(TAG_Gameplay_AbilityInputBlocked))
	{
		ClearAbilityInput();
		return;
	}

	static TArray<FGameplayAbilitySpecHandle> AbilitiesToActivate;
	AbilitiesToActivate.Reset();

	//@TODO: See if we can use FScopedServerAbilityRPCBatcher ScopedRPCBatcher in some of these loops

	//
	// Process all abilities that activate when the input is held.
	//
	for (const FGameplayAbilitySpecHandle& SpecHandle : InputHeldSpecHandles)
	{
		if (const FGameplayAbilitySpec* AbilitySpec = FindAbilitySpecFromHandle(SpecHandle))
		{
			if (AbilitySpec->Ability && !AbilitySpec->IsActive())
			{
				const UDJ01GameplayAbility* DJ01AbilityCDO = Cast<UDJ01GameplayAbility>(AbilitySpec->Ability);
				if (DJ01AbilityCDO && DJ01AbilityCDO->GetActivationPolicy() == EDJ01AbilityActivationPolicy::WhileInputActive)
				{
					AbilitiesToActivate.AddUnique(AbilitySpec->Handle);
				}
			}
		}
	}

	//
	// Process all abilities that had their input pressed this frame.
	//
	for (const FGameplayAbilitySpecHandle& SpecHandle : InputPressedSpecHandles)
	{
		if (FGameplayAbilitySpec* AbilitySpec = FindAbilitySpecFromHandle(SpecHandle))
		{
			if (AbilitySpec->Ability)
			{
				AbilitySpec->InputPressed = true;

				if (AbilitySpec->IsActive())
				{
					// Ability is active so pass along the input event.
					AbilitySpecInputPressed(*AbilitySpec);
				}
				else
				{
					const UDJ01GameplayAbility* DJ01AbilityCDO = Cast<UDJ01GameplayAbility>(AbilitySpec->Ability);

					if (DJ01AbilityCDO && DJ01AbilityCDO->GetActivationPolicy() == EDJ01AbilityActivationPolicy::OnInputTriggered)
					{
						AbilitiesToActivate.AddUnique(AbilitySpec->Handle);
					}
				}
			}
		}
	}

	//
	// Try to activate all the abilities that are from presses and holds.
	// We do it all at once so that held inputs don't activate the ability
	// and then also send a input event to the ability because of the press.
	//
	for (const FGameplayAbilitySpecHandle& AbilitySpecHandle : AbilitiesToActivate)
	{
		TryActivateAbility(AbilitySpecHandle);
	}

	//
	// Process all abilities that had their input released this frame.
	//
	for (const FGameplayAbilitySpecHandle& SpecHandle : InputReleasedSpecHandles)
	{
		if (FGameplayAbilitySpec* AbilitySpec = FindAbilitySpecFromHandle(SpecHandle))
		{
			if (AbilitySpec->Ability)
			{
				AbilitySpec->InputPressed = false;

				if (AbilitySpec->IsActive())
				{
					// Ability is active so pass along the input event.
					AbilitySpecInputReleased(*AbilitySpec);
				}
			}
		}
	}

	//
	// Clear the cached ability handles.
	//
	InputPressedSpecHandles.Reset();
	InputReleasedSpecHandles.Reset();
}

void UDJ01AbilitySystemComponent::ClearAbilityInput()
{
	InputPressedSpecHandles.Reset();
	InputReleasedSpecHandles.Reset();
	InputHeldSpecHandles.Reset();
}

void UDJ01AbilitySystemComponent::NotifyAbilityActivated(const FGameplayAbilitySpecHandle Handle, UGameplayAbility* Ability)
{
	Super::NotifyAbilityActivated(Handle, Ability);

	if (UDJ01GameplayAbility* DJ01Ability = Cast<UDJ01GameplayAbility>(Ability))
	{
		AddAbilityToActivationGroup(DJ01Ability->GetActivationGroup(), DJ01Ability);
	}
}

void UDJ01AbilitySystemComponent::NotifyAbilityFailed(const FGameplayAbilitySpecHandle Handle, UGameplayAbility* Ability, const FGameplayTagContainer& FailureReason)
{
	Super::NotifyAbilityFailed(Handle, Ability, FailureReason);

	if (APawn* Avatar = Cast<APawn>(GetAvatarActor()))
	{
		if (!Avatar->IsLocallyControlled() && Ability->IsSupportedForNetworking())
		{
			ClientNotifyAbilityFailed(Ability, FailureReason);
			return;
		}
	}

	HandleAbilityFailed(Ability, FailureReason);
}

void UDJ01AbilitySystemComponent::NotifyAbilityEnded(FGameplayAbilitySpecHandle Handle, UGameplayAbility* Ability, bool bWasCancelled)
{
	Super::NotifyAbilityEnded(Handle, Ability, bWasCancelled);

	if (UDJ01GameplayAbility* DJ01Ability = Cast<UDJ01GameplayAbility>(Ability))
	{
		RemoveAbilityFromActivationGroup(DJ01Ability->GetActivationGroup(), DJ01Ability);
	}
}

void UDJ01AbilitySystemComponent::ApplyAbilityBlockAndCancelTags(const FGameplayTagContainer& AbilityTags, UGameplayAbility* RequestingAbility, bool bEnableBlockTags, const FGameplayTagContainer& BlockTags, bool bExecuteCancelTags, const FGameplayTagContainer& CancelTags)
{
	FGameplayTagContainer ModifiedBlockTags = BlockTags;
	FGameplayTagContainer ModifiedCancelTags = CancelTags;

	if (TagRelationshipMapping)
	{
		// Use the mapping to expand the ability tags into block and cancel tag
		TagRelationshipMapping->GetAbilityTagsToBlockAndCancel(AbilityTags, &ModifiedBlockTags, &ModifiedCancelTags);
	}

	Super::ApplyAbilityBlockAndCancelTags(AbilityTags, RequestingAbility, bEnableBlockTags, ModifiedBlockTags, bExecuteCancelTags, ModifiedCancelTags);

	//@TODO: Apply any special logic like blocking input or movement
}

void UDJ01AbilitySystemComponent::HandleChangeAbilityCanBeCanceled(const FGameplayTagContainer& AbilityTags, UGameplayAbility* RequestingAbility, bool bCanBeCanceled)
{
	Super::HandleChangeAbilityCanBeCanceled(AbilityTags, RequestingAbility, bCanBeCanceled);

	//@TODO: Apply any special logic like blocking input or movement
}

void UDJ01AbilitySystemComponent::GetAdditionalActivationTagRequirements(const FGameplayTagContainer& AbilityTags, FGameplayTagContainer& OutActivationRequired, FGameplayTagContainer& OutActivationBlocked) const
{
	if (TagRelationshipMapping)
	{
		TagRelationshipMapping->GetRequiredAndBlockedActivationTags(AbilityTags, &OutActivationRequired, &OutActivationBlocked);
	}
}

void UDJ01AbilitySystemComponent::SetTagRelationshipMapping(UDJ01AbilityTagRelationshipMapping* NewMapping)
{
	TagRelationshipMapping = NewMapping;
}

void UDJ01AbilitySystemComponent::ClientNotifyAbilityFailed_Implementation(const UGameplayAbility* Ability, const FGameplayTagContainer& FailureReason)
{
	HandleAbilityFailed(Ability, FailureReason);
}

void UDJ01AbilitySystemComponent::HandleAbilityFailed(const UGameplayAbility* Ability, const FGameplayTagContainer& FailureReason)
{
	//UE_LOG(LogDJ01AbilitySystem, Warning, TEXT("Ability %s failed to activate (tags: %s)"), *GetPathNameSafe(Ability), *FailureReason.ToString());

	if (const UDJ01GameplayAbility* DJ01Ability = Cast<const UDJ01GameplayAbility>(Ability))
	{
		DJ01Ability->OnAbilityFailedToActivate(FailureReason);
	}	
}

bool UDJ01AbilitySystemComponent::IsActivationGroupBlocked(EDJ01AbilityActivationGroup Group) const
{
	bool bBlocked = false;

	switch (Group)
	{
	case EDJ01AbilityActivationGroup::Independent:
		// Independent abilities are never blocked.
		bBlocked = false;
		break;

	case EDJ01AbilityActivationGroup::Exclusive_Replaceable:
	case EDJ01AbilityActivationGroup::Exclusive_Blocking:
		// Exclusive abilities can activate if nothing is blocking.
		bBlocked = (ActivationGroupCounts[(uint8)EDJ01AbilityActivationGroup::Exclusive_Blocking] > 0);
		break;

	default:
		checkf(false, TEXT("IsActivationGroupBlocked: Invalid ActivationGroup [%d]\n"), (uint8)Group);
		break;
	}

	return bBlocked;
}

void UDJ01AbilitySystemComponent::AddAbilityToActivationGroup(EDJ01AbilityActivationGroup Group, UDJ01GameplayAbility* DJ01Ability)
{
	check(DJ01Ability);
	check(ActivationGroupCounts[(uint8)Group] < INT32_MAX);

	ActivationGroupCounts[(uint8)Group]++;

	const bool bReplicateCancelAbility = false;

	switch (Group)
	{
	case EDJ01AbilityActivationGroup::Independent:
		// Independent abilities do not cancel any other abilities.
		break;

	case EDJ01AbilityActivationGroup::Exclusive_Replaceable:
	case EDJ01AbilityActivationGroup::Exclusive_Blocking:
		CancelActivationGroupAbilities(EDJ01AbilityActivationGroup::Exclusive_Replaceable, DJ01Ability, bReplicateCancelAbility);
		break;

	default:
		checkf(false, TEXT("AddAbilityToActivationGroup: Invalid ActivationGroup [%d]\n"), (uint8)Group);
		break;
	}

	const int32 ExclusiveCount = ActivationGroupCounts[(uint8)EDJ01AbilityActivationGroup::Exclusive_Replaceable] + ActivationGroupCounts[(uint8)EDJ01AbilityActivationGroup::Exclusive_Blocking];
	if (!ensure(ExclusiveCount <= 1))
	{
		UE_LOG(LogDJ01AbilitySystem, Error, TEXT("AddAbilityToActivationGroup: Multiple exclusive abilities are running."));
	}
}

void UDJ01AbilitySystemComponent::RemoveAbilityFromActivationGroup(EDJ01AbilityActivationGroup Group, UDJ01GameplayAbility* DJ01Ability)
{
	check(DJ01Ability);
	check(ActivationGroupCounts[(uint8)Group] > 0);

	ActivationGroupCounts[(uint8)Group]--;
}

void UDJ01AbilitySystemComponent::CancelActivationGroupAbilities(EDJ01AbilityActivationGroup Group, UDJ01GameplayAbility* IgnoreDJ01Ability, bool bReplicateCancelAbility)
{
	auto ShouldCancelFunc = [this, Group, IgnoreDJ01Ability](const UDJ01GameplayAbility* DJ01Ability, FGameplayAbilitySpecHandle Handle)
	{
		return ((DJ01Ability->GetActivationGroup() == Group) && (DJ01Ability != IgnoreDJ01Ability));
	};

	CancelAbilitiesByFunc(ShouldCancelFunc, bReplicateCancelAbility);
}

void UDJ01AbilitySystemComponent::AddDynamicTagGameplayEffect(const FGameplayTag& Tag)
{
	const TSubclassOf<UGameplayEffect> DynamicTagGE = UDJ01AssetManager::GetSubclass(UDJ01GameData::Get().DynamicTagGameplayEffect);
	if (!DynamicTagGE)
	{
		UE_LOG(LogDJ01AbilitySystem, Warning, TEXT("AddDynamicTagGameplayEffect: Unable to find DynamicTagGameplayEffect [%s]."), *UDJ01GameData::Get().DynamicTagGameplayEffect.GetAssetName());
		return;
	}

	const FGameplayEffectSpecHandle SpecHandle = MakeOutgoingSpec(DynamicTagGE, 1.0f, MakeEffectContext());
	FGameplayEffectSpec* Spec = SpecHandle.Data.Get();

	if (!Spec)
	{
		UE_LOG(LogDJ01AbilitySystem, Warning, TEXT("AddDynamicTagGameplayEffect: Unable to make outgoing spec for [%s]."), *GetNameSafe(DynamicTagGE));
		return;
	}

	Spec->DynamicGrantedTags.AddTag(Tag);

	ApplyGameplayEffectSpecToSelf(*Spec);
}

void UDJ01AbilitySystemComponent::RemoveDynamicTagGameplayEffect(const FGameplayTag& Tag)
{
	const TSubclassOf<UGameplayEffect> DynamicTagGE = UDJ01AssetManager::GetSubclass(UDJ01GameData::Get().DynamicTagGameplayEffect);
	if (!DynamicTagGE)
	{
		UE_LOG(LogDJ01AbilitySystem, Warning, TEXT("RemoveDynamicTagGameplayEffect: Unable to find gameplay effect [%s]."), *UDJ01GameData::Get().DynamicTagGameplayEffect.GetAssetName());
		return;
	}

	FGameplayEffectQuery Query = FGameplayEffectQuery::MakeQuery_MatchAnyOwningTags(FGameplayTagContainer(Tag));
	Query.EffectDefinition = DynamicTagGE;

	RemoveActiveEffects(Query);
}

void UDJ01AbilitySystemComponent::GetAbilityTargetData(const FGameplayAbilitySpecHandle AbilityHandle, FGameplayAbilityActivationInfo ActivationInfo, FGameplayAbilityTargetDataHandle& OutTargetDataHandle)
{
	TSharedPtr<FAbilityReplicatedDataCache> ReplicatedData = AbilityTargetDataMap.Find(FGameplayAbilitySpecHandleAndPredictionKey(AbilityHandle, ActivationInfo.GetActivationPredictionKey()));
	if (ReplicatedData.IsValid())
	{
		OutTargetDataHandle = ReplicatedData->TargetData;
	}
}

//~============================================================================
// 属性集 Tag 映射
//~============================================================================

void UDJ01AbilitySystemComponent::RegisterAttributeSetTag(UAttributeSet* AttributeSet, const FGameplayTag& AttributeSetTag)
{
	if (AttributeSet && AttributeSetTag.IsValid())
	{
		AttributeSetTagMap.Add(AttributeSetTag, AttributeSet);
		UE_LOG(LogDJ01AbilitySystem, Log, TEXT("RegisterAttributeSetTag: Registered [%s] with tag [%s]"), 
			*GetNameSafe(AttributeSet), *AttributeSetTag.ToString());
	}
}

void UDJ01AbilitySystemComponent::UnregisterAttributeSetTag(UAttributeSet* AttributeSet)
{
	if (AttributeSet)
	{
		// 找到并移除该属性集的所有映射
		for (auto It = AttributeSetTagMap.CreateIterator(); It; ++It)
		{
			if (It.Value() == AttributeSet)
			{
				UE_LOG(LogDJ01AbilitySystem, Log, TEXT("UnregisterAttributeSetTag: Unregistered [%s] from tag [%s]"), 
					*GetNameSafe(AttributeSet), *It.Key().ToString());
				It.RemoveCurrent();
			}
		}
	}
}

const UAttributeSet* UDJ01AbilitySystemComponent::GetAttributeSetByTag(const FGameplayTag& AttributeSetTag) const
{
	if (AttributeSetTag.IsValid())
	{
		if (const TObjectPtr<UAttributeSet>* FoundSet = AttributeSetTagMap.Find(AttributeSetTag))
		{
			return *FoundSet;
		}
	}
	return nullptr;
}


