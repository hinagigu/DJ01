// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/AbilitySystem/Public/DJ01GlobalAbilitySystem.h"

#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01GlobalAbilitySystem)

void FGlobalAppliedAbilityList::AddToASC(TSubclassOf<UGameplayAbility> Ability, UDJ01AbilitySystemComponent* ASC)
{
	if (FGameplayAbilitySpecHandle* SpecHandle = Handles.Find(ASC))
	{
		RemoveFromASC(ASC);
	}

	UGameplayAbility* AbilityCDO = Ability->GetDefaultObject<UGameplayAbility>();
	FGameplayAbilitySpec AbilitySpec(AbilityCDO);
	const FGameplayAbilitySpecHandle AbilitySpecHandle = ASC->GiveAbility(AbilitySpec);
	Handles.Add(ASC, AbilitySpecHandle);
}

void FGlobalAppliedAbilityList::RemoveFromASC(UDJ01AbilitySystemComponent* ASC)
{
	if (FGameplayAbilitySpecHandle* SpecHandle = Handles.Find(ASC))
	{
		ASC->ClearAbility(*SpecHandle);
		Handles.Remove(ASC);
	}
}

void FGlobalAppliedAbilityList::RemoveFromAll()
{
	for (auto& KVP : Handles)
	{
		if (KVP.Key != nullptr)
		{
			KVP.Key->ClearAbility(KVP.Value);
		}
	}
	Handles.Empty();
}



void FGlobalAppliedEffectList::AddToASC(TSubclassOf<UGameplayEffect> Effect, UDJ01AbilitySystemComponent* ASC)
{
	if (FActiveGameplayEffectHandle* EffectHandle = Handles.Find(ASC))
	{
		RemoveFromASC(ASC);
	}

	const UGameplayEffect* GameplayEffectCDO = Effect->GetDefaultObject<UGameplayEffect>();
	const FActiveGameplayEffectHandle GameplayEffectHandle = ASC->ApplyGameplayEffectToSelf(GameplayEffectCDO, /*Level=*/ 1, ASC->MakeEffectContext());
	Handles.Add(ASC, GameplayEffectHandle);
}

void FGlobalAppliedEffectList::RemoveFromASC(UDJ01AbilitySystemComponent* ASC)
{
	if (FActiveGameplayEffectHandle* EffectHandle = Handles.Find(ASC))
	{
		ASC->RemoveActiveGameplayEffect(*EffectHandle);
		Handles.Remove(ASC);
	}
}

void FGlobalAppliedEffectList::RemoveFromAll()
{
	for (auto& KVP : Handles)
	{
		if (KVP.Key != nullptr)
		{
			KVP.Key->RemoveActiveGameplayEffect(KVP.Value);
		}
	}
	Handles.Empty();
}

UDJ01GlobalAbilitySystem::UDJ01GlobalAbilitySystem()
{
}

void UDJ01GlobalAbilitySystem::ApplyAbilityToAll(TSubclassOf<UGameplayAbility> Ability)
{
	if ((Ability.Get() != nullptr) && (!AppliedAbilities.Contains(Ability)))
	{
		FGlobalAppliedAbilityList& Entry = AppliedAbilities.Add(Ability);		
		for (UDJ01AbilitySystemComponent* ASC : RegisteredASCs)
		{
			Entry.AddToASC(Ability, ASC);
		}
	}
}

void UDJ01GlobalAbilitySystem::ApplyEffectToAll(TSubclassOf<UGameplayEffect> Effect)
{
	if ((Effect.Get() != nullptr) && (!AppliedEffects.Contains(Effect)))
	{
		FGlobalAppliedEffectList& Entry = AppliedEffects.Add(Effect);
		for (UDJ01AbilitySystemComponent* ASC : RegisteredASCs)
		{
			Entry.AddToASC(Effect, ASC);
		}
	}
}

void UDJ01GlobalAbilitySystem::RemoveAbilityFromAll(TSubclassOf<UGameplayAbility> Ability)
{
	if ((Ability.Get() != nullptr) && AppliedAbilities.Contains(Ability))
	{
		FGlobalAppliedAbilityList& Entry = AppliedAbilities[Ability];
		Entry.RemoveFromAll();
		AppliedAbilities.Remove(Ability);
	}
}

void UDJ01GlobalAbilitySystem::RemoveEffectFromAll(TSubclassOf<UGameplayEffect> Effect)
{
	if ((Effect.Get() != nullptr) && AppliedEffects.Contains(Effect))
	{
		FGlobalAppliedEffectList& Entry = AppliedEffects[Effect];
		Entry.RemoveFromAll();
		AppliedEffects.Remove(Effect);
	}
}

void UDJ01GlobalAbilitySystem::RegisterASC(UDJ01AbilitySystemComponent* ASC)
{
	check(ASC);

	for (auto& Entry : AppliedAbilities)
	{
		Entry.Value.AddToASC(Entry.Key, ASC);
	}
	for (auto& Entry : AppliedEffects)
	{
		Entry.Value.AddToASC(Entry.Key, ASC);
	}

	RegisteredASCs.AddUnique(ASC);
}

void UDJ01GlobalAbilitySystem::UnregisterASC(UDJ01AbilitySystemComponent* ASC)
{
	check(ASC);
	for (auto& Entry : AppliedAbilities)
	{
		Entry.Value.RemoveFromASC(ASC);
	}
	for (auto& Entry : AppliedEffects)
	{
		Entry.Value.RemoveFromASC(ASC);
	}

	RegisteredASCs.Remove(ASC);
}


