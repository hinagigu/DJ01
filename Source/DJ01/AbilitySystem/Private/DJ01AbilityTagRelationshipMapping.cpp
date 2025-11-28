// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/AbilitySystem/Public/DJ01AbilityTagRelationshipMapping.h"


#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01AbilityTagRelationshipMapping)

void UDJ01AbilityTagRelationshipMapping::GetAbilityTagsToBlockAndCancel(const FGameplayTagContainer& AbilityTags, FGameplayTagContainer* OutTagsToBlock, FGameplayTagContainer* OutTagsToCancel) const
{
	// Simple iteration for now
	for (int32 i = 0; i < AbilityTagRelationships.Num(); i++)
	{
		const FDJ01AbilityTagRelationship& Tags = AbilityTagRelationships[i];
		if (AbilityTags.HasTag(Tags.AbilityTag))
		{
			if (OutTagsToBlock)
			{
				OutTagsToBlock->AppendTags(Tags.AbilityTagsToBlock);
			}
			if (OutTagsToCancel)
			{
				OutTagsToCancel->AppendTags(Tags.AbilityTagsToCancel);
			}
		}
	}
}

void UDJ01AbilityTagRelationshipMapping::GetRequiredAndBlockedActivationTags(const FGameplayTagContainer& AbilityTags, FGameplayTagContainer* OutActivationRequired, FGameplayTagContainer* OutActivationBlocked) const
{
	// Simple iteration for now
	for (int32 i = 0; i < AbilityTagRelationships.Num(); i++)
	{
		const FDJ01AbilityTagRelationship& Tags = AbilityTagRelationships[i];
		if (AbilityTags.HasTag(Tags.AbilityTag))
		{
			if (OutActivationRequired)
			{
				OutActivationRequired->AppendTags(Tags.ActivationRequiredTags);
			}
			if (OutActivationBlocked)
			{
				OutActivationBlocked->AppendTags(Tags.ActivationBlockedTags);
			}
		}
	}
}

bool UDJ01AbilityTagRelationshipMapping::IsAbilityCancelledByTag(const FGameplayTagContainer& AbilityTags, const FGameplayTag& ActionTag) const
{
	// Simple iteration for now
	for (int32 i = 0; i < AbilityTagRelationships.Num(); i++)
	{
		const FDJ01AbilityTagRelationship& Tags = AbilityTagRelationships[i];

		if (Tags.AbilityTag == ActionTag && Tags.AbilityTagsToCancel.HasAny(AbilityTags))
		{
			return true;
		}
	}

	return false;
}


