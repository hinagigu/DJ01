// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Blueprint/UserWidget.h"
#include "DJ01LoadingScreenWidget.generated.h"

/**
 * UDJ01LoadingScreenWidget
 * 
 * Base class for loading screen widgets.
 * You can create a Blueprint based on this class and customize the appearance.
 */
UCLASS(Abstract, Blueprintable)
class LOADINGSCREEN_API UDJ01LoadingScreenWidget : public UUserWidget
{
	GENERATED_BODY()

protected:
	virtual void NativeConstruct() override;
	virtual void NativeDestruct() override;

	/** Called when the loading screen is shown */
	UFUNCTION(BlueprintImplementableEvent, Category="Loading Screen")
	void OnLoadingScreenShown();

	/** Called when the loading screen is about to be hidden */
	UFUNCTION(BlueprintImplementableEvent, Category="Loading Screen")
	void OnLoadingScreenHidden();

public:
	/** Updates the loading progress (0.0 to 1.0) */
	UFUNCTION(BlueprintCallable, Category="Loading Screen")
	void SetLoadingProgress(float Progress);

	/** Updates the loading tip/message text */
	UFUNCTION(BlueprintCallable, Category="Loading Screen")
	void SetLoadingTipText(const FText& TipText);

protected:
	/** Override in Blueprint to update progress bar */
	UFUNCTION(BlueprintImplementableEvent, Category="Loading Screen")
	void OnProgressUpdated(float Progress);

	/** Override in Blueprint to update tip text */
	UFUNCTION(BlueprintImplementableEvent, Category="Loading Screen")
	void OnTipTextUpdated(const FText& TipText);

	UPROPERTY(BlueprintReadOnly, Category="Loading Screen")
	float CurrentProgress = 0.0f;

	UPROPERTY(BlueprintReadOnly, Category="Loading Screen")
	FText CurrentTipText;
};