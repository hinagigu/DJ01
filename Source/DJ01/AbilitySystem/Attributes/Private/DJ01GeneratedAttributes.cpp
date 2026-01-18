// ============================================================
// DJ01 Generated Attributes
// 自动生成的文件，请勿手动修改！
// 生成时间: 2026-01-05 10:24:22
// ============================================================

#include "DJ01/AbilitySystem/Attributes/Public/DJ01GeneratedAttributes.h"
#include "Net/UnrealNetwork.h"
#include "GameplayTagsManager.h"
#include "AbilitySystemComponent.h"
#include "GameplayEffectExtension.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01GeneratedAttributes)


// ##########################################################
// UDJ01StatSet
// ##########################################################

UDJ01StatSet::UDJ01StatSet()
{
    InitBaseAttackPower(100.0f);
    InitFlatAttackPower(0.0f);
    InitPercentAttackPower(0.0f);
    InitBaseMagicPower(80.0f);
    InitFlatMagicPower(0.0f);
    InitPercentMagicPower(0.0f);
    InitBaseDefense(50.0f);
    InitFlatDefense(0.0f);
    InitPercentDefense(0.0f);
    InitBaseMagicDefense(40.0f);
    InitFlatMagicDefense(0.0f);
    InitPercentMagicDefense(0.0f);
    InitBaseCriticalRate(0.05f);
    InitFlatCriticalRate(0.0f);
    InitPercentCriticalRate(0.0f);
    InitBaseCriticalDamage(1.5f);
    InitFlatCriticalDamage(0.0f);
    InitPercentCriticalDamage(0.0f);
    InitBaseAttackSpeed(1.0f);
    InitFlatAttackSpeed(0.0f);
    InitPercentAttackSpeed(0.0f);
    InitBaseHealingBonus(0.0f);
    InitFlatHealingBonus(0.0f);
    InitPercentHealingBonus(0.0f);
}

void UDJ01StatSet::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    REGISTER_LAYERED_ATTRIBUTE_REPLICATION(UDJ01StatSet, AttackPower)
    REGISTER_LAYERED_ATTRIBUTE_REPLICATION(UDJ01StatSet, MagicPower)
    REGISTER_LAYERED_ATTRIBUTE_REPLICATION(UDJ01StatSet, Defense)
    REGISTER_LAYERED_ATTRIBUTE_REPLICATION(UDJ01StatSet, MagicDefense)
    REGISTER_LAYERED_ATTRIBUTE_REPLICATION(UDJ01StatSet, CriticalRate)
    REGISTER_LAYERED_ATTRIBUTE_REPLICATION(UDJ01StatSet, CriticalDamage)
    REGISTER_LAYERED_ATTRIBUTE_REPLICATION(UDJ01StatSet, AttackSpeed)
    REGISTER_LAYERED_ATTRIBUTE_REPLICATION(UDJ01StatSet, HealingBonus)
}

IMPLEMENT_LAYERED_ATTRIBUTE_ONREP(UDJ01StatSet, AttackPower)
IMPLEMENT_LAYERED_ATTRIBUTE_ONREP(UDJ01StatSet, MagicPower)
IMPLEMENT_LAYERED_ATTRIBUTE_ONREP(UDJ01StatSet, Defense)
IMPLEMENT_LAYERED_ATTRIBUTE_ONREP(UDJ01StatSet, MagicDefense)
IMPLEMENT_LAYERED_ATTRIBUTE_ONREP(UDJ01StatSet, CriticalRate)
IMPLEMENT_LAYERED_ATTRIBUTE_ONREP(UDJ01StatSet, CriticalDamage)
IMPLEMENT_LAYERED_ATTRIBUTE_ONREP(UDJ01StatSet, AttackSpeed)
IMPLEMENT_LAYERED_ATTRIBUTE_ONREP(UDJ01StatSet, HealingBonus)


// ##########################################################
// UDJ01MoveMent
// ##########################################################

UDJ01MoveMent::UDJ01MoveMent()
{
    InitBaseSpeed(100.0f);
    InitFlatSpeed(0.0f);
    InitPercentSpeed(0.0f);
    InitBaseSlowResistance(0.0f);
    InitFlatSlowResistance(0.0f);
    InitPercentSlowResistance(0.0f);
}

void UDJ01MoveMent::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    REGISTER_LAYERED_ATTRIBUTE_REPLICATION(UDJ01MoveMent, Speed)
    REGISTER_LAYERED_ATTRIBUTE_REPLICATION(UDJ01MoveMent, SlowResistance)
}

IMPLEMENT_LAYERED_ATTRIBUTE_ONREP(UDJ01MoveMent, Speed)
IMPLEMENT_LAYERED_ATTRIBUTE_ONREP(UDJ01MoveMent, SlowResistance)


// ##########################################################
// UDJ01ResourceSet
// ##########################################################

UDJ01ResourceSet::UDJ01ResourceSet()
{
    InitBaseMaxHealth(100.0f);
    InitFlatMaxHealth(0.0f);
    InitPercentMaxHealth(0.0f);
    InitHealth(100.0f);
    InitBaseMaxMana(100.0f);
    InitFlatMaxMana(0.0f);
    InitPercentMaxMana(0.0f);
    InitMana(100.0f);
}

void UDJ01ResourceSet::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    REGISTER_RESOURCE_ATTRIBUTE_REPLICATION(UDJ01ResourceSet, Health)
    REGISTER_RESOURCE_ATTRIBUTE_REPLICATION(UDJ01ResourceSet, Mana)
}

IMPLEMENT_RESOURCE_ATTRIBUTE_ONREP(UDJ01ResourceSet, Health)
IMPLEMENT_RESOURCE_ATTRIBUTE_ONREP(UDJ01ResourceSet, Mana)

void UDJ01ResourceSet::PreAttributeChange(const FGameplayAttribute& Attribute, float& NewValue)
{
    Super::PreAttributeChange(Attribute, NewValue);

    // ===== Health Clamp =====
    if (Attribute == GetHealthAttribute())
    {
        // Resource 自动 Clamp: [0, MaxHealth]
        NewValue = FMath::Clamp(NewValue, 0.f, GetTotalMaxHealth());
    }

    // ===== Mana Clamp =====
    if (Attribute == GetManaAttribute())
    {
        // Resource 自动 Clamp: [0, MaxMana]
        NewValue = FMath::Clamp(NewValue, 0.f, GetTotalMaxMana());
    }

}

void UDJ01ResourceSet::PostAttributeChange(const FGameplayAttribute& Attribute, float OldValue, float NewValue)
{
    Super::PostAttributeChange(Attribute, OldValue, NewValue);

    // ===== MaxHealth 变化时联动调整 Health 和 PercentHealth =====
    if (Attribute == GetBaseMaxHealthAttribute() ||
        Attribute == GetFlatMaxHealthAttribute() ||
        Attribute == GetPercentMaxHealthAttribute())
    {
        // KeepCurrent: 保持当前值，超限时 Clamp
        const float CurrentValue = GetHealth();
        const float NewMax = GetTotalMaxHealth();
        if (CurrentValue > NewMax)
        {
            SetHealth(NewMax);
        }
        // 更新百分比属性
        UpdateHealthPercent();
    }

    // ===== Health (Current) 变化时更新 PercentHealth =====
    if (Attribute == GetHealthAttribute())
    {
        UpdateHealthPercent();
    }

    // ===== MaxMana 变化时联动调整 Mana 和 PercentMana =====
    if (Attribute == GetBaseMaxManaAttribute() ||
        Attribute == GetFlatMaxManaAttribute() ||
        Attribute == GetPercentMaxManaAttribute())
    {
        // KeepCurrent: 保持当前值，超限时 Clamp
        const float CurrentValue = GetMana();
        const float NewMax = GetTotalMaxMana();
        if (CurrentValue > NewMax)
        {
            SetMana(NewMax);
        }
        // 更新百分比属性
        UpdateManaPercent();
    }

    // ===== Mana (Current) 变化时更新 PercentMana =====
    if (Attribute == GetManaAttribute())
    {
        UpdateManaPercent();
    }

    // ===== Health 变化处理 =====
    if (Attribute == GetHealthAttribute())
    {
        // 减少时广播
        if (NewValue < OldValue)
        {
            OnHealthDecreased.Broadcast(nullptr, nullptr, nullptr, OldValue - NewValue, OldValue, NewValue);
        }

    }

}


// ##########################################################
// UDJ01MetaAttributes
// ##########################################################

UDJ01MetaAttributes::UDJ01MetaAttributes()
{
    InitDamageIncoming(0.0f);
    InitHealIncoming(0.0f);
}

void UDJ01MetaAttributes::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
}


void UDJ01MetaAttributes::PostGameplayEffectExecute(const FGameplayEffectModCallbackData& Data)
{
    Super::PostGameplayEffectExecute(Data);

    // ===== Meta 属性: DamageIncoming =====
    if (Data.EvaluatedData.Attribute == GetDamageIncomingAttribute())
    {
        // 获取 Meta 属性的值
        const float LocalValue = GetDamageIncoming();

        // 跨 AttributeSet 访问: 将 Meta 值转发到 UDJ01ResourceSet::Health
        if (LocalValue != 0.0f)
        {
            if (UAbilitySystemComponent* ASC = GetOwningAbilitySystemComponent())
            {
                if (UDJ01ResourceSet* TargetSet = const_cast<UDJ01ResourceSet*>(ASC->GetSet<UDJ01ResourceSet>()))
                {
                    const float NewValue = TargetSet->GetHealth() + LocalValue;
                    TargetSet->SetHealth(NewValue);
                }
            }
        }

        // 重置 Meta 属性
        SetDamageIncoming(0.0f);
    }

    // ===== Meta 属性: HealIncoming =====
    if (Data.EvaluatedData.Attribute == GetHealIncomingAttribute())
    {
        // 获取 Meta 属性的值
        const float LocalValue = GetHealIncoming();

        // TODO: 在这里处理 HealIncoming 的逻辑
        // 示例: 将伤害应用到 Health
        // if (LocalValue != 0.0f)
        // {
        //     SetHealth(GetHealth() + LocalValue);
        // }

        // 重置 Meta 属性
        SetHealIncoming(0.0f);
    }

}
