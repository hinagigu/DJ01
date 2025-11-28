// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "Engine/DataAsset.h"

#include "DJ01GameData.generated.h"

class UGameplayEffect;
class UObject;

/**
* UDJ01GameData
*
*	Non-mutable data asset that contains global game data.
*/
UCLASS(BlueprintType, Const, Meta = (DisplayName = "DJ01 Game Data", ShortTooltip = "Data asset containing global game data."))
class UDJ01GameData : public UPrimaryDataAsset
{
	GENERATED_BODY()

public:

	UDJ01GameData();

	// Returns the loaded game data.
	static const UDJ01GameData& Get();

public:

	// Gameplay effect used to apply damage.  Uses SetByCaller for the damage magnitude.
	UPROPERTY(EditDefaultsOnly, Category = "Default Gameplay Effects", meta = (DisplayName = "Damage Gameplay Effect (SetByCaller)"))
	TSoftClassPtr<UGameplayEffect> DamageGameplayEffect_SetByCaller;

	// Gameplay effect used to apply healing.  Uses SetByCaller for the healing magnitude.
	UPROPERTY(EditDefaultsOnly, Category = "Default Gameplay Effects", meta = (DisplayName = "Heal Gameplay Effect (SetByCaller)"))
	TSoftClassPtr<UGameplayEffect> HealGameplayEffect_SetByCaller;

	// Gameplay effect used to add and remove dynamic tags.
	UPROPERTY(EditDefaultsOnly, Category = "Default Gameplay Effects")
	TSoftClassPtr<UGameplayEffect> DynamicTagGameplayEffect;
};
