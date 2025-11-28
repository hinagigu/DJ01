// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "ModularAIController.h"
#include "DJ01/Team/Public/DJ01TeamAgentInterface.h"

#include "DJ01PlayerBotController.generated.h"

namespace ETeamAttitude { enum Type : int; }
struct FGenericTeamId;

class APlayerState;
class UAIPerceptionComponent;
class UObject;
struct FFrame;

/**
* ADJ01PlayerBotController
*
*	The controller class used by player bots in this project.
*/
UCLASS(Blueprintable)
class ADJ01PlayerBotController : public AModularAIController, public IDJ01TeamAgentInterface
{
	GENERATED_BODY()

public:
	ADJ01PlayerBotController(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

	//~IDJ01TeamAgentInterface interface
	virtual void SetGenericTeamId(const FGenericTeamId& NewTeamID) override;
	virtual FGenericTeamId GetGenericTeamId() const override;
	virtual FDJ01TeamConfigChangedDelegate* GetTeamChangedDelegate() override;
	virtual void SetTeamConfig(const FDJ01TeamConfig& NewConfig) override;
	virtual FDJ01TeamConfig GetTeamConfig() const override;
	ETeamAttitude::Type GetTeamAttitudeTowards(const AActor& Other) const override;
	//~End of IDJ01TeamAgentInterface interface

	// Attempts to restart this controller (e.g., to respawn it)
	void ServerRestartController();

	//Update Team Attitude for the AI
	UFUNCTION(BlueprintCallable, Category = "DJ01 AI Player Controller")
	void UpdateTeamAttitude(UAIPerceptionComponent* AIPerception);

	virtual void OnUnPossess() override;


private:
	UFUNCTION()
	void OnPlayerStateChangedTeam(UObject* TeamAgent, FDJ01TeamConfig OldConfig, FDJ01TeamConfig NewConfig);

protected:
	// Called when the player state is set or cleared
	virtual void OnPlayerStateChanged();

private:
	void BroadcastOnPlayerStateChanged();

protected:	
	//~AController interface
	virtual void InitPlayerState() override;
	virtual void CleanupPlayerState() override;
	virtual void OnRep_PlayerState() override;
	//~End of AController interface

private:
	UPROPERTY()
	FDJ01TeamConfigChangedDelegate OnTeamChangedDelegate;

	UPROPERTY()
	TObjectPtr<APlayerState> LastSeenPlayerState;
};
