// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Player/Public/DJ01PlayerSpawningManagerComponent.h"
#include "GameFramework/PlayerState.h"
#include "EngineUtils.h"
#include "Engine/PlayerStartPIE.h"
#include "DJ01/Player/Public/DJ01PlayerStart.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01PlayerSpawningManagerComponent)

DEFINE_LOG_CATEGORY_STATIC(LogPlayerSpawning, Log, All);

UDJ01PlayerSpawningManagerComponent::UDJ01PlayerSpawningManagerComponent(const FObjectInitializer& ObjectInitializer)
: Super(ObjectInitializer)
{
	SetIsReplicatedByDefault(false);
	bAutoRegister = true;
	bAutoActivate = true;
	bWantsInitializeComponent = true;
	PrimaryComponentTick.TickGroup = TG_PrePhysics;
	PrimaryComponentTick.bCanEverTick = true;
	PrimaryComponentTick.bAllowTickOnDedicatedServer = true;
	PrimaryComponentTick.bStartWithTickEnabled = false;
}

void UDJ01PlayerSpawningManagerComponent::InitializeComponent()
{
	Super::InitializeComponent();

	FWorldDelegates::LevelAddedToWorld.AddUObject(this, &ThisClass::OnLevelAdded);

	UWorld* World = GetWorld();
	World->AddOnActorSpawnedHandler(FOnActorSpawned::FDelegate::CreateUObject(this, &ThisClass::HandleOnActorSpawned));

	for (TActorIterator<ADJ01PlayerStart> It(World); It; ++It)
	{
		if (ADJ01PlayerStart* PlayerStart = *It)
		{
			CachedPlayerStarts.Add(PlayerStart);
		}
	}
}

void UDJ01PlayerSpawningManagerComponent::OnLevelAdded(ULevel* InLevel, UWorld* InWorld)
{
	if (InWorld == GetWorld())
	{
		for (AActor* Actor : InLevel->Actors)
		{
			if (ADJ01PlayerStart* PlayerStart = Cast<ADJ01PlayerStart>(Actor))
			{
				ensure(!CachedPlayerStarts.Contains(PlayerStart));
				CachedPlayerStarts.Add(PlayerStart);
			}
		}
	}
}

void UDJ01PlayerSpawningManagerComponent::HandleOnActorSpawned(AActor* SpawnedActor)
{
	if (ADJ01PlayerStart* PlayerStart = Cast<ADJ01PlayerStart>(SpawnedActor))
	{
		CachedPlayerStarts.Add(PlayerStart);
	}
}

// ADJ01GameMode Proxied Calls - Need to handle when someone chooses
// to restart a player the normal way in the engine.
//======================================================================

AActor* UDJ01PlayerSpawningManagerComponent::ChoosePlayerStart(AController* Player)
{
	if (Player)
	{
#if WITH_EDITOR
		if (APlayerStart* PlayerStart = FindPlayFromHereStart(Player))
		{
			return PlayerStart;
		}
#endif

		TArray<ADJ01PlayerStart*> StarterPoints;
		for (auto StartIt = CachedPlayerStarts.CreateIterator(); StartIt; ++StartIt)
		{
			if (ADJ01PlayerStart* Start = (*StartIt).Get())
			{
				StarterPoints.Add(Start);
			}
			else
			{
				StartIt.RemoveCurrent();
			}
		}

		if (APlayerState* PlayerState = Player->GetPlayerState<APlayerState>())
		{
			// start dedicated spectators at any random starting location, but they do not claim it
			if (PlayerState->IsOnlyASpectator())
			{
				if (!StarterPoints.IsEmpty())
				{
					return StarterPoints[FMath::RandRange(0, StarterPoints.Num() - 1)];
				}

				return nullptr;
			}
		}

		AActor* PlayerStart = OnChoosePlayerStart(Player, StarterPoints);

		if (!PlayerStart)
		{
			PlayerStart = GetFirstRandomUnoccupiedPlayerStart(Player, StarterPoints);
		}

		if (ADJ01PlayerStart* DJ01Start = Cast<ADJ01PlayerStart>(PlayerStart))
		{
			DJ01Start->TryClaim(Player);
		}

		return PlayerStart;
	}

	return nullptr;
}

#if WITH_EDITOR
APlayerStart* UDJ01PlayerSpawningManagerComponent::FindPlayFromHereStart(AController* Player)
{
	// Only 'Play From Here' for a player controller, bots etc. should all spawn from normal spawn points.
	if (Player->IsA<APlayerController>())
	{
		if (UWorld* World = GetWorld())
		{
			for (TActorIterator<APlayerStart> It(World); It; ++It)
			{
				if (APlayerStart* PlayerStart = *It)
				{
					if (PlayerStart->IsA<APlayerStartPIE>())
					{
						// Always prefer the first "Play from Here" PlayerStart, if we find one while in PIE mode
						return PlayerStart;
					}
				}
			}
		}
	}

	return nullptr;
}
#endif

bool UDJ01PlayerSpawningManagerComponent::ControllerCanRestart(AController* Player)
{
	bool bCanRestart = true;

	// TODO Can they restart?

	return bCanRestart;
}

void UDJ01PlayerSpawningManagerComponent::FinishRestartPlayer(AController* NewPlayer, const FRotator& StartRotation)
{
	OnFinishRestartPlayer(NewPlayer, StartRotation);
	K2_OnFinishRestartPlayer(NewPlayer, StartRotation);
}

//================================================================

void UDJ01PlayerSpawningManagerComponent::TickComponent(float DeltaTime, enum ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
{
	Super::TickComponent(DeltaTime, TickType, ThisTickFunction);
}

APlayerStart* UDJ01PlayerSpawningManagerComponent::GetFirstRandomUnoccupiedPlayerStart(AController* Controller, const TArray<ADJ01PlayerStart*>& StartPoints) const
{
	if (Controller)
	{
		TArray<ADJ01PlayerStart*> UnOccupiedStartPoints;
		TArray<ADJ01PlayerStart*> OccupiedStartPoints;

		for (ADJ01PlayerStart* StartPoint : StartPoints)
		{
			EDJ01PlayerStartLocationOccupancy State = StartPoint->GetLocationOccupancy(Controller);

			switch (State)
			{
				case EDJ01PlayerStartLocationOccupancy::Empty:
					UnOccupiedStartPoints.Add(StartPoint);
					break;
				case EDJ01PlayerStartLocationOccupancy::Partial:
					OccupiedStartPoints.Add(StartPoint);
					break;

			}
		}

		if (UnOccupiedStartPoints.Num() > 0)
		{
			return UnOccupiedStartPoints[FMath::RandRange(0, UnOccupiedStartPoints.Num() - 1)];
		}
		else if (OccupiedStartPoints.Num() > 0)
		{
			return OccupiedStartPoints[FMath::RandRange(0, OccupiedStartPoints.Num() - 1)];
		}
	}

	return nullptr;
}

