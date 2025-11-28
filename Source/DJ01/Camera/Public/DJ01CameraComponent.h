// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "Camera/CameraComponent.h"
#include "GameFramework/Actor.h"

#include "DJ01CameraComponent.generated.h"

class UCanvas;
class UDJ01CameraMode;
class UDJ01CameraModeStack;
class UObject;
struct FFrame;
struct FGameplayTag;
struct FMinimalViewInfo;
template <class TClass> class TSubclassOf;

DECLARE_DELEGATE_RetVal(TSubclassOf<UDJ01CameraMode>, FDJ01CameraModeDelegate);


/**
* UDJ01CameraComponent
*
*	The base camera component class used by this project.
*/
UCLASS()
class DJ01_API UDJ01CameraComponent : public UCameraComponent
{
	GENERATED_BODY()

public:

	UDJ01CameraComponent(const FObjectInitializer& ObjectInitializer);

	// Returns the camera component if one exists on the specified actor.
	UFUNCTION(BlueprintPure, Category = "DJ01|Camera")
	static UDJ01CameraComponent* FindCameraComponent(const AActor* Actor) { return (Actor ? Actor->FindComponentByClass<UDJ01CameraComponent>() : nullptr); }

	// Returns the target actor that the camera is looking at.
	virtual AActor* GetTargetActor() const { return GetOwner(); }

	// Delegate used to query for the best camera mode.
	FDJ01CameraModeDelegate DetermineCameraModeDelegate;

	// Add an offset to the field of view.  The offset is only for one frame, it gets cleared once it is applied.
	void AddFieldOfViewOffset(float FovOffset) { FieldOfViewOffset += FovOffset; }

	virtual void DrawDebug(UCanvas* Canvas) const;

	// Gets the tag associated with the top layer and the blend weight of it
	void GetBlendInfo(float& OutWeightOfTopLayer, FGameplayTag& OutTagOfTopLayer) const;

protected:

	virtual void OnRegister() override;
	virtual void GetCameraView(float DeltaTime, FMinimalViewInfo& DesiredView) override;

	virtual void UpdateCameraModes();

protected:

	// Stack used to blend the camera modes.
	UPROPERTY()
	TObjectPtr<UDJ01CameraModeStack> CameraModeStack;

	// Offset applied to the field of view.  The offset is only for one frame, it gets cleared once it is applied.
	float FieldOfViewOffset;

	// 项目特定的相机配置
	UPROPERTY(EditDefaultsOnly, Category = "DJ01|Camera")
	float CameraLagSpeed = 10.0f;

	UPROPERTY(EditDefaultsOnly, Category = "DJ01|Camera")
	float CameraRotationLagSpeed = 10.0f;

	UPROPERTY(EditDefaultsOnly, Category = "DJ01|Camera")
	float DefaultArmLength = 300.0f;

};
