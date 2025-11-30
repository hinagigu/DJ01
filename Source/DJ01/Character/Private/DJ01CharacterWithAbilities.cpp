// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01/Character/Public/DJ01CharacterWithAbilities.h"

#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"

#include "Components/GameFrameworkComponentManager.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01CharacterWithAbilities)

const FName ADJ01CharacterWithAbilities::NAME_DJ01AbilityReady("DJ01AbilitiesReady");

ADJ01CharacterWithAbilities::ADJ01CharacterWithAbilities(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
	// 创建自包含的 AbilitySystemComponent
	AbilitySystemComponent = ObjectInitializer.CreateDefaultSubobject<UDJ01AbilitySystemComponent>(this, TEXT("AbilitySystemComponent"));
	AbilitySystemComponent->SetIsReplicated(true);
	AbilitySystemComponent->SetReplicationMode(EGameplayEffectReplicationMode::Mixed);

	// 属性集（HealthSet, CombatSet）现在通过 GameFeatureAction_AddAbilities 动态添加
	// 不再在此处硬编码创建

	// AbilitySystemComponent 需要高频率更新以保证网络同步
	NetUpdateFrequency = 100.0f;
}

void ADJ01CharacterWithAbilities::PostInitializeComponents()
{
	Super::PostInitializeComponents();

	check(AbilitySystemComponent);
	// 设置 AbilityActorInfo：Owner 和 Avatar 都是自己
	// 与 PlayerState 持有 ASC 的情况不同，这里 ASC 就在角色自身
	AbilitySystemComponent->InitAbilityActorInfo(this, this);

	// 发送能力就绪事件，通知 GameFeature 系统可以添加 Abilities 和 AttributeSets
	UGameFrameworkComponentManager::SendGameFrameworkComponentExtensionEvent(this, NAME_DJ01AbilityReady);
}

UAbilitySystemComponent* ADJ01CharacterWithAbilities::GetAbilitySystemComponent() const
{
	return AbilitySystemComponent;
}


