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
* 战斗属性集 - 定义角色战斗相关的属性
* 
* 基础战斗属性：
* - AttackPower: 物理攻击力
* - MagicPower: 魔法攻击力（影响所有魔法伤害）
* - Defense: 物理防御力
* - MagicDefense: 魔法防御力
* - CriticalRate: 暴击率
* - CriticalDamage: 暴击伤害倍率
* 
* 七系元素亲和度（0-100，影响对应元素魔法的威力和效果）：
* - WindAffinity: 风系亲和 - 机动控制
* - LightAffinity: 光系亲和 - 支援治疗
* - IceAffinity: 冰系亲和 - 控制防御
* - DarkAffinity: 暗系亲和 - 潜行心控
* - FireAffinity: 火系亲和 - 爆发输出
* - WaterAffinity: 水系亲和 - 净化治疗
* - ThunderAffinity: 雷系亲和 - 速度爆发
* 
* 七系元素抗性（百分比减伤）：
* - WindResistance, LightResistance, IceResistance
* - DarkResistance, FireResistance, WaterResistance, ThunderResistance
*/
UCLASS(BlueprintType)
class DJ01_API UDJ01CombatSet : public UDJ01AttributeSet
{
	GENERATED_BODY()

public:

	UDJ01CombatSet();

	// ==================== 基础战斗属性 ====================
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, AttackPower);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, MagicPower);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, Defense);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, MagicDefense);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, CriticalRate);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, CriticalDamage);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, AttackSpeed);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, MovementSpeedBonus);
	
	// ==================== 七系元素亲和度 ====================
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, WindAffinity);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, LightAffinity);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, IceAffinity);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, DarkAffinity);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, FireAffinity);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, WaterAffinity);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, ThunderAffinity);
	
	// ==================== 七系元素抗性 ====================
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, WindResistance);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, LightResistance);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, IceResistance);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, DarkResistance);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, FireResistance);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, WaterResistance);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, ThunderResistance);
	
	// ==================== 元属性（伤害计算用） ====================
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, BaseDamage);
	ATTRIBUTE_ACCESSORS(UDJ01CombatSet, BaseHeal);

protected:

	// ==================== 基础战斗属性复制 ====================
	UFUNCTION()
	void OnRep_AttackPower(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_MagicPower(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_Defense(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_MagicDefense(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_CriticalRate(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_CriticalDamage(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_AttackSpeed(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_MovementSpeedBonus(const FGameplayAttributeData& OldValue);

	// ==================== 元素亲和度复制 ====================
	UFUNCTION()
	void OnRep_WindAffinity(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_LightAffinity(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_IceAffinity(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_DarkAffinity(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_FireAffinity(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_WaterAffinity(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_ThunderAffinity(const FGameplayAttributeData& OldValue);

	// ==================== 元素抗性复制 ====================
	UFUNCTION()
	void OnRep_WindResistance(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_LightResistance(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_IceResistance(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_DarkResistance(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_FireResistance(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_WaterResistance(const FGameplayAttributeData& OldValue);
	
	UFUNCTION()
	void OnRep_ThunderResistance(const FGameplayAttributeData& OldValue);

	// ==================== 元属性复制 ====================
	UFUNCTION()
	void OnRep_BaseDamage(const FGameplayAttributeData& OldValue);

	UFUNCTION()
	void OnRep_BaseHeal(const FGameplayAttributeData& OldValue);

	virtual void PreAttributeChange(const FGameplayAttribute& Attribute, float& NewValue) override;

private:

	// ==================== 基础战斗属性 ====================
	
	// 物理攻击力 - 影响物理技能和武器伤害
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_AttackPower, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData AttackPower;
	
	// 魔法攻击力 - 影响所有魔法伤害的基础加成
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_MagicPower, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData MagicPower;
	
	// 物理防御力 - 减少受到的物理伤害
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_Defense, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData Defense;
	
	// 魔法防御力 - 减少受到的魔法伤害
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_MagicDefense, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData MagicDefense;
	
	// 暴击率 (0-100%)
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_CriticalRate, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData CriticalRate;
	
	// 暴击伤害倍率 (默认 1.5 = 150%)
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_CriticalDamage, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData CriticalDamage;
	
	// 攻击速度加成 (百分比)
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_AttackSpeed, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData AttackSpeed;
	
	// 移动速度加成 (百分比)
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_MovementSpeedBonus, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData MovementSpeedBonus;

	// ==================== 七系元素亲和度 (0-100) ====================
	// 亲和度影响对应元素魔法的威力、效果持续时间、特殊效果触发概率
	
	// 风系亲和 - 机动控制：疾风步、推拒之风、风刃
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_WindAffinity, Category = "DJ01|ElementalAffinity", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData WindAffinity;
	
	// 光系亲和 - 支援治疗：治愈之光、光束射击、圣光屏障
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_LightAffinity, Category = "DJ01|ElementalAffinity", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData LightAffinity;
	
	// 冰系亲和 - 控制防御：冰锥射击、冰墙术、冰牢困敌
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_IceAffinity, Category = "DJ01|ElementalAffinity", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData IceAffinity;
	
	// 暗系亲和 - 潜行心控：阴影隐身、恐惧术、心灵控制
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_DarkAffinity, Category = "DJ01|ElementalAffinity", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData DarkAffinity;
	
	// 火系亲和 - 爆发输出：火球术、火焰喷射、烈焰风暴
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_FireAffinity, Category = "DJ01|ElementalAffinity", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData FireAffinity;
	
	// 水系亲和 - 净化治疗：水球射击、净化之水、治愈泉水
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_WaterAffinity, Category = "DJ01|ElementalAffinity", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData WaterAffinity;
	
	// 雷系亲和 - 速度爆发：闪电箭、连锁闪电、超载爆发
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_ThunderAffinity, Category = "DJ01|ElementalAffinity", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData ThunderAffinity;

	// ==================== 七系元素抗性 (0-100%) ====================
	// 抗性表示对应元素伤害的百分比减免
	
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_WindResistance, Category = "DJ01|ElementalResistance", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData WindResistance;
	
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_LightResistance, Category = "DJ01|ElementalResistance", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData LightResistance;
	
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_IceResistance, Category = "DJ01|ElementalResistance", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData IceResistance;
	
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_DarkResistance, Category = "DJ01|ElementalResistance", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData DarkResistance;
	
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_FireResistance, Category = "DJ01|ElementalResistance", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData FireResistance;
	
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_WaterResistance, Category = "DJ01|ElementalResistance", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData WaterResistance;
	
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_ThunderResistance, Category = "DJ01|ElementalResistance", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData ThunderResistance;

	// ==================== 元属性（伤害计算用） ====================
	
	// 基础伤害 - 伤害计算执行中使用
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseDamage, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData BaseDamage;

	// 基础治疗 - 治疗计算执行中使用
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_BaseHeal, Category = "DJ01|Combat", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData BaseHeal;
};
