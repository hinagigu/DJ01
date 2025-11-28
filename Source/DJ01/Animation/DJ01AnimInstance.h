// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Animation/AnimInstance.h"
#include "GameplayEffectTypes.h"
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
	 * 应使用此映射而非手动查询GameplayTag
	 */
	UPROPERTY(EditDefaultsOnly, Category = "GameplayTags")
	FGameplayTagBlueprintPropertyMap GameplayTagPropertyMap;

	/** 角色到地面的距离，用于跳跃/降落动画控制 */
	UPROPERTY(BlueprintReadOnly, Category = "Character State Data")
	float GroundDistance = -1.0f;
};
