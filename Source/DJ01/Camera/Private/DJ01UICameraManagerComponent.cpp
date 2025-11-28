// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Camera/Public/DJ01UICameraManagerComponent.h"

#include "GameFramework/HUD.h"
#include "GameFramework/PlayerController.h"
#include "DJ01/Camera/Public/DJ01PlayerCameraManager.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01UICameraManagerComponent)

class AActor;
class FDebugDisplayInfo;

UDJ01UICameraManagerComponent* UDJ01UICameraManagerComponent::GetComponent(APlayerController* PC)
{
	if (PC != nullptr)
	{
		if (ADJ01PlayerCameraManager* PCCamera = Cast<ADJ01PlayerCameraManager>(PC->PlayerCameraManager))
		{
			return PCCamera->GetUICameraComponent();
		}
	}

	return nullptr;
}

UDJ01UICameraManagerComponent::UDJ01UICameraManagerComponent()
{
	bWantsInitializeComponent = true;

	if (!HasAnyFlags(RF_ClassDefaultObject))
	{
		// Register "showdebug" hook.
		if (!IsRunningDedicatedServer())
		{
			AHUD::OnShowDebugInfo.AddUObject(this, &ThisClass::OnShowDebugInfo);
		}
	}
}

void UDJ01UICameraManagerComponent::InitializeComponent()
{
	Super::InitializeComponent();
}

void UDJ01UICameraManagerComponent::SetViewTarget(AActor* InViewTarget, FViewTargetTransitionParams TransitionParams)
{
	TGuardValue<bool> UpdatingViewTargetGuard(bUpdatingViewTarget, true);

	ViewTarget = InViewTarget;
	CastChecked<ADJ01PlayerCameraManager>(GetOwner())->SetViewTarget(ViewTarget, TransitionParams);
}

bool UDJ01UICameraManagerComponent::NeedsToUpdateViewTarget() const
{
	return false;
}

void UDJ01UICameraManagerComponent::UpdateViewTarget(struct FTViewTarget& OutVT, float DeltaTime)
{
}

void UDJ01UICameraManagerComponent::OnShowDebugInfo(AHUD* HUD, UCanvas* Canvas, const FDebugDisplayInfo& DisplayInfo, float& YL, float& YPos)
{
}
