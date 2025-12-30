// Copyright DJ01 Team. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "AttributeSet.h"
#include "AbilitySystemComponent.h"
#include "Net/UnrealNetwork.h"

/**
 * DJ01 三层属性系统宏定义
 * 
 * ============================================================
 * 属性层级
 * ============================================================
 * - Base: 基础值（角色固有、等级成长）
 * - Flat: 固定加成（装备、被动技能）
 * - Percent: 百分比加成（Buff、光环），值为小数如 0.3 = 30%
 * 
 * ============================================================
 * 计算公式
 * ============================================================
 * Total = (Base + Flat) * (1 + Percent)
 * Extra = Total - Base（即"额外值"，如LOL的"额外AD"）
 * 
 * ============================================================
 * 使用示例
 * ============================================================
 * 
 * // ===== 头文件 (.h) =====
 * 
 * UCLASS()
 * class UMyStatSet : public UDJ01AttributeSet
 * {
 *     GENERATED_BODY()
 * public:
 *     // 声明三层属性
 *     DECLARE_LAYERED_ATTRIBUTE(UMyStatSet, AttackPower)
 * protected:
 *     // 声明 OnRep 函数
 *     DECLARE_LAYERED_ATTRIBUTE_ONREP(AttackPower)
 * };
 * 
 * // ===== 实现文件 (.cpp) =====
 * 
 * void UMyStatSet::GetLifetimeReplicatedProps(...)
 * {
 *     Super::GetLifetimeReplicatedProps(OutLifetimeProps);
 *     REGISTER_LAYERED_ATTRIBUTE_REPLICATION(UMyStatSet, AttackPower)
 * }
 * 
 * IMPLEMENT_LAYERED_ATTRIBUTE_ONREP(UMyStatSet, AttackPower)
 * 
 * ============================================================
 * 生成的接口
 * ============================================================
 * 
 * 使用 DECLARE_LAYERED_ATTRIBUTE(UMyStatSet, AttackPower) 后生成：
 * 
 * 属性:
 *   - BaseAttackPower      (FGameplayAttributeData)
 *   - FlatAttackPower      (FGameplayAttributeData)
 *   - PercentAttackPower   (FGameplayAttributeData)
 * 
 * Getter:
 *   - GetBaseAttackPower()      -> float
 *   - GetFlatAttackPower()      -> float
 *   - GetPercentAttackPower()   -> float
 *   - GetTotalAttackPower()     -> float (计算后的总值)
 *   - GetExtraAttackPower()     -> float (总值 - 基础值)
 * 
 * Setter:
 *   - SetBaseAttackPower(float)
 *   - SetFlatAttackPower(float)
 *   - SetPercentAttackPower(float)
 * 
 * Initter:
 *   - InitBaseAttackPower(float)
 *   - InitFlatAttackPower(float)
 *   - InitPercentAttackPower(float)
 * 
 * GAS 属性获取:
 *   - GetBaseAttackPowerAttribute()    -> FGameplayAttribute
 *   - GetFlatAttackPowerAttribute()    -> FGameplayAttribute
 *   - GetPercentAttackPowerAttribute() -> FGameplayAttribute
 */


// ============================================================
// 三层属性声明宏（头文件使用）
// ============================================================

/**
 * DECLARE_LAYERED_ATTRIBUTE
 * 
 * 声明三层属性：Base + Flat + Percent
 * 
 * @param ClassName - 所在类名（如 UDJ01StatSet）
 * @param AttrName - 属性名（如 AttackPower）
 */
#define DECLARE_LAYERED_ATTRIBUTE(ClassName, AttrName) \
	/* ========== 基础值：角色固有，等级成长 ========== */ \
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_Base##AttrName, Category = "DJ01|"#AttrName, Meta = (AllowPrivateAccess = true)) \
	FGameplayAttributeData Base##AttrName; \
	ATTRIBUTE_ACCESSORS(ClassName, Base##AttrName) \
	\
	/* ========== 固定加成：装备、被动技能 ========== */ \
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_Flat##AttrName, Category = "DJ01|"#AttrName, Meta = (AllowPrivateAccess = true)) \
	FGameplayAttributeData Flat##AttrName; \
	ATTRIBUTE_ACCESSORS(ClassName, Flat##AttrName) \
	\
	/* ========== 百分比加成：Buff、光环 (0.3 = 30%) ========== */ \
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_Percent##AttrName, Category = "DJ01|"#AttrName, Meta = (AllowPrivateAccess = true)) \
	FGameplayAttributeData Percent##AttrName; \
	ATTRIBUTE_ACCESSORS(ClassName, Percent##AttrName) \
	\
	/* ========== 计算函数 ========== */ \
	/** 获取总值: (Base + Flat) * (1 + Percent) */ \
	UFUNCTION(BlueprintPure, Category = "DJ01|Attributes") \
	float GetTotal##AttrName() const \
	{ \
		return (GetBase##AttrName() + GetFlat##AttrName()) * (1.f + GetPercent##AttrName()); \
	} \
	\
	/** 获取额外值: Total - Base（LOL式"额外AD"） */ \
	UFUNCTION(BlueprintPure, Category = "DJ01|Attributes") \
	float GetExtra##AttrName() const \
	{ \
		return GetTotal##AttrName() - GetBase##AttrName(); \
	}


/**
 * DECLARE_LAYERED_ATTRIBUTE_ONREP
 * 
 * 声明三层属性的 OnRep 函数（放在 protected 区域）
 */
#define DECLARE_LAYERED_ATTRIBUTE_ONREP(AttrName) \
	UFUNCTION() \
	void OnRep_Base##AttrName(const FGameplayAttributeData& OldValue); \
	UFUNCTION() \
	void OnRep_Flat##AttrName(const FGameplayAttributeData& OldValue); \
	UFUNCTION() \
	void OnRep_Percent##AttrName(const FGameplayAttributeData& OldValue);


// ============================================================
// 三层属性实现宏（CPP 文件使用）
// ============================================================

/**
 * IMPLEMENT_LAYERED_ATTRIBUTE_ONREP
 * 
 * 实现三层属性的 OnRep 函数
 */
#define IMPLEMENT_LAYERED_ATTRIBUTE_ONREP(ClassName, AttrName) \
	void ClassName::OnRep_Base##AttrName(const FGameplayAttributeData& OldValue) \
	{ \
		GAMEPLAYATTRIBUTE_REPNOTIFY(ClassName, Base##AttrName, OldValue); \
	} \
	void ClassName::OnRep_Flat##AttrName(const FGameplayAttributeData& OldValue) \
	{ \
		GAMEPLAYATTRIBUTE_REPNOTIFY(ClassName, Flat##AttrName, OldValue); \
	} \
	void ClassName::OnRep_Percent##AttrName(const FGameplayAttributeData& OldValue) \
	{ \
		GAMEPLAYATTRIBUTE_REPNOTIFY(ClassName, Percent##AttrName, OldValue); \
	}


/**
 * REGISTER_LAYERED_ATTRIBUTE_REPLICATION
 * 
 * 注册三层属性的网络复制
 * 在 GetLifetimeReplicatedProps 中使用
 */
#define REGISTER_LAYERED_ATTRIBUTE_REPLICATION(ClassName, AttrName) \
	DOREPLIFETIME_CONDITION_NOTIFY(ClassName, Base##AttrName, COND_None, REPNOTIFY_Always); \
	DOREPLIFETIME_CONDITION_NOTIFY(ClassName, Flat##AttrName, COND_None, REPNOTIFY_Always); \
	DOREPLIFETIME_CONDITION_NOTIFY(ClassName, Percent##AttrName, COND_None, REPNOTIFY_Always);


// ============================================================
// 简化的单层属性宏（用于不需要分层的属性，如 Health）
// ============================================================

/**
 * DECLARE_SIMPLE_ATTRIBUTE
 * 
 * 声明普通单层属性（无 Base/Flat/Percent 区分）
 * 适用于：Health, MaxHealth, Mana 等资源类属性
 */
#define DECLARE_SIMPLE_ATTRIBUTE(ClassName, AttrName) \
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_##AttrName, Category = "DJ01|Attributes", Meta = (AllowPrivateAccess = true)) \
	FGameplayAttributeData AttrName; \
	ATTRIBUTE_ACCESSORS(ClassName, AttrName)

#define DECLARE_SIMPLE_ATTRIBUTE_ONREP(AttrName) \
	UFUNCTION() \
	void OnRep_##AttrName(const FGameplayAttributeData& OldValue);

#define IMPLEMENT_SIMPLE_ATTRIBUTE_ONREP(ClassName, AttrName) \
	void ClassName::OnRep_##AttrName(const FGameplayAttributeData& OldValue) \
	{ \
		GAMEPLAYATTRIBUTE_REPNOTIFY(ClassName, AttrName, OldValue); \
	}

#define REGISTER_SIMPLE_ATTRIBUTE_REPLICATION(ClassName, AttrName) \
	DOREPLIFETIME_CONDITION_NOTIFY(ClassName, AttrName, COND_None, REPNOTIFY_Always);


// ============================================================
// 资源型属性宏 (Max + Current + Percent 配对)
// ============================================================

/**
 * DECLARE_RESOURCE_ATTRIBUTE
 * 
 * 声明资源型配对属性：MaxXxx (Layered) + Xxx (Simple) + PercentXxx (百分比)
 * 
 * 例如 DECLARE_RESOURCE_ATTRIBUTE(UMySet, Health) 生成:
 *   - BaseMaxHealth, FlatMaxHealth, PercentMaxHealth (Layered)
 *   - Health (Simple, 当前值)
 *   - PercentHealth (Simple, 百分比 = Health / MaxHealth)
 *   - GetTotalMaxHealth(), GetExtraMaxHealth() (计算函数)
 *   - UpdateHealthPercent() (更新百分比的函数)
 * 
 * @param ClassName - 所在类名
 * @param AttrName - 属性名（如 Health，会生成 MaxHealth + Health + PercentHealth）
 */
#define DECLARE_RESOURCE_ATTRIBUTE(ClassName, AttrName) \
    /* Max 属性 - Layered (支持基础/额外/百分比加成) */ \
    DECLARE_LAYERED_ATTRIBUTE(ClassName, Max##AttrName) \
    /* Current 属性 - Simple (当前值，直接修改) */ \
    DECLARE_SIMPLE_ATTRIBUTE(ClassName, AttrName) \
    /* Percent 属性 - 百分比 (Current / Max)，用于 UI 绑定 */ \
    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_Percent##AttrName, Category = "DJ01|"#AttrName, Meta = (AllowPrivateAccess = true)) \
    FGameplayAttributeData Percent##AttrName; \
    ATTRIBUTE_ACCESSORS(ClassName, Percent##AttrName) \
    \
    /** 更新百分比属性 (Current / Max)，在 Current 或 Max 变化后调用 */ \
    void Update##AttrName##Percent() \
    { \
        const float MaxVal = GetTotalMax##AttrName(); \
        const float NewPercent = (MaxVal > 0.f) ? (Get##AttrName() / MaxVal) : 0.f; \
        SetPercent##AttrName(NewPercent); \
    }

#define DECLARE_RESOURCE_ATTRIBUTE_ONREP(AttrName) \
    DECLARE_LAYERED_ATTRIBUTE_ONREP(Max##AttrName) \
    DECLARE_SIMPLE_ATTRIBUTE_ONREP(AttrName) \
    DECLARE_SIMPLE_ATTRIBUTE_ONREP(Percent##AttrName)

#define IMPLEMENT_RESOURCE_ATTRIBUTE_ONREP(ClassName, AttrName) \
    IMPLEMENT_LAYERED_ATTRIBUTE_ONREP(ClassName, Max##AttrName) \
    IMPLEMENT_SIMPLE_ATTRIBUTE_ONREP(ClassName, AttrName) \
    IMPLEMENT_SIMPLE_ATTRIBUTE_ONREP(ClassName, Percent##AttrName)

#define REGISTER_RESOURCE_ATTRIBUTE_REPLICATION(ClassName, AttrName) \
    REGISTER_LAYERED_ATTRIBUTE_REPLICATION(ClassName, Max##AttrName) \
    REGISTER_SIMPLE_ATTRIBUTE_REPLICATION(ClassName, AttrName) \
    REGISTER_SIMPLE_ATTRIBUTE_REPLICATION(ClassName, Percent##AttrName)


// ============================================================
// 元属性宏（用于计算中间值，如 Damage、Healing）
// ============================================================

/**
 * DECLARE_META_ATTRIBUTE
 * 
 * 声明元属性（不复制，仅用于计算）
 * 适用于：Damage, Healing 等中间计算值
 */
#define DECLARE_META_ATTRIBUTE(ClassName, AttrName) \
    UPROPERTY(BlueprintReadOnly, Category = "DJ01|Meta", Meta = (HideFromModifiers, AllowPrivateAccess = true)) \
    FGameplayAttributeData AttrName; \
    ATTRIBUTE_ACCESSORS(ClassName, AttrName)