// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Player/Public/DJ01PlayerBotController.h"

// #include "AbilitySystemComponent.h" // TODO: AbilitySystem
// #include "AbilitySystemGlobals.h" // TODO: AbilitySystem
#include "Engine/World.h"
#include "GameFramework/PlayerState.h"
#include "DJ01/System/Public/DJ01GameMode.h"
#include "DJ01/System/Public/DJ01LogChannels.h"
#include "Perception/AIPerceptionComponent.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01PlayerBotController)

class UObject;

ADJ01PlayerBotController::ADJ01PlayerBotController(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
	bWantsPlayerState = true;
	bStopAILogicOnUnposses = false;
}

void ADJ01PlayerBotController::OnPlayerStateChangedTeam(UObject* TeamAgent, FDJ01TeamConfig OldConfig, FDJ01TeamConfig NewConfig)
{
	OnTeamChangedDelegate.Broadcast(this, OldConfig, NewConfig);
}

void ADJ01PlayerBotController::OnPlayerStateChanged()
{
	// Empty, place for derived classes to implement without having to hook all the other events
}

void ADJ01PlayerBotController::BroadcastOnPlayerStateChanged()
{
	OnPlayerStateChanged();

	// Unbind from the old player state, if any
	FDJ01TeamConfig OldConfig;
	if (LastSeenPlayerState != nullptr)
	{
		if (IDJ01TeamAgentInterface* PlayerStateTeamInterface = Cast<IDJ01TeamAgentInterface>(LastSeenPlayerState))
		{
			OldConfig = PlayerStateTeamInterface->GetTeamConfig();
			PlayerStateTeamInterface->GetTeamChangedDelegate()->RemoveAll(this);
		}
	}

	// Bind to the new player state, if any
	FDJ01TeamConfig NewConfig;
	if (PlayerState != nullptr)
	{
		if (IDJ01TeamAgentInterface* PlayerStateTeamInterface = Cast<IDJ01TeamAgentInterface>(PlayerState))
		{
			NewConfig = PlayerStateTeamInterface->GetTeamConfig();
			PlayerStateTeamInterface->GetTeamChangedDelegate()->AddDynamic(this, &ThisClass::OnPlayerStateChangedTeam);
		}
	}

	// Broadcast the team change (if it really has)
	if (OldConfig.MyTeam != NewConfig.MyTeam)
	{
		OnTeamChangedDelegate.Broadcast(this, OldConfig, NewConfig);
	}

	LastSeenPlayerState = PlayerState;
}

void ADJ01PlayerBotController::InitPlayerState()
{
	Super::InitPlayerState();
	BroadcastOnPlayerStateChanged();
}

void ADJ01PlayerBotController::CleanupPlayerState()
{
	Super::CleanupPlayerState();
	BroadcastOnPlayerStateChanged();
}

void ADJ01PlayerBotController::OnRep_PlayerState()
{
	Super::OnRep_PlayerState();
	BroadcastOnPlayerStateChanged();
}

void ADJ01PlayerBotController::SetGenericTeamId(const FGenericTeamId& NewTeamID)
{
	// UE_LOG(LogDJ01Teams, Error, TEXT("You can't set the team ID on a player bot controller (%s); it's driven by the associated player state"), *GetPathNameSafe(this));
}

FGenericTeamId ADJ01PlayerBotController::GetGenericTeamId() const
{
	if (IDJ01TeamAgentInterface* PSWithTeamInterface = Cast<IDJ01TeamAgentInterface>(PlayerState))
	{
		return PSWithTeamInterface->GetGenericTeamId();
	}
	return FGenericTeamId::NoTeam;
}

FDJ01TeamConfigChangedDelegate* ADJ01PlayerBotController::GetTeamChangedDelegate()
{
	return &OnTeamChangedDelegate;
}

void ADJ01PlayerBotController::SetTeamConfig(const FDJ01TeamConfig& NewConfig)
{
	// Bot controller delegates to PlayerState usually, or handles it internally
}

FDJ01TeamConfig ADJ01PlayerBotController::GetTeamConfig() const
{
	if (const IDJ01TeamAgentInterface* PSWithTeamInterface = Cast<IDJ01TeamAgentInterface>(PlayerState))
	{
		return PSWithTeamInterface->GetTeamConfig();
	}
	return FDJ01TeamConfig();
}


void ADJ01PlayerBotController::ServerRestartController()
{
	if (GetNetMode() == NM_Client)
	{
		return;
	}

	ensure((GetPawn() == nullptr) && IsInState(NAME_Inactive));

	if (IsInState(NAME_Inactive) || (IsInState(NAME_Spectating)))
	{
		ADJ01GameMode* const GameMode = GetWorld()->GetAuthGameMode<ADJ01GameMode>();

		if ((GameMode == nullptr) || !GameMode->ControllerCanRestart(this))
		{
			return;
		}

		// If we're still attached to a Pawn, leave it
		if (GetPawn() != nullptr)
		{
			UnPossess();
		}

		// Re-enable input, similar to code in ClientRestart
		ResetIgnoreInputFlags();

		GameMode->RestartPlayer(this);
	}
}

ETeamAttitude::Type ADJ01PlayerBotController::GetTeamAttitudeTowards(const AActor& Other) const
{
	if (const APawn* OtherPawn = Cast<APawn>(&Other)) {

		if (const IDJ01TeamAgentInterface* TeamAgent = Cast<IDJ01TeamAgentInterface>(OtherPawn->GetController()))
		{
			FGenericTeamId OtherTeamID = TeamAgent->GetGenericTeamId();

			//Checking Other pawn ID to define Attitude
			if (OtherTeamID.GetId() != GetGenericTeamId().GetId())
			{
				return ETeamAttitude::Hostile;
			}
			else
			{
				return ETeamAttitude::Friendly;
			}
		}
	}

	return ETeamAttitude::Neutral;
}

void ADJ01PlayerBotController::UpdateTeamAttitude(UAIPerceptionComponent* AIPerception)
{
	if (AIPerception)
	{
		AIPerception->RequestStimuliListenerUpdate();
	}
}

void ADJ01PlayerBotController::OnUnPossess()
{
	// Make sure the pawn that is being unpossessed doesn't remain our ASC's avatar actor
	// if (APawn* PawnBeingUnpossessed = GetPawn()) // TODO: AbilitySystem
	// {
	// 	if (UAbilitySystemComponent* ASC = UAbilitySystemGlobals::GetAbilitySystemComponentFromActor(PlayerState))
	// 	{
	// 		if (ASC->GetAvatarActor() == PawnBeingUnpossessed)
	// 		{
	// 			ASC->SetAvatarActor(nullptr);
	// 		}
	// 	}
	// }

	Super::OnUnPossess();
}

