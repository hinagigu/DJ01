// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "Engine/DeveloperSettings.h"
#include "LoadingScreenSettings.generated.h"

class UUserWidget;

/**
 * Settings for the Loading Screen system
 */
UCLASS(config=Game, defaultconfig, meta=(DisplayName="Loading Screen"))
class ULoadingScreenSettings : public UDeveloperSettings
{
	GENERATED_BODY()

public:
	ULoadingScreenSettings();

	//~UDeveloperSettings interface
	virtual FName GetCategoryName() const override;
	//~End of UDeveloperSettings interface

public:
	/** The widget to display for the loading screen */
	UPROPERTY(config, EditAnywhere, Category=Display, meta=(AllowedClasses="/Script/UMGEditor.WidgetBlueprint"))
	FSoftClassPath LoadingScreenWidget;

	/** The Z-order to use when adding the loading screen widget to the viewport */
	UPROPERTY(config, EditAnywhere, Category=Display)
	int32 LoadingScreenZOrder;

	/** How long to hold the loading screen up after other loading finishes (to allow texture streaming) */
	UPROPERTY(config, EditAnywhere, Category=Display, meta=(Units="Seconds"))
	float HoldLoadingScreenAdditionalSecs;

	/** Should we hold the loading screen for texture streaming even in the editor? */
	UPROPERTY(config, EditAnywhere, Category=Display)
	bool HoldLoadingScreenAdditionalSecsEvenInEditor;

	/** Should we force tick the loading screen even in the editor? */
	UPROPERTY(config, EditAnywhere, Category=Display)
	bool ForceTickLoadingScreenEvenInEditor;

	/** How often to log why the loading screen is still up (0 = never) */
	UPROPERTY(config, EditAnywhere, Category=Debug, meta=(Units="Seconds"))
	float LogLoadingScreenHeartbeatInterval;

	/** How long before we consider the loading screen hung and trigger the hang detector */
	UPROPERTY(config, EditAnywhere, Category=Debug, meta=(Units="Seconds"))
	float LoadingScreenHeartbeatHangDuration;
};