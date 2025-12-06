// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01DamageCalculator.h"
#include "DJ01DamageFormulaConfig.h"
#include "AbilitySystemComponent.h"
#include "GameplayTagContainer.h"

FDamageCalculationResult UDJ01DamageCalculator::CalculateDamage(
	const FDamageCalculationContext& Context,
	const UDJ01DamageFormulaConfig* Config)
{
	FDamageCalculationResult Result;
	
	if (!Config)
	{
		Result.FinalDamage = Context.BaseDamage;
		Result.DebugLog.Add(TEXT("No config provided, using base damage"));
		return Result;
	}
	
	float CurrentDamage = Context.BaseDamage;
	
	if (Config->bEnableDebugLog)
	{
		Result.DebugLog.Add(FString::Printf(TEXT("=== Damage Calculation Start ===\nBase Damage: %.2f"), Context.BaseDamage));
	}
	
	// 获取所有修正器并按优先级排序
	TArray<FDamageModifierConfig> AllModifiers = Config->GetAllModifiersSorted();
	
	// 依次应用修正器
	for (const FDamageModifierConfig& Modifier : AllModifiers)
	{
		if (!Modifier.bEnabled)
		{
			continue;
		}
		
		// 真实伤害跳过防御相关的修正器
		if (Context.bIsTrueDamage && 
			Modifier.Source == EDamageModifierSource::Defender &&
			Modifier.Operation == EDamageModifierOperation::Reduction)
		{
			if (Config->bEnableDebugLog)
			{
				Result.DebugLog.Add(FString::Printf(TEXT("[SKIP] %s (True Damage ignores defense)"), *Modifier.ModifierName));
			}
			continue;
		}
		
		// 检查条件
		if (Modifier.Condition.bCheckTag && !CheckModifierCondition(Modifier.Condition, Context))
		{
			continue;
		}
		
		float PreviousDamage = CurrentDamage;
		CurrentDamage = ApplyModifier(CurrentDamage, Modifier, Context, Result);
		
		if (Config->bEnableDebugLog)
		{
			Result.DebugLog.Add(FString::Printf(TEXT("[%s] %.2f -> %.2f"), 
				*Modifier.ModifierName, PreviousDamage, CurrentDamage));
		}
	}
	
	// 应用伤害限制
	Result.FinalDamage = Config->ClampDamage(CurrentDamage);
	
	if (Config->bEnableDebugLog)
	{
		Result.DebugLog.Add(FString::Printf(TEXT("=== Final Damage: %.2f ==="), Result.FinalDamage));
	}
	
	return Result;
}

float UDJ01DamageCalculator::ApplyModifier(
	float CurrentDamage,
	const FDamageModifierConfig& Modifier,
	const FDamageCalculationContext& Context,
	FDamageCalculationResult& OutResult)
{
	// 获取源属性值
	float SourceValue = 0.0f;
	
	if (Modifier.SourceAttribute.IsValid())
	{
		const UAbilitySystemComponent* SourceASC = nullptr;
		
		switch (Modifier.Source)
		{
		case EDamageModifierSource::Attacker:
			SourceASC = Context.AttackerASC.Get();
			break;
		case EDamageModifierSource::Defender:
			SourceASC = Context.DefenderASC.Get();
			break;
		default:
			break;
		}
		
		if (SourceASC)
		{
			SourceValue = GetAttributeValue(SourceASC, Modifier.SourceAttribute);
		}
	}
	
	// 根据操作类型计算
	switch (Modifier.Operation)
	{
	case EDamageModifierOperation::Scale:
		// Damage *= (1 + Attribute * Coefficient)
		return CurrentDamage * (1.0f + SourceValue * Modifier.Coefficient);
		
	case EDamageModifierOperation::Reduction:
		// Damage *= Constant / (Constant + Attribute)
		{
			float Multiplier = Modifier.Constant / (Modifier.Constant + FMath::Max(0.0f, SourceValue));
			return CurrentDamage * Multiplier;
		}
		
	case EDamageModifierOperation::Multiply:
		// Damage *= Coefficient (条件已在外部检查)
		if (Modifier.Condition.bCheckTag)
		{
			OutResult.bHitWeakness = true;  // 假设条件触发的倍乘是弱点
		}
		return CurrentDamage * Modifier.Coefficient;
		
	case EDamageModifierOperation::Compare:
		// 攻防对抗 (如暴击)
		{
			float DefenderValue = 0.0f;
			if (Context.DefenderASC.IsValid() && Modifier.CompareAttribute.IsValid())
			{
				DefenderValue = GetAttributeValue(Context.DefenderASC.Get(), Modifier.CompareAttribute);
			}
			
			// 简单的对抗公式: 成功率 = SourceValue - DefenderValue
			float SuccessRate = FMath::Clamp((SourceValue - DefenderValue) / 100.0f, 0.0f, 1.0f);
			
			// 随机判定
			if (FMath::FRand() < SuccessRate)
			{
				OutResult.bWasCritical = true;
				return CurrentDamage * Modifier.Coefficient;
			}
			return CurrentDamage;
		}
		
	case EDamageModifierOperation::Penetration:
		// 穿透: 减少对方防御效果
		// 这个需要配合 Reduction 使用，这里简化处理
		return CurrentDamage;
		
	default:
		return CurrentDamage;
	}
}

float UDJ01DamageCalculator::GetAttributeValue(
	const UAbilitySystemComponent* ASC,
	const FGameplayAttribute& Attribute)
{
	if (!ASC || !Attribute.IsValid())
	{
		return 0.0f;
	}
	
	bool bFound = false;
	float Value = ASC->GetGameplayAttributeValue(Attribute, bFound);
	
	return bFound ? Value : 0.0f;
}

bool UDJ01DamageCalculator::CheckModifierCondition(
	const FDamageModifierCondition& Condition,
	const FDamageCalculationContext& Context)
{
	if (!Condition.bCheckTag)
	{
		return true;
	}
	
	bool bAttackerHasTag = true;
	bool bDefenderHasTag = true;
	
	if (Condition.RequiredAttackerTag.IsValid())
	{
		bAttackerHasTag = Context.AttackerTags && 
			Context.AttackerTags->HasTag(Condition.RequiredAttackerTag);
	}
	
	if (Condition.RequiredDefenderTag.IsValid())
	{
		bDefenderHasTag = Context.DefenderTags && 
			Context.DefenderTags->HasTag(Condition.RequiredDefenderTag);
	}
	
	if (Condition.bRequireBothTags)
	{
		return bAttackerHasTag && bDefenderHasTag;
	}
	
	return bAttackerHasTag || bDefenderHasTag;
}