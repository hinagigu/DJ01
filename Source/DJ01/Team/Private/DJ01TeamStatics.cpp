// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Team/Public/DJ01TeamStatics.h"
#include "DJ01/Team/Public/DJ01TeamAgentInterface.h"
#include "DJ01/Team/Public/DJ01TeamComponent.h"
#include "GameFramework/Actor.h"

bool UDJ01TeamStatics::CanConfigAttackTeam(const FDJ01TeamConfig& AttackerConfig, EDJ01Team TargetTeam)
{
    return AttackerConfig.CanAttack(TargetTeam);
}

bool UDJ01TeamStatics::AreConfigsFriendly(const FDJ01TeamConfig& ConfigA, const FDJ01TeamConfig& ConfigB)
{
    return DJ01Team::AreFriends(ConfigA, ConfigB);
}

bool UDJ01TeamStatics::AreConfigsHostile(const FDJ01TeamConfig& ConfigA, const FDJ01TeamConfig& ConfigB)
{
    return DJ01Team::AreEnemies(ConfigA, ConfigB);
}

bool UDJ01TeamStatics::GetActorTeamConfig(AActor* Actor, FDJ01TeamConfig& OutConfig)
{
    if (!Actor)
    {
        return false;
    }
    
    // 首先检查Actor是否直接实现了团队接口
    if (IDJ01TeamAgentInterface* TeamInterface = Cast<IDJ01TeamAgentInterface>(Actor))
    {
        OutConfig = TeamInterface->GetTeamConfig();
        return true;
    }
    
    // 查找团队组件
    if (UDJ01TeamComponent* TeamComp = Actor->FindComponentByClass<UDJ01TeamComponent>())
    {
        OutConfig = TeamComp->GetTeamConfig();
        return true;
    }
    
    return false;
}

void UDJ01TeamStatics::SetActorTeamConfig(AActor* Actor, const FDJ01TeamConfig& NewConfig)
{
    if (!Actor)
    {
        return;
    }
    
    // 首先检查Actor是否直接实现了团队接口
    if (IDJ01TeamAgentInterface* TeamInterface = Cast<IDJ01TeamAgentInterface>(Actor))
    {
        TeamInterface->SetTeamConfig(NewConfig);
        return;
    }
    
    // 查找团队组件
    if (UDJ01TeamComponent* TeamComp = Actor->FindComponentByClass<UDJ01TeamComponent>())
    {
        TeamComp->SetTeamConfig(NewConfig);
        return;
    }
    
    UE_LOG(LogTemp, Warning, TEXT("UDJ01TeamStatics::SetActorTeamConfig - Actor %s has no team interface or component"), 
           Actor ? *Actor->GetName() : TEXT("NULL"));
}

bool UDJ01TeamStatics::CanActorAttackActor(AActor* Attacker, AActor* Target)
{
    FDJ01TeamConfig AttackerConfig, TargetConfig;
    
    if (!GetActorTeamConfig(Attacker, AttackerConfig) || !GetActorTeamConfig(Target, TargetConfig))
    {
        return false;
    }
    
    return AttackerConfig.CanAttack(TargetConfig.MyTeam);
}

bool UDJ01TeamStatics::AreActorsFriendly(AActor* ActorA, AActor* ActorB)
{
    FDJ01TeamConfig ConfigA, ConfigB;
    
    if (!GetActorTeamConfig(ActorA, ConfigA) || !GetActorTeamConfig(ActorB, ConfigB))
    {
        return true; // 默认友好
    }
    
    return DJ01Team::AreFriends(ConfigA, ConfigB);
}

FString UDJ01TeamStatics::TeamConfigToString(const FDJ01TeamConfig& Config)
{
    FString TeamName = TeamEnumToString(Config.MyTeam);
    
    // 构建攻击目标列表
    TArray<FString> AttackTargets;
    
    for (int32 i = 0; i < 8; ++i) // 检查所有8个bit
    {
        uint8 TeamBit = 1 << i;
        if (Config.AttackMask & TeamBit)
        {
            EDJ01Team TargetTeam = static_cast<EDJ01Team>(TeamBit);
            AttackTargets.Add(TeamEnumToString(TargetTeam));
        }
    }
    
    FString AttackList = AttackTargets.Num() > 0 ? 
        FString::Join(AttackTargets, TEXT(", ")) : 
        TEXT("None");
    
    return FString::Printf(TEXT("Team: %s, Attacks: [%s]"), *TeamName, *AttackList);
}

FString UDJ01TeamStatics::TeamEnumToString(EDJ01Team Team)
{
    switch (Team)
    {
    case EDJ01Team::None:       return TEXT("None");
    case EDJ01Team::Player:     return TEXT("Player");
    case EDJ01Team::Monster:    return TEXT("Monster");
    case EDJ01Team::NPC:        return TEXT("NPC");
    case EDJ01Team::Boss:       return TEXT("Boss");
    case EDJ01Team::Neutral:    return TEXT("Neutral");
    case EDJ01Team::TeamRed:    return TEXT("TeamRed");
    case EDJ01Team::TeamBlue:   return TEXT("TeamBlue");
    case EDJ01Team::TeamGreen:  return TEXT("TeamGreen");
    default:                    return FString::Printf(TEXT("Unknown(%d)"), static_cast<int32>(Team));
    }
}