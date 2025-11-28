// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "Kismet/BlueprintFunctionLibrary.h"
#include "DJ01TeamTypes.h"
#include "DJ01TeamStatics.generated.h"

/**
 * DJ01团队静态函数库 - 为蓝图提供便捷的团队操作
 */
UCLASS()
class DJ01_API UDJ01TeamStatics : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:
    /** 创建预设团队配置 */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Team|Config")
    static FDJ01TeamConfig MakePlayerTeamConfig() { return FDJ01TeamConfig::MakePlayer(); }
    
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Team|Config")
    static FDJ01TeamConfig MakeMonsterTeamConfig() { return FDJ01TeamConfig::MakeMonster(); }
    
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Team|Config")
    static FDJ01TeamConfig MakeFriendlyNPCConfig() { return FDJ01TeamConfig::MakeFriendlyNPC(); }
    
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Team|Config")
    static FDJ01TeamConfig MakeNeutralConfig() { return FDJ01TeamConfig::MakeNeutral(); }

    /** 团队关系判断 */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Team|Relation")
    static bool CanConfigAttackTeam(const FDJ01TeamConfig& AttackerConfig, EDJ01Team TargetTeam);
    
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Team|Relation")
    static bool AreConfigsFriendly(const FDJ01TeamConfig& ConfigA, const FDJ01TeamConfig& ConfigB);
    
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Team|Relation") 
    static bool AreConfigsHostile(const FDJ01TeamConfig& ConfigA, const FDJ01TeamConfig& ConfigB);

    /** Actor级别的团队操作 */
    UFUNCTION(BlueprintCallable, Category = "Team|Actor")
    static bool GetActorTeamConfig(AActor* Actor, FDJ01TeamConfig& OutConfig);
    
    UFUNCTION(BlueprintCallable, Category = "Team|Actor")
    static void SetActorTeamConfig(AActor* Actor, const FDJ01TeamConfig& NewConfig);
    
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Team|Actor")
    static bool CanActorAttackActor(AActor* Attacker, AActor* Target);
    
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Team|Actor")
    static bool AreActorsFriendly(AActor* ActorA, AActor* ActorB);

    /** 工具函数 */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Team|Utility")
    static FString TeamConfigToString(const FDJ01TeamConfig& Config);
    
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Team|Utility")
    static FString TeamEnumToString(EDJ01Team Team);
};