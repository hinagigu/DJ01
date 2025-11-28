// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Player/Public/DJ01LocalPlayer.h"

#include "AudioMixerBlueprintLibrary.h"
#include "Engine/World.h"
#include "GameFramework/PlayerController.h"
// #include "Settings/DJ01SettingsLocal.h" // TODO: Settings
// #include "Settings/DJ01SettingsShared.h" // TODO: Settings
#include "CommonUserSubsystem.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01LocalPlayer)

class UObject;

UDJ01LocalPlayer::UDJ01LocalPlayer()
{
}

void UDJ01LocalPlayer::PostInitProperties()
{
	Super::PostInitProperties();

	// if (UDJ01SettingsLocal* LocalSettings = GetLocalSettings()) // TODO: Settings
	// {
	// 	LocalSettings->OnAudioOutputDeviceChanged.AddUObject(this, &UDJ01LocalPlayer::OnAudioOutputDeviceChanged);
	// }
}

void UDJ01LocalPlayer::SwitchController(class APlayerController* PC)
{
	Super::SwitchController(PC);

	OnPlayerControllerChanged(PlayerController);
}

bool UDJ01LocalPlayer::SpawnPlayActor(const FString& URL, FString& OutError, UWorld* InWorld)
{
	const bool bResult = Super::SpawnPlayActor(URL, OutError, InWorld);

	OnPlayerControllerChanged(PlayerController);

	return bResult;
}

void UDJ01LocalPlayer::InitOnlineSession()
{
	OnPlayerControllerChanged(PlayerController);

	Super::InitOnlineSession();
}

void UDJ01LocalPlayer::OnPlayerControllerChanged(APlayerController* NewController)
{
	// Stop listening for changes from the old controller
	FDJ01TeamConfig OldConfig;
	if (IDJ01TeamAgentInterface* ControllerAsTeamProvider = Cast<IDJ01TeamAgentInterface>(LastBoundPC.Get()))
	{
		OldConfig = ControllerAsTeamProvider->GetTeamConfig();
		ControllerAsTeamProvider->GetTeamChangedDelegate()->RemoveAll(this);
	}

	// Grab the current team ID and listen for future changes
	FDJ01TeamConfig NewConfig;
	if (IDJ01TeamAgentInterface* ControllerAsTeamProvider = Cast<IDJ01TeamAgentInterface>(NewController))
	{
		NewConfig = ControllerAsTeamProvider->GetTeamConfig();
		ControllerAsTeamProvider->GetTeamChangedDelegate()->AddDynamic(this, &ThisClass::OnControllerChangedTeam);
		LastBoundPC = NewController;
	}

	if (OldConfig.MyTeam != NewConfig.MyTeam)
	{
		OnTeamChangedDelegate.Broadcast(this, OldConfig, NewConfig);
	}
}

void UDJ01LocalPlayer::SetGenericTeamId(const FGenericTeamId& NewTeamID)
{
	// Do nothing, we merely observe the team of our associated player controller
}

FGenericTeamId UDJ01LocalPlayer::GetGenericTeamId() const
{
	if (IDJ01TeamAgentInterface* ControllerAsTeamProvider = Cast<IDJ01TeamAgentInterface>(PlayerController))
	{
		return ControllerAsTeamProvider->GetGenericTeamId();
	}
	else
	{
		return FGenericTeamId::NoTeam;
	}
}

FDJ01TeamConfigChangedDelegate* UDJ01LocalPlayer::GetTeamChangedDelegate()
{
	return &OnTeamChangedDelegate;
}

void UDJ01LocalPlayer::SetTeamConfig(const FDJ01TeamConfig& NewConfig)
{
	// Do nothing
}

FDJ01TeamConfig UDJ01LocalPlayer::GetTeamConfig() const
{
	if (IDJ01TeamAgentInterface* ControllerAsTeamProvider = Cast<IDJ01TeamAgentInterface>(PlayerController))
	{
		return ControllerAsTeamProvider->GetTeamConfig();
	}
	return FDJ01TeamConfig();
}

// UDJ01SettingsLocal* UDJ01LocalPlayer::GetLocalSettings() const
// {
// 	return UDJ01SettingsLocal::Get(); // TODO: Settings

// }
//
// UDJ01SettingsShared* UDJ01LocalPlayer::GetSharedSettings() const
// {
// 	if (!SharedSettings)
// 	{
// 		// On PC it's okay to use the sync load because it only checks the disk
// 		// This could use a platform tag to check for proper save support instead
// 		bool bCanLoadBeforeLogin = PLATFORM_DESKTOP;
// 		
// 		if (bCanLoadBeforeLogin)
// 		{
// 			SharedSettings = UDJ01SettingsShared::LoadOrCreateSettings(this);
// 		}
// 		else
// 		{
// 			// We need to wait for user login to get the real settings so return temp ones
// 			SharedSettings = UDJ01SettingsShared::CreateTemporarySettings(this);
// 		}
// 	}
//
// 	return SharedSettings;
// }

// void UDJ01LocalPlayer::LoadSharedSettingsFromDisk(bool bForceLoad)
// {
// 	FUniqueNetIdRepl CurrentNetId = GetCachedUniqueNetId();
// 	if (!bForceLoad && SharedSettings && CurrentNetId == NetIdForSharedSettings)
// 	{
// 		// Already loaded once, don't reload
// 		return;
// 	}
//
// 	ensure(UDJ01SettingsShared::AsyncLoadOrCreateSettings(this, UDJ01SettingsShared::FOnSettingsLoadedEvent::CreateUObject(this, &UDJ01LocalPlayer::OnSharedSettingsLoaded)));
// }

// void UDJ01LocalPlayer::OnSharedSettingsLoaded(UDJ01SettingsShared* LoadedOrCreatedSettings)
// {
// 	// The settings are applied before it gets here
// 	if (ensure(LoadedOrCreatedSettings))
// 	{
// 		// This will replace the temporary or previously loaded object which will GC out normally
// 		SharedSettings = LoadedOrCreatedSettings;
//
// 		NetIdForSharedSettings = GetCachedUniqueNetId();
// 	}
// }

void UDJ01LocalPlayer::OnAudioOutputDeviceChanged(const FString& InAudioOutputDeviceId)
{
	FOnCompletedDeviceSwap DevicesSwappedCallback;
	DevicesSwappedCallback.BindUFunction(this, FName("OnCompletedAudioDeviceSwap"));
	UAudioMixerBlueprintLibrary::SwapAudioOutputDevice(GetWorld(), InAudioOutputDeviceId, DevicesSwappedCallback);
}

void UDJ01LocalPlayer::OnCompletedAudioDeviceSwap(const FSwapAudioOutputResult& SwapResult)
{
	if (SwapResult.Result == ESwapAudioOutputDeviceResultState::Failure)
	{
	}
}

void UDJ01LocalPlayer::OnControllerChangedTeam(UObject* TeamAgent, FDJ01TeamConfig OldConfig, FDJ01TeamConfig NewConfig)
{
	OnTeamChangedDelegate.Broadcast(this, OldConfig, NewConfig);
}

