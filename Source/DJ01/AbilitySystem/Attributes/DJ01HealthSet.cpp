// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01HealthSet.h"
#include "DJ01AttributeSet.h"
#include "DJ01/System/Public/DJ01GameplayTags.h"
#include "Net/UnrealNetwork.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"
#include "Engine/World.h"
#include "GameplayEffectExtension.h"
#include "GameFramework/GameplayMessageSubsystem.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01HealthSet)

UE_DEFINE_GAMEPLAY_TAG(TAG_Gameplay_Damage, "Gameplay.Damage");
UE_DEFINE_GAMEPLAY_TAG(TAG_Gameplay_DamageImmunity, "Gameplay.DamageImmunity");
UE_DEFINE_GAMEPLAY_TAG(TAG_Gameplay_DamageSelfDestruct, "Gameplay.Damage.SelfDestruct");
UE_DEFINE_GAMEPLAY_TAG(TAG_Gameplay_FellOutOfWorld, "Gameplay.Damage.FellOutOfWorld");
UE_DEFINE_GAMEPLAY_TAG(TAG_DJ01_Damage_Message, "DJ01.Damage.Message");

UDJ01HealthSet::UDJ01HealthSet()
	: Health(100.0f)
	, MaxHealth(100.0f)
	, ManaEnergy(100.0f)
	, MaxManaEnergy(100.0f)
	, Stamina(100.0f)
	, MaxStamina(100.0f)
{
	bOutOfHealth = false;
	bOutOfManaEnergy = false;
	bOutOfStamina = false;
	
	HealthBeforeAttributeChange = 0.0f;
	MaxHealthBeforeAttributeChange = 0.0f;
	ManaEnergyBeforeAttributeChange = 0.0f;
	MaxManaEnergyBeforeAttributeChange = 0.0f;
	StaminaBeforeAttributeChange = 0.0f;
	MaxStaminaBeforeAttributeChange = 0.0f;
}

void UDJ01HealthSet::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
	Super::GetLifetimeReplicatedProps(OutLifetimeProps);

	// 生命值
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01HealthSet, Health, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01HealthSet, MaxHealth, COND_None, REPNOTIFY_Always);
	
	// 魔能值
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01HealthSet, ManaEnergy, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01HealthSet, MaxManaEnergy, COND_None, REPNOTIFY_Always);
	
	// 体力值
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01HealthSet, Stamina, COND_None, REPNOTIFY_Always);
	DOREPLIFETIME_CONDITION_NOTIFY(UDJ01HealthSet, MaxStamina, COND_None, REPNOTIFY_Always);
}

// ==================== 生命值复制回调 ====================

void UDJ01HealthSet::OnRep_Health(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01HealthSet, Health, OldValue);

	const float CurrentHealth = GetHealth();
	const float EstimatedMagnitude = CurrentHealth - OldValue.GetCurrentValue();
	
	OnHealthChanged.Broadcast(nullptr, nullptr, nullptr, EstimatedMagnitude, OldValue.GetCurrentValue(), CurrentHealth);

	if (!bOutOfHealth && CurrentHealth <= 0.0f)
	{
		OnOutOfHealth.Broadcast(nullptr, nullptr, nullptr, EstimatedMagnitude, OldValue.GetCurrentValue(), CurrentHealth);
	}

	bOutOfHealth = (CurrentHealth <= 0.0f);
}

void UDJ01HealthSet::OnRep_MaxHealth(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01HealthSet, MaxHealth, OldValue);
	OnMaxHealthChanged.Broadcast(nullptr, nullptr, nullptr, GetMaxHealth() - OldValue.GetCurrentValue(), OldValue.GetCurrentValue(), GetMaxHealth());
}

// ==================== 魔能值复制回调 ====================

void UDJ01HealthSet::OnRep_ManaEnergy(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01HealthSet, ManaEnergy, OldValue);

	const float CurrentManaEnergy = GetManaEnergy();
	const float EstimatedMagnitude = CurrentManaEnergy - OldValue.GetCurrentValue();
	
	OnManaEnergyChanged.Broadcast(nullptr, nullptr, nullptr, EstimatedMagnitude, OldValue.GetCurrentValue(), CurrentManaEnergy);

	if (!bOutOfManaEnergy && CurrentManaEnergy <= 0.0f)
	{
		OnOutOfManaEnergy.Broadcast(nullptr, nullptr, nullptr, EstimatedMagnitude, OldValue.GetCurrentValue(), CurrentManaEnergy);
	}

	bOutOfManaEnergy = (CurrentManaEnergy <= 0.0f);
}

void UDJ01HealthSet::OnRep_MaxManaEnergy(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01HealthSet, MaxManaEnergy, OldValue);
}

// ==================== 体力值复制回调 ====================

void UDJ01HealthSet::OnRep_Stamina(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01HealthSet, Stamina, OldValue);

	const float CurrentStamina = GetStamina();
	const float EstimatedMagnitude = CurrentStamina - OldValue.GetCurrentValue();
	
	OnStaminaChanged.Broadcast(nullptr, nullptr, nullptr, EstimatedMagnitude, OldValue.GetCurrentValue(), CurrentStamina);

	if (!bOutOfStamina && CurrentStamina <= 0.0f)
	{
		OnOutOfStamina.Broadcast(nullptr, nullptr, nullptr, EstimatedMagnitude, OldValue.GetCurrentValue(), CurrentStamina);
	}

	bOutOfStamina = (CurrentStamina <= 0.0f);
}

void UDJ01HealthSet::OnRep_MaxStamina(const FGameplayAttributeData& OldValue)
{
	GAMEPLAYATTRIBUTE_REPNOTIFY(UDJ01HealthSet, MaxStamina, OldValue);
}

// ==================== GameplayEffect 处理 ====================

bool UDJ01HealthSet::PreGameplayEffectExecute(FGameplayEffectModCallbackData& Data)
{
	if (!Super::PreGameplayEffectExecute(Data))
	{
		return false;
	}

	// 处理伤害
	if (Data.EvaluatedData.Attribute == GetDamageAttribute())
	{
		if (Data.EvaluatedData.Magnitude > 0.0f)
		{
			const bool bIsDamageFromSelfDestruct = Data.EffectSpec.GetDynamicAssetTags().HasTagExact(TAG_Gameplay_DamageSelfDestruct);

			if (Data.Target.HasMatchingGameplayTag(TAG_Gameplay_DamageImmunity) && !bIsDamageFromSelfDestruct)
			{
				Data.EvaluatedData.Magnitude = 0.0f;
				return false;
			}

#if !UE_BUILD_SHIPPING
			// 开发模式：检查无敌作弊
			if (Data.Target.HasMatchingGameplayTag(DJ01GameplayTags::Cheat_GodMode) && !bIsDamageFromSelfDestruct)
			{
				Data.EvaluatedData.Magnitude = 0.0f;
				return false;
			}
#endif
		}
	}

	// 保存变化前的值
	HealthBeforeAttributeChange = GetHealth();
	MaxHealthBeforeAttributeChange = GetMaxHealth();
	ManaEnergyBeforeAttributeChange = GetManaEnergy();
	MaxManaEnergyBeforeAttributeChange = GetMaxManaEnergy();
	StaminaBeforeAttributeChange = GetStamina();
	MaxStaminaBeforeAttributeChange = GetMaxStamina();

	return true;
}

void UDJ01HealthSet::PostGameplayEffectExecute(const FGameplayEffectModCallbackData& Data)
{
	Super::PostGameplayEffectExecute(Data);

	const bool bIsDamageFromSelfDestruct = Data.EffectSpec.GetDynamicAssetTags().HasTagExact(TAG_Gameplay_DamageSelfDestruct);
	float MinimumHealth = 0.0f;

#if !UE_BUILD_SHIPPING
	if (!bIsDamageFromSelfDestruct &&
		(Data.Target.HasMatchingGameplayTag(DJ01GameplayTags::Cheat_GodMode) || Data.Target.HasMatchingGameplayTag(DJ01GameplayTags::Cheat_UnlimitedHealth)))
	{
		MinimumHealth = 1.0f;
	}
#endif

	const FGameplayEffectContextHandle& EffectContext = Data.EffectSpec.GetEffectContext();
	AActor* Instigator = EffectContext.GetOriginalInstigator();
	AActor* Causer = EffectContext.GetEffectCauser();

	// ==================== 处理伤害 ====================
	if (Data.EvaluatedData.Attribute == GetDamageAttribute())
	{
		// TODO: 添加伤害消息广播（需要实现 DJ01VerbMessage）
		
		SetHealth(FMath::Clamp(GetHealth() - GetDamage(), MinimumHealth, GetMaxHealth()));
		SetDamage(0.0f);
	}
	// ==================== 处理治疗 ====================
	else if (Data.EvaluatedData.Attribute == GetHealingAttribute())
	{
		SetHealth(FMath::Clamp(GetHealth() + GetHealing(), MinimumHealth, GetMaxHealth()));
		SetHealing(0.0f);
	}
	// ==================== 处理生命值直接修改 ====================
	else if (Data.EvaluatedData.Attribute == GetHealthAttribute())
	{
		SetHealth(FMath::Clamp(GetHealth(), MinimumHealth, GetMaxHealth()));
	}
	// ==================== 处理最大生命值变化 ====================
	else if (Data.EvaluatedData.Attribute == GetMaxHealthAttribute())
	{
		OnMaxHealthChanged.Broadcast(Instigator, Causer, &Data.EffectSpec, Data.EvaluatedData.Magnitude, MaxHealthBeforeAttributeChange, GetMaxHealth());
	}
	// ==================== 处理魔能恢复 ====================
	else if (Data.EvaluatedData.Attribute == GetManaEnergyRecoveryAttribute())
	{
		SetManaEnergy(FMath::Clamp(GetManaEnergy() + GetManaEnergyRecovery(), 0.0f, GetMaxManaEnergy()));
		SetManaEnergyRecovery(0.0f);
	}
	// ==================== 处理魔能值直接修改 ====================
	else if (Data.EvaluatedData.Attribute == GetManaEnergyAttribute())
	{
		SetManaEnergy(FMath::Clamp(GetManaEnergy(), 0.0f, GetMaxManaEnergy()));
	}
	// ==================== 处理体力恢复 ====================
	else if (Data.EvaluatedData.Attribute == GetStaminaRecoveryAttribute())
	{
		SetStamina(FMath::Clamp(GetStamina() + GetStaminaRecovery(), 0.0f, GetMaxStamina()));
		SetStaminaRecovery(0.0f);
	}
	// ==================== 处理体力值直接修改 ====================
	else if (Data.EvaluatedData.Attribute == GetStaminaAttribute())
	{
		SetStamina(FMath::Clamp(GetStamina(), 0.0f, GetMaxStamina()));
	}

	// 生命值变化回调
	if (GetHealth() != HealthBeforeAttributeChange)
	{
		OnHealthChanged.Broadcast(Instigator, Causer, &Data.EffectSpec, Data.EvaluatedData.Magnitude, HealthBeforeAttributeChange, GetHealth());
	}

	// 生命耗尽回调
	if ((GetHealth() <= 0.0f) && !bOutOfHealth)
	{
		OnOutOfHealth.Broadcast(Instigator, Causer, &Data.EffectSpec, Data.EvaluatedData.Magnitude, HealthBeforeAttributeChange, GetHealth());
	}

	// 魔能值变化回调
	if (GetManaEnergy() != ManaEnergyBeforeAttributeChange)
	{
		OnManaEnergyChanged.Broadcast(Instigator, Causer, &Data.EffectSpec, Data.EvaluatedData.Magnitude, ManaEnergyBeforeAttributeChange, GetManaEnergy());
	}

	// 魔能耗尽回调
	if ((GetManaEnergy() <= 0.0f) && !bOutOfManaEnergy)
	{
		OnOutOfManaEnergy.Broadcast(Instigator, Causer, &Data.EffectSpec, Data.EvaluatedData.Magnitude, ManaEnergyBeforeAttributeChange, GetManaEnergy());
	}

	// 体力变化回调
	if (GetStamina() != StaminaBeforeAttributeChange)
	{
		OnStaminaChanged.Broadcast(Instigator, Causer, &Data.EffectSpec, Data.EvaluatedData.Magnitude, StaminaBeforeAttributeChange, GetStamina());
	}

	// 体力耗尽回调
	if ((GetStamina() <= 0.0f) && !bOutOfStamina)
	{
		OnOutOfStamina.Broadcast(Instigator, Causer, &Data.EffectSpec, Data.EvaluatedData.Magnitude, StaminaBeforeAttributeChange, GetStamina());
	}

	// 更新状态标记
	bOutOfHealth = (GetHealth() <= 0.0f);
	bOutOfManaEnergy = (GetManaEnergy() <= 0.0f);
	bOutOfStamina = (GetStamina() <= 0.0f);
}

void UDJ01HealthSet::PreAttributeBaseChange(const FGameplayAttribute& Attribute, float& NewValue) const
{
	Super::PreAttributeBaseChange(Attribute, NewValue);
	ClampAttribute(Attribute, NewValue);
}

void UDJ01HealthSet::PreAttributeChange(const FGameplayAttribute& Attribute, float& NewValue)
{
	Super::PreAttributeChange(Attribute, NewValue);
	ClampAttribute(Attribute, NewValue);
}

void UDJ01HealthSet::PostAttributeChange(const FGameplayAttribute& Attribute, float OldValue, float NewValue)
{
	Super::PostAttributeChange(Attribute, OldValue, NewValue);

	UDJ01AbilitySystemComponent* DJ01ASC = GetDJ01AbilitySystemComponent();
	
	// 最大生命值变化时，确保当前生命值不超过新的最大值
	if (Attribute == GetMaxHealthAttribute())
	{
		if (GetHealth() > NewValue && DJ01ASC)
		{
			DJ01ASC->ApplyModToAttribute(GetHealthAttribute(), EGameplayModOp::Override, NewValue);
		}
	}
	// 最大魔能值变化时
	else if (Attribute == GetMaxManaEnergyAttribute())
	{
		if (GetManaEnergy() > NewValue && DJ01ASC)
		{
			DJ01ASC->ApplyModToAttribute(GetManaEnergyAttribute(), EGameplayModOp::Override, NewValue);
		}
	}
	// 最大体力值变化时
	else if (Attribute == GetMaxStaminaAttribute())
	{
		if (GetStamina() > NewValue && DJ01ASC)
		{
			DJ01ASC->ApplyModToAttribute(GetStaminaAttribute(), EGameplayModOp::Override, NewValue);
		}
	}

	// 重置 OutOf 状态标记
	if (bOutOfHealth && (GetHealth() > 0.0f))
	{
		bOutOfHealth = false;
	}
	if (bOutOfManaEnergy && (GetManaEnergy() > 0.0f))
	{
		bOutOfManaEnergy = false;
	}
	if (bOutOfStamina && (GetStamina() > 0.0f))
	{
		bOutOfStamina = false;
	}
}

void UDJ01HealthSet::ClampAttribute(const FGameplayAttribute& Attribute, float& NewValue) const
{
	// 生命值
	if (Attribute == GetHealthAttribute())
	{
		NewValue = FMath::Clamp(NewValue, 0.0f, GetMaxHealth());
	}
	else if (Attribute == GetMaxHealthAttribute())
	{
		NewValue = FMath::Max(NewValue, 1.0f);
	}
	// 魔能值
	else if (Attribute == GetManaEnergyAttribute())
	{
		NewValue = FMath::Clamp(NewValue, 0.0f, GetMaxManaEnergy());
	}
	else if (Attribute == GetMaxManaEnergyAttribute())
	{
		NewValue = FMath::Max(NewValue, 0.0f);
	}
	// 体力值
	else if (Attribute == GetStaminaAttribute())
	{
		NewValue = FMath::Clamp(NewValue, 0.0f, GetMaxStamina());
	}
	else if (Attribute == GetMaxStaminaAttribute())
	{
		NewValue = FMath::Max(NewValue, 0.0f);
	}
}

