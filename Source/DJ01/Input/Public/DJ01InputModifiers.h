// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "InputModifiers.h"

#include "UObject/UnrealType.h"
#include "DJ01InputModifiers.generated.h"

struct FInputActionValue;

class FProperty;
class UEnhancedPlayerInput;
class UObject;

/** 
*  Scales input basedon a double property in the SharedUserSettings
*/
UCLASS(NotBlueprintable, MinimalAPI, meta = (DisplayName = "Setting Based Scalar"))
class UDJ01SettingBasedScalar : public UInputModifier
{
	GENERATED_BODY()

public:

	/** Name of the property that will be used to clamp the X Axis of this value */
	UPROPERTY(EditInstanceOnly, BlueprintReadWrite, Category=Settings)
	FName XAxisScalarSettingName = NAME_None;

	/** Name of the property that will be used to clamp the Y Axis of this value */
	UPROPERTY(EditInstanceOnly, BlueprintReadWrite, Category=Settings)
	FName YAxisScalarSettingName = NAME_None;

	/** Name of the property that will be used to clamp the Z Axis of this value */
	UPROPERTY(EditInstanceOnly, BlueprintReadWrite, Category=Settings)
	FName ZAxisScalarSettingName = NAME_None;
	
	/** Set the maximium value of this setting on each axis. */
	UPROPERTY(EditInstanceOnly, BlueprintReadWrite, Category=Settings)
	FVector MaxValueClamp = FVector(10.0, 10.0, 10.0);
	
	/** Set the minimum value of this setting on each axis. */
	UPROPERTY(EditInstanceOnly, BlueprintReadWrite, Category=Settings)
	FVector MinValueClamp = FVector::ZeroVector;

protected:
	virtual FInputActionValue ModifyRaw_Implementation(const UEnhancedPlayerInput* PlayerInput, FInputActionValue CurrentValue, float DeltaTime) override;

	/** FProperty Cache that will be populated with any found FProperty's on the settings class so that we don't need to look them up each frame */
	TArray<const FProperty*> PropertyCache;
};

/** Represents which stick that this deadzone is for, either the move or the look stick */
UENUM()
enum class EDeadzoneStick : uint8
{
	/** Deadzone for the movement stick */
	MoveStick = 0,

	/** Deadzone for the looking stick */
	LookStick = 1,
};

/**
* This is a deadzone input modifier that will have it's thresholds driven by what is in the DJ01 Shared game settings. 
*/
UCLASS(NotBlueprintable, MinimalAPI, meta = (DisplayName = "DJ01 Settings Driven Dead Zone"))
class UDJ01InputModifierDeadZone : public UInputModifier
{
	GENERATED_BODY()

public:

	UPROPERTY(EditInstanceOnly, BlueprintReadWrite, Category=Settings, Config)
	EDeadZoneType Type = EDeadZoneType::Radial;
	
	// Threshold above which input is clamped to 1
	UPROPERTY(EditInstanceOnly, BlueprintReadWrite, Category=Settings, Config)
	float UpperThreshold = 1.0f;

	/** Which stick this deadzone is for. This controls which setting will be used when calculating the deadzone */
	UPROPERTY(EditInstanceOnly, BlueprintReadWrite, Category=Settings, Config)
	EDeadzoneStick DeadzoneStick = EDeadzoneStick::MoveStick;

protected:
	virtual FInputActionValue ModifyRaw_Implementation(const UEnhancedPlayerInput* PlayerInput, FInputActionValue CurrentValue, float DeltaTime) override;

	// Visualize as black when unmodified. Red when blocked (with differing intensities to indicate axes)
	// Mirrors visualization in https://www.gamasutra.com/blogs/JoshSutphin/20130416/190541/Doing_Thumbstick_Dead_Zones_Right.php.
	virtual FLinearColor GetVisualizationColor_Implementation(FInputActionValue SampleValue, FInputActionValue FinalValue) const override;
};

/** The type of targeting sensitity that should be considered */
UENUM()
enum class EDJ01TargetingType : uint8
{
	/** Sensitivity to be applied why normally looking around */
	Normal = 0,

	/** The sensitivity that should be applied while Aiming Down Sights */
	ADS = 1,
};

/** Applies a scalar modifier based on the current gamepad settings in DJ01 Shared game settings.  */
UCLASS(NotBlueprintable, MinimalAPI, meta = (DisplayName = "DJ01 Gamepad Sensitivity"))
class UDJ01InputModifierGamepadSensitivity : public UInputModifier
{
	GENERATED_BODY()
public:
	
	/** The type of targeting to use for this Sensitivity */
	UPROPERTY(EditInstanceOnly, BlueprintReadWrite, Category=Settings, Config)
	EDJ01TargetingType TargetingType = EDJ01TargetingType::Normal;


protected:
	virtual FInputActionValue ModifyRaw_Implementation(const UEnhancedPlayerInput* PlayerInput, FInputActionValue CurrentValue, float DeltaTime) override;
};

/** Applies an inversion of axis values based on a setting in the DJ01 Shared game settings */
UCLASS(NotBlueprintable, MinimalAPI, meta = (DisplayName = "DJ01 Aim Inversion Setting"))
class UDJ01InputModifierAimInversion : public UInputModifier
{
	GENERATED_BODY()
	
protected:
	virtual FInputActionValue ModifyRaw_Implementation(const UEnhancedPlayerInput* PlayerInput, FInputActionValue CurrentValue, float DeltaTime) override;	
};
