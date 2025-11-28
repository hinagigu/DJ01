// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/AbilitySystem/Public/DJ01GameplayAbilityTargetData_SingleTargetHit.h"

#include "DJ01/AbilitySystem/Public/DJ01GameplayEffectContext.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01GameplayAbilityTargetData_SingleTargetHit)

struct FGameplayEffectContextHandle;

//////////////////////////////////////////////////////////////////////

void FDJ01GameplayAbilityTargetData_SingleTargetHit::AddTargetDataToContext(FGameplayEffectContextHandle& Context, bool bIncludeActorArray) const
{
	FGameplayAbilityTargetData_SingleTargetHit::AddTargetDataToContext(Context, bIncludeActorArray);

	// Add game-specific data
	if (FDJ01GameplayEffectContext* TypedContext = FDJ01GameplayEffectContext::ExtractEffectContext(Context))
	{
		TypedContext->CartridgeID = CartridgeID;
	}
}

bool FDJ01GameplayAbilityTargetData_SingleTargetHit::NetSerialize(FArchive& Ar, class UPackageMap* Map, bool& bOutSuccess)
{
	FGameplayAbilityTargetData_SingleTargetHit::NetSerialize(Ar, Map, bOutSuccess);

	Ar << CartridgeID;

	return true;
}


