// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01LoadingScreenWidget.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01LoadingScreenWidget)

void UDJ01LoadingScreenWidget::NativeConstruct()
{
	Super::NativeConstruct();
	
	OnLoadingScreenShown();
}

void UDJ01LoadingScreenWidget::NativeDestruct()
{
	OnLoadingScreenHidden();
	
	Super::NativeDestruct();
}

void UDJ01LoadingScreenWidget::SetLoadingProgress(float Progress)
{
	CurrentProgress = FMath::Clamp(Progress, 0.0f, 1.0f);
	OnProgressUpdated(CurrentProgress);
}

void UDJ01LoadingScreenWidget::SetLoadingTipText(const FText& TipText)
{
	CurrentTipText = TipText;
	OnTipTextUpdated(CurrentTipText);
}