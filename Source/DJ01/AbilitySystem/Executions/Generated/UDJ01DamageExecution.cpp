// ============================================================
// UDJ01DamageExecution
// 自动生成，可根据需要修改计算逻辑
// 生成时间: 2026-01-05 10:24:53
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
        FGameplayEffectAttributeCaptureDefinition BaseDefense_TargetDef;
        FGameplayEffectAttributeCaptureDefinition FlatDefense_TargetDef;
        FGameplayEffectAttributeCaptureDefinition PercentDefense_TargetDef;
        FGameplayEffectAttributeCaptureDefinition BaseMagicDefense_TargetDef;
        FGameplayEffectAttributeCaptureDefinition FlatMagicDefense_TargetDef;
        FGameplayEffectAttributeCaptureDefinition PercentMagicDefense_TargetDef;

        void Initialize()
        {
            if (bInitialized) return;
            bInitialized = true;

            BaseDefense_TargetDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetBaseDefenseAttribute(), EGameplayEffectAttributeCaptureSource::Target, false);
            FlatDefense_TargetDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetFlatDefenseAttribute(), EGameplayEffectAttributeCaptureSource::Target, false);
            PercentDefense_TargetDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetPercentDefenseAttribute(), EGameplayEffectAttributeCaptureSource::Target, false);
            BaseMagicDefense_TargetDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetBaseMagicDefenseAttribute(), EGameplayEffectAttributeCaptureSource::Target, false);
            FlatMagicDefense_TargetDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetFlatMagicDefenseAttribute(), EGameplayEffectAttributeCaptureSource::Target, false);
            PercentMagicDefense_TargetDef = FGameplayEffectAttributeCaptureDefinition(UDJ01StatSet::GetPercentMagicDefenseAttribute(), EGameplayEffectAttributeCaptureSource::Target, false);
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

    // ========== SetByCaller 参数（技能传入） ==========
    const float RawDamage = Spec.GetSetByCallerMagnitude(
        DJ01GameplayTags::SetByCaller_Damage_Raw, false, 0.0f);
    const float DamageType = Spec.GetSetByCallerMagnitude(
        DJ01GameplayTags::SetByCaller_Damage_Type, false, 0.0f);

    // ========== 获取属性值 ==========
    float BaseDefense_Target = 0.f, FlatDefense_Target = 0.f, PercentDefense_Target = 0.f;
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.BaseDefense_TargetDef, EvalParams, BaseDefense_Target);
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.FlatDefense_TargetDef, EvalParams, FlatDefense_Target);
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.PercentDefense_TargetDef, EvalParams, PercentDefense_Target);
    const float Defense_TargetValue = (BaseDefense_Target + FlatDefense_Target) * (1.f + PercentDefense_Target);

    float BaseMagicDefense_Target = 0.f, FlatMagicDefense_Target = 0.f, PercentMagicDefense_Target = 0.f;
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.BaseMagicDefense_TargetDef, EvalParams, BaseMagicDefense_Target);
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.FlatMagicDefense_TargetDef, EvalParams, FlatMagicDefense_Target);
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.PercentMagicDefense_TargetDef, EvalParams, PercentMagicDefense_Target);
    const float MagicDefense_TargetValue = (BaseMagicDefense_Target + FlatMagicDefense_Target) * (1.f + PercentMagicDefense_Target);


    // ========== 计算逻辑 ==========
    // RawDamage: 技能层计算的原始伤害
    // DamageType: 0=物理, 1=魔法, 2=真实
    
    float FinalValue = 0.0f;
    const int32 DamageTypeInt = FMath::RoundToInt(DamageType);
    
    if (!bTarget_Status_Immunity_Damage && RawDamage > 0.f)
    {
        if (DamageTypeInt == 0) // 物理
        {
            // 护甲减伤: Damage * 100 / (100 + Armor)
            FinalValue = RawDamage * 100.f / (100.f + FMath::Max(Defense_TargetValue, 0.f));
        }
        else if (DamageTypeInt == 1) // 魔法
        {
            FinalValue = RawDamage * 100.f / (100.f + FMath::Max(MagicDefense_TargetValue, 0.f));
        }
        else // 真实伤害
        {
            FinalValue = RawDamage;
        }
    }

    // ========== 输出结果 ==========
    if (FinalValue != 0.f)
    {
        OutExecutionOutput.AddOutputModifier(FGameplayModifierEvaluatedData(
            UDJ01MetaAttributes::GetDamageIncomingAttribute(), EGameplayModOp::Additive, FinalValue));
    }
}
