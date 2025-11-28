// Copyright Epic Games, Inc. All Rights Reserved.

#include "LoadingScreenSettings.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(LoadingScreenSettings)

ULoadingScreenSettings::ULoadingScreenSettings()
{
	LoadingScreenZOrder = 10000;
	HoldLoadingScreenAdditionalSecs = 2.0f;
	HoldLoadingScreenAdditionalSecsEvenInEditor = false;
	ForceTickLoadingScreenEvenInEditor = false;
	LogLoadingScreenHeartbeatInterval = 5.0f;
	LoadingScreenHeartbeatHangDuration = 90.0f;
}

FName ULoadingScreenSettings::GetCategoryName() const
{
	return FName(TEXT("Game"));
}