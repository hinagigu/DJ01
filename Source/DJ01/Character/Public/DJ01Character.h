// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "ModularCharacter.h"
#include "AbilitySystemInterface.h"
#include "GameplayTagAssetInterface.h"
#include "DJ01Character.generated.h"

class UDJ01PawnExtensionComponent;
class UDJ01CameraComponent;
class UAbilitySystemComponent;
struct FGameplayTag;
struct FGameplayTagContainer;

/**
* ADJ01Character
* 
* 项目的基础角色类，使用模块化游戏框架
* 负责向 Pawn 组件发送事件
* 新行为应尽可能通过 Pawn 组件添加
* 
* 注意：HeroComponent 不在这里创建，而是通过 Game Feature Data (GFD) 的 Action 动态添加
*/

/**
* ADJ01Character
* 
* 项目的基础角色类，使用模块化游戏框架
* - 实现 IAbilitySystemInterface 以支持技能系统
* - 实现 IGameplayTagAssetInterface 以支持 GameplayTag 查询
* - 负责向 Pawn 组件发送事件
* - 新行为应尽可能通过 Pawn 组件添加
* 
* 注意：HeroComponent 不在这里创建，而是通过 Game Feature Data (GFD) 的 Action 动态添加
*/
UCLASS(Config = Game, Meta = (ShortTooltip = "The base character pawn class used by this project."))
class DJ01_API ADJ01Character : public AModularCharacter, public IAbilitySystemInterface, public IGameplayTagAssetInterface
{
	GENERATED_BODY()

public:
	ADJ01Character(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

	//~ Begin IAbilitySystemInterface
	virtual UAbilitySystemComponent* GetAbilitySystemComponent() const override;
	//~ End IAbilitySystemInterface

	//~ Begin IGameplayTagAssetInterface
	virtual void GetOwnedGameplayTags(FGameplayTagContainer& TagContainer) const override;
	virtual bool HasMatchingGameplayTag(FGameplayTag TagToCheck) const override;
	virtual bool HasAllMatchingGameplayTags(const FGameplayTagContainer& TagContainer) const override;
	virtual bool HasAnyMatchingGameplayTags(const FGameplayTagContainer& TagContainer) const override;
	//~ End IGameplayTagAssetInterface

	//~ Begin AActor Interface
	virtual void PreInitializeComponents() override;
	virtual void BeginPlay() override;
	virtual void EndPlay(const EEndPlayReason::Type EndPlayReason) override;
	virtual void Reset() override;
	//~ End AActor Interface

	//~ Begin APawn Interface
	virtual void PossessedBy(AController* NewController) override;
	virtual void UnPossessed() override;
	virtual void OnRep_Controller() override;
	virtual void OnRep_PlayerState() override;
	virtual void SetupPlayerInputComponent(UInputComponent* PlayerInputComponent) override;
	//~ End APawn Interface

protected:
	/** 当 AbilitySystem 初始化完成时调用 */
	virtual void OnAbilitySystemInitialized();
	
	/** 当 AbilitySystem 取消初始化时调用 */
	virtual void OnAbilitySystemUninitialized();

private:
	// PawnExtension 组件 - 管理 Pawn 的生命周期和初始化状态
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "DJ01|Character", Meta = (AllowPrivateAccess = "true"))
	TObjectPtr<UDJ01PawnExtensionComponent> PawnExtComponent;

	// Camera 组件 - 处理相机逻辑
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "DJ01|Character", Meta = (AllowPrivateAccess = "true"))
	TObjectPtr<UDJ01CameraComponent> CameraComponent;
};