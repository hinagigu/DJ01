// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemStatics.h"

#include "AbilitySystemInterface.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"
#include "Engine/World.h"
#include "GameFramework/Pawn.h"
#include "GameFramework/PlayerState.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01AbilitySystemStatics)

UAbilitySystemComponent* UDJ01AbilitySystemStatics::GetAbilitySystemComponent(AActor* Actor)
{
	if (!Actor)
	{
		return nullptr;
	}
	
	// 尝试通过 IAbilitySystemInterface 获取
	if (const IAbilitySystemInterface* ASI = Cast<IAbilitySystemInterface>(Actor))
	{
		return ASI->GetAbilitySystemComponent();
	}
	
	// 对于 Pawn，尝试从 PlayerState 获取（Lyra 模式）
	if (const APawn* Pawn = Cast<APawn>(Actor))
	{
		if (const APlayerState* PS = Pawn->GetPlayerState())
		{
			if (const IAbilitySystemInterface* ASI = Cast<IAbilitySystemInterface>(PS))
			{
				return ASI->GetAbilitySystemComponent();
			}
		}
	}
	
	return nullptr;
}

UDJ01AbilitySystemComponent* UDJ01AbilitySystemStatics::GetDJ01AbilitySystemComponent(AActor* Actor)
{
	return Cast<UDJ01AbilitySystemComponent>(GetAbilitySystemComponent(Actor));
}

const UAttributeSet* UDJ01AbilitySystemStatics::GetAttributeSetByTag(AActor* Actor, FGameplayTag AttributeSetTag)
{
	if (UDJ01AbilitySystemComponent* DJ01ASC = GetDJ01AbilitySystemComponent(Actor))
	{
		return DJ01ASC->GetAttributeSetByTag(AttributeSetTag);
	}
	return nullptr;
}

const UAttributeSet* UDJ01AbilitySystemStatics::GetAttributeSetByTagFromASC(UDJ01AbilitySystemComponent* ASC, FGameplayTag AttributeSetTag)
{
	if (ASC)
	{
		return ASC->GetAttributeSetByTag(AttributeSetTag);
	}
	return nullptr;
}