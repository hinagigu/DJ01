// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01DamageExecution.h"
#include "DJ01DamageFormulaConfig.h"
#include "DJ01DamageCalculator.h"
#include "DJ01/AbilitySystem/Attributes/DJ01HealthSet.h"
#include "DJ01/AbilitySystem/Attributes/DJ01CombatSet.h"
#include "DJ01/AbilitySystem/Public/DJ01GameplayEffectContext.h"
#include "DJ01/Team/Public/DJ01TeamSubsystem.h"
#include "DJ01/System/Public/DJ01GameplayTags.h"
#include "AbilitySystemComponent.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01DamageExecution)

// ============================================================
// 属性捕获定义
// ============================================================

struct FDJ01DamageStatics
{
	// 源方（攻击者）属性
	FGameplayEffectAttributeCaptureDefinition BaseDamageDef;
	FGameplayEffectAttributeCaptureDefinition AttackPowerDef;
	FGameplayEffectAttributeCaptureDefinition MagicPowerDef;
	
	// 目标方（防御者）属性
	FGameplayEffectAttributeCaptureDefinition DefenseDef;
	FGameplayEffectAttributeCaptureDefinition MagicDefenseDef;

	FDJ01DamageStatics()
	{
		// 源方属性
		BaseDamageDef = FGameplayEffectAttributeCaptureDefinition(
			UDJ01CombatSet::GetBaseDamageAttribute(), 
			EGameplayEffectAttributeCaptureSource::Source, true);
		AttackPowerDef = FGameplayEffectAttributeCaptureDefinition(
			UDJ01CombatSet::GetAttackPowerAttribute(), 
			EGameplayEffectAttributeCaptureSource::Source, true);
		MagicPowerDef = FGameplayEffectAttributeCaptureDefinition(
			UDJ01CombatSet::GetMagicPowerAttribute(), 
			EGameplayEffectAttributeCaptureSource::Source, true);
		
		// 目标方属性
		DefenseDef = FGameplayEffectAttributeCaptureDefinition(
			UDJ01CombatSet::GetDefenseAttribute(), 
			EGameplayEffectAttributeCaptureSource::Target, true);
		MagicDefenseDef = FGameplayEffectAttributeCaptureDefinition(
			UDJ01CombatSet::GetMagicDefenseAttribute(), 
			EGameplayEffectAttributeCaptureSource::Target, true);
	}
};

static FDJ01DamageStatics& DamageStatics()
{
	static FDJ01DamageStatics Statics;
	return Statics;
}


// ============================================================
// 构造函数
// ============================================================

UDJ01DamageExecution::UDJ01DamageExecution()
{
	// 注册需要捕获的属性（用于硬编码后备模式）
	RelevantAttributesToCapture.Add(DamageStatics().BaseDamageDef);
	RelevantAttributesToCapture.Add(DamageStatics().AttackPowerDef);
	RelevantAttributesToCapture.Add(DamageStatics().MagicPowerDef);
	RelevantAttributesToCapture.Add(DamageStatics().DefenseDef);
	RelevantAttributesToCapture.Add(DamageStatics().MagicDefenseDef);
}


// ============================================================
// 核心执行逻辑
// ============================================================

void UDJ01DamageExecution::Execute_Implementation(
	const FGameplayEffectCustomExecutionParameters& ExecutionParams, 
	FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const
{
#if WITH_SERVER_CODE
	const FGameplayEffectSpec& Spec = ExecutionParams.GetOwningSpec();
	FDJ01GameplayEffectContext* TypedContext = FDJ01GameplayEffectContext::ExtractEffectContext(Spec.GetContext());
	check(TypedContext);

	const FGameplayTagContainer* SourceTags = Spec.CapturedSourceTags.GetAggregatedTags();
	const FGameplayTagContainer* TargetTags = Spec.CapturedTargetTags.GetAggregatedTags();

	// ============================================================
	// Step 1: 计算伤害（选择模式）
	// ============================================================
	
	float CalculatedDamage = 0.0f;
	
	// 尝试加载数据驱动配置
	const UDJ01DamageFormulaConfig* Config = DefaultFormulaConfig.LoadSynchronous();
	
	if (Config)
	{
		// 数据驱动模式
		CalculatedDamage = CalculateDamageWithConfig(ExecutionParams, Config, SourceTags, TargetTags);
		
		UE_LOG(LogTemp, Verbose, TEXT("DJ01 Damage [DataDriven]: Using formula '%s', Result=%.1f"),
			*Config->FormulaName.ToString(), CalculatedDamage);
	}
	else
	{
		// 硬编码后备模式
		CalculatedDamage = CalculateDamageHardcoded(ExecutionParams, SourceTags, TargetTags);
		
		UE_LOG(LogTemp, Verbose, TEXT("DJ01 Damage [Hardcoded]: No config, using fallback formula, Result=%.1f"),
			CalculatedDamage);
	}
	
	// ============================================================
	// Step 2: 团队伤害检查
	// ============================================================
	
	float TeamMultiplier = 1.0f;
	
	const AActor* EffectCauser = TypedContext->GetEffectCauser();
	UAbilitySystemComponent* TargetASC = ExecutionParams.GetTargetAbilitySystemComponent();
	AActor* TargetActor = TargetASC ? TargetASC->GetAvatarActor_Direct() : nullptr;
	
	if (TargetActor && EffectCauser)
	{
		if (UDJ01TeamSubsystem* TeamSubsystem = UDJ01TeamSubsystem::Get(TargetActor->GetWorld()))
		{
			// 如果不能攻击目标（同队友军），伤害为0
			TeamMultiplier = TeamSubsystem->CanObjectAttackObject(EffectCauser, TargetActor) ? 1.0f : 0.0f;
		}
	}

	// ============================================================
	// Step 3: 输出最终伤害
	// ============================================================
	
	const float FinalDamage = FMath::Max(CalculatedDamage * TeamMultiplier, 0.0f);

	if (FinalDamage > 0.0f)
	{
		OutExecutionOutput.AddOutputModifier(
			FGameplayModifierEvaluatedData(
				UDJ01HealthSet::GetDamageAttribute(), 
				EGameplayModOp::Additive, 
				FinalDamage));
	}

#endif // #if WITH_SERVER_CODE
}


// ============================================================
// 数据驱动模式计算
// ============================================================

float UDJ01DamageExecution::CalculateDamageWithConfig(
	const FGameplayEffectCustomExecutionParameters& ExecutionParams,
	const UDJ01DamageFormulaConfig* Config,
	const FGameplayTagContainer* SourceTags,
	const FGameplayTagContainer* TargetTags) const
{
	UAbilitySystemComponent* SourceASC = ExecutionParams.GetSourceAbilitySystemComponent();
	UAbilitySystemComponent* TargetASC = ExecutionParams.GetTargetAbilitySystemComponent();
	
	// 构建计算上下文
	FDamageCalculationContext Context;
	Context.AttackerASC = SourceASC;
	Context.DefenderASC = TargetASC;
	Context.AttackerTags = SourceTags;
	Context.DefenderTags = TargetTags;
	
	// 判断伤害类型
	Context.bIsMagical = SourceTags && SourceTags->HasTag(DJ01GameplayTags::Damage_Type_Magical);
	Context.bIsTrueDamage = SourceTags && SourceTags->HasTag(DJ01GameplayTags::Damage_Type_True);
	
	// 设置初始伤害（从捕获的 BaseDamage 属性获取）
	FAggregatorEvaluateParameters EvaluateParameters;
	EvaluateParameters.SourceTags = SourceTags;
	EvaluateParameters.TargetTags = TargetTags;
	
	float InitialBaseDamage = 0.0f;
	ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(
		DamageStatics().BaseDamageDef, EvaluateParameters, InitialBaseDamage);
	Context.BaseDamage = InitialBaseDamage;
	
	// 调用计算器
	FDamageCalculationResult Result = UDJ01DamageCalculator::CalculateDamage(Context, Config);
	
	return Result.FinalDamage;
}


// ============================================================
// 硬编码后备模式
// ============================================================

float UDJ01DamageExecution::CalculateDamageHardcoded(
	const FGameplayEffectCustomExecutionParameters& ExecutionParams,
	const FGameplayTagContainer* SourceTags,
	const FGameplayTagContainer* TargetTags) const
{
	FAggregatorEvaluateParameters EvaluateParameters;
	EvaluateParameters.SourceTags = SourceTags;
	EvaluateParameters.TargetTags = TargetTags;

	// 获取属性
	float BaseDamage = 0.0f;
	float AttackPower = 0.0f;
	float MagicPower = 0.0f;
	float Defense = 0.0f;
	float MagicDefense = 0.0f;
	
	ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(DamageStatics().BaseDamageDef, EvaluateParameters, BaseDamage);
	ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(DamageStatics().AttackPowerDef, EvaluateParameters, AttackPower);
	ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(DamageStatics().MagicPowerDef, EvaluateParameters, MagicPower);
	ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(DamageStatics().DefenseDef, EvaluateParameters, Defense);
	ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(DamageStatics().MagicDefenseDef, EvaluateParameters, MagicDefense);

	// 判断伤害类型
	bool bIsMagical = SourceTags && SourceTags->HasTag(DJ01GameplayTags::Damage_Type_Magical);
	bool bIsTrue = SourceTags && SourceTags->HasTag(DJ01GameplayTags::Damage_Type_True);
	
	// 计算攻击加成
	float ScaledDamage = BaseDamage;
	if (bIsTrue)
	{
		ScaledDamage = BaseDamage;
	}
	else if (bIsMagical)
	{
		ScaledDamage = BaseDamage * (1.0f + MagicPower / 100.0f);
	}
	else
	{
		ScaledDamage = BaseDamage * (1.0f + AttackPower / 100.0f);
	}
	
	// 防御减免
	float DefendedDamage = ScaledDamage;
	if (!bIsTrue)
	{
		float EffectiveDefense = bIsMagical ? MagicDefense : Defense;
		EffectiveDefense = FMath::Max(0.0f, EffectiveDefense);
		float DefenseMultiplier = 100.0f / (100.0f + EffectiveDefense);
		DefendedDamage = ScaledDamage * DefenseMultiplier;
	}
	
	// 弱点检查
	float FinalDamage = DefendedDamage;
	if (!bIsTrue && CheckWeaknessHit(SourceTags, TargetTags))
	{
		FinalDamage = DefendedDamage * WeaknessMultiplier;
	}
	
	return FinalDamage;
}


// ============================================================
// 弱点检查
// ============================================================

bool UDJ01DamageExecution::CheckWeaknessHit(
	const FGameplayTagContainer* SourceTags, 
	const FGameplayTagContainer* TargetTags) const
{
	if (!SourceTags || !TargetTags)
	{
		return false;
	}
	
	// 检查每种元素：技能有对应元素 && 目标有对应弱点
	
	if (SourceTags->HasTag(DJ01GameplayTags::Damage_Element_Fire) && 
		TargetTags->HasTag(DJ01GameplayTags::Weakness_Element_Fire))
	{
		return true;
	}
	
	if (SourceTags->HasTag(DJ01GameplayTags::Damage_Element_Ice) && 
		TargetTags->HasTag(DJ01GameplayTags::Weakness_Element_Ice))
	{
		return true;
	}
	
	if (SourceTags->HasTag(DJ01GameplayTags::Damage_Element_Thunder) && 
		TargetTags->HasTag(DJ01GameplayTags::Weakness_Element_Thunder))
	{
		return true;
	}
	
	if (SourceTags->HasTag(DJ01GameplayTags::Damage_Element_Wind) && 
		TargetTags->HasTag(DJ01GameplayTags::Weakness_Element_Wind))
	{
		return true;
	}
	
	if (SourceTags->HasTag(DJ01GameplayTags::Damage_Element_Light) && 
		TargetTags->HasTag(DJ01GameplayTags::Weakness_Element_Light))
	{
		return true;
	}
	
	if (SourceTags->HasTag(DJ01GameplayTags::Damage_Element_Dark) && 
		TargetTags->HasTag(DJ01GameplayTags::Weakness_Element_Dark))
	{
		return true;
	}
	
	if (SourceTags->HasTag(DJ01GameplayTags::Damage_Element_Water) && 
		TargetTags->HasTag(DJ01GameplayTags::Weakness_Element_Water))
	{
		return true;
	}
	
	return false;
}