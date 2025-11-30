// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "AbilitySystemComponent.h"
#include "DJ01AttributeSet.h"
#include "NativeGameplayTags.h"

#include "DJ01HealthSet.generated.h"

class UObject;
struct FFrame;

DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(TAG_Gameplay_Damage);
DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(TAG_Gameplay_DamageImmunity);
DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(TAG_Gameplay_DamageSelfDestruct);
DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(TAG_Gameplay_FellOutOfWorld);
DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(TAG_DJ01_Damage_Message);

struct FGameplayEffectModCallbackData;


/**
* UDJ01HealthSet
*
* 健康属性集 - 定义角色生存相关的属性
* 
* 包含属性：
* - Health/MaxHealth: 生命值
* - ManaEnergy/MaxManaEnergy: 魔能值（魔法朋克世界的核心资源）
* - Stamina/MaxStamina: 体力值（用于物理动作如闪避、冲刺）
* 
* 元属性（用于计算，不直接存储）：
* - Healing: 治疗量
* - Damage: 伤害量
* - ManaEnergyRecovery: 魔能恢复量
*/
UCLASS(BlueprintType)
class DJ01_API UDJ01HealthSet : public UDJ01AttributeSet
{
	GENERATED_BODY()

public:

	UDJ01HealthSet();

	// ==================== 生命值 ====================
	ATTRIBUTE_ACCESSORS(UDJ01HealthSet, Health);
	ATTRIBUTE_ACCESSORS(UDJ01HealthSet, MaxHealth);
	
	// ==================== 魔能值 ====================
	// 魔能值是魔法朋克世界的核心资源，用于施放魔法
	ATTRIBUTE_ACCESSORS(UDJ01HealthSet, ManaEnergy);
	ATTRIBUTE_ACCESSORS(UDJ01HealthSet, MaxManaEnergy);
	
	// ==================== 体力值 ====================
	// 体力用于物理动作：闪避、冲刺、重击等
	ATTRIBUTE_ACCESSORS(UDJ01HealthSet, Stamina);
	ATTRIBUTE_ACCESSORS(UDJ01HealthSet, MaxStamina);
	
	// ==================== 元属性（计算用） ====================
	ATTRIBUTE_ACCESSORS(UDJ01HealthSet, Healing);
	ATTRIBUTE_ACCESSORS(UDJ01HealthSet, Damage);
	ATTRIBUTE_ACCESSORS(UDJ01HealthSet, ManaEnergyRecovery);
	ATTRIBUTE_ACCESSORS(UDJ01HealthSet, StaminaRecovery);

	// ==================== 事件委托 ====================
	
	// 生命值变化时触发
	mutable FDJ01AttributeEvent OnHealthChanged;
	// 最大生命值变化时触发
	mutable FDJ01AttributeEvent OnMaxHealthChanged;
	// 生命值归零时触发
	mutable FDJ01AttributeEvent OnOutOfHealth;
	
	// 魔能值变化时触发
	mutable FDJ01AttributeEvent OnManaEnergyChanged;
	// 魔能值耗尽时触发
	mutable FDJ01AttributeEvent OnOutOfManaEnergy;
	
	// 体力值变化时触发
	mutable FDJ01AttributeEvent OnStaminaChanged;
	// 体力值耗尽时触发
	mutable FDJ01AttributeEvent OnOutOfStamina;

protected:

	UFUNCTION()
	void OnRep_Health(const FGameplayAttributeData& OldValue);

	UFUNCTION()
	void OnRep_MaxHealth(const FGameplayAttributeData& OldValue);

	UFUNCTION()
	void OnRep_ManaEnergy(const FGameplayAttributeData& OldValue);

	UFUNCTION()
	void OnRep_MaxManaEnergy(const FGameplayAttributeData& OldValue);

	UFUNCTION()
	void OnRep_Stamina(const FGameplayAttributeData& OldValue);

	UFUNCTION()
	void OnRep_MaxStamina(const FGameplayAttributeData& OldValue);

	virtual bool PreGameplayEffectExecute(FGameplayEffectModCallbackData& Data) override;
	virtual void PostGameplayEffectExecute(const FGameplayEffectModCallbackData& Data) override;

	virtual void PreAttributeBaseChange(const FGameplayAttribute& Attribute, float& NewValue) const override;
	virtual void PreAttributeChange(const FGameplayAttribute& Attribute, float& NewValue) override;
	virtual void PostAttributeChange(const FGameplayAttribute& Attribute, float OldValue, float NewValue) override;

	void ClampAttribute(const FGameplayAttribute& Attribute, float& NewValue) const;

private:

	// ==================== 生命值属性 ====================
	
	// 当前生命值，受 MaxHealth 限制
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_Health, Category = "DJ01|Health", Meta = (HideFromModifiers, AllowPrivateAccess = true))
	FGameplayAttributeData Health;

	// 最大生命值
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_MaxHealth, Category = "DJ01|Health", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData MaxHealth;

	// ==================== 魔能值属性 ====================
	
	// 当前魔能值，魔法朋克世界的核心资源
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_ManaEnergy, Category = "DJ01|ManaEnergy", Meta = (HideFromModifiers, AllowPrivateAccess = true))
	FGameplayAttributeData ManaEnergy;

	// 最大魔能值
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_MaxManaEnergy, Category = "DJ01|ManaEnergy", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData MaxManaEnergy;

	// ==================== 体力值属性 ====================
	
	// 当前体力值
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_Stamina, Category = "DJ01|Stamina", Meta = (HideFromModifiers, AllowPrivateAccess = true))
	FGameplayAttributeData Stamina;

	// 最大体力值
	UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_MaxStamina, Category = "DJ01|Stamina", Meta = (AllowPrivateAccess = true))
	FGameplayAttributeData MaxStamina;

	// ==================== 状态追踪 ====================
	
	bool bOutOfHealth;
	bool bOutOfManaEnergy;
	bool bOutOfStamina;

	// 变化前的值（用于事件广播）
	float HealthBeforeAttributeChange;
	float MaxHealthBeforeAttributeChange;
	float ManaEnergyBeforeAttributeChange;
	float MaxManaEnergyBeforeAttributeChange;
	float StaminaBeforeAttributeChange;
	float MaxStaminaBeforeAttributeChange;

	// ==================== 元属性 ====================
	// 这些属性不是"状态"，而是用于计算的临时值
	
	// 治疗量，直接映射到 +Health
	UPROPERTY(BlueprintReadOnly, Category="DJ01|Health", Meta=(AllowPrivateAccess=true))
	FGameplayAttributeData Healing;

	// 伤害量，直接映射到 -Health
	UPROPERTY(BlueprintReadOnly, Category="DJ01|Health", Meta=(HideFromModifiers, AllowPrivateAccess=true))
	FGameplayAttributeData Damage;

	// 魔能恢复量，映射到 +ManaEnergy
	UPROPERTY(BlueprintReadOnly, Category="DJ01|ManaEnergy", Meta=(AllowPrivateAccess=true))
	FGameplayAttributeData ManaEnergyRecovery;

	// 体力恢复量，映射到 +Stamina
	UPROPERTY(BlueprintReadOnly, Category="DJ01|Stamina", Meta=(AllowPrivateAccess=true))
	FGameplayAttributeData StaminaRecovery;
};
