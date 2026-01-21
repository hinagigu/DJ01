// ============================================================
// DJ01HealEffect.cpp
// 治疗效果实现
// ============================================================

#include "DJ01/AbilitySystem/Abilities/Public/DJ01HealEffect.h"
#include "DJ01/AbilitySystem/Abilities/Public/DJ01DamageEffect.h"
#include "AbilitySystemComponent.h"
#include "GameplayTagsManager.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01HealEffect)

UDJ01HealEffect::UDJ01HealEffect()
{
    DisplayName = FText::FromString(TEXT("Heal"));
}

bool UDJ01HealEffect::Execute_Implementation(FDJ01EffectContext& Context)
{
    UAbilitySystemComponent* InstigatorASC = Context.GetInstigatorASC();
    if (!InstigatorASC || !HealGameplayEffect)
    {
        return false;
    }

    // 计算原始治疗量
    float RawHeal = CalculateRawHeal(Context);
    if (RawHeal <= 0.0f)
    {
        return false;
    }

    // 确定治疗目标
    TArray<UAbilitySystemComponent*> HealTargets;
    if (bHealSelf)
    {
        HealTargets.Add(InstigatorASC);
    }
    else
    {
        HealTargets = Context.GetValidTargetASCs();
        if (HealTargets.Num() == 0)
        {
            // 默认治疗自己
            HealTargets.Add(InstigatorASC);
        }
    }

    // 为每个目标应用治疗
    for (UAbilitySystemComponent* TargetASC : HealTargets)
    {
        if (!TargetASC)
        {
            continue;
        }

        // 创建 GE Spec
        FGameplayEffectSpecHandle SpecHandle = InstigatorASC->MakeOutgoingSpec(
            HealGameplayEffect,
            Context.AbilityLevel,
            InstigatorASC->MakeEffectContext()
        );

        if (!SpecHandle.IsValid())
        {
            continue;
        }

        // 设置 SetByCaller 数据
        FGameplayTag HealRawTag = FGameplayTag::RequestGameplayTag(FName("SetByCaller.Heal.Raw"));
        SpecHandle.Data->SetSetByCallerMagnitude(HealRawTag, RawHeal);

        // 应用到目标
        InstigatorASC->ApplyGameplayEffectSpecToTarget(*SpecHandle.Data, TargetASC);
    }

    return true;
}

float UDJ01HealEffect::CalculateRawHeal(const FDJ01EffectContext& Context) const
{
    float TotalHeal = BaseHeal;

    UAbilitySystemComponent* InstigatorASC = Context.GetInstigatorASC();
    if (!InstigatorASC)
    {
        return TotalHeal;
    }

    // 应用属性缩放 - 使用 DamageEffect 的静态方法
    for (const FDJ01AttributeScaling& Scaling : AttributeScalings)
    {
        float AttrValue = UDJ01DamageEffect::GetAttributeValue(InstigatorASC, Scaling.AttributeName);
        TotalHeal += AttrValue * Scaling.Ratio;
    }

    return TotalHeal;
}

FString UDJ01HealEffect::GetEffectDescription_Implementation() const
{
    FString Desc = FString::Printf(TEXT("恢复 %.0f 点生命值"), BaseHeal);

    for (const FDJ01AttributeScaling& Scaling : AttributeScalings)
    {
        Desc += FString::Printf(TEXT(" (+%.0f%% %s)"), Scaling.Ratio * 100.0f, *Scaling.AttributeName.ToString());
    }

    if (bHealSelf)
    {
        Desc += TEXT(" (自身)");
    }

    return Desc;
}

FText UDJ01HealEffect::GetEffectTypeName() const
{
    return FText::FromString(TEXT("治疗效果"));
}