// ============================================================
// UDJ01DamageExecution
// 自动生成，可根据需要修改计算逻辑
// 生成时间: 2025-12-21 19:21:36
// ============================================================

#include "UDJ01DamageExecution.h"
#include "DJ01/AbilitySystem/Attributes/Public/DJ01GeneratedAttributes.h"
#include "DJ01/System/Public/DJ01GameplayTags.h"
#include "AbilitySystemComponent.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(UDJ01DamageExecution)

namespace
{
    struct FCapturedAttributes
    {
        bool bInitialized = false;
        FGameplayEffectAttributeCaptureDefinition BaseAttackPowerDef;
        FGameplayEffectAttributeCaptureDefinition FlatAttackPowerDef;
        FGameplayEffectAttributeCaptureDefinition PercentAttackPowerDef;
        FGameplayEffectAttributeCaptureDefinition BaseDefense_TargetDef;
        FGameplayEffectAttributeCaptureDefinition FlatDefense_TargetDef;
        FGameplayEffectAttributeCaptureDefinition PercentDefense_TargetDef;

        void Initialize()
        {
            if (bInitialized) return;
            bInitialized = true;

            BaseAttackPowerDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetBaseAttackPowerAttribute(), EGameplayEffectAttributeCaptureSource::Source, false);
            FlatAttackPowerDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetFlatAttackPowerAttribute(), EGameplayEffectAttributeCaptureSource::Source, false);
            PercentAttackPowerDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetPercentAttackPowerAttribute(), EGameplayEffectAttributeCaptureSource::Source, false);
            BaseDefense_TargetDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetBaseDefenseAttribute(), EGameplayEffectAttributeCaptureSource::Target, false);
            FlatDefense_TargetDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetFlatDefenseAttribute(), EGameplayEffectAttributeCaptureSource::Target, false);
            PercentDefense_TargetDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetPercentDefenseAttribute(), EGameplayEffectAttributeCaptureSource::Target, false);
        }
    };

    static FCapturedAttributes& GetCapturedAttributes()
    {
        static FCapturedAttributes Attributes;
        return Attributes;
    }
}

UDJ01DamageExecution::UDJ01DamageExecution()
{
    // 捕获定义延迟到 Execute_Implementation 首次调用时初始化
    // 避免静态初始化顺序问题
}

void UDJ01DamageExecution::Execute_Implementation(
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
    const bool bTarget_Status_Immunity_Damage = EvalParams.TargetTags && EvalParams.TargetTags->HasTag(DJ01GameplayTags::Status_Immunity_Damage);

    // ========== 获取属性值 ==========
    float BaseAttackPower = 0.f, FlatAttackPower = 0.f, PercentAttackPower = 0.f;
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.BaseAttackPowerDef, EvalParams, BaseAttackPower);
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.FlatAttackPowerDef, EvalParams, FlatAttackPower);
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.PercentAttackPowerDef, EvalParams, PercentAttackPower);
    const float AttackPowerValue = (BaseAttackPower + FlatAttackPower) * (1.f + PercentAttackPower);

    float BaseDefense_Target = 0.f, FlatDefense_Target = 0.f, PercentDefense_Target = 0.f;
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.BaseDefense_TargetDef, EvalParams, BaseDefense_Target);
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.FlatDefense_TargetDef, EvalParams, FlatDefense_Target);
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.PercentDefense_TargetDef, EvalParams, PercentDefense_Target);
    const float Defense_TargetValue = (BaseDefense_Target + FlatDefense_Target) * (1.f + PercentDefense_Target);


    // ========== 计算逻辑 ==========
    float FinalValue = 0.0f;
    FinalValue = FMath::Max(AttackPowerValue - Defense_TargetValue, 0);
    if (bTarget_Status_Immunity_Damage){
    FinalValue = 0;
    }

    // ========== 输出结果 ==========
    if (FinalValue != 0.f)
    {
        OutExecutionOutput.AddOutputModifier(FGameplayModifierEvaluatedData(
            UDJ01MetaAttributes::GetDamageIncomingAttribute(), EGameplayModOp::Additive, FinalValue));
    }
}
