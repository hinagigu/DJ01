// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01DamageFormulaConfig.h"
#include "Algo/Sort.h"

UDJ01DamageFormulaConfig::UDJ01DamageFormulaConfig()
{
	// 默认名称
	FormulaName = TEXT("DefaultPhysicalDamage");
	Description = TEXT("Standard physical damage formula with attack scaling and defense reduction.");
	
	// 设置默认的物理伤害公式
	
	// 1. 攻击力缩放
	FDamageModifierConfig AttackScaling;
	AttackScaling.ModifierName = TEXT("Physical Attack Scaling");
	AttackScaling.Source = EDamageModifierSource::Attacker;
	AttackScaling.Operation = EDamageModifierOperation::Scale;
	AttackScaling.Coefficient = 0.01f;  // 每点攻击力 +1%
	AttackScaling.Priority = 10;
	AttackerModifiers.Add(AttackScaling);
	
	// 2. 防御减伤
	FDamageModifierConfig DefenseReduction;
	DefenseReduction.ModifierName = TEXT("Physical Defense Reduction");
	DefenseReduction.Source = EDamageModifierSource::Defender;
	DefenseReduction.Operation = EDamageModifierOperation::Reduction;
	DefenseReduction.Constant = 100.0f;
	DefenseReduction.Priority = 10;
	DefenderModifiers.Add(DefenseReduction);
	
	// 3. 弱点加成 (需要配置 Tag 条件)
	FDamageModifierConfig WeaknessBonus;
	WeaknessBonus.ModifierName = TEXT("Elemental Weakness");
	WeaknessBonus.Source = EDamageModifierSource::Context;
	WeaknessBonus.Operation = EDamageModifierOperation::Multiply;
	WeaknessBonus.Coefficient = 1.5f;
	WeaknessBonus.Condition.bCheckTag = true;
	WeaknessBonus.Condition.bRequireBothTags = true;
	WeaknessBonus.Priority = 10;
	WeaknessBonus.bEnabled = false;  // 默认关闭，需要配置具体的元素 Tag
	FinalModifiers.Add(WeaknessBonus);
}

TArray<FDamageModifierConfig> UDJ01DamageFormulaConfig::GetAllModifiersSorted() const
{
	TArray<FDamageModifierConfig> AllModifiers;
	AllModifiers.Append(AttackerModifiers);
	AllModifiers.Append(DefenderModifiers);
	AllModifiers.Append(FinalModifiers);
	
	// 按优先级排序
	AllModifiers.Sort([](const FDamageModifierConfig& A, const FDamageModifierConfig& B)
	{
		return A.Priority < B.Priority;
	});
	
	return AllModifiers;
}

float UDJ01DamageFormulaConfig::ClampDamage(float Damage) const
{
	float Result = FMath::Max(Damage, MinimumDamage);
	
	if (MaximumDamage > 0.0f)
	{
		Result = FMath::Min(Result, MaximumDamage);
	}
	
	return Result;
}

FPrimaryAssetId UDJ01DamageFormulaConfig::GetPrimaryAssetId() const
{
	return FPrimaryAssetId(TEXT("DamageFormulaConfig"), GetFName());
}