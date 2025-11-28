// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "Engine/DebugCameraController.h"

#include "DJ01DebugCameraController.generated.h"

class UObject;


/**
 * ADJ01DebugCameraController
 *
 *	Used for controlling the debug camera when it is enabled via the cheat manager.
 */
UCLASS()
class ADJ01DebugCameraController : public ADebugCameraController
{
    GENERATED_BODY()

public:

    ADJ01DebugCameraController(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

protected:

	virtual void AddCheats(bool bForce) override;
};
