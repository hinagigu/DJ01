// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CommonLocalPlayer.h"
#include "DJ01/Team/Public/DJ01TeamAgentInterface.h"

#include "DJ01LocalPlayer.generated.h"

struct FGenericTeamId;

class APlayerController;
class UInputMappingContext;
// class UDJ01SettingsLocal; // TODO: Settings
// class UDJ01SettingsShared; // TODO: Settings
class UObject;
class UWorld;
struct FFrame;
struct FSwapAudioOutputResult;

/**
* UDJ01LocalPlayer
*/
UCLASS()
class DJ01_API UDJ01LocalPlayer : public UCommonLocalPlayer, public IDJ01TeamAgentInterface
{
	GENERATED_BODY()

public:

	UDJ01LocalPlayer();

	//~UObject interface
	virtual void PostInitProperties() override;
	//~End of UObject interface

	//~UPlayer interface
	virtual void SwitchController(class APlayerController* PC) override;
	//~End of UPlayer interface

	//~ULocalPlayer interface
	virtual bool SpawnPlayActor(const FString& URL, FString& OutError, UWorld* InWorld) override;
	virtual void InitOnlineSession() override;
	//~End of ULocalPlayer interface

	//~IDJ01TeamAgentInterface interface
	virtual void SetGenericTeamId(const FGenericTeamId& NewTeamID) override;
	virtual FGenericTeamId GetGenericTeamId() const override;
	virtual FDJ01TeamConfigChangedDelegate* GetTeamChangedDelegate() override;
	virtual void SetTeamConfig(const FDJ01TeamConfig& NewConfig) override;
	virtual FDJ01TeamConfig GetTeamConfig() const override;
	//~End of IDJ01TeamAgentInterface interface

	/** Gets the local settings for this player, this is read from config files at process startup and is always valid */
	// UFUNCTION()
	// UDJ01SettingsLocal* GetLocalSettings() const; // TODO: Settings

	/** Gets the shared setting for this player, this is read using the save game system so may not be correct until after user login */
	// UFUNCTION()
	// UDJ01SettingsShared* GetSharedSettings() const; // TODO: Settings

	/** Starts an async request to load the shared settings, this will call OnSharedSettingsLoaded after loading or creating new ones */
	// void LoadSharedSettingsFromDisk(bool bForceLoad = false); // TODO: Settings

protected:
	// void OnSharedSettingsLoaded(UDJ01SettingsShared* LoadedOrCreatedSettings); // TODO: Settings

	void OnAudioOutputDeviceChanged(const FString& InAudioOutputDeviceId);
	
	UFUNCTION()
	void OnCompletedAudioDeviceSwap(const FSwapAudioOutputResult& SwapResult);

	void OnPlayerControllerChanged(APlayerController* NewController);

	UFUNCTION()
	void OnControllerChangedTeam(UObject* TeamAgent, FDJ01TeamConfig OldConfig, FDJ01TeamConfig NewConfig);

private:
	// UPROPERTY(Transient)
	// mutable TObjectPtr<UDJ01SettingsShared> SharedSettings; // TODO: Settings

	FUniqueNetIdRepl NetIdForSharedSettings;

	UPROPERTY(Transient)
	mutable TObjectPtr<const UInputMappingContext> InputMappingContext;

	UPROPERTY()
	FDJ01TeamConfigChangedDelegate OnTeamChangedDelegate;

	UPROPERTY()
	TWeakObjectPtr<APlayerController> LastBoundPC;
};
