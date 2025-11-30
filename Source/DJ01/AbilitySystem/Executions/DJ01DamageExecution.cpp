// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01DamageExecution.h"
#include "DJ01/AbilitySystem/Attributes/DJ01HealthSet.h"
#include "DJ01/AbilitySystem/Attributes/DJ01CombatSet.h"
#include "DJ01/AbilitySystem/Public/DJ01GameplayEffectContext.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilitySourceInterface.h"
#include "DJ01/Team/Public/DJ01TeamSubsystem.h"
#include "Engine/World.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01DamageExecution)

struct FDJ01DamageStatics
{
	FGameplayEffectAttributeCaptureDefinition BaseDamageDef;

	FDJ01DamageStatics()
	{
		BaseDamageDef = FGameplayEffectAttributeCaptureDefinition(UDJ01CombatSet::GetBaseDamageAttribute(), EGameplayEffectAttributeCaptureSource::Source, true);
	}
};

static FDJ01DamageStatics& DamageStatics()
{
	static FDJ01DamageStatics Statics;
	return Statics;
}


UDJ01DamageExecution::UDJ01DamageExecution()
{
	RelevantAttributesToCapture.Add(DamageStatics().BaseDamageDef);
}

void UDJ01DamageExecution::Execute_Implementation(const FGameplayEffectCustomExecutionParameters& ExecutionParams, FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const
{
#if WITH_SERVER_CODE
	const FGameplayEffectSpec& Spec = ExecutionParams.GetOwningSpec();
	FDJ01GameplayEffectContext* TypedContext = FDJ01GameplayEffectContext::ExtractEffectContext(Spec.GetContext());
	check(TypedContext);

	const FGameplayTagContainer* SourceTags = Spec.CapturedSourceTags.GetAggregatedTags();
	const FGameplayTagContainer* TargetTags = Spec.CapturedTargetTags.GetAggregatedTags();

	FAggregatorEvaluateParameters EvaluateParameters;
	EvaluateParameters.SourceTags = SourceTags;
	EvaluateParameters.TargetTags = TargetTags;

	float BaseDamage = 0.0f;
	ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(DamageStatics().BaseDamageDef, EvaluateParameters, BaseDamage);

	const AActor* EffectCauser = TypedContext->GetEffectCauser();
	const FHitResult* HitActorResult = TypedContext->GetHitResult();

	AActor* HitActor = nullptr;
	FVector ImpactLocation = FVector::ZeroVector;
	FVector ImpactNormal = FVector::ZeroVector;
	FVector StartTrace = FVector::ZeroVector;
	FVector EndTrace = FVector::ZeroVector;

	// 从命中结果中获取命中信息
	// 如果没有命中结果（例如直接添加的效果），则使用回退信息
	if (HitActorResult)
	{
		const FHitResult& CurHitResult = *HitActorResult;
		HitActor = CurHitResult.HitObjectHandle.FetchActor();
		if (HitActor)
		{
			ImpactLocation = CurHitResult.ImpactPoint;
			ImpactNormal = CurHitResult.ImpactNormal;
			StartTrace = CurHitResult.TraceStart;
			EndTrace = CurHitResult.TraceEnd;
		}
	}

	// 处理没有命中结果或命中结果没有返回Actor的情况
	UAbilitySystemComponent* TargetAbilitySystemComponent = ExecutionParams.GetTargetAbilitySystemComponent();
	if (!HitActor)
	{
		HitActor = TargetAbilitySystemComponent ? TargetAbilitySystemComponent->GetAvatarActor_Direct() : nullptr;
		if (HitActor)
		{
			ImpactLocation = HitActor->GetActorLocation();
		}
	}

	// 应用团队伤害规则（队友伤害/自伤等）
	float DamageInteractionAllowedMultiplier = 0.0f;
	if (HitActor)
	{
		if (UDJ01TeamSubsystem* TeamSubsystem = UDJ01TeamSubsystem::Get(HitActor->GetWorld()))
		{
			DamageInteractionAllowedMultiplier = TeamSubsystem->CanObjectAttackObject(EffectCauser, HitActor) ? 1.0f : 0.0f;
		}
		else
		{
			// 如果没有团队子系统，默认允许伤害
			DamageInteractionAllowedMultiplier = 1.0f;
		}
	}

	// 计算距离
	double Distance = WORLD_MAX;

	if (TypedContext->HasOrigin())
	{
		Distance = FVector::Dist(TypedContext->GetOrigin(), ImpactLocation);
	}
	else if (EffectCauser)
	{
		Distance = FVector::Dist(EffectCauser->GetActorLocation(), ImpactLocation);
	}
	else
	{
		ensureMsgf(false, TEXT("伤害计算无法从 %s 推断来源位置；回退使用 WORLD_MAX 距离！"), *GetPathNameSafe(Spec.Def));
	}

	// 应用技能源修正器（距离衰减、物理材质衰减）
	float PhysicalMaterialAttenuation = 1.0f;
	float DistanceAttenuation = 1.0f;
	if (const IDJ01AbilitySourceInterface* AbilitySource = TypedContext->GetAbilitySource())
	{
		if (const UPhysicalMaterial* PhysMat = TypedContext->GetPhysicalMaterial())
		{
			PhysicalMaterialAttenuation = AbilitySource->GetPhysicalMaterialAttenuation(PhysMat, SourceTags, TargetTags);
		}

		DistanceAttenuation = AbilitySource->GetDistanceAttenuation(Distance, SourceTags, TargetTags);
	}
	DistanceAttenuation = FMath::Max(DistanceAttenuation, 0.0f);

	// 计算最终伤害（clamp在转换为负生命值时完成）
	const float DamageDone = FMath::Max(BaseDamage * DistanceAttenuation * PhysicalMaterialAttenuation * DamageInteractionAllowedMultiplier, 0.0f);

	if (DamageDone > 0.0f)
	{
		// 应用伤害修正器，这会在目标的 HealthSet 中被转换为 -Health
		OutExecutionOutput.AddOutputModifier(FGameplayModifierEvaluatedData(UDJ01HealthSet::GetDamageAttribute(), EGameplayModOp::Additive, DamageDone));
	}
#endif // #if WITH_SERVER_CODE
}