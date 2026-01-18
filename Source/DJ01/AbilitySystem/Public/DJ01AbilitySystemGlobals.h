// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "Abilities/ComboGraphAbilitySystemGlobals.h"

#include "DJ01AbilitySystemGlobals.generated.h"

class UObject;
struct FGameplayEffectContext;

/**
* DJ01 项目的 AbilitySystemGlobals
* 继承自 ComboGraph 的版本以支持 Combo 系统的 Gameplay Cue Container
*/
UCLASS(Config=Game)
class UDJ01AbilitySystemGlobals : public UComboGraphAbilitySystemGlobals
{
	GENERATED_UCLASS_BODY()

	//~UAbilitySystemGlobals interface
	virtual FGameplayEffectContext* AllocGameplayEffectContext() const override;
	//~End of UAbilitySystemGlobals interface
};

