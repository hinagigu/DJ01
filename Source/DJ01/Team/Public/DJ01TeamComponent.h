// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "Components/ActorComponent.h"
#include "Net/Serialization/FastArraySerializer.h"
#include "DJ01TeamTypes.h"
#include "DJ01TeamAgentInterface.h"
#include "DJ01TeamComponent.generated.h"

/**
 * DJ01团队组件 - 为Actor提供团队功能的组件
 * 可以挂载到任何需要团队功能的Actor上
 */
UCLASS(BlueprintType, ClassGroup=(Team), meta=(BlueprintSpawnableComponent))
class DJ01_API UDJ01TeamComponent : public UActorComponent, public IDJ01TeamAgentInterface
{
    GENERATED_BODY()

public:
    UDJ01TeamComponent();

    //~UActorComponent interface
    virtual void BeginPlay() override;
    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;
    //~End of UActorComponent interface

    //~IDJ01TeamAgentInterface interface
    virtual FDJ01TeamConfig GetTeamConfig() const override { return TeamConfig; }
    virtual void SetTeamConfig(const FDJ01TeamConfig& NewConfig) override;
    virtual FDJ01TeamConfigChangedDelegate* GetTeamChangedDelegate() override { return &OnTeamConfigChanged; }
    //~End of IDJ01TeamAgentInterface interface
    
    //~IGenericTeamAgentInterface interface
    // 使用接口中的默认实现即可，无需重写，除非有特殊需求
    //~End of IGenericTeamAgentInterface interface

    /** 蓝图访问 */
    UFUNCTION(BlueprintCallable, Category = "Team")
    FDJ01TeamConfig GetTeamConfiguration() const { return TeamConfig; }
    
    UFUNCTION(BlueprintCallable, Category = "Team")
    void SetTeamConfiguration(const FDJ01TeamConfig& NewConfig) { SetTeamConfig(NewConfig); }
    
    UFUNCTION(BlueprintCallable, Category = "Team")
    bool CanAttackActor(AActor* TargetActor) const;
    
    UFUNCTION(BlueprintCallable, Category = "Team")
    bool IsFriendlyToActor(AActor* TargetActor) const;

public:
    /** 团队配置变化时触发 */
    UPROPERTY(BlueprintAssignable, Category = "Team")
    FDJ01TeamConfigChangedDelegate OnTeamConfigChanged;

protected:
    /** 当前团队配置 */
    UPROPERTY(EditAnywhere, BlueprintReadOnly, Replicated, Category = "Team")
    FDJ01TeamConfig TeamConfig;

    UFUNCTION()
    void OnRep_TeamConfig(const FDJ01TeamConfig& OldConfig);

private:
    void BroadcastTeamChanged(const FDJ01TeamConfig& OldConfig, const FDJ01TeamConfig& NewConfig);
};