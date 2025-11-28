// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Team/Public/DJ01TeamComponent.h"
#include "DJ01/Team/Public/DJ01TeamAgentInterface.h"
#include "Engine/World.h"
#include "Net/UnrealNetwork.h"
#include "GameFramework/Actor.h"

UDJ01TeamComponent::UDJ01TeamComponent()
{
    PrimaryComponentTick.bCanEverTick = false;
    SetIsReplicatedByDefault(true);
    
    // 默认为无团队配置
    TeamConfig = FDJ01TeamConfig();
}

void UDJ01TeamComponent::BeginPlay()
{
    Super::BeginPlay();
    
    // 在BeginPlay时广播初始团队状态
    BroadcastTeamChanged(FDJ01TeamConfig(), TeamConfig);
}

void UDJ01TeamComponent::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    
    DOREPLIFETIME(UDJ01TeamComponent, TeamConfig);
}

void UDJ01TeamComponent::SetTeamConfig(const FDJ01TeamConfig& NewConfig)
{
    const FDJ01TeamConfig OldConfig = TeamConfig;
    
    // 只有在Server端或者单机模式下才能修改
    if (GetOwner()->HasAuthority())
    {
        TeamConfig = NewConfig;
        BroadcastTeamChanged(OldConfig, NewConfig);
    }
    else
    {
        UE_LOG(LogTemp, Warning, TEXT("UDJ01TeamComponent::SetTeamConfig - Only server can change team config"));
    }
}

bool UDJ01TeamComponent::CanAttackActor(AActor* TargetActor) const
{
    if (!TargetActor)
    {
        return false;
    }
    
    // 查找目标Actor的团队组件
    if (UDJ01TeamComponent* TargetTeamComp = TargetActor->FindComponentByClass<UDJ01TeamComponent>())
    {
        return TeamConfig.CanAttack(TargetTeamComp->GetTeamConfig().MyTeam);
    }
    
    // 检查目标是否直接实现了团队接口
    if (IDJ01TeamAgentInterface* TeamInterface = Cast<IDJ01TeamAgentInterface>(TargetActor))
    {
        return TeamConfig.CanAttack(TeamInterface->GetTeamConfig().MyTeam);
    }
    
    // 如果目标没有团队信息，根据设计决定是否可以攻击
    // 这里默认不能攻击没有团队信息的目标
    return false;
}

bool UDJ01TeamComponent::IsFriendlyToActor(AActor* TargetActor) const
{
    if (!TargetActor)
    {
        return false;
    }
    
    // 查找目标Actor的团队组件
    if (UDJ01TeamComponent* TargetTeamComp = TargetActor->FindComponentByClass<UDJ01TeamComponent>())
    {
        return TeamConfig.IsFriendly(TargetTeamComp->GetTeamConfig().MyTeam);
    }
    
    // 检查目标是否直接实现了团队接口
    if (IDJ01TeamAgentInterface* TeamInterface = Cast<IDJ01TeamAgentInterface>(TargetActor))
    {
        return TeamConfig.IsFriendly(TeamInterface->GetTeamConfig().MyTeam);
    }
    
    // 如果目标没有团队信息，默认为中立（友好）
    return true;
}

void UDJ01TeamComponent::OnRep_TeamConfig(const FDJ01TeamConfig& OldConfig)
{
    BroadcastTeamChanged(OldConfig, TeamConfig);
}

void UDJ01TeamComponent::BroadcastTeamChanged(const FDJ01TeamConfig& OldConfig, const FDJ01TeamConfig& NewConfig)
{
    // 只有在团队确实发生变化时才广播
    if (OldConfig.MyTeam != NewConfig.MyTeam || OldConfig.AttackMask != NewConfig.AttackMask)
    {
        OnTeamConfigChanged.Broadcast(GetOwner(), OldConfig, NewConfig);
    }
}