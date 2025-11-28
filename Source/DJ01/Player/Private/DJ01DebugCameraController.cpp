// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Player/Public/DJ01DebugCameraController.h"
#include "DJ01/Player/Public/DJ01CheatManager.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01DebugCameraController)


ADJ01DebugCameraController::ADJ01DebugCameraController(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
	// Use the same cheat class as DJ01PlayerController to allow toggling the debug camera through cheats.
	CheatClass = UDJ01CheatManager::StaticClass();
}

void ADJ01DebugCameraController::AddCheats(bool bForce)
{
	// Mirrors DJ01PlayerController's AddCheats() to avoid the player becoming stuck in the debug camera.
#if USING_CHEAT_MANAGER
	Super::AddCheats(true);
#else //#if USING_CHEAT_MANAGER
	Super::AddCheats(bForce);
#endif // #else //#if USING_CHEAT_MANAGER
}

