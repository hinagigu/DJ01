// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "AttributeSet.h"
#include "GameplayTagContainer.h"
#include "DJ01DamageModifierTypes.generated.h"

/**
 * 伤害修正器数据来源
 */
UENUM(BlueprintType)
enum class EDamageModifierSource : uint8
{
	Attacker    UMETA(DisplayName = "攻击方"),
	Defender    UMETA(DisplayName = "防守方"),
	Context     UMETA(DisplayName = "上下文/Tag")
};

/**
 * 伤害修正器计算方式
 */
UENUM(BlueprintType)
enum class EDamageModifierOperation : uint8
{
	// 缩放: Damage *= (1 + Attribute * Coefficient)
	// 例: 攻击力100, 系数0.01 -> 伤害 *1.01
	Scale               UMETA(DisplayName = "属性缩放"),
	
	// 减伤公式: Damage *= Constant / (Constant + Attribute)
	// 例: 防御100, 常数100 -> 伤害 *0.5
	Reduction           UMETA(DisplayName = "减伤公式"),
	
	// 直接乘法: Damage *= Coefficient (当条件满足时)
	// 例: 命中弱点 -> 伤害 *1.5
	Multiply            UMETA(DisplayName = "直接倍乘"),
	
	// 攻防对抗: 用攻击方属性 vs 防守方属性计算
	// 例: 暴击率 vs 暴击抗性
	Compare             UMETA(DisplayName = "攻防对抗"),
	
	// 穿透: 减少对方防御效果
	// 例: 护甲穿透30 -> 对方防御视为减少30
	Penetration         UMETA(DisplayName = "穿透减免")
};

/**
 * 修正器触发条件
 */
USTRUCT(BlueprintType)
struct DJ01_API FDamageModifierCondition
{
	GENERATED_BODY()

	/** 是否需要检查 Tag */
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	bool bCheckTag = false;
	
	/** 攻击方必须拥有的 Tag (如 Damage.Element.Fire) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, meta = (EditCondition = "bCheckTag"))
	FGameplayTag RequiredAttackerTag;
	
	/** 防守方必须拥有的 Tag (如 Weakness.Element.Fire) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, meta = (EditCondition = "bCheckTag"))
	FGameplayTag RequiredDefenderTag;
	
	/** 是否需要两个 Tag 都存在 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, meta = (EditCondition = "bCheckTag"))
	bool bRequireBothTags = false;
};

/**
 * 单个伤害修正器配置
 */
USTRUCT(BlueprintType)
struct DJ01_API FDamageModifierConfig
{
	GENERATED_BODY()

	/** 修正器名称 (用于调试) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	FString ModifierName = TEXT("Unnamed");

	/** 是否启用此修正器 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	bool bEnabled = true;
	
	/** 数据来源 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	EDamageModifierSource Source = EDamageModifierSource::Attacker;
	
	/** 读取的属性 (来自 Source 指定的一方) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	FGameplayAttribute SourceAttribute;
	
	/** 计算方式 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	EDamageModifierOperation Operation = EDamageModifierOperation::Scale;
	
	/** 对抗属性 (仅 Compare/Penetration 模式使用) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, meta = (EditCondition = "Operation == EDamageModifierOperation::Compare || Operation == EDamageModifierOperation::Penetration"))
	FGameplayAttribute CompareAttribute;
	
	/** 系数 (根据 Operation 有不同含义) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	float Coefficient = 1.0f;
	
	/** 常数 (用于 Reduction 公式) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, meta = (EditCondition = "Operation == EDamageModifierOperation::Reduction"))
	float Constant = 100.0f;
	
	/** 触发条件 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	FDamageModifierCondition Condition;
	
	/** 处理优先级 (数值小的先执行) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	int32 Priority = 100;
};