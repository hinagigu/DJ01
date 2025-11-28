// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/AbilitySystem/Public/DJ01TaggedActor.h"
#include "UObject/UnrealType.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01TaggedActor)

ADJ01TaggedActor::ADJ01TaggedActor(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
}

void ADJ01TaggedActor::GetOwnedGameplayTags(FGameplayTagContainer& TagContainer) const
{
	TagContainer.AppendTags(StaticGameplayTags);
}

#if WITH_EDITOR
bool ADJ01TaggedActor::CanEditChange(const FProperty* InProperty) const
{
	// Prevent editing of the other tags property
	if (InProperty->GetFName() == GET_MEMBER_NAME_CHECKED(AActor, Tags))
	{
		return false;
	}

	return Super::CanEditChange(InProperty);
}
#endif


