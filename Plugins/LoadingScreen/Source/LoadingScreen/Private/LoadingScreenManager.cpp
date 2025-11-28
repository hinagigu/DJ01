// Copyright Epic Games, Inc. All Rights Reserved.

#include "LoadingScreenManager.h"

#include "HAL/ThreadHeartBeat.h"
#include "Engine/GameInstance.h"
#include "Engine/GameViewportClient.h"
#include "Engine/Engine.h"
#include "GameFramework/GameStateBase.h"
#include "GameFramework/WorldSettings.h"
#include "Misc/CommandLine.h"
#include "Misc/ConfigCacheIni.h"

#include "LoadingProcessInterface.h"
#include "LoadingScreenSettings.h"

#include "Framework/Application/IInputProcessor.h"
#include "Framework/Application/SlateApplication.h"

#include "ShaderPipelineCache.h"

#include "Widgets/Images/SThrobber.h"
#include "Blueprint/UserWidget.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(LoadingScreenManager)

DEFINE_LOG_CATEGORY_STATIC(LogLoadingScreen, Log, All);

//////////////////////////////////////////////////////////////////////
// ILoadingProcessInterface

bool ILoadingProcessInterface::ShouldShowLoadingScreen(UObject* TestObject, FString& OutReason)
{
	if (TestObject != nullptr)
	{
		if (ILoadingProcessInterface* LoadObserver = Cast<ILoadingProcessInterface>(TestObject))
		{
			FString ObserverReason;
			if (LoadObserver->ShouldShowLoadingScreen(/*out*/ ObserverReason))
			{
				if (ensureMsgf(!ObserverReason.IsEmpty(), TEXT("%s failed to set a reason why it wants to show the loading screen"), *GetPathNameSafe(TestObject)))
				{
					OutReason = ObserverReason;
				}
				return true;
			}
		}
	}

	return false;
}

//////////////////////////////////////////////////////////////////////
// Console Variables

namespace LoadingScreenCVars
{
	static float HoldLoadingScreenAdditionalSecs = 2.0f;
	static FAutoConsoleVariableRef CVarHoldLoadingScreenUpAtLeastThisLongInSecs(
		TEXT("LoadingScreen.HoldLoadingScreenAdditionalSecs"),
		HoldLoadingScreenAdditionalSecs,
		TEXT("How long to hold the loading screen up after other loading finishes (in seconds)"),
		ECVF_Default);

	static bool LogLoadingScreenReasonEveryFrame = false;
	static FAutoConsoleVariableRef CVarLogLoadingScreenReasonEveryFrame(
		TEXT("LoadingScreen.LogLoadingScreenReasonEveryFrame"),
		LogLoadingScreenReasonEveryFrame,
		TEXT("When true, the reason the loading screen is shown or hidden will be printed to the log every frame."),
		ECVF_Default);

	static bool ForceLoadingScreenVisible = false;
	static FAutoConsoleVariableRef CVarForceLoadingScreenVisible(
		TEXT("LoadingScreen.AlwaysShow"),
		ForceLoadingScreenVisible,
		TEXT("Force the loading screen to show."),
		ECVF_Default);
}

//////////////////////////////////////////////////////////////////////
// Input Processor

class FLoadingScreenInputPreProcessor : public IInputProcessor
{
public:
	FLoadingScreenInputPreProcessor() { }
	virtual ~FLoadingScreenInputPreProcessor() { }

	bool CanEatInput() const
	{
		return !GIsEditor;
	}

	virtual void Tick(const float DeltaTime, FSlateApplication& SlateApp, TSharedRef<ICursor> Cursor) override { }
	virtual bool HandleKeyDownEvent(FSlateApplication& SlateApp, const FKeyEvent& InKeyEvent) override { return CanEatInput(); }
	virtual bool HandleKeyUpEvent(FSlateApplication& SlateApp, const FKeyEvent& InKeyEvent) override { return CanEatInput(); }
	virtual bool HandleAnalogInputEvent(FSlateApplication& SlateApp, const FAnalogInputEvent& InAnalogInputEvent) override { return CanEatInput(); }
	virtual bool HandleMouseMoveEvent(FSlateApplication& SlateApp, const FPointerEvent& MouseEvent) override { return CanEatInput(); }
	virtual bool HandleMouseButtonDownEvent(FSlateApplication& SlateApp, const FPointerEvent& MouseEvent) override { return CanEatInput(); }
	virtual bool HandleMouseButtonUpEvent(FSlateApplication& SlateApp, const FPointerEvent& MouseEvent) override { return CanEatInput(); }
	virtual bool HandleMouseButtonDoubleClickEvent(FSlateApplication& SlateApp, const FPointerEvent& MouseEvent) override { return CanEatInput(); }
	virtual bool HandleMouseWheelOrGestureEvent(FSlateApplication& SlateApp, const FPointerEvent& InWheelEvent, const FPointerEvent* InGestureEvent) override { return CanEatInput(); }
	virtual bool HandleMotionDetectedEvent(FSlateApplication& SlateApp, const FMotionEvent& MotionEvent) override { return CanEatInput(); }
};

//////////////////////////////////////////////////////////////////////
// ULoadingScreenManager

void ULoadingScreenManager::Initialize(FSubsystemCollectionBase& Collection)
{
	Super::Initialize(Collection);

	FCoreUObjectDelegates::PreLoadMapWithContext.AddUObject(this, &ThisClass::HandlePreLoadMap);
	FCoreUObjectDelegates::PostLoadMapWithWorld.AddUObject(this, &ThisClass::HandlePostLoadMap);
}

void ULoadingScreenManager::Deinitialize()
{
	StopBlockingInput();
	RemoveWidgetFromViewport();

	FCoreUObjectDelegates::PreLoadMapWithContext.RemoveAll(this);
	FCoreUObjectDelegates::PostLoadMapWithWorld.RemoveAll(this);

	Super::Deinitialize();
}

bool ULoadingScreenManager::ShouldCreateSubsystem(UObject* Outer) const
{
	// Only clients have loading screens
	const UGameInstance* GameInstance = CastChecked<UGameInstance>(Outer);
	const bool bIsServerWorld = GameInstance->IsDedicatedServerInstance();	
	return !bIsServerWorld;
}

void ULoadingScreenManager::Tick(float DeltaTime)
{
	UpdateLoadingScreen();
}

ETickableTickType ULoadingScreenManager::GetTickableTickType() const
{
	return ETickableTickType::Conditional;
}

bool ULoadingScreenManager::IsTickable() const
{
	return !HasAnyFlags(RF_ClassDefaultObject);
}

TStatId ULoadingScreenManager::GetStatId() const
{
	RETURN_QUICK_DECLARE_CYCLE_STAT(ULoadingScreenManager, STATGROUP_Tickables);
}

UWorld* ULoadingScreenManager::GetTickableGameObjectWorld() const
{
	return GetGameInstance()->GetWorld();
}

void ULoadingScreenManager::RegisterLoadingProcessor(TScriptInterface<ILoadingProcessInterface> Interface)
{
	ExternalLoadingProcessors.Add(Interface.GetObject());
}

void ULoadingScreenManager::UnregisterLoadingProcessor(TScriptInterface<ILoadingProcessInterface> Interface)
{
	ExternalLoadingProcessors.Remove(Interface.GetObject());
}

void ULoadingScreenManager::HandlePreLoadMap(const FWorldContext& WorldContext, const FString& MapName)
{
	if (WorldContext.OwningGameInstance == GetGameInstance())
	{
		bCurrentlyInLoadMap = true;
		
		if (GEngine && GEngine->IsInitialized())
		{
			UpdateLoadingScreen();
		}
	}
}

void ULoadingScreenManager::HandlePostLoadMap(UWorld* World)
{
	if ((World != nullptr) && (World->GetGameInstance() == GetGameInstance()))
	{
		bCurrentlyInLoadMap = false;
	}
}

void ULoadingScreenManager::UpdateLoadingScreen()
{
	bool bLogLoadingScreenStatus = LoadingScreenCVars::LogLoadingScreenReasonEveryFrame;

	if (ShouldShowLoadingScreen())
	{
		ShowLoadingScreen();
	}
	else
	{
		HideLoadingScreen();
	}

	if (bLogLoadingScreenStatus)
	{
		UE_LOG(LogLoadingScreen, Log, TEXT("Loading screen showing: %d. Reason: %s"), 
			bCurrentlyShowingLoadingScreen ? 1 : 0, *DebugReasonForShowingOrHidingLoadingScreen);
	}
}

bool ULoadingScreenManager::CheckForAnyNeedToShowLoadingScreen()
{
	DebugReasonForShowingOrHidingLoadingScreen = TEXT("Unknown reason");

	const UGameInstance* LocalGameInstance = GetGameInstance();

	if (LoadingScreenCVars::ForceLoadingScreenVisible)
	{
		DebugReasonForShowingOrHidingLoadingScreen = TEXT("LoadingScreen.AlwaysShow is true");
		return true;
	}

	const FWorldContext* Context = LocalGameInstance->GetWorldContext();
	if (Context == nullptr)
	{
		DebugReasonForShowingOrHidingLoadingScreen = TEXT("The game instance has a null WorldContext");
		return true;
	}

	UWorld* World = Context->World();
	if (World == nullptr)
	{
		DebugReasonForShowingOrHidingLoadingScreen = TEXT("We have no world");
		return true;
	}

	AGameStateBase* GameState = World->GetGameState<AGameStateBase>();
	if (GameState == nullptr)
	{
		DebugReasonForShowingOrHidingLoadingScreen = TEXT("GameState hasn't yet replicated");
		return true;
	}

	if (bCurrentlyInLoadMap)
	{
		DebugReasonForShowingOrHidingLoadingScreen = TEXT("Currently in LoadMap");
		return true;
	}

	if (!Context->TravelURL.IsEmpty())
	{
		DebugReasonForShowingOrHidingLoadingScreen = TEXT("Pending travel");
		return true;
	}

	if (Context->PendingNetGame != nullptr)
	{
		DebugReasonForShowingOrHidingLoadingScreen = TEXT("Connecting to server");
		return true;
	}

	if (!World->HasBegunPlay())
	{
		DebugReasonForShowingOrHidingLoadingScreen = TEXT("World hasn't begun play");
		return true;
	}

	if (World->IsInSeamlessTravel())
	{
		DebugReasonForShowingOrHidingLoadingScreen = TEXT("In seamless travel");
		return true;
	}

	// Ask the game state
	if (ILoadingProcessInterface::ShouldShowLoadingScreen(GameState, /*out*/ DebugReasonForShowingOrHidingLoadingScreen))
	{
		return true;
	}

	// Ask game state components
	for (UActorComponent* TestComponent : GameState->GetComponents())
	{
		if (ILoadingProcessInterface::ShouldShowLoadingScreen(TestComponent, /*out*/ DebugReasonForShowingOrHidingLoadingScreen))
		{
			return true;
		}
	}

	// Ask external loading processors
	for (const TWeakInterfacePtr<ILoadingProcessInterface>& Processor : ExternalLoadingProcessors)
	{
		if (ILoadingProcessInterface::ShouldShowLoadingScreen(Processor.GetObject(), /*out*/ DebugReasonForShowingOrHidingLoadingScreen))
		{
			return true;
		}
	}

	// Check player controllers
	bool bFoundAnyLocalPC = false;
	bool bMissingAnyLocalPC = false;

	for (ULocalPlayer* LP : LocalGameInstance->GetLocalPlayers())
	{
		if (LP != nullptr)
		{
			if (APlayerController* PC = LP->PlayerController)
			{
				bFoundAnyLocalPC = true;

				if (ILoadingProcessInterface::ShouldShowLoadingScreen(PC, /*out*/ DebugReasonForShowingOrHidingLoadingScreen))
				{
					return true;
				}

				for (UActorComponent* TestComponent : PC->GetComponents())
				{
					if (ILoadingProcessInterface::ShouldShowLoadingScreen(TestComponent, /*out*/ DebugReasonForShowingOrHidingLoadingScreen))
					{
						return true;
					}
				}
			}
			else
			{
				bMissingAnyLocalPC = true;
			}
		}
	}

	if (!bFoundAnyLocalPC)
	{
		DebugReasonForShowingOrHidingLoadingScreen = TEXT("Need at least one local player controller");
		return true;
	}

	DebugReasonForShowingOrHidingLoadingScreen = TEXT("(nothing wants to show it anymore)");
	return false;
}

bool ULoadingScreenManager::ShouldShowLoadingScreen()
{
	const ULoadingScreenSettings* Settings = GetDefault<ULoadingScreenSettings>();

#if !UE_BUILD_SHIPPING
	static bool bCmdLineNoLoadingScreen = FParse::Param(FCommandLine::Get(), TEXT("NoLoadingScreen"));
	if (bCmdLineNoLoadingScreen)
	{
		DebugReasonForShowingOrHidingLoadingScreen = TEXT("CommandLine has 'NoLoadingScreen'");
		return false;
	}
#endif

	const bool bNeedToShowLoadingScreen = CheckForAnyNeedToShowLoadingScreen();

	bool bWantToForceShowLoadingScreen = false;
	if (bNeedToShowLoadingScreen)
	{
		TimeLoadingScreenLastDismissed = -1.0;
	}
	else
	{
		const double CurrentTime = FPlatformTime::Seconds();
		const bool bCanHoldLoadingScreen = (!GIsEditor || Settings->HoldLoadingScreenAdditionalSecsEvenInEditor);
		const double HoldLoadingScreenAdditionalSecs = bCanHoldLoadingScreen ? LoadingScreenCVars::HoldLoadingScreenAdditionalSecs : 0.0;

		if (TimeLoadingScreenLastDismissed < 0.0)
		{
			TimeLoadingScreenLastDismissed = CurrentTime;
		}
		const double TimeSinceScreenDismissed = CurrentTime - TimeLoadingScreenLastDismissed;

		if ((HoldLoadingScreenAdditionalSecs > 0.0) && (TimeSinceScreenDismissed < HoldLoadingScreenAdditionalSecs))
		{
			UGameViewportClient* GameViewportClient = GetGameInstance()->GetGameViewportClient();
			if (GameViewportClient)
			{
				GameViewportClient->bDisableWorldRendering = false;
			}

			DebugReasonForShowingOrHidingLoadingScreen = FString::Printf(
				TEXT("Keeping loading screen up for an additional %.2f seconds to allow texture streaming"), 
				HoldLoadingScreenAdditionalSecs);
			bWantToForceShowLoadingScreen = true;
		}
	}

	return bNeedToShowLoadingScreen || bWantToForceShowLoadingScreen;
}

void ULoadingScreenManager::ShowLoadingScreen()
{
	if (bCurrentlyShowingLoadingScreen)
	{
		return;
	}

	TimeLoadingScreenShown = FPlatformTime::Seconds();
	bCurrentlyShowingLoadingScreen = true;

	UE_LOG(LogLoadingScreen, Log, TEXT("Showing loading screen: %s"), *DebugReasonForShowingOrHidingLoadingScreen);

	UGameInstance* LocalGameInstance = GetGameInstance();
	StartBlockingInput();
	LoadingScreenVisibilityChanged.Broadcast(/*bIsVisible=*/ true);

	const ULoadingScreenSettings* Settings = GetDefault<ULoadingScreenSettings>();

	// Create loading screen widget
	TSubclassOf<UUserWidget> LoadingScreenWidgetClass = Settings->LoadingScreenWidget.TryLoadClass<UUserWidget>();
	if (LoadingScreenWidgetClass && LocalGameInstance)
	{
		if (UUserWidget* UserWidget = CreateWidget<UUserWidget>(LocalGameInstance, LoadingScreenWidgetClass))
		{
			LoadingScreenWidget = UserWidget->TakeWidget();
		}
	}

	if (!LoadingScreenWidget.IsValid())
	{
		UE_LOG(LogLoadingScreen, Warning, TEXT("Failed to load loading screen widget, using fallback"));
		LoadingScreenWidget = SNew(SThrobber);
	}

	// Add to viewport
	if (UGameViewportClient* GameViewportClient = LocalGameInstance->GetGameViewportClient())
	{
		GameViewportClient->AddViewportWidgetContent(LoadingScreenWidget.ToSharedRef(), Settings->LoadingScreenZOrder);
	}

	ChangePerformanceSettings(/*bEnableLoadingScreen=*/ true);

	if (!GIsEditor || Settings->ForceTickLoadingScreenEvenInEditor)
	{
		if (FSlateApplication::IsInitialized())
		{
			FSlateApplication::Get().Tick();
		}
	}
}

void ULoadingScreenManager::HideLoadingScreen()
{
	if (!bCurrentlyShowingLoadingScreen)
	{
		return;
	}

	StopBlockingInput();

	UE_LOG(LogLoadingScreen, Log, TEXT("Hiding loading screen: %s"), *DebugReasonForShowingOrHidingLoadingScreen);

	if (GEngine)
	{
		GEngine->ForceGarbageCollection(true);
	}

	RemoveWidgetFromViewport();
	ChangePerformanceSettings(/*bEnableLoadingScreen=*/ false);

	LoadingScreenVisibilityChanged.Broadcast(/*bIsVisible=*/ false);

	const double LoadingScreenDuration = FPlatformTime::Seconds() - TimeLoadingScreenShown;
	UE_LOG(LogLoadingScreen, Log, TEXT("LoadingScreen was visible for %.2fs"), LoadingScreenDuration);

	bCurrentlyShowingLoadingScreen = false;
}

void ULoadingScreenManager::RemoveWidgetFromViewport()
{
	if (LoadingScreenWidget.IsValid())
	{
		if (UGameInstance* LocalGameInstance = GetGameInstance())
		{
			if (UGameViewportClient* GameViewportClient = LocalGameInstance->GetGameViewportClient())
			{
				GameViewportClient->RemoveViewportWidgetContent(LoadingScreenWidget.ToSharedRef());
			}
		}
		LoadingScreenWidget.Reset();
	}
}

void ULoadingScreenManager::StartBlockingInput()
{
	if (!InputPreProcessor.IsValid())
	{
		InputPreProcessor = MakeShareable(new FLoadingScreenInputPreProcessor());
		if (FSlateApplication::IsInitialized())
		{
			FSlateApplication::Get().RegisterInputPreProcessor(InputPreProcessor, 0);
		}
	}
}

void ULoadingScreenManager::StopBlockingInput()
{
	if (InputPreProcessor.IsValid())
	{
		if (FSlateApplication::IsInitialized())
		{
			FSlateApplication::Get().UnregisterInputPreProcessor(InputPreProcessor);
		}
		InputPreProcessor.Reset();
	}
}

void ULoadingScreenManager::ChangePerformanceSettings(bool bEnabingLoadingScreen)
{
	UGameInstance* LocalGameInstance = GetGameInstance();
	if (!LocalGameInstance)
	{
		return;
	}

	UGameViewportClient* GameViewportClient = LocalGameInstance->GetGameViewportClient();
	if (!GameViewportClient)
	{
		return;
	}

	FShaderPipelineCache::SetBatchMode(bEnabingLoadingScreen ? 
		FShaderPipelineCache::BatchMode::Fast : 
		FShaderPipelineCache::BatchMode::Background);

	GameViewportClient->bDisableWorldRendering = bEnabingLoadingScreen;

	if (UWorld* ViewportWorld = GameViewportClient->GetWorld())
	{
		if (AWorldSettings* WorldSettings = ViewportWorld->GetWorldSettings(false, false))
		{
			WorldSettings->bHighPriorityLoadingLocal = bEnabingLoadingScreen;
		}
	}

	if (bEnabingLoadingScreen)
	{
		double HangDurationMultiplier = 1.0;
		GConfig->GetDouble(TEXT("Core.System"), TEXT("LoadingScreenHangDurationMultiplier"), 
			HangDurationMultiplier, GEngineIni);
		FThreadHeartBeat::Get().SetDurationMultiplier(HangDurationMultiplier);
		FGameThreadHitchHeartBeat::Get().SuspendHeartBeat();
	}
	else
	{
		FThreadHeartBeat::Get().SetDurationMultiplier(1.0);
		FGameThreadHitchHeartBeat::Get().ResumeHeartBeat();
	}
}