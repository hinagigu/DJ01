// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01CombatSet.h"

#include "DJ01AttributeSet.h"
#include "Net/UnrealNetwork.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01CombatSet)

class FLifetimeProperty;

UDJ01CombatSet::UDJ01CombatSet()
	// 基础战斗属性
	: AttackPower(10.0f)
	, MagicPower(10.0f)
	, Defense(5.0f)
	, MagicDefense(5.0f)
	, CriticalRate(5.0f)      // 5% 暴击率
	, CriticalDamage(150.0f)  // 150% 暴击伤害
	, AttackSpeed(100.0f)     // 攻击速度基准值
	, MovementSpeedBonus(0.0f) // 移动速度加成
	// 七元素亲和力 (默认值 0)
	, WindAffinity(0.0f)
	, LightAffinity(0.0f)
	, IceAffinity(0.0f)
	, DarkAffinity(0.0f)
	, FireAffinity(0.0f)
	, WaterAffinity(0.0f)
	, ThunderAffinity(0.0f)
	// 七元素抗性 (默认值 0)
	, WindResistance(0.0f)
	, LightResistance(0.0f)
	, IceResistance(0.0f)
	, DarkResistance(0.0f)
	, FireResistance(0.0f)
	, WaterResistance(0.0f)
	, ThunderResistance(0.0f)
	// 输出修正属性
	, BaseDamage(0.0f)
	, BaseHeal(0.0f)
{
}

void UDJ01CombatSet::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
	Super::GetLifetimeReplicatedProps(OutLifetimeProps);

	// 基础战斗属性
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, AttackPower, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, MagicPower, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, Defense, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, MagicDefense, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, CriticalRate, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, CriticalDamage, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, AttackSpeed, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, MovementSpeedBonus, COND_None, REPNOTIFY_Always);

	// 七元素亲和力
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, WindAffinity, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, LightAffinity, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, IceAffinity, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, DarkAffinity, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, FireAffinity, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, WaterAffinity, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, ThunderAffinity, COND_None, REPNOTIFY_Always);

	// 七元素抗性
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, WindResistance, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, LightResistance, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, IceResistance, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, DarkResistance, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, FireResistance, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, WaterResistance, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, ThunderResistance, COND_None, REPNOTIFY_Always);

	// 输出修正属性 (只发送给拥有者)
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, BaseDamage, COND_OwnerOnly, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, BaseHeal, COND_OwnerOnly, REPNOTIFY_Always);
}

// ==================== 基础战斗属性复制回调 ====================

void UDJ01CombatSet::OnRep_AttackPower(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, AttackPower, OldValue);
}

void UDJ01CombatSet::OnRep_MagicPower(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, MagicPower, OldValue);
}

void UDJ01CombatSet::OnRep_Defense(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, Defense, OldValue);
}

void UDJ01CombatSet::OnRep_MagicDefense(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, MagicDefense, OldValue);
}

void UDJ01CombatSet::OnRep_CriticalRate(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, CriticalRate, OldValue);
}

void UDJ01CombatSet::OnRep_CriticalDamage(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, CriticalDamage, OldValue);
}

void UDJ01CombatSet::OnRep_AttackSpeed(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, AttackSpeed, OldValue);
}

void UDJ01CombatSet::OnRep_MovementSpeedBonus(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, MovementSpeedBonus, OldValue);
}

// ==================== 元素亲和力复制回调 ====================

void UDJ01CombatSet::OnRep_WindAffinity(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, WindAffinity, OldValue);
}

void UDJ01CombatSet::OnRep_LightAffinity(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, LightAffinity, OldValue);
}

void UDJ01CombatSet::OnRep_IceAffinity(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, IceAffinity, OldValue);
}

void UDJ01CombatSet::OnRep_DarkAffinity(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, DarkAffinity, OldValue);
}

void UDJ01CombatSet::OnRep_FireAffinity(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, FireAffinity, OldValue);
}

void UDJ01CombatSet::OnRep_WaterAffinity(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, WaterAffinity, OldValue);
}

void UDJ01CombatSet::OnRep_ThunderAffinity(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, ThunderAffinity, OldValue);
}

// ==================== 元素抗性复制回调 ====================

void UDJ01CombatSet::OnRep_WindResistance(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, WindResistance, OldValue);
}

void UDJ01CombatSet::OnRep_LightResistance(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, LightResistance, OldValue);
}

void UDJ01CombatSet::OnRep_IceResistance(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, IceResistance, OldValue);
}

void UDJ01CombatSet::OnRep_DarkResistance(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, DarkResistance, OldValue);
}

void UDJ01CombatSet::OnRep_FireResistance(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, FireResistance, OldValue);
}

void UDJ01CombatSet::OnRep_WaterResistance(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, WaterResistance, OldValue);
}

void UDJ01CombatSet::OnRep_ThunderResistance(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, ThunderResistance, OldValue);
}

// ==================== 输出修正属性复制回调 ====================

void UDJ01CombatSet::OnRep_BaseDamage(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, BaseDamage, OldValue);
}

void UDJ01CombatSet::OnRep_BaseHeal(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, BaseHeal, OldValue);
}

void UDJ01CombatSet::PreAttributeChange(const FGameplayAttribute& Attribute, float& NewValue)
{
	Super::PreAttributeChange(Attribute, NewValue);

	// 限制暴击率在 0-100%
	if (Attribute == GetCriticalRateAttribute())
	{
		NewValue = FMath::Clamp(NewValue, 0.0f, 100.0f);
	}
	// 暴击伤害最小 100%
	else if (Attribute == GetCriticalDamageAttribute())
	{
		NewValue = FMath::Max(NewValue, 100.0f);
	}
	// 攻击速度最小 10%
	else if (Attribute == GetAttackSpeedAttribute())
	{
		NewValue = FMath::Max(NewValue, 10.0f);
	}
	// 元素抗性限制在 -100% 到 100%（允许负抗性，表示弱点）
	else if (Attribute == GetWindResistanceAttribute() ||
			 Attribute == GetLightResistanceAttribute() ||
			 Attribute == GetIceResistanceAttribute() ||
			 Attribute == GetDarkResistanceAttribute() ||
			 Attribute == GetFireResistanceAttribute() ||
			 Attribute == GetWaterResistanceAttribute() ||
			 Attribute == GetThunderResistanceAttribute())
	{
		NewValue = FMath::Clamp(NewValue, -100.0f, 100.0f);
	}
	// 元素亲和度限制在 0-200（允许超过100通过装备或增益）
	else if (Attribute == GetWindAffinityAttribute() ||
			 Attribute == GetLightAffinityAttribute() ||
			 Attribute == GetIceAffinityAttribute() ||
			 Attribute == GetDarkAffinityAttribute() ||
			 Attribute == GetFireAffinityAttribute() ||
			 Attribute == GetWaterAffinityAttribute() ||
			 Attribute == GetThunderAffinityAttribute())
	{
		NewValue = FMath::Clamp(NewValue, 0.0f, 200.0f);
	}
	// 防御属性不允许负数
	else if (Attribute == GetDefenseAttribute() || Attribute == GetMagicDefenseAttribute())
	{
		NewValue = FMath::Max(NewValue, 0.0f);
	}
}

