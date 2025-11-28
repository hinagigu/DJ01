// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Player/Public/DJ01PlayerState.h"

#include "DJ01/Team/Public/DJ01TeamStatics.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilitySet.h"
// TODO_ATTRIBUTE_SYSTEM: 属性集将在属性系统完成后添加
// #include "DJ01/AbilitySystem/Attributes/Public/DJ01HealthSet.h"
// #include "DJ01/AbilitySystem/Attributes/Public/DJ01CombatSet.h"
#include "DJ01/Character/Public/DJ01PawnData.h"
#include "DJ01/Character/Public/DJ01PawnExtensionComponent.h"
#include "Components/GameFrameworkComponentManager.h"
#include "Engine/World.h"
#include "GameFramework/GameplayMessageSubsystem.h"
#include "DJ01/Experience/Public/DJ01ExperienceManagerComponent.h"
//@TODO: Would like to isolate this a bit better to get the pawn data in here without this having to know about other stuff
#include "DJ01/System/Public/DJ01GameMode.h"
#include "DJ01/System/Public/DJ01LogChannels.h"
#include "DJ01/Player/Public/DJ01PlayerController.h"
// #include "Messages/LyraVerbMessage.h" // TODO: Messages
#include "Net/UnrealNetwork.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01PlayerState)

class AController;
class APlayerState;
class FLifetimeProperty;

const FName ADJ01PlayerState::NAME_DJ01AbilityReady("DJ01AbilitiesReady");

ADJ01PlayerState::ADJ01PlayerState(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
	, MyPlayerConnectionType(EDJ01PlayerConnectionType::Player)
{
	// 创建 AbilitySystemComponent，玩家的ASC由PlayerState持有
	AbilitySystemComponent = ObjectInitializer.CreateDefaultSubobject<UDJ01AbilitySystemComponent>(this, TEXT("AbilitySystemComponent"));
	AbilitySystemComponent->SetIsReplicated(true);
	// Mixed模式：GameplayEffects复制给所有人，GameplayTags和GameplayCues复制给Owner
	AbilitySystemComponent->SetReplicationMode(EGameplayEffectReplicationMode::Mixed);

	// TODO_ATTRIBUTE_SYSTEM: 属性集将在属性系统完成后添加
	// 这些属性集会被 AbilitySystemComponent::InitializeComponent 自动检测并注册
	// HealthSet = CreateDefaultSubobject<UDJ01HealthSet>(TEXT("HealthSet"));
	// CombatSet = CreateDefaultSubobject<UDJ01CombatSet>(TEXT("CombatSet"));

	// AbilitySystemComponent 需要高频率网络更新以保证同步
	NetUpdateFrequency = 100.0f;

	MyTeamID = FGenericTeamId::NoTeam;
	MySquadID = INDEX_NONE;
}

void ADJ01PlayerState::PreInitializeComponents()
{
	Super::PreInitializeComponents();
}

void ADJ01PlayerState::Reset()
{
	Super::Reset();
}

void ADJ01PlayerState::ClientInitialize(AController* C)
{
	Super::ClientInitialize(C);

	if (UDJ01PawnExtensionComponent* PawnExtComp = UDJ01PawnExtensionComponent::FindPawnExtensionComponent(GetPawn()))
	{
		PawnExtComp->CheckDefaultInitialization();
	}
}

void ADJ01PlayerState::CopyProperties(APlayerState* PlayerState)
{
	Super::CopyProperties(PlayerState);

	//@TODO: Copy stats
}

void ADJ01PlayerState::OnDeactivated()
{
	bool bDestroyDeactivatedPlayerState = false;

	switch (GetPlayerConnectionType())
	{
		case EDJ01PlayerConnectionType::Player:
		case EDJ01PlayerConnectionType::InactivePlayer:
			//@TODO: Ask the experience if we should destroy disconnecting players immediately or leave them around
			// (e.g., for long running servers where they might build up if lots of players cycle through)
			bDestroyDeactivatedPlayerState = true;
			break;
		default:
			bDestroyDeactivatedPlayerState = true;
			break;
	}
	
	SetPlayerConnectionType(EDJ01PlayerConnectionType::InactivePlayer);

	if (bDestroyDeactivatedPlayerState)
	{
		Destroy();
	}
}

void ADJ01PlayerState::OnReactivated()
{
	if (GetPlayerConnectionType() == EDJ01PlayerConnectionType::InactivePlayer)
	{
		SetPlayerConnectionType(EDJ01PlayerConnectionType::Player);
	}
}

void ADJ01PlayerState::OnExperienceLoaded(const UDJ01ExperienceDefinition* /*CurrentExperience*/)
{
	if (ADJ01GameMode* DJ01GameMode = GetWorld()->GetAuthGameMode<ADJ01GameMode>())
	{
		if (const UDJ01PawnData* NewPawnData = DJ01GameMode->GetPawnDataForController(GetOwningController()))
		{
			SetPawnData(NewPawnData);
		}
		else
		{
			// UE_LOG(LogDJ01, Error, TEXT("ADJ01PlayerState::OnExperienceLoaded(): Unable to find PawnData to initialize player state [%s]!"), *GetNameSafe(this));
		}
	}
}

void ADJ01PlayerState::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
	Super::GetLifetimeReplicatedProps(OutLifetimeProps);

	FDoRepLifetimeParams SharedParams;
	SharedParams.bIsPushBased = true;

	DOREPLIFETIME_WITH_PARAMS_FAST(ThisClass, PawnData, SharedParams);
	DOREPLIFETIME_WITH_PARAMS_FAST(ThisClass, MyPlayerConnectionType, SharedParams)
	DOREPLIFETIME_WITH_PARAMS_FAST(ThisClass, MyTeamID, SharedParams);
	DOREPLIFETIME_WITH_PARAMS_FAST(ThisClass, MySquadID, SharedParams);

	SharedParams.Condition = ELifetimeCondition::COND_SkipOwner;
	DOREPLIFETIME_WITH_PARAMS_FAST(ThisClass, ReplicatedViewRotation, SharedParams);

	DOREPLIFETIME(ThisClass, StatTags);	
}

FRotator ADJ01PlayerState::GetReplicatedViewRotation() const
{
	// Could replace this with custom replication
	return ReplicatedViewRotation;
}

void ADJ01PlayerState::SetReplicatedViewRotation(const FRotator& NewRotation)
{
	if (NewRotation != ReplicatedViewRotation)
	{
		MARK_PROPERTY_DIRTY_FROM_NAME(ThisClass, ReplicatedViewRotation, this);
		ReplicatedViewRotation = NewRotation;
	}
}

ADJ01PlayerController* ADJ01PlayerState::GetDJ01PlayerController() const
{
	return Cast<ADJ01PlayerController>(GetOwner());
}

UAbilitySystemComponent* ADJ01PlayerState::GetAbilitySystemComponent() const
{
	return GetDJ01AbilitySystemComponent();
}

void ADJ01PlayerState::PostInitializeComponents()
{
	Super::PostInitializeComponents();

	// 初始化 ASC 的 ActorInfo
	// OwnerActor = PlayerState (技能的拥有者)
	// AvatarActor = Pawn (技能效果的实际执行者，此时可能还没有Pawn)
	check(AbilitySystemComponent);
	AbilitySystemComponent->InitAbilityActorInfo(this, GetPawn());

	UWorld* World = GetWorld();
	if (World && World->IsGameWorld() && World->GetNetMode() != NM_Client)
	{
		AGameStateBase* GameState = GetWorld()->GetGameState();
		check(GameState);
		UDJ01ExperienceManagerComponent* ExperienceComponent = GameState->FindComponentByClass<UDJ01ExperienceManagerComponent>();
		check(ExperienceComponent);
		ExperienceComponent->CallOrRegister_OnExperienceLoaded(FOnDJ01ExperienceLoaded::FDelegate::CreateUObject(this, &ThisClass::OnExperienceLoaded));
	}
}

void ADJ01PlayerState::SetPawnData(const UDJ01PawnData* InPawnData)
{
	check(InPawnData);

	if (GetLocalRole() != ROLE_Authority)
	{
		return;
	}

	if (PawnData)
	{
		// UE_LOG(LogDJ01, Error, TEXT("Trying to set PawnData [%s] on player state [%s] that already has valid PawnData [%s]."), *GetNameSafe(InPawnData), *GetNameSafe(this), *GetNameSafe(PawnData));
		return;
	}

	MARK_PROPERTY_DIRTY_FROM_NAME(ThisClass, PawnData, this);
	PawnData = InPawnData;

	// 将 PawnData 中定义的技能集授予给玩家
	for (const UDJ01AbilitySet* AbilitySet : PawnData->AbilitySets)
	{
		if (AbilitySet)
		{
			AbilitySet->GiveToAbilitySystem(AbilitySystemComponent, nullptr);
		}
	}

	UGameFrameworkComponentManager::SendGameFrameworkComponentExtensionEvent(this, NAME_DJ01AbilityReady);
	
	ForceNetUpdate();
}

void ADJ01PlayerState::OnRep_PawnData()
{
}

void ADJ01PlayerState::SetPlayerConnectionType(EDJ01PlayerConnectionType NewType)
{
	MARK_PROPERTY_DIRTY_FROM_NAME(ThisClass, MyPlayerConnectionType, this);
	MyPlayerConnectionType = NewType;
}

void ADJ01PlayerState::SetSquadID(int32 NewSquadId)
{
	if (HasAuthority())
	{
		MARK_PROPERTY_DIRTY_FROM_NAME(ThisClass, MySquadID, this);

		MySquadID = NewSquadId;
	}
}

void ADJ01PlayerState::SetGenericTeamId(const FGenericTeamId& NewTeamID)
{
	// 适配层：当外部系统（如AI）设置GenericID时，我们将其转换为默认的TeamConfig
	if (HasAuthority())
	{
		const FGenericTeamId OldTeamID = MyTeamID;
		MARK_PROPERTY_DIRTY_FROM_NAME(ThisClass, MyTeamID, this);
		MyTeamID = NewTeamID;
		
		if (OldTeamID != NewTeamID)
		{
			// 广播变更。注意：这里我们只能推断 Config
			FDJ01TeamConfig OldConfig;
			OldConfig.MyTeam = DJ01Team::FromGenericTeamId(OldTeamID);
			
			OnTeamChangedDelegate.Broadcast(this, OldConfig, GetTeamConfig());
		}
	}
}

FGenericTeamId ADJ01PlayerState::GetGenericTeamId() const
{
	return MyTeamID;
}

FDJ01TeamConfigChangedDelegate* ADJ01PlayerState::GetTeamChangedDelegate()
{
	return &OnTeamChangedDelegate;
}

void ADJ01PlayerState::SetTeamConfig(const FDJ01TeamConfig& NewConfig)
{
	if (HasAuthority())
	{
		// 将 Config 的 MyTeam 部分同步到 GenericTeamId 以便网络复制
		// 注意：AttackMask 目前没有被复制，如果需要支持复杂的敌对关系动态变化，
		// 你可能需要添加一个新的 Replicated 属性来存储 AttackMask
		SetGenericTeamId(DJ01Team::ToGenericTeamId(NewConfig.MyTeam));
	}
}

FDJ01TeamConfig ADJ01PlayerState::GetTeamConfig() const
{
	// 从 ID 重建 Config
	EDJ01Team Team = DJ01Team::FromGenericTeamId(MyTeamID);
	
	// 使用你的静态库获取默认配置（例如 Player 默认攻击 Monster）
	if (Team == EDJ01Team::Player) return FDJ01TeamConfig::MakePlayer();
	if (Team == EDJ01Team::Monster) return FDJ01TeamConfig::MakeMonster();
	if (Team == EDJ01Team::NPC) return FDJ01TeamConfig::MakeFriendlyNPC();
	if (Team == EDJ01Team::Neutral) return FDJ01TeamConfig::MakeNeutral();
	
	// 回退情况
	FDJ01TeamConfig Config;
	Config.MyTeam = Team;
	return Config;
}

void ADJ01PlayerState::OnRep_MyTeamID(FGenericTeamId OldTeamID)
{
	if (OldTeamID != MyTeamID)
	{
		FDJ01TeamConfig OldConfig;
		OldConfig.MyTeam = DJ01Team::FromGenericTeamId(OldTeamID);
		
		OnTeamChangedDelegate.Broadcast(this, OldConfig, GetTeamConfig());
	}
}

void ADJ01PlayerState::OnRep_MySquadID()
{
	//@TODO: Let the squad subsystem know (once that exists)
}

void ADJ01PlayerState::AddStatTagStack(FGameplayTag Tag, int32 StackCount)
{
	StatTags.AddStack(Tag, StackCount);
}

void ADJ01PlayerState::RemoveStatTagStack(FGameplayTag Tag, int32 StackCount)
{
	StatTags.RemoveStack(Tag, StackCount);
}

int32 ADJ01PlayerState::GetStatTagStackCount(FGameplayTag Tag) const
{
	return StatTags.GetStackCount(Tag);
}

bool ADJ01PlayerState::HasStatTag(FGameplayTag Tag) const
{
	return StatTags.ContainsTag(Tag);
}

// void ADJ01PlayerState::ClientBroadcastMessage_Implementation(const FLyraVerbMessage Message) // TODO: Messages
// {
// 	// This check is needed to prevent running the action when in standalone mode
// 	if (GetNetMode() == NM_Client)
// 	{
// 		// UGameplayMessageSubsystem::Get(this).BroadcastMessage(Message.Verb, Message);
// 	}
// }

