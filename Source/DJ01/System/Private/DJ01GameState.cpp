// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/System/Public/DJ01GameState.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"
#include "Async/TaskGraphInterfaces.h"
#include "GameFramework/GameplayMessageSubsystem.h"
#include "DJ01/Experience/Public/DJ01ExperienceManagerComponent.h"
#include "DJ01/Player/Public/DJ01PlayerSpawningManagerComponent.h"
// #include "Messages/DJ01VerbMessage.h" // TODO: 需要迁移
#include "DJ01/Player/Public/DJ01PlayerState.h"
#include "DJ01/System/Public/DJ01LogChannels.h"
#include "Net/UnrealNetwork.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01GameState)

class APlayerState;
class FLifetimeProperty;

extern ENGINE_API float GAverageFPS;


ADJ01GameState::ADJ01GameState(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
	PrimaryActorTick.bCanEverTick = true;
	PrimaryActorTick.bStartWithTickEnabled = true;

	// 创建游戏级别的 AbilitySystem 组件（主要用于 GameplayCue）
	AbilitySystemComponent = ObjectInitializer.CreateDefaultSubobject<UDJ01AbilitySystemComponent>(this, TEXT("AbilitySystemComponent"));
	AbilitySystemComponent->SetIsReplicated(true);
	AbilitySystemComponent->SetReplicationMode(EGameplayEffectReplicationMode::Mixed);

	ExperienceManagerComponent = CreateDefaultSubobject<UDJ01ExperienceManagerComponent>(TEXT("ExperienceManagerComponent"));
	
	// Create the player spawning manager component
	CreateDefaultSubobject<UDJ01PlayerSpawningManagerComponent>(TEXT("PlayerSpawningManagerComponent"));

	ServerFPS = 0.0f;
}

void ADJ01GameState::PreInitializeComponents()
{
	Super::PreInitializeComponents();
}

void ADJ01GameState::PostInitializeComponents()
{
	Super::PostInitializeComponents();

	check(AbilitySystemComponent);
	AbilitySystemComponent->InitAbilityActorInfo(/*Owner=*/ this, /*Avatar=*/ this);
}

UAbilitySystemComponent* ADJ01GameState::GetAbilitySystemComponent() const
{
	return AbilitySystemComponent;
}

void ADJ01GameState::EndPlay(const EEndPlayReason::Type EndPlayReason)
{
	Super::EndPlay(EndPlayReason);
}

void ADJ01GameState::AddPlayerState(APlayerState* PlayerState)
{
	Super::AddPlayerState(PlayerState);
}

void ADJ01GameState::RemovePlayerState(APlayerState* PlayerState)
{
	//@TODO: This isn't getting called right now (only the 'rich' AGameMode uses it, not AGameModeBase)
	// Need to at least comment the engine code, and possibly move things around
	Super::RemovePlayerState(PlayerState);
}

void ADJ01GameState::SeamlessTravelTransitionCheckpoint(bool bToTransitionMap)
{
	// Remove inactive and bots
	for (int32 i = PlayerArray.Num() - 1; i >= 0; i--)
	{
		APlayerState* PlayerState = PlayerArray[i];
		if (PlayerState && (PlayerState->IsABot() || PlayerState->IsInactive()))
		{
			RemovePlayerState(PlayerState);
		}
	}
}

void ADJ01GameState::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
	Super::GetLifetimeReplicatedProps(OutLifetimeProps);

	DOREPLIFETIME(ThisClass, ServerFPS);
	DOREPLIFETIME_CONDITION(ThisClass, RecorderPlayerState, COND_ReplayOnly);
}

void ADJ01GameState::Tick(float DeltaSeconds)
{
	Super::Tick(DeltaSeconds);

	if (GetLocalRole() == ROLE_Authority)
	{
		ServerFPS = GAverageFPS;
	}
}

// TODO: VerbMessage系统需要迁移
// void ADJ01GameState::MulticastMessageToClients_Implementation(const FDJ01VerbMessage Message)
// {
// 	if (GetNetMode() == NM_Client)
// 	{
// 		UGameplayMessageSubsystem::Get(this).BroadcastMessage(Message.Verb, Message);
// 	}
// }

// void ADJ01GameState::MulticastReliableMessageToClients_Implementation(const FDJ01VerbMessage Message)
// {
// 	MulticastMessageToClients_Implementation(Message);
// }

float ADJ01GameState::GetServerFPS() const
{
	return ServerFPS;
}

void ADJ01GameState::SetRecorderPlayerState(APlayerState* NewPlayerState)
{
	if (RecorderPlayerState == nullptr)
	{
		// Set it and call the rep callback so it can do any record-time setup
		RecorderPlayerState = NewPlayerState;
		OnRep_RecorderPlayerState();
	}
	else
	{
		UE_LOG(LogDJ01, Warning, TEXT("SetRecorderPlayerState was called on %s but should only be called once per game on the primary user"), *GetName());
	}
}

APlayerState* ADJ01GameState::GetRecorderPlayerState() const
{
	// TODO: Maybe auto select it if null?

	return RecorderPlayerState;
}

void ADJ01GameState::OnRep_RecorderPlayerState()
{
	OnRecorderPlayerStateChangedEvent.Broadcast(RecorderPlayerState);
}