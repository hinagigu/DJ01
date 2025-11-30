// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "DJ01/Character/Public/DJ01Character.h"

#include "DJ01CharacterWithAbilities.generated.h"

class UAbilitySystemComponent;
class UDJ01AbilitySystemComponent;

/**
* ADJ01CharacterWithAbilities
* 
* ADJ01Character 通常从控制它的 PlayerState 获取 AbilitySystemComponent。
* 这个类代表一个带有自包含 AbilitySystemComponent 的角色。
* 
* 使用场景：
* - AI 控制的角色（没有 PlayerState）
* - 不需要持久化技能状态的角色
* - 单机游戏中的简化角色
* 
* 注意：属性集（HealthSet, CombatSet 等）现在通过 GameFeatureAction_AddAbilities 动态添加，
* 而非在此类中硬编码。请在对应的 GameFeature 配置中添加属性集。
*/
UCLASS(Blueprintable)
class DJ01_API ADJ01CharacterWithAbilities : public ADJ01Character
{
	GENERATED_BODY()

public:
	ADJ01CharacterWithAbilities(const FObjectInitializer& ObjectInitializer);

	virtual void PostInitializeComponents() override;

	//~ Begin IAbilitySystemInterface
	virtual UAbilitySystemComponent* GetAbilitySystemComponent() const override;
	//~ End IAbilitySystemInterface

	/** 获取 DJ01 版本的 AbilitySystemComponent */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Character")
	UDJ01AbilitySystemComponent* GetDJ01AbilitySystemComponent() const { return AbilitySystemComponent; }

	/** 用于 GameFrameworkComponentManager 的能力就绪事件名称 */
	static const FName NAME_DJ01AbilityReady;

private:

	// 此角色使用的 AbilitySystemComponent（自包含，不依赖 PlayerState）
	UPROPERTY(VisibleAnywhere, Category = "DJ01|AbilitySystem")
	TObjectPtr<UDJ01AbilitySystemComponent> AbilitySystemComponent;
};
