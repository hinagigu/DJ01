// ============================================================
// DJ01 Generated Attributes
// 自动生成的文件，请勿手动修改！
// 生成时间: 2025-12-30 20:12:09
// ============================================================

#pragma once

#include "DJ01/AbilitySystem/Attributes/Public/DJ01AttributeSet.h"
#include "DJ01/AbilitySystem/Attributes/Public/DJ01AttributeMacros.h"
#include "AbilitySystemComponent.h"
#include "DJ01GeneratedAttributes.generated.h"


// ##########################################################
// UDJ01StatSet
// ##########################################################
/** StatSet - 包含 7 个属性 */
UCLASS(BlueprintType)
class DJ01_API UDJ01StatSet : public UDJ01AttributeSet
{
    GENERATED_BODY()

public:
    UDJ01StatSet();

    // ---------- Combat ----------
    /** 物理攻击力 */
    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseAttackPower, Category = "DJ01|AttackPower", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData BaseAttackPower;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, BaseAttackPower)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_FlatAttackPower, Category = "DJ01|AttackPower", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData FlatAttackPower;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, FlatAttackPower)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_PercentAttackPower, Category = "DJ01|AttackPower", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData PercentAttackPower;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, PercentAttackPower)

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetTotalAttackPower() const
    {
        return (GetBaseAttackPower() + GetFlatAttackPower()) * (1.f + GetPercentAttackPower());
    }

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetExtraAttackPower() const
    {
        return GetTotalAttackPower() - GetBaseAttackPower();
    }

    /** 魔法攻击力 */
    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseMagicPower, Category = "DJ01|MagicPower", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData BaseMagicPower;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, BaseMagicPower)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_FlatMagicPower, Category = "DJ01|MagicPower", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData FlatMagicPower;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, FlatMagicPower)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_PercentMagicPower, Category = "DJ01|MagicPower", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData PercentMagicPower;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, PercentMagicPower)

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetTotalMagicPower() const
    {
        return (GetBaseMagicPower() + GetFlatMagicPower()) * (1.f + GetPercentMagicPower());
    }

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetExtraMagicPower() const
    {
        return GetTotalMagicPower() - GetBaseMagicPower();
    }

    /** 物理防御 */
    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseDefense, Category = "DJ01|Defense", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData BaseDefense;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, BaseDefense)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_FlatDefense, Category = "DJ01|Defense", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData FlatDefense;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, FlatDefense)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_PercentDefense, Category = "DJ01|Defense", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData PercentDefense;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, PercentDefense)

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetTotalDefense() const
    {
        return (GetBaseDefense() + GetFlatDefense()) * (1.f + GetPercentDefense());
    }

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetExtraDefense() const
    {
        return GetTotalDefense() - GetBaseDefense();
    }

    /** 魔法防御 */
    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseMagicDefense, Category = "DJ01|MagicDefense", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData BaseMagicDefense;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, BaseMagicDefense)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_FlatMagicDefense, Category = "DJ01|MagicDefense", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData FlatMagicDefense;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, FlatMagicDefense)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_PercentMagicDefense, Category = "DJ01|MagicDefense", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData PercentMagicDefense;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, PercentMagicDefense)

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetTotalMagicDefense() const
    {
        return (GetBaseMagicDefense() + GetFlatMagicDefense()) * (1.f + GetPercentMagicDefense());
    }

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetExtraMagicDefense() const
    {
        return GetTotalMagicDefense() - GetBaseMagicDefense();
    }

    /** 暴击率(0.05=5%) */
    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseCriticalRate, Category = "DJ01|CriticalRate", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData BaseCriticalRate;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, BaseCriticalRate)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_FlatCriticalRate, Category = "DJ01|CriticalRate", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData FlatCriticalRate;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, FlatCriticalRate)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_PercentCriticalRate, Category = "DJ01|CriticalRate", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData PercentCriticalRate;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, PercentCriticalRate)

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetTotalCriticalRate() const
    {
        return (GetBaseCriticalRate() + GetFlatCriticalRate()) * (1.f + GetPercentCriticalRate());
    }

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetExtraCriticalRate() const
    {
        return GetTotalCriticalRate() - GetBaseCriticalRate();
    }

    /** 暴击伤害倍率 */
    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseCriticalDamage, Category = "DJ01|CriticalDamage", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData BaseCriticalDamage;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, BaseCriticalDamage)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_FlatCriticalDamage, Category = "DJ01|CriticalDamage", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData FlatCriticalDamage;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, FlatCriticalDamage)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_PercentCriticalDamage, Category = "DJ01|CriticalDamage", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData PercentCriticalDamage;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, PercentCriticalDamage)

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetTotalCriticalDamage() const
    {
        return (GetBaseCriticalDamage() + GetFlatCriticalDamage()) * (1.f + GetPercentCriticalDamage());
    }

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetExtraCriticalDamage() const
    {
        return GetTotalCriticalDamage() - GetBaseCriticalDamage();
    }

    /** 攻击速度倍率 */
    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseAttackSpeed, Category = "DJ01|AttackSpeed", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData BaseAttackSpeed;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, BaseAttackSpeed)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_FlatAttackSpeed, Category = "DJ01|AttackSpeed", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData FlatAttackSpeed;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, FlatAttackSpeed)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_PercentAttackSpeed, Category = "DJ01|AttackSpeed", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData PercentAttackSpeed;
    ATTRIBUTE_ACCESSORS(UDJ01StatSet, PercentAttackSpeed)

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetTotalAttackSpeed() const
    {
        return (GetBaseAttackSpeed() + GetFlatAttackSpeed()) * (1.f + GetPercentAttackSpeed());
    }

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetExtraAttackSpeed() const
    {
        return GetTotalAttackSpeed() - GetBaseAttackSpeed();
    }

protected:
    UFUNCTION()
    void OnRep_BaseAttackPower(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_FlatAttackPower(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_PercentAttackPower(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_BaseMagicPower(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_FlatMagicPower(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_PercentMagicPower(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_BaseDefense(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_FlatDefense(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_PercentDefense(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_BaseMagicDefense(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_FlatMagicDefense(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_PercentMagicDefense(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_BaseCriticalRate(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_FlatCriticalRate(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_PercentCriticalRate(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_BaseCriticalDamage(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_FlatCriticalDamage(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_PercentCriticalDamage(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_BaseAttackSpeed(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_FlatAttackSpeed(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_PercentAttackSpeed(const FGameplayAttributeData& OldValue);

    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;
};

// ##########################################################
// UDJ01MoveMent
// ##########################################################
/** MoveMent - 包含 2 个属性 */
UCLASS(BlueprintType)
class DJ01_API UDJ01MoveMent : public UDJ01AttributeSet
{
    GENERATED_BODY()

public:
    UDJ01MoveMent();

    // ---------- Resource ----------
    /** 移动速度 */
    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseSpeed, Category = "DJ01|Speed", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData BaseSpeed;
    ATTRIBUTE_ACCESSORS(UDJ01MoveMent, BaseSpeed)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_FlatSpeed, Category = "DJ01|Speed", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData FlatSpeed;
    ATTRIBUTE_ACCESSORS(UDJ01MoveMent, FlatSpeed)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_PercentSpeed, Category = "DJ01|Speed", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData PercentSpeed;
    ATTRIBUTE_ACCESSORS(UDJ01MoveMent, PercentSpeed)

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetTotalSpeed() const
    {
        return (GetBaseSpeed() + GetFlatSpeed()) * (1.f + GetPercentSpeed());
    }

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetExtraSpeed() const
    {
        return GetTotalSpeed() - GetBaseSpeed();
    }

    // ---------- Combat ----------
    /** 减速抗性 */
    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseSlowResistance, Category = "DJ01|SlowResistance", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData BaseSlowResistance;
    ATTRIBUTE_ACCESSORS(UDJ01MoveMent, BaseSlowResistance)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_FlatSlowResistance, Category = "DJ01|SlowResistance", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData FlatSlowResistance;
    ATTRIBUTE_ACCESSORS(UDJ01MoveMent, FlatSlowResistance)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_PercentSlowResistance, Category = "DJ01|SlowResistance", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData PercentSlowResistance;
    ATTRIBUTE_ACCESSORS(UDJ01MoveMent, PercentSlowResistance)

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetTotalSlowResistance() const
    {
        return (GetBaseSlowResistance() + GetFlatSlowResistance()) * (1.f + GetPercentSlowResistance());
    }

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetExtraSlowResistance() const
    {
        return GetTotalSlowResistance() - GetBaseSlowResistance();
    }

protected:
    UFUNCTION()
    void OnRep_BaseSpeed(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_FlatSpeed(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_PercentSpeed(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_BaseSlowResistance(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_FlatSlowResistance(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_PercentSlowResistance(const FGameplayAttributeData& OldValue);

    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;
};

// ##########################################################
// UDJ01ResourceSet
// ##########################################################
/** ResourceSet - 包含 2 个属性 */
UCLASS(BlueprintType)
class DJ01_API UDJ01ResourceSet : public UDJ01AttributeSet
{
    GENERATED_BODY()

public:
    UDJ01ResourceSet();

    // ---------- Resource ----------
    /** 生命值 */
    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseMaxHealth, Category = "DJ01|MaxHealth", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData BaseMaxHealth;
    ATTRIBUTE_ACCESSORS(UDJ01ResourceSet, BaseMaxHealth)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_FlatMaxHealth, Category = "DJ01|MaxHealth", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData FlatMaxHealth;
    ATTRIBUTE_ACCESSORS(UDJ01ResourceSet, FlatMaxHealth)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_PercentMaxHealth, Category = "DJ01|MaxHealth", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData PercentMaxHealth;
    ATTRIBUTE_ACCESSORS(UDJ01ResourceSet, PercentMaxHealth)

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetTotalMaxHealth() const
    {
        return (GetBaseMaxHealth() + GetFlatMaxHealth()) * (1.f + GetPercentMaxHealth());
    }

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetExtraMaxHealth() const
    {
        return GetTotalMaxHealth() - GetBaseMaxHealth();
    }

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_Health, Category = "DJ01|Attributes", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData Health;
    ATTRIBUTE_ACCESSORS(UDJ01ResourceSet, Health)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_PercentHealth, Category = "DJ01|Health", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData PercentHealth;
    ATTRIBUTE_ACCESSORS(UDJ01ResourceSet, PercentHealth)

    /** 更新 Health 百分比（Current / Max），内部调用 */
    void UpdateHealthPercent()
    {
        const float MaxVal = GetTotalMaxHealth();
        const float NewPercent = (MaxVal > 0.f) ? (GetHealth() / MaxVal) : 0.f;
        SetPercentHealth(NewPercent);
    }

    /** 法力值 */
    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseMaxMana, Category = "DJ01|MaxMana", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData BaseMaxMana;
    ATTRIBUTE_ACCESSORS(UDJ01ResourceSet, BaseMaxMana)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_FlatMaxMana, Category = "DJ01|MaxMana", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData FlatMaxMana;
    ATTRIBUTE_ACCESSORS(UDJ01ResourceSet, FlatMaxMana)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_PercentMaxMana, Category = "DJ01|MaxMana", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData PercentMaxMana;
    ATTRIBUTE_ACCESSORS(UDJ01ResourceSet, PercentMaxMana)

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetTotalMaxMana() const
    {
        return (GetBaseMaxMana() + GetFlatMaxMana()) * (1.f + GetPercentMaxMana());
    }

    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")
    float GetExtraMaxMana() const
    {
        return GetTotalMaxMana() - GetBaseMaxMana();
    }

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_Mana, Category = "DJ01|Attributes", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData Mana;
    ATTRIBUTE_ACCESSORS(UDJ01ResourceSet, Mana)

    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_PercentMana, Category = "DJ01|Mana", Meta = (AllowPrivateAccess = true))
    FGameplayAttributeData PercentMana;
    ATTRIBUTE_ACCESSORS(UDJ01ResourceSet, PercentMana)

    /** 更新 Mana 百分比（Current / Max），内部调用 */
    void UpdateManaPercent()
    {
        const float MaxVal = GetTotalMaxMana();
        const float NewPercent = (MaxVal > 0.f) ? (GetMana() / MaxVal) : 0.f;
        SetPercentMana(NewPercent);
    }

    // ---------- 属性变化委托 ----------
    /** Health 减少委托 */
    FDJ01AttributeEvent OnHealthDecreased;

protected:
    UFUNCTION()
    void OnRep_BaseMaxHealth(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_FlatMaxHealth(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_PercentMaxHealth(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_Health(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_PercentHealth(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_BaseMaxMana(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_FlatMaxMana(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_PercentMaxMana(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_Mana(const FGameplayAttributeData& OldValue);
    UFUNCTION()
    void OnRep_PercentMana(const FGameplayAttributeData& OldValue);

    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;
    virtual void PreAttributeChange(const FGameplayAttribute& Attribute, float& NewValue) override;
    virtual void PostAttributeChange(const FGameplayAttribute& Attribute, float OldValue, float NewValue) override;
};

// ##########################################################
// UDJ01MetaAttributes
// ##########################################################
/** MetaAttributes - 包含 1 个属性 */
UCLASS(BlueprintType)
class DJ01_API UDJ01MetaAttributes : public UDJ01AttributeSet
{
    GENERATED_BODY()

public:
    UDJ01MetaAttributes();

    // ---------- Combat ----------
    /** 伤害属性 */
    UPROPERTY(BlueprintReadOnly, Category = "DJ01|Meta", Meta = (HideFromModifiers, AllowPrivateAccess = true))
    FGameplayAttributeData DamageIncoming;
    ATTRIBUTE_ACCESSORS(UDJ01MetaAttributes, DamageIncoming)

protected:

    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;
    virtual void PostGameplayEffectExecute(const FGameplayEffectModCallbackData& Data) override;
};