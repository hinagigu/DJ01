// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "UserSettings/EnhancedInputUserSettings.h"

#include "DJ01PlayerMappableKeyProfile.generated.h"

UCLASS()
class DJ01_API UDJ01PlayerMappableKeyProfile : public UEnhancedPlayerMappableKeyProfile
{
	GENERATED_BODY()

protected:

	//~ Begin UEnhancedPlayerMappableKeyProfile interface
	virtual void EquipProfile() override;
	virtual void UnEquipProfile() override;
	//~ End UEnhancedPlayerMappableKeyProfile interface
};