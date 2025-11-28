// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Team/Public/DJ01TeamSubsystem.h"
#include "DJ01/Team/Public/DJ01TeamAgentInterface.h"
#include "DJ01/Team/Public/DJ01TeamComponent.h"
#include "GameFramework/Actor.h"
#include "Engine/World.h"

EDJ01TeamRelation UDJ01TeamSubsystem::CompareTeamRelation(const UObject* ObjectA, const UObject* ObjectB) const
{
    FDJ01TeamConfig ConfigA, ConfigB;
    
    const bool bFoundA = GetObjectTeamConfig(ObjectA, ConfigA);
    const bool bFoundB = GetObjectTeamConfig(ObjectB, ConfigB);
    
    if (!bFoundA || !bFoundB)
    {
        return EDJ01TeamRelation::Invalid;
    }
    
    // 检查是否同一团队
    if (ConfigA.MyTeam == ConfigB.MyTeam)
    {
        return EDJ01TeamRelation::SameTeam;
    }
    
    // 检查是否敌对（任一方可以攻击对方）
    if (ConfigA.CanAttack(ConfigB.MyTeam) || ConfigB.CanAttack(ConfigA.MyTeam))
    {
        return EDJ01TeamRelation::Hostile;
    }
    
    // 否则为友好/中立
    return EDJ01TeamRelation::Friendly;
}

bool UDJ01TeamSubsystem::CanObjectAttackObject(const UObject* Attacker, const UObject* Target) const
{
    FDJ01TeamConfig AttackerConfig, TargetConfig;
    
    if (!GetObjectTeamConfig(Attacker, AttackerConfig) || !GetObjectTeamConfig(Target, TargetConfig))
    {
        return false;
    }
    
    return AttackerConfig.CanAttack(TargetConfig.MyTeam);
}

bool UDJ01TeamSubsystem::AreObjectsFriendly(const UObject* ObjectA, const UObject* ObjectB) const
{
    FDJ01TeamConfig ConfigA, ConfigB;
    
    if (!GetObjectTeamConfig(ObjectA, ConfigA) || !GetObjectTeamConfig(ObjectB, ConfigB))
    {
        return true; // 默认为友好
    }
    
    return DJ01Team::AreFriends(ConfigA, ConfigB);
}

bool UDJ01TeamSubsystem::GetObjectTeamConfig(const UObject* Object, FDJ01TeamConfig& OutTeamConfig) const
{
    if (!Object)
    {
        return false;
    }
    
    // 首先检查是否直接实现了团队接口
    if (const IDJ01TeamAgentInterface* TeamInterface = Cast<IDJ01TeamAgentInterface>(Object))
    {
        OutTeamConfig = TeamInterface->GetTeamConfig();
        return true;
    }
    
    // 如果是Actor，查找团队组件
    if (const AActor* Actor = Cast<AActor>(Object))
    {
        if (const UDJ01TeamComponent* TeamComp = Actor->FindComponentByClass<UDJ01TeamComponent>())
        {
            OutTeamConfig = TeamComp->GetTeamConfig();
            return true;
        }
    }
    
    return false;
}

UDJ01TeamSubsystem* UDJ01TeamSubsystem::Get(const UWorld* World)
{
    if (World)
    {
        return World->GetSubsystem<UDJ01TeamSubsystem>();
    }
    return nullptr;
}

EDJ01TeamRelation UDJ01TeamSubsystem::GetTeamRelation(const UWorld* World, const UObject* ObjectA, const UObject* ObjectB)
{
    if (UDJ01TeamSubsystem* Subsystem = Get(World))
    {
        return Subsystem->CompareTeamRelation(ObjectA, ObjectB);
    }
    return EDJ01TeamRelation::Invalid;
}

bool UDJ01TeamSubsystem::CanAttack(const UWorld* World, const UObject* Attacker, const UObject* Target)
{
    if (UDJ01TeamSubsystem* Subsystem = Get(World))
    {
        return Subsystem->CanObjectAttackObject(Attacker, Target);
    }
    return false;
}