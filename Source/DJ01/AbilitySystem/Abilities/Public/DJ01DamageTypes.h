// ============================================================
// DJ01DamageTypes.h
// LOL风格伤害配置数据结构
// 与 AttributeGenerator 生成的属性系统完美配合
// ============================================================

#pragma once

#include "CoreMinimal.h"
#include "AttributeSet.h"
#include "DJ01DamageTypes.generated.h"

class UAbilitySystemComponent;

/**
 * 属性层级类型
 * 对应 AttributeGenerator 生成的分层属性
 */
UENUM(BlueprintType)
enum class EDJ01AttributeLayer : uint8
{
    /** 基础值 - GetBaseXxx() */
    Base UMETA(DisplayName = "Base (基础)"),
    
    /** 额外值 - GetExtraXxx() = Total - Base */
    Bonus UMETA(DisplayName = "Bonus (额外)"),
    
    /** 全额值 - GetTotalXxx() = (Base + Flat) * (1 + Percent) */
    Total UMETA(DisplayName = "Total (全额)")
};

/**
 * 伤害类型
 */
UENUM(BlueprintType)
enum class EDJ01DamageType : uint8
{
    /** 物理伤害 - 被护甲(Defense)减免 */
    Physical UMETA(DisplayName = "Physical (物理)"),
    
    /** 魔法伤害 - 被魔抗(MagicDefense)减免 */
    Magical UMETA(DisplayName = "Magical (魔法)"),
    
    /** 真实伤害 - 无视防御 */
    Pure UMETA(DisplayName = "Pure (真实)")
};

/**
 * 效果类型 (伤害/治疗)
 */
UENUM(BlueprintType)
enum class EDJ01EffectType : uint8
{
    /** 伤害 - 减少目标生命值 */
    Damage UMETA(DisplayName = "Damage (伤害)"),
    
    /** 治疗 - 恢复目标生命值 */
    Heal UMETA(DisplayName = "Heal (治疗)")
};

/**
 * 单个伤害加成配置
 * 
 * 示例配置:
 * - "+80% Total AD": Layer=Total, AttributeSetClass=UDJ01StatSet, AttributeName="AttackPower", Ratio=0.8
 * - "+10% Target MaxHP": Layer=Total, AttributeName="MaxHealth", bFromTarget=true, Ratio=0.1
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01DamageScaling
{
    GENERATED_BODY()

    FDJ01DamageScaling()
        : Layer(EDJ01AttributeLayer::Total)
        , Ratio(0.f)
        , bFromTarget(false)
    {}

    /** 
     * 属性集类 (如 UDJ01StatSet, UDJ01ResourceSet)
     * 留空则使用 AttributeName 在所有 AttributeSet 中查找
     */
    UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Scaling")
    TSubclassOf<UAttributeSet> AttributeSetClass;

    /** 
     * 属性名称 (如 "AttackPower", "MagicPower", "MaxHealth")
     * 必须是 AttributeGenerator 生成的属性名
     */
    UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Scaling")
    FName AttributeName;

    /** 属性层级 (Base/Bonus/Total) */
    UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Scaling")
    EDJ01AttributeLayer Layer = EDJ01AttributeLayer::Total;

    /** 加成比例 (0.8 = 80%) */
    UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Scaling")
    float Ratio = 0.f;

    /** 是否从目标获取 (false = 从自身/施法者获取) */
    UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Scaling")
    bool bFromTarget = false;

    /** 获取描述字符串 (用于编辑器/UI显示) */
    FString GetDescription() const;
    
    /** 从 ASC 获取属性值 */
    float GetAttributeValue(UAbilitySystemComponent* ASC) const;
};

/**
 * 完整的伤害配置
 * 用于技能/Combo节点配置
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01DamageConfig
{
    GENERATED_BODY()

    FDJ01DamageConfig()
        : BaseDamage(0.f)
        , DamageType(EDJ01DamageType::Physical)
    {}

    /** 基础伤害值 (固定数值) */
    UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Damage")
    float BaseDamage = 0.f;

    /** 伤害类型 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Damage")
    EDJ01DamageType DamageType = EDJ01DamageType::Physical;

    /** 属性加成列表 (LOL风格: +80% AD, +60% AP 等) */
    UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Damage", meta = (TitleProperty = "{Ratio} x {AttributeName}"))
    TArray<FDJ01DamageScaling> Scalings;

    /** 
     * 计算最终原始伤害 (未减防) 
     * @param SourceASC - 施法者的 ASC
     * @param TargetASC - 目标的 ASC (可为空，如果没有来自目标的加成)
     * @return 原始伤害值
     */
    float CalculateRawDamage(UAbilitySystemComponent* SourceASC, UAbilitySystemComponent* TargetASC = nullptr) const;

    /** 获取伤害描述 (用于技能提示UI) */
    FString GetDamageDescription() const;
};

/**
 * 治疗配置
 * 治疗不需要护甲减免，但可以有治疗效果加成
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01HealConfig
{
    GENERATED_BODY()

    FDJ01HealConfig()
        : BaseHeal(0.f)
    {}

    /** 基础治疗量 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Heal")
    float BaseHeal = 0.f;

    /** 属性加成列表 (如 +60% AP, +10% MaxHP) */
    UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Heal", meta = (TitleProperty = "{Ratio} x {AttributeName}"))
    TArray<FDJ01DamageScaling> Scalings;

    /** 
     * 计算最终治疗量 
     * @param SourceASC - 施法者的 ASC
     * @param TargetASC - 目标的 ASC (可为空)
     * @return 治疗量 (正值)
     */
    float CalculateRawHeal(UAbilitySystemComponent* SourceASC, UAbilitySystemComponent* TargetASC = nullptr) const;

    /** 获取治疗描述 */
    FString GetHealDescription() const;
};

/**
 * 通用效果配置 (伤害或治疗)
 * 适用于既可以造成伤害又可以治疗的技能
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01EffectConfig
{
    GENERATED_BODY()

    FDJ01EffectConfig()
        : EffectType(EDJ01EffectType::Damage)
    {}

    /** 效果类型 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Effect")
    EDJ01EffectType EffectType = EDJ01EffectType::Damage;

    /** 伤害配置 (当 EffectType = Damage 时使用) */
    UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Effect", meta = (EditCondition = "EffectType == EDJ01EffectType::Damage", EditConditionHides))
    FDJ01DamageConfig DamageConfig;

    /** 治疗配置 (当 EffectType = Heal 时使用) */
    UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Effect", meta = (EditCondition = "EffectType == EDJ01EffectType::Heal", EditConditionHides))
    FDJ01HealConfig HealConfig;
};