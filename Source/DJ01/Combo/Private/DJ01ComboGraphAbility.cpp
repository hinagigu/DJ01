// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Combo/Public/DJ01ComboGraphAbility.h"
#include "Abilities/Tasks/ComboGraphAbilityTask_StartGraph.h"
#include "Graph/ComboGraph.h"
#include "Graph/ComboGraphNodeAnimBase.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01ComboGraphAbility)

UDJ01ComboGraphAbility::UDJ01ComboGraphAbility(const FObjectInitializer& ObjectInitializer)
    : Super(ObjectInitializer)
{
    // 连招技能的默认设置
    ActivationPolicy = EDJ01AbilityActivationPolicy::OnInputTriggered;
    // 使用 Blocking 防止连招被自己重复激活取消
    // 连招期间的后续输入由 ComboGraph 内部处理转换
    ActivationGroup = EDJ01AbilityActivationGroup::Exclusive_Blocking;
}

UComboGraphNodeAnimBase* UDJ01ComboGraphAbility::GetCurrentComboNode() const
{
    if (ComboTask)
    {
        return ComboTask->GetCurrentNode();
    }
    return nullptr;
} 

UComboGraphNodeAnimBase* UDJ01ComboGraphAbility::GetPreviousComboNode() const
{
    if (ComboTask)
    {
        return ComboTask->GetPreviousNode();
    }
    return nullptr;
}

bool UDJ01ComboGraphAbility::IsComboGraphRunning() const
{
    return ComboTask != nullptr && ComboTask->IsActive();
}

void UDJ01ComboGraphAbility::ActivateAbility(
    const FGameplayAbilitySpecHandle Handle,
    const FGameplayAbilityActorInfo* ActorInfo,
    const FGameplayAbilityActivationInfo ActivationInfo,
    const FGameplayEventData* TriggerEventData)
{
    Super::ActivateAbility(Handle, ActorInfo, ActivationInfo, TriggerEventData);

    if (!ComboGraph)
    {
        UE_LOG(LogTemp, Warning, TEXT("UDJ01ComboGraphAbility::ActivateAbility - ComboGraph is null for %s"), *GetName());
        CancelAbility(Handle, ActorInfo, ActivationInfo, true);
        return;
    }

    if (!CommitAbility(Handle, ActorInfo, ActivationInfo))
    {
        CancelAbility(Handle, ActorInfo, ActivationInfo, true);
        return;
    }

    // 尝试从 TriggerEventData 获取 InitialInputAction
    UInputAction* ResolvedInitialInput = InitialInputAction;
    if (TriggerEventData && TriggerEventData->OptionalObject2)
    {
        if (UInputAction* EventInputAction = const_cast<UInputAction*>(Cast<const UInputAction>(TriggerEventData->OptionalObject2)))
        {
            ResolvedInitialInput = EventInputAction;
        }
    }

    // 调试日志
    UE_LOG(LogTemp, Warning, TEXT("[ComboGraph] ActivateAbility - ComboGraph: %s"), *GetNameSafe(ComboGraph));
    UE_LOG(LogTemp, Warning, TEXT("[ComboGraph] ActivateAbility - InitialInputAction: %s"), *GetNameSafe(InitialInputAction));
    UE_LOG(LogTemp, Warning, TEXT("[ComboGraph] ActivateAbility - ResolvedInitialInput: %s"), *GetNameSafe(ResolvedInitialInput));
    UE_LOG(LogTemp, Warning, TEXT("[ComboGraph] ActivateAbility - bBroadcastInternalEvents: %s"), bBroadcastInternalEvents ? TEXT("true") : TEXT("false"));

    ComboTask = UComboGraphAbilityTask_StartGraph::CreateStartComboGraph(
        this,
        ComboGraph,
        ResolvedInitialInput,
        bBroadcastInternalEvents
    );

    if (!ComboTask)
    {
        UE_LOG(LogTemp, Error, TEXT("UDJ01ComboGraphAbility::ActivateAbility - Failed to create ComboGraph task for %s"), *GetName());
        CancelAbility(Handle, ActorInfo, ActivationInfo, true);
        return;
    }

    ComboTask->OnGraphStart.AddDynamic(this, &UDJ01ComboGraphAbility::HandleGraphStart);
    ComboTask->OnGraphEnd.AddDynamic(this, &UDJ01ComboGraphAbility::HandleGraphEnd);
    ComboTask->EventReceived.AddDynamic(this, &UDJ01ComboGraphAbility::HandleEventReceived);

    CachedPreviousNode = nullptr;
    ComboTask->ReadyForActivation();
}

void UDJ01ComboGraphAbility::EndAbility(
    const FGameplayAbilitySpecHandle Handle,
    const FGameplayAbilityActorInfo* ActorInfo,
    const FGameplayAbilityActivationInfo ActivationInfo,
    bool bReplicateEndAbility,
    bool bWasCancelled)
{
    if (ComboTask)
    {
        if (ComboTask->IsActive())
        {
            ComboTask->EndTask();
        }
        ComboTask = nullptr;
    }
    CachedPreviousNode = nullptr;

    Super::EndAbility(Handle, ActorInfo, ActivationInfo, bReplicateEndAbility, bWasCancelled);
}

void UDJ01ComboGraphAbility::HandleGraphStart(FGameplayTag EventTag, FGameplayEventData EventData)
{
    UE_LOG(LogTemp, Warning, TEXT("[ComboGraph] ★ HandleGraphStart - EventTag: %s"), *EventTag.ToString());
    OnComboGraphStarted();
    K2_OnComboGraphStarted();
}

void UDJ01ComboGraphAbility::HandleGraphEnd(FGameplayTag EventTag, FGameplayEventData EventData)
{
    const bool bWasCancelled = !IsActive();
    UE_LOG(LogTemp, Warning, TEXT("[ComboGraph] ★ HandleGraphEnd - EventTag: %s, WasCancelled: %s"), 
        *EventTag.ToString(), bWasCancelled ? TEXT("true") : TEXT("false"));
    
    OnComboGraphEnded(bWasCancelled);
    K2_OnComboGraphEnded(bWasCancelled);

    if (bEndAbilityOnGraphEnd)
    {
        EndAbility(CurrentSpecHandle, CurrentActorInfo, CurrentActivationInfo, true, bWasCancelled);
    }
}

void UDJ01ComboGraphAbility::HandleEventReceived(FGameplayTag EventTag, FGameplayEventData EventData)
{
    UE_LOG(LogTemp, Warning, TEXT("[ComboGraph] ★★ HandleEventReceived - EventTag: %s"), *EventTag.ToString());
    
    // 触发 Effects 系统
    TArray<AActor*> Targets;
    if (const AActor* TargetActor = EventData.Target.Get())
    {
        Targets.Add(const_cast<AActor*>(TargetActor));
    }
    TriggerEffectsByEvent(EventTag, Targets);

    UComboGraphNodeAnimBase* CurrentNode = GetCurrentComboNode();
    UE_LOG(LogTemp, Warning, TEXT("[ComboGraph] CurrentNode: %s, CachedPreviousNode: %s"), 
        *GetNameSafe(CurrentNode), *GetNameSafe(CachedPreviousNode));
    
    if (CurrentNode && CurrentNode != CachedPreviousNode)
    {
        UE_LOG(LogTemp, Warning, TEXT("[ComboGraph] ★★★ Node Changed! %s -> %s"), 
            *GetNameSafe(CachedPreviousNode), *GetNameSafe(CurrentNode));
        OnComboNodeChanged(CachedPreviousNode, CurrentNode);
        K2_OnComboNodeChanged(CachedPreviousNode, CurrentNode);
        CachedPreviousNode = CurrentNode;
    }

    K2_OnComboEventReceived(EventTag, EventData);
}

void UDJ01ComboGraphAbility::OnComboGraphStarted() {}
void UDJ01ComboGraphAbility::OnComboGraphEnded(bool bWasCancelled) {}
void UDJ01ComboGraphAbility::OnComboNodeChanged(UComboGraphNodeAnimBase* PreviousNode, UComboGraphNodeAnimBase* NewNode) {}