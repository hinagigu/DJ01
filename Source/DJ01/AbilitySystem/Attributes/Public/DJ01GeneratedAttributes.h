// ============================================================
// DJ01 Generated Attributes
// 自动生成的文件，请勿手动修改！
// 生成时间: 2025-12-20 19:36:15
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
    DECLARE_LAYERED_ATTRIBUTE(UDJ01StatSet, AttackPower)

    /** 魔法攻击力 */
    DECLARE_LAYERED_ATTRIBUTE(UDJ01StatSet, MagicPower)

    /** 物理防御 */
    DECLARE_LAYERED_ATTRIBUTE(UDJ01StatSet, Defense)

    /** 魔法防御 */
    DECLARE_LAYERED_ATTRIBUTE(UDJ01StatSet, MagicDefense)

    /** 暴击率(0.05=5%) */
    DECLARE_LAYERED_ATTRIBUTE(UDJ01StatSet, CriticalRate)

    /** 暴击伤害倍率 */
    DECLARE_LAYERED_ATTRIBUTE(UDJ01StatSet, CriticalDamage)

    /** 攻击速度倍率 */
    DECLARE_LAYERED_ATTRIBUTE(UDJ01StatSet, AttackSpeed)

protected:
    DECLARE_LAYERED_ATTRIBUTE_ONREP(AttackPower)
    DECLARE_LAYERED_ATTRIBUTE_ONREP(MagicPower)
    DECLARE_LAYERED_ATTRIBUTE_ONREP(Defense)
    DECLARE_LAYERED_ATTRIBUTE_ONREP(MagicDefense)
    DECLARE_LAYERED_ATTRIBUTE_ONREP(CriticalRate)
    DECLARE_LAYERED_ATTRIBUTE_ONREP(CriticalDamage)
    DECLARE_LAYERED_ATTRIBUTE_ONREP(AttackSpeed)

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
    DECLARE_LAYERED_ATTRIBUTE(UDJ01MoveMent, Speed)

    // ---------- Combat ----------
    /** 减速抗性 */
    DECLARE_LAYERED_ATTRIBUTE(UDJ01MoveMent, SlowResistance)

protected:
    DECLARE_LAYERED_ATTRIBUTE_ONREP(Speed)
    DECLARE_LAYERED_ATTRIBUTE_ONREP(SlowResistance)

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
    DECLARE_RESOURCE_ATTRIBUTE(UDJ01ResourceSet, Health)

    /** 新属性 */
    DECLARE_RESOURCE_ATTRIBUTE(UDJ01ResourceSet, Mana)

protected:
    DECLARE_RESOURCE_ATTRIBUTE_ONREP(Health)
    DECLARE_RESOURCE_ATTRIBUTE_ONREP(Mana)

    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;
    virtual void PreAttributeChange(const FGameplayAttribute& Attribute, float& NewValue) override;
};