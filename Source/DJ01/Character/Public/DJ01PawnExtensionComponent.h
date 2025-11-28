// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Components/GameFrameworkInitStateInterface.h"
#include "Components/PawnComponent.h"
#include "DJ01PawnExtensionComponent.generated.h"

namespace EEndPlayReason { enum Type : int; }

class UGameFrameworkComponentManager;
class UDJ01PawnData;
class UDJ01AbilitySystemComponent;
class UObject;
struct FActorInitStateChangedParams;
struct FFrame;
struct FGameplayTag;

/**
 * UDJ01PawnExtensionComponent
 * 
 * 为所有 Pawn 类添加功能的组件，可用于角色/载具等
 * 协调其他组件的初始化顺序，管理 Pawn 的整个生命周期
 * 
 * 初始化状态链：Spawned -> DataAvailable -> DataInitialized -> GameplayReady
 */
UCLASS()
class DJ01_API UDJ01PawnExtensionComponent : public UPawnComponent, public IGameFrameworkInitStateInterface
{
	GENERATED_BODY()

public:
	UDJ01PawnExtensionComponent(const FObjectInitializer& ObjectInitializer);

	/** 此功能的名称，依赖于其他命名组件功能 */
	static const FName NAME_ActorFeatureName;

	//~ Begin IGameFrameworkInitStateInterface interface
	virtual FName GetFeatureName() const override { return NAME_ActorFeatureName; }
	virtual bool CanChangeInitState(UGameFrameworkComponentManager* Manager, FGameplayTag CurrentState, FGameplayTag DesiredState) const override;
	virtual void HandleChangeInitState(UGameFrameworkComponentManager* Manager, FGameplayTag CurrentState, FGameplayTag DesiredState) override;
	virtual void OnActorInitStateChanged(const FActorInitStateChangedParams& Params) override;
	virtual void CheckDefaultInitialization() override;
	//~ End IGameFrameworkInitStateInterface interface

	/** 如果指定的 Actor 上存在 PawnExtension 组件，则返回它 */
	UFUNCTION(BlueprintPure, Category = "DJ01|Pawn")
	static UDJ01PawnExtensionComponent* FindPawnExtensionComponent(const AActor* Actor) 
	{ 
		return (Actor ? Actor->FindComponentByClass<UDJ01PawnExtensionComponent>() : nullptr); 
	}

	/** 获取 PawnData，用于在数据中指定 Pawn 属性 */
	template <class T>
	const T* GetPawnData() const { return Cast<T>(PawnData); }

	/** 设置当前的 PawnData */
	void SetPawnData(const UDJ01PawnData* InPawnData);

	/** 获取当前的 AbilitySystem 组件，可能由不同的 Actor 拥有 */
	UFUNCTION(BlueprintPure, Category = "DJ01|Pawn")
	UDJ01AbilitySystemComponent* GetDJ01AbilitySystemComponent() const { return AbilitySystemComponent; }

	/** 拥有此组件的 Pawn 应调用此方法以成为 AbilitySystem 的 Avatar */
	void InitializeAbilitySystem(UDJ01AbilitySystemComponent* InASC, AActor* InOwnerActor);

	/** 拥有此组件的 Pawn 应调用此方法以移除自己作为 AbilitySystem 的 Avatar */
	void UninitializeAbilitySystem();

	/** 当 Pawn 的 Controller 改变时，拥有此组件的 Pawn 应调用此方法 */
	void HandleControllerChanged();

	/** 当 PlayerState 已复制时，拥有此组件的 Pawn 应调用此方法 */
	void HandlePlayerStateReplicated();

	/** 当设置输入组件时，拥有此组件的 Pawn 应调用此方法 */
	void SetupPlayerInputComponent();

	/** 注册 OnAbilitySystemInitialized 委托，如果我们的 Pawn 已注册到 AbilitySystem，则立即广播 */
	void OnAbilitySystemInitialized_RegisterAndCall(FSimpleMulticastDelegate::FDelegate Delegate);

	/** 注册 OnAbilitySystemUninitialized 委托，当我们的 Pawn 从 AbilitySystem 的 Avatar Actor 中移除时触发 */
	void OnAbilitySystemUninitialized_Register(FSimpleMulticastDelegate::FDelegate Delegate);

protected:
	virtual void OnRegister() override;
	virtual void BeginPlay() override;
	virtual void EndPlay(const EEndPlayReason::Type EndPlayReason) override;

	UFUNCTION()
	void OnRep_PawnData();

	/** 当我们的 Pawn 成为 AbilitySystem 的 Avatar Actor 时触发的委托 */
	FSimpleMulticastDelegate OnAbilitySystemInitialized;

	/** 当我们的 Pawn 从 AbilitySystem 的 Avatar Actor 中移除时触发的委托 */
	FSimpleMulticastDelegate OnAbilitySystemUninitialized;

	/** 用于创建 Pawn 的 PawnData。从生成函数指定或在已放置的实例上指定 */
	UPROPERTY(EditInstanceOnly, ReplicatedUsing = OnRep_PawnData, Category = "DJ01|Pawn")
	TObjectPtr<const UDJ01PawnData> PawnData;

	/** 为方便起见缓存的 AbilitySystem 组件指针 */
	UPROPERTY(Transient)
	TObjectPtr<UDJ01AbilitySystemComponent> AbilitySystemComponent;
};