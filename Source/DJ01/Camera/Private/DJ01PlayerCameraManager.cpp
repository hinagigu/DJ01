// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Camera/Public/DJ01PlayerCameraManager.h"

#include "Async/TaskGraphInterfaces.h"
#include "Engine/Canvas.h"
#include "Engine/Engine.h"
#include "GameFramework/Pawn.h"
#include "GameFramework/PlayerController.h"
#include "DJ01/Camera/Public/DJ01CameraComponent.h"
#include "DJ01/Camera/Public/DJ01UICameraManagerComponent.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01PlayerCameraManager)

class FDebugDisplayInfo;

static FName UICameraComponentName(TEXT("UICamera"));

ADJ01PlayerCameraManager::ADJ01PlayerCameraManager(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
	DefaultFOV = DJ01_CAMERA_DEFAULT_FOV;
	ViewPitchMin = DJ01_CAMERA_DEFAULT_PITCH_MIN;
	ViewPitchMax = DJ01_CAMERA_DEFAULT_PITCH_MAX;

	UICamera = CreateDefaultSubobject<UDJ01UICameraManagerComponent>(UICameraComponentName);
}

UDJ01UICameraManagerComponent* ADJ01PlayerCameraManager::GetUICameraComponent() const
{
	return UICamera;
}

void ADJ01PlayerCameraManager::UpdateViewTarget(FTViewTarget& OutVT, float DeltaTime)
{
	// If the UI Camera is looking at something, let it have priority.
	if (UICamera && UICamera->NeedsToUpdateViewTarget())
	{
		Super::UpdateViewTarget(OutVT, DeltaTime);
		UICamera->UpdateViewTarget(OutVT, DeltaTime);
		return;
	}

	Super::UpdateViewTarget(OutVT, DeltaTime);
}

void ADJ01PlayerCameraManager::DisplayDebug(UCanvas* Canvas, const FDebugDisplayInfo& DebugDisplay, float& YL, float& YPos)
{
	check(Canvas);

	FDisplayDebugManager& DisplayDebugManager = Canvas->DisplayDebugManager;

	DisplayDebugManager.SetFont(GEngine->GetSmallFont());
	DisplayDebugManager.SetDrawColor(FColor::Yellow);
	DisplayDebugManager.DrawString(FString::Printf(TEXT("DJ01PlayerCameraManager: %s"), *GetNameSafe(this)));

	Super::DisplayDebug(Canvas, DebugDisplay, YL, YPos);

	const APawn* Pawn = (PCOwner ? PCOwner->GetPawn() : nullptr);

	if (const UDJ01CameraComponent* CameraComponent = UDJ01CameraComponent::FindCameraComponent(Pawn))
	{
		CameraComponent->DrawDebug(Canvas);
	}
}

