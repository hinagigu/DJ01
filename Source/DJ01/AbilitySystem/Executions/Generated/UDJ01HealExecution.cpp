// ============================================================
// UDJ01HealExecution
// 自动生成，可根据需要修改计算逻辑
// 生成时间: 2026-01-05 10:24:53
// ============================================================

#include "UDJ01HealExecution.h"
#include "DJ01/AbilitySystem/Attributes/Public/DJ01GeneratedAttributes.h"
#include "DJ01/System/Public/DJ01GameplayTags.h"
#include "AbilitySystemComponent.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(UDJ01HealExecution)

namespace
{
    struct FCapturedAttributes
    {
        bool bInitialized = false;
        FGameplayEffectAttributeCaptureDefinition BaseHealingBonus_TargetDef;
        FGameplayEffectAttributeCaptureDefinition FlatHealingBonus_TargetDef;
        FGameplayEffectAttributeCaptureDefinition PercentHealingBonus_TargetDef;

        void Initialize()
        {
            if (bInitialized) return;
            bInitialized = true;

            BaseHealingBonus_TargetDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetBaseHealingBonusAttribute(), EGameplayEffectAttributeCaptureSource::Target, false);
            FlatHealingBonus_TargetDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetFlatHealingBonusAttribute(), EGameplayEffectAttributeCaptureSource::Target, false);
            PercentHealingBonus_TargetDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetPercentHealingBonusAttribute(), EGameplayEffectAttributeCaptureSource::Target, false);
        }
    };

    static FCapturedAttributes& GetCapturedAttributes()
    {
        static FCapturedAttributes Attributes;
        return Attributes;
    }
}

UDJ01HealExecution::UDJ01HealExecution()
{
    // 捕获定义延迟到 Execute_Implementation 首次调用时初始化
    // 避免静态初始化顺序问题
}

void UDJ01HealExecution::Execute_Implementation(
    const FGameplayEffectCustomExecutionParameters& ExecutionParams,
    FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const
{
    // 延迟初始化捕获定义（首次调用时）
    FCapturedAttributes& Attrs = GetCapturedAttributes();
    Attrs.Initialize();

    const FGameplayEffectSpec& Spec = ExecutionParams.GetOwningSpec();
    FAggregatorEvaluateParameters EvalParams;
    EvalParams.SourceTags = Spec.CapturedSourceTags.GetAggregatedTags();
    EvalParams.TargetTags = Spec.CapturedTargetTags.GetAggregatedTags();

    // ========== Tag 状态捕获 ==========
    const bool bTarget_Status_Immunity_Heal = EvalParams.TargetTags && EvalParams.TargetTags->HasTag(DJ01GameplayTags::Status_Immunity_Heal);
    const bool bTarget_Status_Debuff_GrievousWounds = EvalParams.TargetTags && EvalParams.TargetTags->HasTag(DJ01GameplayTags::Status_Debuff_GrievousWounds);

    // ========== SetByCaller 参数（技能传入） ==========
    const float RawHeal = Spec.GetSetByCallerMagnitude(
        DJ01GameplayTags::SetByCaller_Heal_Raw, false, 0.0f);

    // ========== 获取属性值 ==========
    float BaseHealingBonus_Target = 0.f, FlatHealingBonus_Target = 0.f, PercentHealingBonus_Target = 0.f;
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.BaseHealingBonus_TargetDef, EvalParams, BaseHealingBonus_Target);
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.FlatHealingBonus_TargetDef, EvalParams, FlatHealingBonus_Target);
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.PercentHealingBonus_TargetDef, EvalParams, PercentHealingBonus_Target);
    const float HealingBonus_TargetValue = (BaseHealingBonus_Target + FlatHealingBonus_Target) * (1.f + PercentHealingBonus_Target);


    // ========== 计算逻辑 ==========
    // RawHeal: 技能层计算的原始治疗量
    // HealingBonus: 治疗增益百分比 (如 0.2 = +20% 治疗效果)
    // Status.Immunity.Heal: 治疗免疫状态
    // Status.Debuff.GrievousWounds: 重伤效果 (减少50%治疗)
    
    float FinalValue = 0.0f;
    
    if (!bTarget_Status_Immunity_Heal && RawHeal > 0.f)
    {
        // 应用治疗增益
        FinalValue = RawHeal * (1.0f + FMath::Max(HealingBonus_TargetValue, 0.f));
        
        // 重伤效果: 减少50%治疗
        if (bTarget_Status_Debuff_GrievousWounds)
        {
            FinalValue *= 0.5f;
        }
    }

    // ========== 输出结果 ==========
    if (FinalValue != 0.f)
    {
        OutExecutionOutput.AddOutputModifier(FGameplayModifierEvaluatedData(
            UDJ01MetaAttributes::GetHealIncomingAttribute(), EGameplayModOp::Additive, FinalValue));
    }
}
