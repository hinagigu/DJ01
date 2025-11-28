// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "Subsystems/WorldSubsystem.h"
#include "DJ01TeamTypes.h"
#include "DJ01TeamSubsystem.generated.h"

/** 简化的团队关系比较结果 */
UENUM(BlueprintType)
enum class EDJ01TeamRelation : uint8
{
    /** 同一团队 */
    SameTeam,
    
    /** 敌对团队 */
    Hostile,
    
    /** 友好/中立团队 */
    Friendly,
    
    /** 无效对象 */
    Invalid
};

/**
 * DJ01团队子系统 - 提供全局团队查询和管理功能
 * 保持简洁，主要提供便捷的静态查询方法
 */
UCLASS()
class DJ01_API UDJ01TeamSubsystem : public UWorldSubsystem
{
    GENERATED_BODY()

public:
    /** 比较两个对象的团队关系 */
    UFUNCTION(BlueprintCallable, Category = "Team", meta=(ExpandEnumAsExecs=ReturnValue))
    EDJ01TeamRelation CompareTeamRelation(const UObject* ObjectA, const UObject* ObjectB) const;
    
    /** 判断A是否可以攻击B */
    UFUNCTION(BlueprintCallable, Category = "Team")
    bool CanObjectAttackObject(const UObject* Attacker, const UObject* Target) const;
    
    /** 判断两个对象是否是友军 */
    UFUNCTION(BlueprintCallable, Category = "Team")
    bool AreObjectsFriendly(const UObject* ObjectA, const UObject* ObjectB) const;
    
    /** 获取对象的团队配置 */
    UFUNCTION(BlueprintCallable, Category = "Team")
    bool GetObjectTeamConfig(const UObject* Object, FDJ01TeamConfig& OutTeamConfig) const;

    /** 静态便捷方法 */
    static UDJ01TeamSubsystem* Get(const UWorld* World);
    static EDJ01TeamRelation GetTeamRelation(const UWorld* World, const UObject* ObjectA, const UObject* ObjectB);
    static bool CanAttack(const UWorld* World, const UObject* Attacker, const UObject* Target);
};