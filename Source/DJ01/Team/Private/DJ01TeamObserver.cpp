// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Team/Public/DJ01TeamObserver.h"
#include "DJ01/Team/Public/DJ01TeamAgentInterface.h"
#include "Engine/World.h"

UDJ01TeamObserver::UDJ01TeamObserver(const FObjectInitializer& ObjectInitializer)
    : Super(ObjectInitializer)
{
}

UDJ01TeamObserver* UDJ01TeamObserver::ObserveTeamChanges(UObject* TeamAgent)
{
    UDJ01TeamObserver* Action = nullptr;

    if (TeamAgent)
    {
        if (UWorld* World = GEngine->GetWorldFromContextObject(TeamAgent, EGetWorldErrorMode::LogAndReturnNull))
        {
            Action = NewObject<UDJ01TeamObserver>();
            Action->WatchedAgent = TeamAgent;
            Action->RegisterWithGameInstance(World);
        }
    }

    return Action;
}

void UDJ01TeamObserver::Activate()
{
    Super::Activate();

    bool bCouldRegister = false;
    
    if (UObject* Agent = WatchedAgent.Get())
    {
        // 检查对象是否实现了团队接口
        if (IDJ01TeamAgentInterface* TeamInterface = Cast<IDJ01TeamAgentInterface>(Agent))
        {
            // 立即触发一次当前团队状态
            FDJ01TeamConfig CurrentConfig = TeamInterface->GetTeamConfig();
            OnTeamChanged.Broadcast(Agent, EDJ01Team::None, CurrentConfig.MyTeam);
            
            // 监听团队变化
            if (FDJ01TeamConfigChangedDelegate* Delegate = TeamInterface->GetTeamChangedDelegate())
            {
                Delegate->AddDynamic(this, &UDJ01TeamObserver::OnTeamConfigChanged);
                bCouldRegister = true;
            }
        }
        else
        {
            // 如果对象没有实现接口，发送None团队
            OnTeamChanged.Broadcast(Agent, EDJ01Team::None, EDJ01Team::None);
        }
    }

    if (!bCouldRegister)
    {
        // 如果无法注册监听，标记为完成
        SetReadyToDestroy();
    }
}

void UDJ01TeamObserver::SetReadyToDestroy()
{
    if (UObject* Agent = WatchedAgent.Get())
    {
        if (IDJ01TeamAgentInterface* TeamInterface = Cast<IDJ01TeamAgentInterface>(Agent))
        {
            if (FDJ01TeamConfigChangedDelegate* Delegate = TeamInterface->GetTeamChangedDelegate())
            {
                Delegate->RemoveDynamic(this, &UDJ01TeamObserver::OnTeamConfigChanged);
            }
        }
    }

    Super::SetReadyToDestroy();
}

void UDJ01TeamObserver::OnTeamConfigChanged(UObject* Agent, FDJ01TeamConfig OldConfig, FDJ01TeamConfig NewConfig)
{
    OnTeamChanged.Broadcast(Agent, OldConfig.MyTeam, NewConfig.MyTeam);
}