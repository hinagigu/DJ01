// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Engine/DataAsset.h"
#include "DJ01DamageModifierTypes.h"
#include "DJ01DamageFormulaConfig.generated.h"

/**
 * UDJ01DamageFormulaConfig
 * 
 * 可配置的伤害公式系统
 * 
 * ============================================================
 * 设计理念:
 * ============================================================
 * 伤害计算 = BaseDamage → [攻击方修正器链] → [防守方修正器链] → [最终修正器链] → FinalDamage
 * 
 * 每个修正器都是可配置的，支持:
 * - 属性缩放 (如: 攻击力提升伤害)
 * - 减伤公式 (如: 防御降低伤害)
 * - 攻防对抗 (如: 暴击率 vs 暴击抗性)
 * - 条件触发 (如: 命中弱点时额外加成)
 * 
 * ============================================================
 * 使用示例:
 * ============================================================
 * 
 * 标准物理伤害公式:
 * 1. [攻击方] AttackPower 缩放: Damage *= (1 + AttackPower * 0.01)
 * 2. [防守方] Defense 减伤: Damage *= 100 / (100 + Defense)
 * 3. [最终] 弱点检查: if (命中弱点) Damage *= 1.5
 * 
 * 未来扩展 - 暴击系统:
 * 1. [攻击方] CriticalRate vs [防守方] CriticalResist
 * 2. if (暴击成功) Damage *= CriticalDamage / 100
 */
UCLASS(BlueprintType, Const)
class DJ01_API UDJ01DamageFormulaConfig : public UPrimaryDataAsset
{
	GENERATED_BODY()

public:
	UDJ01DamageFormulaConfig();

	// ============================================================
	// 基本信息
	// ============================================================
	
	/** 公式名称 (用于调试和识别) */
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Info")
	FName FormulaName = NAME_None;
	
	/** 公式描述 */
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Info", meta = (MultiLine = true))
	FString Description;

	// ============================================================
	// 修正器链配置
	// ============================================================
	
	/** 攻击方修正器 (按 Priority 排序执行) */
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Modifier Chain")
	TArray<FDamageModifierConfig> AttackerModifiers;
	
	/** 防守方修正器 */
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Modifier Chain")
	TArray<FDamageModifierConfig> DefenderModifiers;
	
	/** 最终修正器 (弱点、环境等) */
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Modifier Chain")
	TArray<FDamageModifierConfig> FinalModifiers;

	// ============================================================
	// 伤害限制
	// ============================================================
	
	/** 最小伤害 */
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Limits")
	float MinimumDamage = 1.0f;
	
	/** 最大伤害 (0 = 无限制) */
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Limits")
	float MaximumDamage = 0.0f;

	// ============================================================
	// 调试选项
	// ============================================================
	
	/** 是否输出调试日志 */
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Debug")
	bool bEnableDebugLog = false;

	// ============================================================
	// 辅助函数
	// ============================================================
	
	/** 获取所有修正器 (已按优先级排序) */
	UFUNCTION(BlueprintPure, Category = "Damage Formula")
	TArray<FDamageModifierConfig> GetAllModifiersSorted() const;
	
	/** 限制伤害值 */
	UFUNCTION(BlueprintPure, Category = "Damage Formula")
	float ClampDamage(float Damage) const;

	// DataAsset 接口
	virtual FPrimaryAssetId GetPrimaryAssetId() const override;
};