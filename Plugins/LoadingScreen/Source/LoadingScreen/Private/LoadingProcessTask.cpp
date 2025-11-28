// Copyright Epic Games, Inc. All Rights Reserved.

#include "LoadingProcessTask.h"
#include "LoadingScreenManager.h"
#include "Engine/GameInstance.h"
#include "Engine/World.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(LoadingProcessTask)

ULoadingProcessTask* ULoadingProcessTask::CreateLoadingScreenProcessTask(UObject* WorldContextObject, const FString& ShowLoadingScreenReason)
{
	ULoadingProcessTask* Task = NewObject<ULoadingProcessTask>();
	Task->Reason = ShowLoadingScreenReason;

	if (UWorld* World = GEngine->GetWorldFromContextObject(WorldContextObject, EGetWorldErrorMode::ReturnNull))
	{
		if (UGameInstance* GameInstance = World->GetGameInstance())
		{
			if (ULoadingScreenManager* LoadingScreenManager = GameInstance->GetSubsystem<ULoadingScreenManager>())
			{
				LoadingScreenManager->RegisterLoadingProcessor(Task);
			}
		}
	}

	return Task;
}

void ULoadingProcessTask::Unregister()
{
	// Find the game instance to unregister from
	for (TObjectIterator<UGameInstance> It; It; ++It)
	{
		if (ULoadingScreenManager* LoadingScreenManager = It->GetSubsystem<ULoadingScreenManager>())
		{
			LoadingScreenManager->UnregisterLoadingProcessor(this);
		}
	}

	MarkAsGarbage();
}

void ULoadingProcessTask::SetShowLoadingScreenReason(const FString& InReason)
{
	Reason = InReason;
}

bool ULoadingProcessTask::ShouldShowLoadingScreen(FString& OutReason) const
{
	OutReason = Reason;
	return true;
}