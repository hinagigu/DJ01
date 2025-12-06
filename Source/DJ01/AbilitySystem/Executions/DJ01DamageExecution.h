// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "GameplayEffectExecutionCalculation.h"

#include "DJ01DamageExecution.generated.h"

class UObject;
class UDJ01DamageFormulaConfig;

/**
 * UDJ01DamageExecution
 *
 * 伤害执行计算 - 支持数据驱动配置
 * 
 * ============================================================
 * 工作模式:
 * ============================================================
 * 
 * 1. 数据驱动模式 (推荐):
 *    - 设置 DefaultFormulaConfig 指向一个 UDJ01DamageFormulaConfig 资产
 *    - 所有计算逻辑由配置中的修正器链决定
 *    - 支持运行时热更新公式
 * 
 * 2. 硬编码模式 (后备):
 *    - 当 DefaultFormulaConfig 为空时使用
 *    - 使用简化的硬编码公式
 * 
 * ============================================================
 * 硬编码公式 (后备模式):
 * ============================================================
 * 
 * 物理伤害:
 *   FinalDamage = BaseDamage * (1 + AttackPower/100) * (100 / (100 + Defense)) * WeaknessMultiplier
 * 
 * 魔法伤害:
 *   FinalDamage = BaseDamage * (1 + MagicPower/100) * (100 / (100 + MagicDefense)) * WeaknessMultiplier
 * 
 * 真实伤害:
 *   FinalDamage = BaseDamage（无视防御和弱点）
 * 
 * ============================================================
 * GameplayTag 约定:
 * ============================================================
 * 
 * 伤害类型 (必须指定其一):
 *   - Damage.Type.Physical  物理伤害（默认）
 *   - Damage.Type.Magical   魔法伤害
 *   - Damage.Type.True      真实伤害
 * 
 * 元素类型 (可选，用于弱点判定):
 *   - Damage.Element.Wind    风元素
 *   - Damage.Element.Light   光元素
 *   - Damage.Element.Ice     冰元素
 *   - Damage.Element.Dark    暗元素
 *   - Damage.Element.Fire    火元素
 *   - Damage.Element.Water   水元素
 *   - Damage.Element.Thunder 雷元素
 * 
 * 弱点标记 (挂在目标身上):
 *   - Weakness.Element.Fire  对火焰弱点
 *   - 等等...
 * 
 * ============================================================
 */
UCLASS(Blueprintable)
class DJ01_API UDJ01DamageExecution : public UGameplayEffectExecutionCalculation
{
    GENERATED_BODY()

public:

    UDJ01DamageExecution();

    /** 弱点命中时的伤害倍率 (仅硬编码模式使用) */
    static constexpr float WeaknessMultiplier = 1.5f;
    
    /** 
     * 默认伤害公式配置
     * 如果设置了此配置，将使用数据驱动模式
     * 如果为空，则使用硬编码公式作为后备
     */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Damage Formula")
    TSoftObjectPtr<UDJ01DamageFormulaConfig> DefaultFormulaConfig;

protected:

    virtual void Execute_Implementation(const FGameplayEffectCustomExecutionParameters& ExecutionParams, FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const override;

private:
    
    /**
     * 使用数据驱动配置计算伤害
     */
    float CalculateDamageWithConfig(
        const FGameplayEffectCustomExecutionParameters& ExecutionParams,
        const UDJ01DamageFormulaConfig* Config,
        const FGameplayTagContainer* SourceTags,
        const FGameplayTagContainer* TargetTags) const;
    
    /**
     * 使用硬编码公式计算伤害 (后备)
     */
    float CalculateDamageHardcoded(
        const FGameplayEffectCustomExecutionParameters& ExecutionParams,
        const FGameplayTagContainer* SourceTags,
        const FGameplayTagContainer* TargetTags) const;
	
    /**
     * 检查是否命中弱点 (仅硬编码模式使用)
     * @param SourceTags 技能携带的Tag（包含元素类型）
     * @param TargetTags 目标身上的Tag（包含弱点标记）
     * @return 是否命中弱点
     */
    bool CheckWeaknessHit(const FGameplayTagContainer* SourceTags, const FGameplayTagContainer* TargetTags) const;
};