// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "Components/GameStateComponent.h"
#include "LoadingProcessInterface.h"

#include "DJ01ExperienceManagerComponent.generated.h"

namespace UE::GameFeatures { struct FResult; }

class UDJ01ExperienceDefinition;

DECLARE_MULTICAST_DELEGATE_OneParam(FOnDJ01ExperienceLoaded, const UDJ01ExperienceDefinition* /*Experience*/);

enum class EDJ01ExperienceLoadState
{
	Unloaded,
	Loading,
	LoadingGameFeatures,
	LoadingChaosTestingDelay,
	ExecutingActions,
	Loaded,
	Deactivating
};

UCLASS()
class UDJ01ExperienceManagerComponent final : public UGameStateComponent, public ILoadingProcessInterface
{
	GENERATED_BODY()

public:

	UDJ01ExperienceManagerComponent(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

	//~UActorComponent interface
	virtual void EndPlay(const EEndPlayReason::Type EndPlayReason) override;
	//~End of UActorComponent interface

	//~ILoadingProcessInterface interface
	virtual bool ShouldShowLoadingScreen(FString& OutReason) const override;
	//~End of ILoadingProcessInterface

	// Tries to set the current experience, either a UI or gameplay one
	void SetCurrentExperience(FPrimaryAssetId ExperienceId);

	// Ensures the delegate is called once the experience has been loaded,
	// before others are called.
	// However, if the experience has already loaded, calls the delegate immediately.
	void CallOrRegister_OnExperienceLoaded_HighPriority(FOnDJ01ExperienceLoaded::FDelegate&& Delegate);

	// Ensures the delegate is called once the experience has been loaded
	// If the experience has already loaded, calls the delegate immediately
	void CallOrRegister_OnExperienceLoaded(FOnDJ01ExperienceLoaded::FDelegate&& Delegate);

	// Ensures the delegate is called once the experience has been loaded
	// If the experience has already loaded, calls the delegate immediately
	void CallOrRegister_OnExperienceLoaded_LowPriority(FOnDJ01ExperienceLoaded::FDelegate&& Delegate);

	// This returns the current experience if it is fully loaded, asserting otherwise
	// (i.e., if you called it too soon)
	const UDJ01ExperienceDefinition* GetCurrentExperienceChecked() const;

	// Returns true if the experience is fully loaded
	bool IsExperienceLoaded() const;

private:
	UFUNCTION()
	void OnRep_CurrentExperience();

	void StartExperienceLoad();
	void OnExperienceLoadComplete();
	void OnGameFeaturePluginLoadComplete(const UE::GameFeatures::FResult& Result);
	void OnExperienceFullLoadCompleted();

	void OnActionDeactivationCompleted();
	void OnAllActionsDeactivated();

private:
	UPROPERTY(ReplicatedUsing=OnRep_CurrentExperience)
	TObjectPtr<const UDJ01ExperienceDefinition> CurrentExperience;

	EDJ01ExperienceLoadState LoadState = EDJ01ExperienceLoadState::Unloaded;

	int32 NumGameFeaturePluginsLoading = 0;
	TArray<FString> GameFeaturePluginURLs;

	int32 NumObservedPausers = 0;
	int32 NumExpectedPausers = 0;

	/**
	 * Delegate called when the experience has finished loading just before others
	 * (e.g., subsystems that set up for regular gameplay)
	 */
	FOnDJ01ExperienceLoaded OnExperienceLoaded_HighPriority;

	/** Delegate called when the experience has finished loading */
	FOnDJ01ExperienceLoaded OnExperienceLoaded;

	/** Delegate called when the experience has finished loading */
	FOnDJ01ExperienceLoaded OnExperienceLoaded_LowPriority;
};
