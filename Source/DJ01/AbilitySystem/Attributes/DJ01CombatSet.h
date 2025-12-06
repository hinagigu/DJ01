// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "AbilitySystemComponent.h"
#include "DJ01AttributeSet.h"

#include "DJ01CombatSet.generated.h"

class UObject;
struct FFrame;


/**
* UDJ01CombatSet
*
* 战斗属性集 - 简化版
* 
* ============================================================
* 设计理念:
* ============================================================
* 保持属性最小化，复杂逻辑用 GameplayTag 驱动
* 
* 核心战斗属性（4个）:
* - AttackPower: 物理攻击力 - 影响物理伤害
* - MagicPower: 魔法攻击力 - 影响魔法伤害
* - Defense: 物理防御力 - 减免物理伤害
* - MagicDefense: 魔法防御力 - 减免魔法伤害
* 
* 辅助属性（2个）:
* - AttackSpeed: 攻击速度加成
* - MovementSpeedBonus: 移动速度加成
* 
* 元属性（2个，计算用）:
* - BaseDamage: 技能基础伤害
* - BaseHeal: 技能基础治疗
* 
* ============================================================
* 元素系统说明:
* ============================================================
* 元素不再使用属性，改用 GameplayTag 弱点系统:
* - 敌人身上挂 Tag: Weakness.Element.Fire, Weakness.Element.Ice 等
* - 技能携带 Tag: Damage.Element.Fire 等
* - 命中弱点时伤害 +50%（在 DamageExecution 中处理）
* 
* 这样设计的好处:
* 1. 属性数量从 24 降到 8
* 2. 敌人配置更简单（只标记弱点，不用填14个元素值）
* 3. 平衡更容易（弱点就是 +50%，没有复杂的公式）
*/
UCLASS(BlueprintType)
class DJ01_API UDJ01CombatSet : public UDJ01AttributeSet
{
	GENERATED_BODY()

public:

	UDJ01CombatSet();

	// ==================== 核心战斗属性（4个） ====================
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, AttackPower);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, MagicPower);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, Defense);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, MagicDefense);
	
	// ==================== 辅助属性（2个） ====================
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, AttackSpeed);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, MovementSpeedBonus);
	
	// ==================== 元属性（2个，伤害计算用） ====================
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, BaseDamage);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, BaseHeal);

protected:

	// ==================== 属性复制回调 ====================
	UFUNCTION()
	void OnRep_AttackPower(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_MagicPower(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_Defense(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_MagicDefense(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_AttackSpeed(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_MovementSpeedBonus(const FGameplayAttributeData& OldValue);

	UFUNCTION()
	void OnRep_BaseDamage(const FGameplayAttributeData& OldValue);

	UFUNCTION()
	void OnRep_BaseHeal(const FGameplayAttributeData& OldValue);

	virtual void PreAttributeChange(const FGameplayAttribute& Attribute, float& NewValue) override;

private:

	// ==================== 核心战斗属性 ====================
	
	// 物理攻击力 - 影响物理技能和武器伤害
	// 公式: 物理伤害 = BaseDamage * (1 + AttackPower / 100)
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_AttackPower, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData AttackPower;
	
	// 魔法攻击力 - 影响所有魔法伤害
	// 公式: 魔法伤害 = BaseDamage * (1 + MagicPower / 100)
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_MagicPower, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData MagicPower;
	
	// 物理防御力 - 减少受到的物理伤害
	// 公式: 减伤率 = 100 / (100 + Defense)
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_Defense, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData Defense;
	
	// 魔法防御力 - 减少受到的魔法伤害
	// 公式: 减伤率 = 100 / (100 + MagicDefense)
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_MagicDefense, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData MagicDefense;

	// ==================== 辅助属性 ====================
	
	// 攻击速度加成 (百分比，0 = 正常速度，50 = 快50%)
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_AttackSpeed, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData AttackSpeed;
	
	// 移动速度加成 (百分比，0 = 正常速度，50 = 快50%)
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_MovementSpeedBonus, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData MovementSpeedBonus;

	// ==================== 元属性（计算用，不持久化） ====================
	
	// 基础伤害 - 由技能设置，在 DamageExecution 中使用
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseDamage, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData BaseDamage;

	// 基础治疗 - 由技能设置，在 HealExecution 中使用
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseHeal, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData BaseHeal;
};
