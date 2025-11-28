// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "AbilitySystemInterface.h"
#include "ModularPlayerState.h"
#include "DJ01/System/Public/GameplayTagStack.h"
#include "DJ01/Team/Public/DJ01TeamAgentInterface.h"
#include "GameplayTagContainer.h"

#include "DJ01PlayerState.generated.h"

struct FDJ01VerbMessage;

class AController;
class ADJ01PlayerController;
class APlayerState;
class FName;
class UAbilitySystemComponent;
class UDJ01AbilitySystemComponent;
class UDJ01ExperienceDefinition;
class UDJ01PawnData;
class UObject;
struct FFrame;
struct FGameplayTag;

/** Defines the types of client connected */
UENUM()
enum class EDJ01PlayerConnectionType : uint8
{
	// An active player
	Player = 0,

	// Spectator connected to a running game
	LiveSpectator,

	// Spectating a demo recording offline
	ReplaySpectator,

	// A deactivated player (disconnected)
	InactivePlayer
};

/**
* ADJ01PlayerState
*
*	Base player state class used by this project.
*	玩家状态类，持有玩家的 AbilitySystemComponent。
*	在Lyra架构中，ASC由PlayerState持有而非Pawn，这样可以在Pawn死亡/重生时保持技能状态。
*/
UCLASS(Config = Game)
class DJ01_API ADJ01PlayerState : public AModularPlayerState, public IAbilitySystemInterface, public IDJ01TeamAgentInterface
{
	GENERATED_BODY()

public:
	ADJ01PlayerState(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

	UFUNCTION(BlueprintCallable, Category = "DJ01|PlayerState")
	ADJ01PlayerController* GetDJ01PlayerController() const;

	/** 获取玩家的 AbilitySystemComponent */
	UFUNCTION(BlueprintCallable, Category = "DJ01|PlayerState")
	UDJ01AbilitySystemComponent* GetDJ01AbilitySystemComponent() const { return AbilitySystemComponent; }

	//~ Begin IAbilitySystemInterface
	virtual UAbilitySystemComponent* GetAbilitySystemComponent() const override;
	//~ End IAbilitySystemInterface

	template <class T>
	const T* GetPawnData() const { return Cast<T>(PawnData); }

	void SetPawnData(const UDJ01PawnData* InPawnData);

	//~AActor interface
	virtual void PreInitializeComponents() override;
	virtual void PostInitializeComponents() override;
	//~End of AActor interface

	//~APlayerState interface
	virtual void Reset() override;
	virtual void ClientInitialize(AController* C) override;
	virtual void CopyProperties(APlayerState* PlayerState) override;
	virtual void OnDeactivated() override;
	virtual void OnReactivated() override;
	//~End of APlayerState interface

	//~IDJ01TeamAgentInterface interface
	virtual void SetGenericTeamId(const FGenericTeamId& NewTeamID) override;
	virtual FGenericTeamId GetGenericTeamId() const override;
	virtual FDJ01TeamConfigChangedDelegate* GetTeamChangedDelegate() override;
	virtual void SetTeamConfig(const FDJ01TeamConfig& NewConfig) override;
	virtual FDJ01TeamConfig GetTeamConfig() const override;
	//~End of IDJ01TeamAgentInterface interface

	static const FName NAME_DJ01AbilityReady;

	void SetPlayerConnectionType(EDJ01PlayerConnectionType NewType);
	EDJ01PlayerConnectionType GetPlayerConnectionType() const { return MyPlayerConnectionType; }

	/** Returns the Squad ID of the squad the player belongs to. */
	UFUNCTION(BlueprintCallable)
	int32 GetSquadId() const
	{
		return MySquadID;
	}

	/** Returns the Team ID of the team the player belongs to. */
	UFUNCTION(BlueprintCallable)
	int32 GetTeamId() const
	{
		return GenericTeamIdToInteger(MyTeamID);
	}

	void SetSquadID(int32 NewSquadID);

	// Adds a specified number of stacks to the tag (does nothing if StackCount is below 1)
	UFUNCTION(BlueprintCallable, BlueprintAuthorityOnly, Category=Teams)
	void AddStatTagStack(FGameplayTag Tag, int32 StackCount);

	// Removes a specified number of stacks from the tag (does nothing if StackCount is below 1)
	UFUNCTION(BlueprintCallable, BlueprintAuthorityOnly, Category=Teams)
	void RemoveStatTagStack(FGameplayTag Tag, int32 StackCount);

	// Returns the stack count of the specified tag (or 0 if the tag is not present)
	UFUNCTION(BlueprintCallable, Category=Teams)
	int32 GetStatTagStackCount(FGameplayTag Tag) const;

	// Returns true if there is at least one stack of the specified tag
	UFUNCTION(BlueprintCallable, Category=Teams)
	bool HasStatTag(FGameplayTag Tag) const;

	// Send a message to just this player
	// (use only for client notifications like accolades, quest toasts, etc... that can handle being occasionally lost)
	// UFUNCTION(Client, Unreliable, BlueprintCallable, Category = "DJ01|PlayerState")
	// void ClientBroadcastMessage(const FLyraVerbMessage Message); // TODO: Messages

	// Gets the replicated view rotation of this player, used for spectating
	FRotator GetReplicatedViewRotation() const;

	// Sets the replicated view rotation, only valid on the server
	void SetReplicatedViewRotation(const FRotator& NewRotation);

private:
	void OnExperienceLoaded(const UDJ01ExperienceDefinition* CurrentExperience);

protected:
	UFUNCTION()
	void OnRep_PawnData();

protected:

	UPROPERTY(ReplicatedUsing = OnRep_PawnData)
	TObjectPtr<const UDJ01PawnData> PawnData;

private:

	/** 玩家的 AbilitySystemComponent，用于管理技能、属性和效果 */
	UPROPERTY(VisibleAnywhere, Category = "DJ01|PlayerState")
	TObjectPtr<UDJ01AbilitySystemComponent> AbilitySystemComponent;

	// TODO_ATTRIBUTE_SYSTEM: 属性集将在属性系统完成后添加
	// /** 生命属性集 */
	// UPROPERTY()
	// TObjectPtr<const class UDJ01HealthSet> HealthSet;
	// 
	// /** 战斗属性集 */
	// UPROPERTY()
	// TObjectPtr<const class UDJ01CombatSet> CombatSet;

	UPROPERTY(Replicated)
	EDJ01PlayerConnectionType MyPlayerConnectionType;

	UPROPERTY()
	FDJ01TeamConfigChangedDelegate OnTeamChangedDelegate;

	UPROPERTY(ReplicatedUsing=OnRep_MyTeamID)
	FGenericTeamId MyTeamID;

	UPROPERTY(ReplicatedUsing=OnRep_MySquadID)
	int32 MySquadID;

	UPROPERTY(Replicated)
	FGameplayTagStackContainer StatTags;

	UPROPERTY(Replicated)
	FRotator ReplicatedViewRotation;

private:
	UFUNCTION()
	void OnRep_MyTeamID(FGenericTeamId OldTeamID);

	UFUNCTION()
	void OnRep_MySquadID();
};
