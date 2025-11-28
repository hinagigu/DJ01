// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "DJ01/Camera/Public/DJ01CameraAssistInterface.h"
#include "CommonPlayerController.h"
#include "DJ01/Team/Public/DJ01TeamAgentInterface.h"

#include "DJ01PlayerController.generated.h"

struct FGenericTeamId;

class ADJ01HUD;
class ADJ01PlayerState;
class APawn;
class APlayerState;
class FPrimitiveComponentId;
class IInputInterface;
class UDJ01AbilitySystemComponent;
class UDJ01SettingsShared;
class UObject;
class UPlayer;
struct FFrame;

/**
* ADJ01PlayerController
*
*	The base player controller class used by this project.
*/
UCLASS(Config = Game, Meta = (ShortTooltip = "The base player controller class used by this project."))
class DJ01_API ADJ01PlayerController : public ACommonPlayerController, public IDJ01CameraAssistInterface, public IDJ01TeamAgentInterface
{
	GENERATED_BODY()

public:

	ADJ01PlayerController(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

	UFUNCTION(BlueprintCallable, Category = "DJ01|PlayerController")
	ADJ01PlayerState* GetDJ01PlayerState() const;

	/** 获取玩家的 AbilitySystemComponent (从 PlayerState 获取) */
	UFUNCTION(BlueprintCallable, Category = "DJ01|PlayerController")
	UDJ01AbilitySystemComponent* GetDJ01AbilitySystemComponent() const;

	UFUNCTION(BlueprintCallable, Category = "DJ01|PlayerController")
	ADJ01HUD* GetDJ01HUD() const;

	// Call from game state logic to start recording an automatic client replay if ShouldRecordClientReplay returns true
	UFUNCTION(BlueprintCallable, Category = "DJ01|PlayerController")
	bool TryToRecordClientReplay();

	// Call to see if we should record a replay, subclasses could change this
	virtual bool ShouldRecordClientReplay();

	// Run a cheat command on the server.
	UFUNCTION(Reliable, Server, WithValidation)
	void ServerCheat(const FString& Msg);

	// Run a cheat command on the server for all players.
	UFUNCTION(Reliable, Server, WithValidation)
	void ServerCheatAll(const FString& Msg);

	//~AActor interface
	virtual void PreInitializeComponents() override;
	virtual void BeginPlay() override;
	virtual void EndPlay(const EEndPlayReason::Type EndPlayReason) override;
	virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;
	//~End of AActor interface

	//~AController interface
	virtual void OnPossess(APawn* InPawn) override;
	virtual void OnUnPossess() override;
	virtual void InitPlayerState() override;
	virtual void CleanupPlayerState() override;
	virtual void OnRep_PlayerState() override;
	//~End of AController interface

	//~APlayerController interface
	virtual void ReceivedPlayer() override;
	virtual void PlayerTick(float DeltaTime) override;
	virtual void SetPlayer(UPlayer* InPlayer) override;
	virtual void AddCheats(bool bForce) override;
	virtual void UpdateForceFeedback(IInputInterface* InputInterface, const int32 ControllerId) override;
	virtual void UpdateHiddenComponents(const FVector& ViewLocation, TSet<FPrimitiveComponentId>& OutHiddenComponents) override;
	virtual void PreProcessInput(const float DeltaTime, const bool bGamePaused) override;
	virtual void PostProcessInput(const float DeltaTime, const bool bGamePaused) override;
	//~End of APlayerController interface

	//~IDJ01CameraAssistInterface interface
	virtual void OnCameraPenetratingTarget() override;
	//~End of IDJ01CameraAssistInterface interface
	
	//~IDJ01TeamAgentInterface interface
	virtual void SetGenericTeamId(const FGenericTeamId& NewTeamID) override;
	virtual FGenericTeamId GetGenericTeamId() const override;
	virtual FDJ01TeamConfigChangedDelegate* GetTeamChangedDelegate() override;
	virtual void SetTeamConfig(const FDJ01TeamConfig& NewConfig) override;
	virtual FDJ01TeamConfig GetTeamConfig() const override;
	//~End of IDJ01TeamAgentInterface interface

	UFUNCTION(BlueprintCallable, Category = "DJ01|Character")
	void SetIsAutoRunning(const bool bEnabled);

	UFUNCTION(BlueprintCallable, Category = "DJ01|Character")
	bool GetIsAutoRunning() const;

private:
	UPROPERTY()
	FDJ01TeamConfigChangedDelegate OnTeamChangedDelegate;

	UPROPERTY()
	TObjectPtr<APlayerState> LastSeenPlayerState;

private:
	UFUNCTION()
	void OnPlayerStateChangedTeam(UObject* TeamAgent, FDJ01TeamConfig OldConfig, FDJ01TeamConfig NewConfig);

protected:
	// Called when the player state is set or cleared
	virtual void OnPlayerStateChanged();

private:
	void BroadcastOnPlayerStateChanged();

protected:

	//~APlayerController interface

	//~End of APlayerController interface

	// void OnSettingsChanged(UDJ01SettingsShared* Settings); // TODO: Settings
	
	void OnStartAutoRun();
	void OnEndAutoRun();

	UFUNCTION(BlueprintImplementableEvent, meta=(DisplayName="OnStartAutoRun"))
	void K2_OnStartAutoRun();

	UFUNCTION(BlueprintImplementableEvent, meta=(DisplayName="OnEndAutoRun"))
	void K2_OnEndAutoRun();

	bool bHideViewTargetPawnNextFrame = false;
};


// A player controller used for replay capture and playback
UCLASS()
class ADJ01ReplayPlayerController : public ADJ01PlayerController
{
	GENERATED_BODY()

	virtual void Tick(float DeltaSeconds) override;
	virtual void SmoothTargetViewRotation(APawn* TargetPawn, float DeltaSeconds) override;
	virtual bool ShouldRecordClientReplay() override;

	// Callback for when the game state's RecorderPlayerState gets replicated during replay playback
	void RecorderPlayerStateUpdated(APlayerState* NewRecorderPlayerState);

	// Callback for when the followed player state changes pawn
	UFUNCTION()
	void OnPlayerStatePawnSet(APlayerState* ChangedPlayerState, APawn* NewPlayerPawn, APawn* OldPlayerPawn);

	// The player state we are currently following */
	UPROPERTY(Transient)
	TObjectPtr<APlayerState> FollowedPlayerState;
};
