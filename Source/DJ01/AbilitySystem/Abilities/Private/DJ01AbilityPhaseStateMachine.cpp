// ============================================================
// DJ01AbilityPhaseStateMachine.cpp
// 技能阶段状态机实现
// ============================================================

#include "DJ01/AbilitySystem/Abilities/Public/DJ01AbilityPhaseStateMachine.h"
#include "DJ01/AbilitySystem/Abilities/Public/DJ01GameplayAbility.h"
#include "DJ01/System/Public/DJ01LogChannels.h"
#include "AbilitySystemComponent.h"
#include "Engine/World.h"
#include "TimerManager.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01AbilityPhaseStateMachine)

UDJ01AbilityPhaseStateMachine::UDJ01AbilityPhaseStateMachine()
{
}

// ============================================================
// 生命周期
// ============================================================

void UDJ01AbilityPhaseStateMachine::Initialize(UDJ01GameplayAbility* InOwnerAbility, const FDJ01AbilityPhaseConfig& InConfig)
{
    OwnerAbility = InOwnerAbility;
    Config = InConfig;
    CurrentPhase = EDJ01AbilityPhase::None;
    PreviousPhase = EDJ01AbilityPhase::None;
    bIsRunning = false;

    UE_LOG(LogDJ01AbilitySystem, Verbose, 
        TEXT("PhaseStateMachine: Initialized for ability [%s]"), 
        InOwnerAbility ? *InOwnerAbility->GetName() : TEXT("None"));
}

void UDJ01AbilityPhaseStateMachine::Start()
{
    if (bIsRunning)
    {
        UE_LOG(LogDJ01AbilitySystem, Warning, TEXT("PhaseStateMachine: Already running"));
        return;
    }

    bIsRunning = true;

    // 决定起始阶段：检查 Startup 是否有意义（有配置时长、Montage 或 Tags）
    const bool bHasStartupPhase = 
        Config.Startup.GetEffectiveDuration() > 0.0f || 
        Config.Startup.HasMontage() ||
        Config.Startup.PhaseTags.Num() > 0 ||
        Config.Startup.TimingMode == EDJ01PhaseTimingMode::Manual;

    if (bHasStartupPhase)
    {
        TransitionToPhase(EDJ01AbilityPhase::Startup);
    }
    else
    {
        TransitionToPhase(EDJ01AbilityPhase::Active);
    }
}

void UDJ01AbilityPhaseStateMachine::Shutdown()
{
    if (!bIsRunning)
    {
        return;
    }

    ClearPhaseTimer();

    // 清理当前阶段的 Tag
    if (CurrentPhase != EDJ01AbilityPhase::None)
    {
        ApplyPhaseTags(CurrentPhase, false);
    }

    bIsRunning = false;
    CurrentPhase = EDJ01AbilityPhase::None;
    PreviousPhase = EDJ01AbilityPhase::None;

    UE_LOG(LogDJ01AbilitySystem, Verbose, TEXT("PhaseStateMachine: Shutdown"));
}

// ============================================================
// 阶段控制
// ============================================================

bool UDJ01AbilityPhaseStateMachine::TransitionToPhase(EDJ01AbilityPhase NewPhase, bool bForce)
{
    // 验证转换是否有效
    if (!bForce && !IsValidPhaseTransition(CurrentPhase, NewPhase))
    {
        UE_LOG(LogDJ01AbilitySystem, Warning,
            TEXT("PhaseStateMachine: Invalid transition from %s to %s"),
            *GetAbilityPhaseName(CurrentPhase), *GetAbilityPhaseName(NewPhase));
        return false;
    }

    EDJ01AbilityPhase OldPhase = CurrentPhase;

    // 退出当前阶段
    if (OldPhase != EDJ01AbilityPhase::None)
    {
        HandlePhaseExit(OldPhase);
    }

    // 清理计时器
    ClearPhaseTimer();

    // 切换阶段
    PreviousPhase = OldPhase;
    CurrentPhase = NewPhase;

    // 进入新阶段
    HandlePhaseEnter(NewPhase);

    // 广播阶段变化
    OnPhaseChanged.Broadcast(OldPhase, NewPhase);

    // 如果是结束阶段，通知状态机完成
    if (NewPhase == EDJ01AbilityPhase::Ended)
    {
        OnFinished.Broadcast();
    }

    return true;
}

bool UDJ01AbilityPhaseStateMachine::CanCurrentPhaseBeInterrupted() const
{
    if (const FDJ01AbilityPhaseInfo* PhaseInfo = Config.GetPhaseInfo(CurrentPhase))
    {
        return PhaseInfo->bCanBeInterrupted;
    }
    return true;
}

bool UDJ01AbilityPhaseStateMachine::CanCurrentPhaseCancelInto() const
{
    if (const FDJ01AbilityPhaseInfo* PhaseInfo = Config.GetPhaseInfo(CurrentPhase))
    {
        return PhaseInfo->bCanCancelInto;
    }
    return false;
}

float UDJ01AbilityPhaseStateMachine::GetCurrentPhaseRemainingTime() const
{
    if (!bIsRunning || !PhaseTimerHandle.IsValid())
    {
        return 0.0f;
    }

    if (UWorld* World = GetWorld())
    {
        return World->GetTimerManager().GetTimerRemaining(PhaseTimerHandle);
    }
    return 0.0f;
}

void UDJ01AbilityPhaseStateMachine::SkipCurrentPhase()
{
    if (!bIsRunning)
    {
        return;
    }

    // 清除计时器并立即触发到期
    ClearPhaseTimer();
    OnPhaseTimerExpired();
}

// ============================================================
// 内部方法
// ============================================================

void UDJ01AbilityPhaseStateMachine::HandlePhaseEnter(EDJ01AbilityPhase Phase)
{
    UE_LOG(LogDJ01AbilitySystem, Verbose,
        TEXT("PhaseStateMachine: Entered phase %s"), *GetAbilityPhaseName(Phase));

    CurrentPhaseStartTime = GetWorld() ? GetWorld()->GetTimeSeconds() : 0.0f;

    // 应用阶段 Tag
    ApplyPhaseTags(Phase, true);

    // 广播进入事件
    OnPhaseEnter.Broadcast(Phase);

    // 根据 TimingMode 设置阶段计时器
    if (const FDJ01AbilityPhaseInfo* PhaseInfo = Config.GetPhaseInfo(Phase))
    {
        // Manual 模式不设置定时器
        if (!PhaseInfo->ShouldAutoTransition())
        {
            UE_LOG(LogDJ01AbilitySystem, Verbose,
                TEXT("PhaseStateMachine: Phase %s is in Manual mode, waiting for script control"),
                *GetAbilityPhaseName(Phase));
            return;
        }

        // 获取实际持续时间
        const float EffectiveDuration = PhaseInfo->GetEffectiveDuration();
		
        if (EffectiveDuration > 0.0f)
        {
            if (UWorld* World = GetWorld())
            {
                World->GetTimerManager().SetTimer(
                    PhaseTimerHandle,
                    this,
                    &UDJ01AbilityPhaseStateMachine::OnPhaseTimerExpired,
                    EffectiveDuration,
                    false
                );

                UE_LOG(LogDJ01AbilitySystem, Verbose,
                    TEXT("PhaseStateMachine: Phase %s timer set for %.2fs (Mode: %s)"),
                    *GetAbilityPhaseName(Phase), 
                    EffectiveDuration,
                    PhaseInfo->TimingMode == EDJ01PhaseTimingMode::UseMontageLength ? TEXT("Montage") : TEXT("Auto"));
            }
        }
        else if (EffectiveDuration == 0.0f)
        {
            // Duration = 0 表示瞬时，立即切换到下一阶段
            // 使用 NextTick 避免递归调用
            if (UWorld* World = GetWorld())
            {
                World->GetTimerManager().SetTimerForNextTick(this, &UDJ01AbilityPhaseStateMachine::OnPhaseTimerExpired);
            }
        }
    }
}

void UDJ01AbilityPhaseStateMachine::HandlePhaseExit(EDJ01AbilityPhase Phase)
{
    UE_LOG(LogDJ01AbilitySystem, Verbose,
        TEXT("PhaseStateMachine: Exited phase %s"), *GetAbilityPhaseName(Phase));

    // 移除阶段 Tag
    ApplyPhaseTags(Phase, false);

    // 广播退出事件
    OnPhaseExit.Broadcast(Phase);
}

void UDJ01AbilityPhaseStateMachine::OnPhaseTimerExpired()
{
    if (!bIsRunning)
    {
        return;
    }

    EDJ01AbilityPhase NextPhase = GetNextAutoPhase();
    if (NextPhase != EDJ01AbilityPhase::None)
    {
        TransitionToPhase(NextPhase);
    }
}

void UDJ01AbilityPhaseStateMachine::ClearPhaseTimer()
{
    if (PhaseTimerHandle.IsValid())
    {
        if (UWorld* World = GetWorld())
        {
            World->GetTimerManager().ClearTimer(PhaseTimerHandle);
        }
        PhaseTimerHandle.Invalidate();
    }
}

EDJ01AbilityPhase UDJ01AbilityPhaseStateMachine::GetNextAutoPhase() const
{
    switch (CurrentPhase)
    {
    case EDJ01AbilityPhase::Startup:
        return EDJ01AbilityPhase::Active;

    case EDJ01AbilityPhase::Active:
        {
            // 检查 Recovery 是否有意义
            const bool bHasRecoveryPhase = 
                Config.Recovery.GetEffectiveDuration() > 0.0f || 
                Config.Recovery.HasMontage() ||
                Config.Recovery.PhaseTags.Num() > 0 ||
                Config.Recovery.TimingMode == EDJ01PhaseTimingMode::Manual;

            return bHasRecoveryPhase ? EDJ01AbilityPhase::Recovery : EDJ01AbilityPhase::Ended;
        }

    case EDJ01AbilityPhase::Recovery:
        return EDJ01AbilityPhase::Ended;

    case EDJ01AbilityPhase::Cooldown:
        return EDJ01AbilityPhase::Ended;

    default:
        return EDJ01AbilityPhase::None;
    }
}

void UDJ01AbilityPhaseStateMachine::ApplyPhaseTags(EDJ01AbilityPhase Phase, bool bAdd)
{
    const FDJ01AbilityPhaseInfo* PhaseInfo = Config.GetPhaseInfo(Phase);
    if (!PhaseInfo || PhaseInfo->PhaseTags.Num() == 0)
    {
        return;
    }

    UDJ01GameplayAbility* Ability = OwnerAbility.Get();
    if (!Ability)
    {
        return;
    }

    UAbilitySystemComponent* ASC = Ability->GetAbilitySystemComponentFromActorInfo();
    if (!ASC)
    {
        return;
    }

    if (bAdd)
    {
        ASC->AddLooseGameplayTags(PhaseInfo->PhaseTags);
    }
    else
    {
        ASC->RemoveLooseGameplayTags(PhaseInfo->PhaseTags);
    }
}

UWorld* UDJ01AbilityPhaseStateMachine::GetWorld() const
{
    if (UDJ01GameplayAbility* Ability = OwnerAbility.Get())
    {
        return Ability->GetWorld();
    }
    return nullptr;
}

bool UDJ01AbilityPhaseStateMachine::IsTransitionValid(EDJ01AbilityPhase From, EDJ01AbilityPhase To) const
{
    return IsValidPhaseTransition(From, To);
}