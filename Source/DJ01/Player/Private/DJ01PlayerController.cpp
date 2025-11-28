// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Player/Public/DJ01PlayerController.h"
#include "CommonInputTypeEnum.h"
#include "Components/PrimitiveComponent.h"
#include "DJ01/System/Public/DJ01LogChannels.h"
#include "DJ01/Player/Public/DJ01CheatManager.h"
#include "DJ01/Player/Public/DJ01PlayerState.h"
#include "DJ01/Camera/Public/DJ01PlayerCameraManager.h"
#include "DJ01/UI/Public/DJ01HUD.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"
#include "EngineUtils.h"
#include "DJ01/System/Public/DJ01GameplayTags.h"
#include "GameFramework/Pawn.h"
#include "Net/UnrealNetwork.h"
#include "Engine/GameInstance.h"
#include "AbilitySystemGlobals.h"
#include "CommonInputSubsystem.h"
#include "DJ01/Player/Public/DJ01LocalPlayer.h"
#include "DJ01/System/Public/DJ01GameState.h"
// #include "Settings/DJ01SettingsLocal.h" // TODO: Settings
// #include "Settings/DJ01SettingsShared.h" // TODO: Settings
// #include "Replays/DJ01ReplaySubsystem.h" // TODO: Replays
#include "ReplaySubsystem.h"
// #include "DJ01/System/Public/DJ01DeveloperSettings.h" // TODO: DeveloperSettings
#include "GameMapsSettings.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01PlayerController)

namespace DJ01
{
	namespace Input
	{
		static int32 ShouldAlwaysPlayForceFeedback = 0;
		static FAutoConsoleVariableRef CVarShouldAlwaysPlayForceFeedback(TEXT("DJ01PC.ShouldAlwaysPlayForceFeedback"),
			ShouldAlwaysPlayForceFeedback,
			TEXT("Should force feedback effects be played, even if the last input device was not a gamepad?"));
	}
}

ADJ01PlayerController::ADJ01PlayerController(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
	PlayerCameraManagerClass = ADJ01PlayerCameraManager::StaticClass();

#if USING_CHEAT_MANAGER
	CheatClass = UDJ01CheatManager::StaticClass();
#endif // #if USING_CHEAT_MANAGER
}

void ADJ01PlayerController::PreInitializeComponents()
{
	Super::PreInitializeComponents();
}

void ADJ01PlayerController::BeginPlay()
{
	Super::BeginPlay();
	SetActorHiddenInGame(false);
}

void ADJ01PlayerController::EndPlay(const EEndPlayReason::Type EndPlayReason)
{
	Super::EndPlay(EndPlayReason);
}

void ADJ01PlayerController::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
	Super::GetLifetimeReplicatedProps(OutLifetimeProps);

	// Disable replicating the PC target view as it doesn't work well for replays or client-side spectating.
	// The engine TargetViewRotation is only set in APlayerController::TickActor if the server knows ahead of time that 
	// a specific pawn is being spectated and it only replicates down for COND_OwnerOnly.
	// In client-saved replays, COND_OwnerOnly is never true and the target pawn is not always known at the time of recording.
	// To support client-saved replays, the replication of this was moved to ReplicatedViewRotation and updated in PlayerTick.
	DISABLE_REPLICATED_PROPERTY(APlayerController, TargetViewRotation);
}

void ADJ01PlayerController::ReceivedPlayer()
{
	Super::ReceivedPlayer();
}

void ADJ01PlayerController::PlayerTick(float DeltaTime)
{
	Super::PlayerTick(DeltaTime);

	// If we are auto running then add some player input
	if (GetIsAutoRunning())
	{
		if (APawn* CurrentPawn = GetPawn())
		{
			const FRotator MovementRotation(0.0f, GetControlRotation().Yaw, 0.0f);
			const FVector MovementDirection = MovementRotation.RotateVector(FVector::ForwardVector);
			CurrentPawn->AddMovementInput(MovementDirection, 1.0f);	
		}
	}

	ADJ01PlayerState* DJ01PlayerState = GetDJ01PlayerState();

	if (PlayerCameraManager && DJ01PlayerState)
	{
		APawn* TargetPawn = PlayerCameraManager->GetViewTargetPawn();

		if (TargetPawn)
		{
			// Update view rotation on the server so it replicates
			if (HasAuthority() || TargetPawn->IsLocallyControlled())
			{
				DJ01PlayerState->SetReplicatedViewRotation(TargetPawn->GetViewRotation());
			}

			// Update the target view rotation if the pawn isn't locally controlled
			if (!TargetPawn->IsLocallyControlled())
			{
				DJ01PlayerState = TargetPawn->GetPlayerState<ADJ01PlayerState>();
				if (DJ01PlayerState)
				{
					// Get it from the spectated pawn's player state, which may not be the same as the PC's playerstate
					TargetViewRotation = DJ01PlayerState->GetReplicatedViewRotation();
				}
			}
		}
	}
}

ADJ01PlayerState* ADJ01PlayerController::GetDJ01PlayerState() const
{
	return CastChecked<ADJ01PlayerState>(PlayerState, ECastCheckedType::NullAllowed);
}

// ULyraAbilitySystemComponent* ADJ01PlayerController::GetDJ01AbilitySystemComponent() const
// {
// 	const ADJ01PlayerState* DJ01PS = GetDJ01PlayerState();
// 	return (DJ01PS ? DJ01PS->GetDJ01AbilitySystemComponent() : nullptr);
// }

UDJ01AbilitySystemComponent* ADJ01PlayerController::GetDJ01AbilitySystemComponent() const
{
	const ADJ01PlayerState* DJ01PS = GetDJ01PlayerState();
	return (DJ01PS ? DJ01PS->GetDJ01AbilitySystemComponent() : nullptr);
}

ADJ01HUD* ADJ01PlayerController::GetDJ01HUD() const
{
	return CastChecked<ADJ01HUD>(GetHUD(), ECastCheckedType::NullAllowed);
}

bool ADJ01PlayerController::TryToRecordClientReplay()
{
	// See if we should record a replay
	if (ShouldRecordClientReplay())
	{
		// if (UDJ01ReplaySubsystem* ReplaySubsystem = GetGameInstance()->GetSubsystem<UDJ01ReplaySubsystem>()) // TODO: Replays
		// {
		// 	APlayerController* FirstLocalPlayerController = GetGameInstance()->GetFirstLocalPlayerController();
		// 	if (FirstLocalPlayerController == this)
		// 	{
		// 		// If this is the first player, update the spectator player for local replays and then record
		// 		if (ADJ01GameState* GameState = Cast<ADJ01GameState>(GetWorld()->GetGameState()))
		// 		{
		// 			GameState->SetRecorderPlayerState(PlayerState);

		// 			ReplaySubsystem->RecordClientReplay(this);
		// 			return true;
		// 		}
		// 	}
		// }
	}
	return false;
}

bool ADJ01PlayerController::ShouldRecordClientReplay()
{
	UWorld* World = GetWorld();
	UGameInstance* GameInstance = GetGameInstance();
	if (GameInstance != nullptr &&
		World != nullptr &&
		!World->IsPlayingReplay() &&
		!World->IsRecordingClientReplay() &&
		NM_DedicatedServer != GetNetMode() &&
		IsLocalPlayerController())
	{
		FString DefaultMap = UGameMapsSettings::GetGameDefaultMap();
		FString CurrentMap = World->URL.Map;

#if WITH_EDITOR
		CurrentMap = UWorld::StripPIEPrefixFromPackageName(CurrentMap, World->StreamingLevelsPrefix);
#endif
		if (CurrentMap == DefaultMap)
		{
			// Never record demos on the default frontend map, this could be replaced with a better check for being in the main menu
			return false;
		}

		if (UReplaySubsystem* ReplaySubsystem = GameInstance->GetSubsystem<UReplaySubsystem>())
		{
			if (ReplaySubsystem->IsRecording() || ReplaySubsystem->IsPlaying())
			{
				// Only one at a time
				return false;
			}
		}

		// If this is possible, now check the settings
		// if (const UDJ01LocalPlayer* DJ01LocalPlayer = Cast<UDJ01LocalPlayer>(GetLocalPlayer())) // TODO: Settings
		// {
		// 	if (DJ01LocalPlayer->GetLocalSettings()->ShouldAutoRecordReplays())
		// 	{
		// 		return true;
		// 	}
		// }
	}
	return false;
}

void ADJ01PlayerController::OnPlayerStateChangedTeam(UObject* TeamAgent, FDJ01TeamConfig OldConfig, FDJ01TeamConfig NewConfig)
{
	OnTeamChangedDelegate.Broadcast(this, OldConfig, NewConfig);
}

void ADJ01PlayerController::OnPlayerStateChanged()
{
	// Empty, place for derived classes to implement without having to hook all the other events
}

void ADJ01PlayerController::BroadcastOnPlayerStateChanged()
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

void ADJ01PlayerController::InitPlayerState()
{
	Super::InitPlayerState();
	BroadcastOnPlayerStateChanged();
}

void ADJ01PlayerController::CleanupPlayerState()
{
	Super::CleanupPlayerState();
	BroadcastOnPlayerStateChanged();
}

void ADJ01PlayerController::OnRep_PlayerState()
{
	Super::OnRep_PlayerState();
	BroadcastOnPlayerStateChanged();
}

void ADJ01PlayerController::SetPlayer(UPlayer* InPlayer)
{
	Super::SetPlayer(InPlayer);

	// if (const UDJ01LocalPlayer* DJ01LocalPlayer = Cast<UDJ01LocalPlayer>(InPlayer)) // TODO: Settings
	// {
	// 	UDJ01SettingsShared* UserSettings = DJ01LocalPlayer->GetSharedSettings();
	// 	UserSettings->OnSettingChanged.AddUObject(this, &ThisClass::OnSettingsChanged);

	// 	OnSettingsChanged(UserSettings);
	// }
}

// void ADJ01PlayerController::OnSettingsChanged(UDJ01SettingsShared* InSettings)
// {
// 	// bForceFeedbackEnabled = InSettings->GetForceFeedbackEnabled(); // TODO: Settings
// }

void ADJ01PlayerController::AddCheats(bool bForce)
{
#if USING_CHEAT_MANAGER
	Super::AddCheats(true);
#else //#if USING_CHEAT_MANAGER
	Super::AddCheats(bForce);
#endif // #else //#if USING_CHEAT_MANAGER
}

void ADJ01PlayerController::ServerCheat_Implementation(const FString& Msg)
{
#if USING_CHEAT_MANAGER
	if (CheatManager)
	{
		// UE_LOG(LogDJ01, Warning, TEXT("ServerCheat: %s"), *Msg);
		ClientMessage(ConsoleCommand(Msg));
	}
#endif // #if USING_CHEAT_MANAGER
}

bool ADJ01PlayerController::ServerCheat_Validate(const FString& Msg)
{
	return true;
}

void ADJ01PlayerController::ServerCheatAll_Implementation(const FString& Msg)
{
#if USING_CHEAT_MANAGER
	if (CheatManager)
	{
		// UE_LOG(LogDJ01, Warning, TEXT("ServerCheatAll: %s"), *Msg);
		for (TActorIterator<ADJ01PlayerController> It(GetWorld()); It; ++It)
		{
			ADJ01PlayerController* DJ01PC = (*It);
			if (DJ01PC)
			{
				DJ01PC->ClientMessage(DJ01PC->ConsoleCommand(Msg));
			}
		}
	}
#endif // #if USING_CHEAT_MANAGER
}

bool ADJ01PlayerController::ServerCheatAll_Validate(const FString& Msg)
{
	return true;
}

void ADJ01PlayerController::PreProcessInput(const float DeltaTime, const bool bGamePaused)
{
	Super::PreProcessInput(DeltaTime, bGamePaused);
}

void ADJ01PlayerController::PostProcessInput(const float DeltaTime, const bool bGamePaused)
{
	// 在输入处理后，让 ASC 处理技能输入
	// 这是技能输入绑定的核心调用点
	if (UDJ01AbilitySystemComponent* DJ01ASC = GetDJ01AbilitySystemComponent())
	{
		DJ01ASC->ProcessAbilityInput(DeltaTime, bGamePaused);
	}

	Super::PostProcessInput(DeltaTime, bGamePaused);
}

void ADJ01PlayerController::OnCameraPenetratingTarget()
{
	bHideViewTargetPawnNextFrame = true;
}

void ADJ01PlayerController::OnPossess(APawn* InPawn)
{
	Super::OnPossess(InPawn);

#if WITH_SERVER_CODE && WITH_EDITOR
	if (GIsEditor && (InPawn != nullptr) && (GetPawn() == InPawn))
	{
		// for (const FDJ01CheatToRun& CheatRow : GetDefault<UDJ01DeveloperSettings>()->CheatsToRun) // TODO: DeveloperSettings
		// {
		// 	if (CheatRow.Phase == ECheatExecutionTime::OnPlayerPawnPossession)
		// 	{
		// 		ConsoleCommand(CheatRow.Cheat, /*bWriteToLog=*/ true);
		// 	}
		// }
	}
#endif

	SetIsAutoRunning(false);
}

void ADJ01PlayerController::SetIsAutoRunning(const bool bEnabled)
{
	const bool bIsAutoRunning = GetIsAutoRunning();
	if (bEnabled != bIsAutoRunning)
	{
		if (!bEnabled)
		{
			OnEndAutoRun();
		}
		else
		{
			OnStartAutoRun();
		}
	}
}

bool ADJ01PlayerController::GetIsAutoRunning() const
{
	bool bIsAutoRunning = false;
	if (const UDJ01AbilitySystemComponent* DJ01ASC = GetDJ01AbilitySystemComponent())
	{
		bIsAutoRunning = DJ01ASC->GetTagCount(DJ01GameplayTags::Status_AutoRunning) > 0;
	}
	return bIsAutoRunning;
}

void ADJ01PlayerController::OnStartAutoRun()
{
	if (UDJ01AbilitySystemComponent* DJ01ASC = GetDJ01AbilitySystemComponent())
	{
		DJ01ASC->SetLooseGameplayTagCount(DJ01GameplayTags::Status_AutoRunning, 1);
		K2_OnStartAutoRun();
	}
}

void ADJ01PlayerController::OnEndAutoRun()
{
	if (UDJ01AbilitySystemComponent* DJ01ASC = GetDJ01AbilitySystemComponent())
	{
		DJ01ASC->SetLooseGameplayTagCount(DJ01GameplayTags::Status_AutoRunning, 0);
		K2_OnEndAutoRun();
	}
}

void ADJ01PlayerController::UpdateForceFeedback(IInputInterface* InputInterface, const int32 ControllerId)
{
	if (bForceFeedbackEnabled)
	{
		if (const UCommonInputSubsystem* CommonInputSubsystem = UCommonInputSubsystem::Get(GetLocalPlayer()))
		{
			const ECommonInputType CurrentInputType = CommonInputSubsystem->GetCurrentInputType();
			if (DJ01::Input::ShouldAlwaysPlayForceFeedback || CurrentInputType == ECommonInputType::Gamepad || CurrentInputType == ECommonInputType::Touch)
			{
				InputInterface->SetForceFeedbackChannelValues(ControllerId, ForceFeedbackValues);
				return;
			}
		}
	}
	
	InputInterface->SetForceFeedbackChannelValues(ControllerId, FForceFeedbackValues());
}

void ADJ01PlayerController::UpdateHiddenComponents(const FVector& ViewLocation, TSet<FPrimitiveComponentId>& OutHiddenComponents)
{
	Super::UpdateHiddenComponents(ViewLocation, OutHiddenComponents);

	if (bHideViewTargetPawnNextFrame)
	{
		AActor* const ViewTargetPawn = PlayerCameraManager ? Cast<AActor>(PlayerCameraManager->GetViewTarget()) : nullptr;
		if (ViewTargetPawn)
		{
			// internal helper func to hide all the components
			auto AddToHiddenComponents = [&OutHiddenComponents](const TInlineComponentArray<UPrimitiveComponent*>& InComponents)
			{
				// add every component and all attached children
				for (UPrimitiveComponent* Comp : InComponents)
				{
					if (Comp->IsRegistered())
					{
						OutHiddenComponents.Add(Comp->GetPrimitiveSceneId());

						for (USceneComponent* AttachedChild : Comp->GetAttachChildren())
						{
							static FName NAME_NoParentAutoHide(TEXT("NoParentAutoHide"));
							UPrimitiveComponent* AttachChildPC = Cast<UPrimitiveComponent>(AttachedChild);
							if (AttachChildPC && AttachChildPC->IsRegistered() && !AttachChildPC->ComponentTags.Contains(NAME_NoParentAutoHide))
							{
								OutHiddenComponents.Add(AttachChildPC->GetPrimitiveSceneId());
							}
						}
					}
				}
			};

			//TODO Solve with an interface.  Gather hidden components or something.
			//TODO Hiding isn't awesome, sometimes you want the effect of a fade out over a proximity, needs to bubble up to designers.

			// hide pawn's components
			TInlineComponentArray<UPrimitiveComponent*> PawnComponents;
			ViewTargetPawn->GetComponents(PawnComponents);
			AddToHiddenComponents(PawnComponents);

			//// hide weapon too
			//if (ViewTargetPawn->CurrentWeapon)
			//{
			//	TInlineComponentArray<UPrimitiveComponent*> WeaponComponents;
			//	ViewTargetPawn->CurrentWeapon->GetComponents(WeaponComponents);
			//	AddToHiddenComponents(WeaponComponents);
			//}
		}

		// we consumed it, reset for next frame
		bHideViewTargetPawnNextFrame = false;
	}
}

void ADJ01PlayerController::SetGenericTeamId(const FGenericTeamId& NewTeamID)
{
	// UE_LOG(LogDJ01Teams, Error, TEXT("You can't set the team ID on a player controller (%s); it's driven by the associated player state"), *GetPathNameSafe(this));
}

FGenericTeamId ADJ01PlayerController::GetGenericTeamId() const
{
	if (const IDJ01TeamAgentInterface* PSWithTeamInterface = Cast<IDJ01TeamAgentInterface>(PlayerState))
	{
		return PSWithTeamInterface->GetGenericTeamId();
	}
	return FGenericTeamId::NoTeam;
}

FDJ01TeamConfigChangedDelegate* ADJ01PlayerController::GetTeamChangedDelegate()
{
	return &OnTeamChangedDelegate;
}

void ADJ01PlayerController::SetTeamConfig(const FDJ01TeamConfig& NewConfig)
{
	if (IDJ01TeamAgentInterface* PlayerStateTeamInterface = Cast<IDJ01TeamAgentInterface>(PlayerState))
	{
		PlayerStateTeamInterface->SetTeamConfig(NewConfig);
	}
}

FDJ01TeamConfig ADJ01PlayerController::GetTeamConfig() const
{
	if (const IDJ01TeamAgentInterface* PlayerStateTeamInterface = Cast<IDJ01TeamAgentInterface>(PlayerState))
	{
		return PlayerStateTeamInterface->GetTeamConfig();
	}
	return FDJ01TeamConfig();
}

void ADJ01PlayerController::OnUnPossess()
{
	// 确保被释放的 Pawn 不再作为 ASC 的 Avatar Actor
	// 这是防止悬空引用的重要清理步骤
	if (APawn* PawnBeingUnpossessed = GetPawn())
	{
		if (UAbilitySystemComponent* ASC = UAbilitySystemGlobals::GetAbilitySystemComponentFromActor(PlayerState))
		{
			if (ASC->GetAvatarActor() == PawnBeingUnpossessed)
			{
				ASC->SetAvatarActor(nullptr);
			}
		}
	}

	Super::OnUnPossess();
}

//////////////////////////////////////////////////////////////////////
// ADJ01ReplayPlayerController

void ADJ01ReplayPlayerController::Tick(float DeltaSeconds)
{
	Super::Tick(DeltaSeconds);

	// The state may go invalid at any time due to scrubbing during a replay
	if (!IsValid(FollowedPlayerState))
	{
		UWorld* World = GetWorld();

		// Listen for changes for both recording and playback
		if (ADJ01GameState* GameState = Cast<ADJ01GameState>(World->GetGameState()))
		{
			if (!GameState->OnRecorderPlayerStateChangedEvent.IsBoundToObject(this))
			{
				GameState->OnRecorderPlayerStateChangedEvent.AddUObject(this, &ThisClass::RecorderPlayerStateUpdated);
			}
			if (APlayerState* RecorderState = GameState->GetRecorderPlayerState())
			{
				RecorderPlayerStateUpdated(RecorderState);
			}
		}
	}
}

void ADJ01ReplayPlayerController::SmoothTargetViewRotation(APawn* TargetPawn, float DeltaSeconds)
{
	// Default behavior is to interpolate to TargetViewRotation which is set from APlayerController::TickActor but it's not very smooth

	Super::SmoothTargetViewRotation(TargetPawn, DeltaSeconds);
}

bool ADJ01ReplayPlayerController::ShouldRecordClientReplay()
{
	return false;
}

void ADJ01ReplayPlayerController::RecorderPlayerStateUpdated(APlayerState* NewRecorderPlayerState)
{
	if (NewRecorderPlayerState)
	{
		FollowedPlayerState = NewRecorderPlayerState;

		// Bind to when pawn changes and call now
		NewRecorderPlayerState->OnPawnSet.AddUniqueDynamic(this, &ADJ01ReplayPlayerController::OnPlayerStatePawnSet);
		OnPlayerStatePawnSet(NewRecorderPlayerState, NewRecorderPlayerState->GetPawn(), nullptr);
	}
}

void ADJ01ReplayPlayerController::OnPlayerStatePawnSet(APlayerState* ChangedPlayerState, APawn* NewPlayerPawn, APawn* OldPlayerPawn)
{
	if (ChangedPlayerState == FollowedPlayerState)
	{
		SetViewTarget(NewPlayerPawn);
	}
}

