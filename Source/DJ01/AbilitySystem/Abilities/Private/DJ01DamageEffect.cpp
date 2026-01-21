// ============================================================
// DJ01DamageEffect.cpp
// 伤害效果实现
// ============================================================

#include "DJ01/AbilitySystem/Abilities/Public/DJ01DamageEffect.h"
#include "AbilitySystemComponent.h"
#include "AbilitySystemBlueprintLibrary.h"
#include "GameplayTagsManager.h"
#include "DJ01/AbilitySystem/Attributes/Public/DJ01GeneratedAttributes.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01DamageEffect)

UDJ01DamageEffect::UDJ01DamageEffect()
{
    DisplayName = FText::FromString(TEXT("Damage"));
}

bool UDJ01DamageEffect::Execute_Implementation(FDJ01EffectContext& Context)
{
    UAbilitySystemComponent* InstigatorASC = Context.GetInstigatorASC();
    if (!InstigatorASC || !DamageGameplayEffect)
    {
        return false;
    }

    // 计算原始伤害
    float RawDamage = CalculateRawDamage(Context);
    if (RawDamage <= 0.0f)
    {
        return false;
    }

    // 获取目标列表
    TArray<UAbilitySystemComponent*> TargetASCs = Context.GetValidTargetASCs();
    if (TargetASCs.Num() == 0)
    {
        // 如果没有目标，跳过
        return false;
    }

    // 为每个目标应用伤害
    for (UAbilitySystemComponent* TargetASC : TargetASCs)
    {
        if (!TargetASC)
        {
            continue;
        }

        // 创建 GE Spec
        FGameplayEffectSpecHandle SpecHandle = InstigatorASC->MakeOutgoingSpec(
            DamageGameplayEffect, 
            Context.AbilityLevel, 
            InstigatorASC->MakeEffectContext()
        );

        if (!SpecHandle.IsValid())
        {
            continue;
        }

        // 设置 SetByCaller 数据
        FGameplayTag DamageRawTag = FGameplayTag::RequestGameplayTag(FName("SetByCaller.Damage.Raw"));
        FGameplayTag DamageTypeTag = FGameplayTag::RequestGameplayTag(FName("SetByCaller.Damage.Type"));

        SpecHandle.Data->SetSetByCallerMagnitude(DamageRawTag, RawDamage);
        SpecHandle.Data->SetSetByCallerMagnitude(DamageTypeTag, static_cast<float>(DamageType));

        // 应用到目标
        InstigatorASC->ApplyGameplayEffectSpecToTarget(*SpecHandle.Data, TargetASC);
    }

    return true;
}

float UDJ01DamageEffect::CalculateRawDamage(const FDJ01EffectContext& Context) const
{
    float TotalDamage = BaseDamage;

    UAbilitySystemComponent* InstigatorASC = Context.GetInstigatorASC();
    if (!InstigatorASC)
    {
        return TotalDamage;
    }

    // 应用属性缩放
    for (const FDJ01AttributeScaling& Scaling : AttributeScalings)
    {
        float AttrValue = GetAttributeValue(InstigatorASC, Scaling.AttributeName);
        TotalDamage += AttrValue * Scaling.Ratio;
    }

    return TotalDamage;
}

float UDJ01DamageEffect::GetAttributeValue(UAbilitySystemComponent* ASC, FName AttributeName)
{
    if (!ASC)
    {
        return 0.0f;
    }

    // 从 StatSet 获取战斗属性
    if (const UDJ01StatSet* StatSet = ASC->GetSet<UDJ01StatSet>())
    {
        if (AttributeName == FName("AttackPower") || AttributeName == FName("AttackDamage") || AttributeName == FName("AD"))
        {
            return StatSet->GetTotalAttackPower();
        }
        if (AttributeName == FName("AbilityPower") || AttributeName == FName("MagicPower") || AttributeName == FName("AP"))
        {
            return StatSet->GetTotalMagicPower();
        }
        if (AttributeName == FName("Defense") || AttributeName == FName("Armor"))
        {
            return StatSet->GetTotalDefense();
        }
        if (AttributeName == FName("MagicDefense") || AttributeName == FName("MagicResist") || AttributeName == FName("MR"))
        {
            return StatSet->GetTotalMagicDefense();
        }
        if (AttributeName == FName("CriticalRate"))
        {
            return StatSet->GetTotalCriticalRate();
        }
        if (AttributeName == FName("CriticalDamage"))
        {
            return StatSet->GetTotalCriticalDamage();
        }
    }

    // 从 ResourceSet 获取资源属性
    if (const UDJ01ResourceSet* ResourceSet = ASC->GetSet<UDJ01ResourceSet>())
    {
        if (AttributeName == FName("Health") || AttributeName == FName("HP"))
        {
            return ResourceSet->GetHealth();
        }
        if (AttributeName == FName("MaxHealth") || AttributeName == FName("MaxHP"))
        {
            return ResourceSet->GetTotalMaxHealth();
        }
        if (AttributeName == FName("Mana") || AttributeName == FName("MP"))
        {
            return ResourceSet->GetMana();
        }
        if (AttributeName == FName("MaxMana") || AttributeName == FName("MaxMP"))
        {
            return ResourceSet->GetTotalMaxMana();
        }
    }

    return 0.0f;
}

FString UDJ01DamageEffect::GetEffectDescription_Implementation() const
{
    FString Desc = FString::Printf(TEXT("造成 %.0f"), BaseDamage);
    
    switch (DamageType)
    {
    case EDJ01DamageType::Physical:
        Desc += TEXT(" 点物理伤害");
        break;
    case EDJ01DamageType::Magical:
        Desc += TEXT(" 点魔法伤害");
        break;
    case EDJ01DamageType::Pure:
        Desc += TEXT(" 点真实伤害");
        break;
    }

    for (const FDJ01AttributeScaling& Scaling : AttributeScalings)
    {
        Desc += FString::Printf(TEXT(" (+%.0f%% %s)"), Scaling.Ratio * 100.0f, *Scaling.AttributeName.ToString());
    }

    return Desc;
}

FText UDJ01DamageEffect::GetEffectTypeName() const
{
    return FText::FromString(TEXT("伤害效果"));
}