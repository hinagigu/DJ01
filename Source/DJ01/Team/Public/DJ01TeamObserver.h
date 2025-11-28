// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "Engine/CancellableAsyncAction.h"
#include "DJ01TeamTypes.h"
#include "DJ01TeamObserver.generated.h"

DECLARE_DYNAMIC_MULTICAST_DELEGATE_ThreeParams(FDJ01TeamChangedDelegate, 
    UObject*, TeamAgent, EDJ01Team, OldTeam, EDJ01Team, NewTeam);

/**
 * 简化版团队观察器 - 基于DJ01的位标志团队系统
 * 用于监听对象的团队变化
 */
UCLASS(BlueprintType)
class UDJ01TeamObserver : public UCancellableAsyncAction
{
    GENERATED_BODY()

public:
    UDJ01TeamObserver(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());


    // 观察指定对象的团队变化
    UFUNCTION(BlueprintCallable, meta=(BlueprintInternalUseOnly="true", Keywords="Watch"))
    static UDJ01TeamObserver* ObserveTeamChanges(UObject* TeamAgent);

    //~UBlueprintAsyncActionBase interface
    virtual void Activate() override;
    virtual void SetReadyToDestroy() override;
    //~End of UBlueprintAsyncActionBase interface

public:
    // 团队改变时触发
    UPROPERTY(BlueprintAssignable)
    FDJ01TeamChangedDelegate OnTeamChanged;

private:
    UFUNCTION()
    void OnTeamConfigChanged(UObject* Agent, FDJ01TeamConfig OldConfig, FDJ01TeamConfig NewConfig);

    TWeakObjectPtr<UObject> WatchedAgent;
};