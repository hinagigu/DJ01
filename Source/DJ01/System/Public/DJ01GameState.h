// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "AbilitySystemInterface.h"
#include "ModularGameState.h"

#include "DJ01GameState.generated.h"

struct FDJ01VerbMessage;

class APlayerState;
class UAbilitySystemComponent;
class UDJ01AbilitySystemComponent;
class UDJ01ExperienceManagerComponent;
class UDJ01PlayerSpawningManagerComponent;
class UObject;
struct FFrame;

/**
* ADJ01GameState
*
*	The base game state class used by this project.
*/
UCLASS(Config = Game)
class DJ01_API ADJ01GameState : public AModularGameStateBase, public IAbilitySystemInterface
{
	GENERATED_BODY()

public:

	ADJ01GameState(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

	//~AActor interface
	virtual void PreInitializeComponents() override;
	virtual void PostInitializeComponents() override;
	virtual void EndPlay(const EEndPlayReason::Type EndPlayReason) override;
	virtual void Tick(float DeltaSeconds) override;
	//~End of AActor interface

	//~AGameStateBase interface
	virtual void AddPlayerState(APlayerState* PlayerState) override;
	virtual void RemovePlayerState(APlayerState* PlayerState) override;
	virtual void SeamlessTravelTransitionCheckpoint(bool bToTransitionMap) override;
	//~End of AGameStateBase interface

	//~IAbilitySystemInterface
	virtual UAbilitySystemComponent* GetAbilitySystemComponent() const override;
	//~End of IAbilitySystemInterface

	/** 获取用于游戏级别内容（主要是 GameplayCue）的 AbilitySystem 组件 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|GameState")
	UDJ01AbilitySystemComponent* GetDJ01AbilitySystemComponent() const { return AbilitySystemComponent; }

	// TODO: VerbMessage系统需要迁移
	// Send a message that all clients will (probably) get
	// (use only for client notifications like eliminations, server join messages, etc... that can handle being lost)
	// UFUNCTION(NetMulticast, Unreliable, BlueprintCallable, Category = "DJ01|GameState")
	// void MulticastMessageToClients(const FDJ01VerbMessage Message);

	// Send a message that all clients will be guaranteed to get
	// (use only for client notifications that cannot handle being lost)
	// UFUNCTION(NetMulticast, Reliable, BlueprintCallable, Category = "DJ01|GameState")
	// void MulticastReliableMessageToClients(const FDJ01VerbMessage Message);

	// Gets the server's FPS, replicated to clients
	float GetServerFPS() const;

	// Indicate the local player state is recording a replay
	void SetRecorderPlayerState(APlayerState* NewPlayerState);

	// Gets the player state that recorded the replay, if valid
	APlayerState* GetRecorderPlayerState() const;

	// Delegate called when the replay player state changes
	DECLARE_MULTICAST_DELEGATE_OneParam(FOnRecorderPlayerStateChanged, APlayerState*);
	FOnRecorderPlayerStateChanged OnRecorderPlayerStateChangedEvent;

private:
	/** 处理加载和管理当前 Gameplay Experience */
	UPROPERTY()
	TObjectPtr<UDJ01ExperienceManagerComponent> ExperienceManagerComponent;

	/** 用于游戏级别内容（主要是 GameplayCue）的 AbilitySystem 组件 */
	UPROPERTY(VisibleAnywhere, Category = "DJ01|GameState")
	TObjectPtr<UDJ01AbilitySystemComponent> AbilitySystemComponent;

protected:
	UPROPERTY(Replicated)
	float ServerFPS;

	// The player state that recorded a replay, it is used to select the right pawn to follow
	// This is only set in replay streams and is not replicated normally
	UPROPERTY(Transient, ReplicatedUsing = OnRep_RecorderPlayerState)
	TObjectPtr<APlayerState> RecorderPlayerState;

	UFUNCTION()
	void OnRep_RecorderPlayerState();

};
