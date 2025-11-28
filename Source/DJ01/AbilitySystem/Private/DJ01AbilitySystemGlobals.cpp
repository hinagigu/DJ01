// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemGlobals.h"

#include "DJ01/AbilitySystem/Public/DJ01GameplayEffectContext.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01AbilitySystemGlobals)

struct FGameplayEffectContext;

UDJ01AbilitySystemGlobals::UDJ01AbilitySystemGlobals(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
}

FGameplayEffectContext* UDJ01AbilitySystemGlobals::AllocGameplayEffectContext() const
{
	return new FDJ01GameplayEffectContext();
}


