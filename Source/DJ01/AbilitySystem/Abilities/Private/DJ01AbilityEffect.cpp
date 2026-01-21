// ============================================================
// DJ01AbilityEffect.cpp
// 技能效果系统实现
// ============================================================

#include "DJ01/AbilitySystem/Abilities/Public/DJ01AbilityEffect.h"
#include "AbilitySystemComponent.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01AbilityEffect)

// ============================================================
// FDJ01EffectContext
// ============================================================

TArray<UAbilitySystemComponent*> FDJ01EffectContext::GetValidTargetASCs() const
{
    TArray<UAbilitySystemComponent*> Result;
    for (const TObjectPtr<UAbilitySystemComponent>& TargetASC : TargetASCs)
    {
        if (IsValid(TargetASC))
        {
            Result.Add(TargetASC.Get());
        }
    }
    return Result;
}

bool FDJ01EffectContext::HasValidTargets() const
{
    for (const TObjectPtr<UAbilitySystemComponent>& TargetASC : TargetASCs)
    {
        if (IsValid(TargetASC))
        {
            return true;
        }
    }
    return false;
}

// ============================================================
// FDJ01AbilityEffectEntry
// ============================================================

bool FDJ01AbilityEffectEntry::ShouldTrigger(EDJ01EffectPhase CurrentPhase, const FGameplayTag& CurrentEventTag) const
{
    // 效果无效或禁用
    if (!Effect || !Effect->bEnabled)
    {
        return false;
    }

    // 阶段不匹配
    if (Phase != CurrentPhase)
    {
        return false;
    }

    // OnAnimEvent 需要匹配事件 Tag
    if (Phase == EDJ01EffectPhase::OnAnimEvent)
    {
        // 如果没有指定 EventTag，则匹配所有动画事件
        if (!EventTag.IsValid())
        {
            return true;
        }
        // 检查事件 Tag 是否匹配（支持父子关系）
        return CurrentEventTag.MatchesTag(EventTag);
    }

    return true;
}

// ============================================================
// UDJ01AbilityEffect
// ============================================================

UDJ01AbilityEffect::UDJ01AbilityEffect()
{
    DisplayName = FText::FromString(TEXT("Effect"));
}

bool UDJ01AbilityEffect::Execute_Implementation(FDJ01EffectContext& Context)
{
    // 基类不执行任何操作，由子类实现
    return false;
}

FString UDJ01AbilityEffect::GetEffectDescription_Implementation() const
{
    return Description.ToString();
}

FText UDJ01AbilityEffect::GetEffectTypeName() const
{
    return FText::FromString(TEXT("Base Effect"));
}

#if WITH_EDITOR
FText UDJ01AbilityEffect::GetNodeTitle() const
{
    if (!DisplayName.IsEmpty())
    {
        return DisplayName;
    }
    return GetEffectTypeName();
}
#endif