// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "DJ01DamageModifierTypes.h"
#include "DJ01DamageCalculator.generated.h"

class UAbilitySystemComponent;
class UDJ01DamageFormulaConfig;
struct FGameplayTagContainer;

/**
 * 伤害计算上下文
 * 包含计算所需的所有信息
 */
USTRUCT(BlueprintType)
struct DJ01_API FDamageCalculationContext
{
	GENERATED_BODY()

	/** 攻击方 ASC */
	UPROPERTY()
	TWeakObjectPtr<UAbilitySystemComponent> AttackerASC;
	
	/** 防守方 ASC */
	UPROPERTY()
	TWeakObjectPtr<UAbilitySystemComponent> DefenderASC;
	
	/** 攻击方 Tags */
	const FGameplayTagContainer* AttackerTags = nullptr;
	
	/** 防守方 Tags */
	const FGameplayTagContainer* DefenderTags = nullptr;
	
	/** 基础伤害 */
	UPROPERTY()
	float BaseDamage = 0.0f;
	
	/** 是否为魔法伤害 */
	UPROPERTY()
	bool bIsMagical = false;
	
	/** 是否为真实伤害 (无视防御) */
	UPROPERTY()
	bool bIsTrueDamage = false;
	
	/** 攻防距离 (用于距离衰减) */
	UPROPERTY()
	float Distance = 0.0f;
};

/**
 * 伤害计算结果
 */
USTRUCT(BlueprintType)
struct DJ01_API FDamageCalculationResult
{
	GENERATED_BODY()

	/** 最终伤害 */
	UPROPERTY()
	float FinalDamage = 0.0f;
	
	/** 是否暴击 */
	UPROPERTY()
	bool bWasCritical = false;
	
	/** 是否命中弱点 */
	UPROPERTY()
	bool bHitWeakness = false;
	
	/** 调试信息 */
	UPROPERTY()
	TArray<FString> DebugLog;
};

/**
 * UDJ01DamageCalculator
 * 
 * 可配置的伤害计算器
 * 根据 DamageFormulaConfig 执行修正器链计算最终伤害
 */
UCLASS(BlueprintType)
class DJ01_API UDJ01DamageCalculator : public UObject
{
	GENERATED_BODY()

public:
	/**
	 * 计算伤害
	 * @param Context 计算上下文
	 * @param Config 伤害公式配置
	 * @return 计算结果
	 */
	UFUNCTION(BlueprintCallable, Category = "Damage Calculator")
	static FDamageCalculationResult CalculateDamage(
		const FDamageCalculationContext& Context,
		const UDJ01DamageFormulaConfig* Config);

private:
	/** 执行单个修正器 */
	static float ApplyModifier(
		float CurrentDamage,
		const FDamageModifierConfig& Modifier,
		const FDamageCalculationContext& Context,
		FDamageCalculationResult& OutResult);
	
	/** 从 ASC 获取属性值 */
	static float GetAttributeValue(
		const UAbilitySystemComponent* ASC,
		const FGameplayAttribute& Attribute);
	
	/** 检查修正器条件是否满足 */
	static bool CheckModifierCondition(
		const FDamageModifierCondition& Condition,
		const FDamageCalculationContext& Context);
};