// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Animation/AnimInstance.h"
#include "DJ01GameplayTagPropertyMap.h"

// 包含自动生成的动画变量和映射初始化宏（必须在 .generated.h 之前）
#include "Generated/DJ01AnimInstanceVars.h"

#include "DJ01AnimInstance.generated.h"

class UAbilitySystemComponent;


/**
* UDJ01AnimInstance
*
* DJ01项目的基础动画实例类
* 
* 功能特性：
* - 与GAS（Gameplay Ability System）集成
* - 支持GameplayTag到蓝图变量的自动映射
* - 提供地面距离信息用于动画状态控制
*/
UCLASS(Config = Game)
class DJ01_API UDJ01AnimInstance : public UAnimInstance
{
	GENERATED_BODY()

public:

	UDJ01AnimInstance(const FObjectInitializer& ObjectInitializer);

	/** 
	 * 使用AbilitySystemComponent初始化动画实例
	 * 会设置GameplayTag属性映射，使得蓝图变量能自动响应Tag变化
	 */
	virtual void InitializeWithAbilitySystem(UAbilitySystemComponent* ASC);

protected:

#if WITH_EDITOR
	virtual EDataValidationResult IsDataValid(class FDataValidationContext& Context) const override;
#endif // WITH_EDITOR

	virtual void NativeInitializeAnimation() override;
	virtual void NativeUpdateAnimation(float DeltaSeconds) override;

protected:

	/** 
	 * GameplayTag到蓝图变量的映射配置
	 * 当对应的Tag添加或移除时，映射的变量会自动更新
	 * 映射在构造函数中自动配置，由 Tag Manager 生成
	 */
	UPROPERTY(EditDefaultsOnly, Category = "GameplayTags")
	FDJ01GameplayTagPropertyMap GameplayTagPropertyMap;

	//========================================
	// 物理状态数据 (从 CharacterMovement 读取)
	// 这些是物理模拟的结果，不由 GAS 控制
	//========================================
	
	/** 
	 * 实际地面移动速度 (XY平面)
	 * 用于 BlendSpace 混合: Idle(0) -> Walk(150) -> Run(600)
	 */
	UPROPERTY(BlueprintReadOnly, Category = "Character State Data|Physics")
	float GroundSpeed = 0.0f;
	
	/** 角色到地面的距离，用于跳跃/降落动画控制 */
	UPROPERTY(BlueprintReadOnly, Category = "Character State Data|Physics")
	float GroundDistance = -1.0f;

	//========================================
	// 逻辑状态数据 (由 GameplayTagPropertyMap 自动映射)
	// 在动画蓝图的 Class Defaults 中配置 Tag 映射
	//========================================
	
	// 自动生成的动画状态变量 - 由 Tag Manager 生成
	// 在 Tag Manager 中配置 AnimVar 列来添加/修改这些变量
	DJ01_ANIM_INSTANCE_GENERATED_VARS
};
