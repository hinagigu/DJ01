// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01CombatSet.h"

#include "DJ01AttributeSet.h"
#include "Net/UnrealNetwork.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01CombatSet)

class FLifetimeProperty;

UDJ01CombatSet::UDJ01CombatSet()
	// 核心战斗属性（简化版 - 只保留4个核心属性）
	: AttackPower(10.0f)       // 物理攻击力
	, MagicPower(10.0f)        // 魔法攻击力
	, Defense(5.0f)            // 物理防御
	, MagicDefense(5.0f)       // 魔法防御
	// 辅助属性
	, AttackSpeed(100.0f)      // 攻击速度基准值
	, MovementSpeedBonus(0.0f) // 移动速度加成
	// 元属性（计算用）
	, BaseDamage(0.0f)
	, BaseHeal(0.0f)
{
}

void UDJ01CombatSet::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
	Super::GetLifetimeReplicatedProps(OutLifetimeProps);

	// 核心战斗属性
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, AttackPower, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, MagicPower, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, Defense, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, MagicDefense, COND_None, REPNOTIFY_Always);
	
	// 辅助属性
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, AttackSpeed, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, MovementSpeedBonus, COND_None, REPNOTIFY_Always);

	// 元属性 (只发送给拥有者)
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, BaseDamage, COND_OwnerOnly, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01CombatSet, BaseHeal, COND_OwnerOnly, REPNOTIFY_Always);
}

// ==================== 核心战斗属性复制回调 ====================

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

void UDJ01CombatSet::OnRep_AttackSpeed(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, AttackSpeed, OldValue);
}

void UDJ01CombatSet::OnRep_MovementSpeedBonus(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01CombatSet, MovementSpeedBonus, OldValue);
}

// ==================== 元属性复制回调 ====================

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

	// 攻击力/魔攻不能为负
	if (Attribute == GetAttackPowerAttribute() || Attribute == GetMagicPowerAttribute())
	{
		NewValue = FMath::Max(NewValue, 0.0f);
	}
	// 防御属性不能为负
	else if (Attribute == GetDefenseAttribute() || Attribute == GetMagicDefenseAttribute())
	{
		NewValue = FMath::Max(NewValue, 0.0f);
	}
	// 攻击速度最小 10%
	else if (Attribute == GetAttackSpeedAttribute())
	{
		NewValue = FMath::Max(NewValue, 10.0f);
	}
	// 移动速度加成最低 -50%（不能完全不动）
	else if (Attribute == GetMovementSpeedBonusAttribute())
	{
		NewValue = FMath::Max(NewValue, -50.0f);
	}
}

