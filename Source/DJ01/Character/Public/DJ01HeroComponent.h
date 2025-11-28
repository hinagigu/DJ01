// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "Components/GameFrameworkInitStateInterface.h"
#include "Components/PawnComponent.h"
// #include "GameFeatures/GameFeatureAction_AddInputContextMapping.h"
#include "GameFeatureActions/GameFeatureAction_AddInputContextMapping.h"
#include "GameplayAbilitySpecHandle.h"
#include "DJ01HeroComponent.generated.h"

namespace EEndPlayReason { enum Type : int; }

class UGameFrameworkComponentManager;
class UInputComponent;
class UDJ01CameraMode;
class UDJ01InputConfig;
class UObject;
struct FActorInitStateChangedParams;
struct FFrame;
struct FGameplayTag;
struct FInputActionValue;

/**
* UDJ01HeroComponent
* 
* 设置玩家控制的 Pawn（或模拟玩家的 Bot）的输入和相机处理的组件
* 此组件依赖于 PawnExtensionComponent 来协调初始化
* 
* 对齐 Lyra 的 HeroComponent，提供：
* - 输入绑定管理
* - 相机模式控制
* - 与 GameFeature 系统的集成
* - 能力系统的输入处理
*/
UCLASS(Blueprintable, Meta=(BlueprintSpawnableComponent))
class DJ01_API UDJ01HeroComponent : public UPawnComponent, public IGameFrameworkInitStateInterface
{
	GENERATED_BODY()

public:

	UDJ01HeroComponent(const FObjectInitializer& ObjectInitializer);

	/** 如果指定的 Actor 上存在 HeroComponent，则返回它 */
	UFUNCTION(BlueprintPure, Category = "DJ01|Hero")
	static UDJ01HeroComponent* FindHeroComponent(const AActor* Actor) { return (Actor ? Actor->FindComponentByClass<UDJ01HeroComponent>() : nullptr); }

	/** 从活动的 Gameplay Ability 覆盖相机模式 */
	void SetAbilityCameraMode(TSubclassOf<UDJ01CameraMode> CameraMode, const FGameplayAbilitySpecHandle& OwningSpecHandle);

	/** 如果已设置，则清除相机覆盖 */
	void ClearAbilityCameraMode(const FGameplayAbilitySpecHandle& OwningSpecHandle);

	/** 添加模式特定的输入配置 */
	void AddAdditionalInputConfig(const UDJ01InputConfig* InputConfig);

	/** 移除已添加的模式特定输入配置 */
	void RemoveAdditionalInputConfig(const UDJ01InputConfig* InputConfig);

	/** 如果由真实玩家控制且初始化已进行到可以添加额外输入绑定的阶段，则返回 true */
	bool IsReadyToBindInputs() const;
	
	/** 通过 UGameFrameworkComponentManager 发送的扩展事件的名称，当能力输入准备好绑定时 */
	static const FName NAME_BindInputsNow;

	/** 此组件实现的功能的名称 */
	static const FName NAME_ActorFeatureName;

	//~ Begin IGameFrameworkInitStateInterface interface
	virtual FName GetFeatureName() const override { return NAME_ActorFeatureName; }
	virtual bool CanChangeInitState(UGameFrameworkComponentManager* Manager, FGameplayTag CurrentState, FGameplayTag DesiredState) const override;
	bool CanChangeInitStateWithLog(UGameFrameworkComponentManager* Manager, FGameplayTag CurrentState, FGameplayTag DesiredState) const;

	virtual void HandleChangeInitState(UGameFrameworkComponentManager* Manager, FGameplayTag CurrentState, FGameplayTag DesiredState) override;
	virtual void OnActorInitStateChanged(const FActorInitStateChangedParams& Params) override;
	virtual void CheckDefaultInitialization() override;
	//~ End IGameFrameworkInitStateInterface interface

protected:

	virtual void OnRegister() override;
	virtual void BeginPlay() override;
	virtual void EndPlay(const EEndPlayReason::Type EndPlayReason) override;

	virtual void InitializePlayerInput(UInputComponent* PlayerInputComponent);

	/** 能力输入标签处理函数 - 当输入动作触发时调用 */
	void Input_AbilityInputTagPressed(FGameplayTag InputTag);
	void Input_AbilityInputTagReleased(FGameplayTag InputTag);

	void Input_Move(const FInputActionValue& InputActionValue);
	void Input_LookMouse(const FInputActionValue& InputActionValue);
	void Input_LookStick(const FInputActionValue& InputActionValue);
	void Input_Crouch(const FInputActionValue& InputActionValue);
	void Input_AutoRun(const FInputActionValue& InputActionValue);

	TSubclassOf<UDJ01CameraMode> DetermineCameraMode() const;
	
	// 以下函数已弃用，使用 FInputMappingContextAndPriority 系统时不再需要
	// void OnInputConfigActivated(const FLoadedMappableConfigPair& ConfigPair);
	// void OnInputConfigDeactivated(const FLoadedMappableConfigPair& ConfigPair);

protected:

	/**
	 * 初始化此玩家时应添加的输入映射。这些配置
	 * 不会在设置中注册，因为它们是在运行时添加的。如果希望配置
	 * 出现在设置中，则通过 GameFeatureAction_AddInputConfig 添加
	 * 
	 * 注意：只有在无法访问游戏功能插件时才应添加到此处。
	 * 如果可以，请使用 GameFeatureAction_AddInputConfig 代替。
	 */
	UPROPERTY(EditAnywhere)
	TArray<FInputMappingContextAndPriority> DefaultInputMappings;
	
	/** 能力设置的相机模式 */
	UPROPERTY()
	TSubclassOf<UDJ01CameraMode> AbilityCameraMode;

	/** 最后一个设置相机模式的能力的规格句柄 */
	FGameplayAbilitySpecHandle AbilityCameraModeOwningSpecHandle;

	/** 当玩家输入绑定已应用时为 true，对于非玩家永远不会为 true */
	bool bReadyToBindInputs;
};