// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Input/Public/DJ01MappableConfigPair.h"

#include "CommonUISettings.h"
#include "ICommonUIModule.h"
#include "PlayerMappableInputConfig.h"
#include "DJ01/System/Public/DJ01AssetManager.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01MappableConfigPair)

PRAGMA_DISABLE_DEPRECATION_WARNINGS

bool FMappableConfigPair::CanBeActivated() const
{
	const FGameplayTagContainer& PlatformTraits = ICommonUIModule::GetSettings().GetPlatformTraits();

	// If the current platform does NOT have all the dependent traits, then don't activate it
	if (!DependentPlatformTraits.IsEmpty() && !PlatformTraits.HasAll(DependentPlatformTraits))
	{
		return false;
	}

	// If the platform has any of the excluded traits, then we shouldn't activate this config.
	if (!ExcludedPlatformTraits.IsEmpty() && PlatformTraits.HasAny(ExcludedPlatformTraits))
	{
		return false;
	}

	return true;
}

bool FMappableConfigPair::RegisterPair(const FMappableConfigPair& Pair)
{
	UDJ01AssetManager& AssetManager = UDJ01AssetManager::Get();

	// TODO: Implement your own settings system
	// For now, we'll just load the config
	if (const UPlayerMappableInputConfig* LoadedConfig = Cast<UPlayerMappableInputConfig>(Pair.Config.Get()))
	{
		// You'll need to implement your own registration system
		return true;
	}
	
	return false;
}

void FMappableConfigPair::UnregisterPair(const FMappableConfigPair& Pair)
{
	UDJ01AssetManager& AssetManager = UDJ01AssetManager::Get();

	// TODO: Implement your own settings system
	if (const UPlayerMappableInputConfig* LoadedConfig = UDJ01AssetManager::GetAsset(Pair.Config))
	{
		// You'll need to implement your own unregistration system
	}
}

PRAGMA_ENABLE_DEPRECATION_WARNINGS