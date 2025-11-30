// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01HealExecution.h"
#include "DJ01/AbilitySystem/Attributes/DJ01HealthSet.h"
#include "DJ01/AbilitySystem/Attributes/DJ01CombatSet.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01HealExecution)


struct FDJ01HealStatics
{
	FGameplayEffectAttributeCaptureDefinition BaseHealDef;

	FDJ01HealStatics()
	{
		BaseHealDef = FGameplayEffectAttributeCaptureDefinition(UDJ01CombatSet::GetBaseHealAttribute(), EGameplayEffectAttributeCaptureSource::Source, true);
	}
};

static FDJ01HealStatics& HealStatics()
{
	static FDJ01HealStatics Statics;
	return Statics;
}


UDJ01HealExecution::UDJ01HealExecution()
{
	RelevantAttributesToCapture.Add(HealStatics().BaseHealDef);
}

void UDJ01HealExecution::Execute_Implementation(const FGameplayEffectCustomExecutionParameters& ExecutionParams, FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const
{
#if WITH_SERVER_CODE
	const FGameplayEffectSpec& Spec = ExecutionParams.GetOwningSpec();

	const FGameplayTagContainer* SourceTags = Spec.CapturedSourceTags.GetAggregatedTags();
	const FGameplayTagContainer* TargetTags = Spec.CapturedTargetTags.GetAggregatedTags();

	FAggregatorEvaluateParameters EvaluateParameters;
	EvaluateParameters.SourceTags = SourceTags;
	EvaluateParameters.TargetTags = TargetTags;

	float BaseHeal = 0.0f;
	ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(HealStatics().BaseHealDef, EvaluateParameters, BaseHeal);

	const float HealingDone = FMath::Max(0.0f, BaseHeal);

	if (HealingDone > 0.0f)
	{
		// 应用治疗修正器，这会在目标的 HealthSet 中被转换为 +Health
		OutExecutionOutput.AddOutputModifier(FGameplayModifierEvaluatedData(UDJ01HealthSet::GetHealingAttribute(), EGameplayModOp::Additive, HealingDone));
	}
#endif // #if WITH_SERVER_CODE
}