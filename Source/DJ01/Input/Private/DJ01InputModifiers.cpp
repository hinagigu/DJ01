// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Input/Public/DJ01InputModifiers.h"

#include "EnhancedPlayerInput.h"
#include "GameFramework/PlayerController.h"
#include "GameFramework/PlayerState.h"
#include "Engine/LocalPlayer.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01InputModifiers)

DEFINE_LOG_CATEGORY_STATIC(LogDJ01InputModifiers, Log, All);

//////////////////////////////////////////////////////////////////////
// DJ01InputModifiersHelpers

namespace DJ01InputModifiersHelpers
{
	/** Returns the owning LocalPlayer of an Enhanced Player Input pointer */
	static ULocalPlayer* GetLocalPlayer(const UEnhancedPlayerInput* PlayerInput)
	{
		if (PlayerInput)
		{
			if (APlayerController* PC = Cast<APlayerController>(PlayerInput->GetOuter()))
			{
				return Cast<ULocalPlayer>(PC->GetLocalPlayer());
			}
		}
		return nullptr;
	}
	
}

//////////////////////////////////////////////////////////////////////
// ULyraSettingBasedScalar

FInputActionValue UDJ01SettingBasedScalar::ModifyRaw_Implementation(const UEnhancedPlayerInput* PlayerInput, FInputActionValue CurrentValue, float DeltaTime)
{
	if (ensureMsgf(CurrentValue.GetValueType() != EInputActionValueType::Boolean, TEXT("Setting Based Scalar modifier doesn't support boolean values.")))
	{
		if (ULocalPlayer* LocalPlayer = DJ01InputModifiersHelpers::GetLocalPlayer(PlayerInput))
		{
			// TODO: Implement your own settings class and logic here
			// For now, we'll return the current value unmodified
			return CurrentValue;
			
			// TODO: Implement settings based scalar logic
			// For now, return the current value with default scaling
			FVector ScalarToUse = FVector(1.0, 1.0, 1.0);
				
			// Apply clamps
			ScalarToUse.X = FMath::Clamp(ScalarToUse.X, MinValueClamp.X, MaxValueClamp.X);
			ScalarToUse.Y = FMath::Clamp(ScalarToUse.Y, MinValueClamp.Y, MaxValueClamp.Y);
			ScalarToUse.Z = FMath::Clamp(ScalarToUse.Z, MinValueClamp.Z, MaxValueClamp.Z);
				
			return CurrentValue.Get<FVector>() * ScalarToUse;
		}
	}
	
	return CurrentValue;	
}

//////////////////////////////////////////////////////////////////////
// ULyraInputModifierDeadZone

FInputActionValue UDJ01InputModifierDeadZone::ModifyRaw_Implementation(const UEnhancedPlayerInput* PlayerInput, FInputActionValue CurrentValue, float DeltaTime)
{
	EInputActionValueType ValueType = CurrentValue.GetValueType();
	ULocalPlayer* LocalPlayer = DJ01InputModifiersHelpers::GetLocalPlayer(PlayerInput);
	if (ValueType == EInputActionValueType::Boolean || !LocalPlayer)
	{
		return CurrentValue;
	}

	// TODO: Implement your own settings class and logic here
	// For now we'll use a default lower threshold
	float LowerThreshold = 0.2f;  // Default deadzone value
	
	LowerThreshold = FMath::Clamp(LowerThreshold, 0.0f, 1.0f);
	
	auto DeadZoneLambda = [LowerThreshold, this](const float AxisVal)
	{
		// We need to translate and scale the input to the +/- 1 range after removing the dead zone.
		return FMath::Min(1.f, (FMath::Max(0.f, FMath::Abs(AxisVal) - LowerThreshold) / (UpperThreshold - LowerThreshold))) * FMath::Sign(AxisVal);
	};

	FVector NewValue = CurrentValue.Get<FVector>();
	switch (Type)
	{
	case EDeadZoneType::Axial:
		NewValue.X = DeadZoneLambda(NewValue.X);
		NewValue.Y = DeadZoneLambda(NewValue.Y);
		NewValue.Z = DeadZoneLambda(NewValue.Z);
		break;
	case EDeadZoneType::Radial:
		if (ValueType == EInputActionValueType::Axis3D)
		{
			NewValue = NewValue.GetSafeNormal() * DeadZoneLambda(NewValue.Size());
		}
		else if (ValueType == EInputActionValueType::Axis2D)
		{
			NewValue = NewValue.GetSafeNormal2D() * DeadZoneLambda(NewValue.Size2D());
		}
		else
		{
			NewValue.X = DeadZoneLambda(NewValue.X);
		}
		break;
	}

	return NewValue;
}

FLinearColor UDJ01InputModifierDeadZone::GetVisualizationColor_Implementation(FInputActionValue SampleValue, FInputActionValue FinalValue) const
{
	// Taken from UInputModifierDeadZone::GetVisualizationColor_Implementation
	if (FinalValue.GetValueType() == EInputActionValueType::Boolean || FinalValue.GetValueType() == EInputActionValueType::Axis1D)
	{
		return FLinearColor(FinalValue.Get<float>() == 0.f ? 1.f : 0.f, 0.f, 0.f);
	}
	return FLinearColor((FinalValue.Get<FVector2D>().X == 0.f ? 0.5f : 0.f) + (FinalValue.Get<FVector2D>().Y == 0.f ? 0.5f : 0.f), 0.f, 0.f);
}

//////////////////////////////////////////////////////////////////////
// ULyraInputModifierGamepadSensitivity

FInputActionValue UDJ01InputModifierGamepadSensitivity::ModifyRaw_Implementation(const UEnhancedPlayerInput* PlayerInput, FInputActionValue CurrentValue, float DeltaTime)
{
	// You can't scale a boolean action type
	ULocalPlayer* LocalPlayer = DJ01InputModifiersHelpers::GetLocalPlayer(PlayerInput);
	if (CurrentValue.GetValueType() == EInputActionValueType::Boolean || !LocalPlayer)
	{
		return CurrentValue;
	}

	// TODO: Implement your own settings class and logic here
	// For now we'll use a default sensitivity scalar
	const float Scalar = 1.0f;  // Default sensitivity

	return CurrentValue.Get<FVector>() * Scalar;
}

//////////////////////////////////////////////////////////////////////
// ULyraInputModifierAimInversion

FInputActionValue UDJ01InputModifierAimInversion::ModifyRaw_Implementation(const UEnhancedPlayerInput* PlayerInput, FInputActionValue CurrentValue, float DeltaTime)
{
	ULocalPlayer* LocalPlayer = DJ01InputModifiersHelpers::GetLocalPlayer(PlayerInput);
	if (!LocalPlayer)
	{
		return CurrentValue;
	}

	// TODO: Implement your own settings class and logic here
	// For now we'll return the current value unmodified
	FVector NewValue = CurrentValue.Get<FVector>();
	
	return NewValue;
}
