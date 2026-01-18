// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "DJ01/AbilitySystem/Attributes/BindingSets/Generated/BindingSets.h"
#include "CoreMinimal.h"
#include "Animation/AnimInstance.h"
#include "DJ01AnimationTypes.h"
#include "DJ01GameplayTagPropertyMap.h"

// AnimTagSet 系统：按需包含对应的 TagSet 头文件
// 例如: #include "Animation/AnimTagSets/AnimTagSet_CommonStatus.h"

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

	// BindingSet: AnimState
	DJ01_DECLARE_BINDING_SET(AnimState)








public:

	UDJ01AnimInstance(const FObjectInitializer& ObjectInitializer);

	/** 
	 * 使用AbilitySystemComponent初始化动画实例
	 * 会设置GameplayTag属性映射，使得蓝图变量能自动响应Tag变化
	 */
	virtual void InitializeWithAbilitySystem(UAbilitySystemComponent* ASC);

	/** 尝试初始化 GAS 绑定，如果 ASC 还没准备好则跳过 */
	void TryInitializeGASBindings();

protected:

#if WITH_EDITOR
	virtual EDataValidationResult IsDataValid(class FDataValidationContext& Context) const override;
#endif // WITH_EDITOR

	virtual void NativeInitializeAnimation() override;
	virtual void NativeUpdateAnimation(float DeltaSeconds) override;

private:
	/** 标记 GAS 绑定是否已初始化 */
	bool bGASBindingsInitialized = false;

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
	
	/** 
	 * 移动方向 (相对于角色朝向，-180 到 180)
	 * 用于 2D BlendSpace 的方向轴
	 * 0=前进, ±90=左右, ±180=后退
	 */
	UPROPERTY(BlueprintReadOnly, Category = "Character State Data|Physics")
	float MoveDirection = 0.0f;
	
	/** 角色到地面的距离，用于跳跃/降落动画控制 */
	UPROPERTY(BlueprintReadOnly, Category = "Character State Data|Physics")
	float GroundDistance = -1.0f;

	/** 是否在空中 (物理状态，来自 CharacterMovement::IsFalling) */
	UPROPERTY(BlueprintReadOnly, Category = "Character State Data|Physics")
	bool bIsFalling = false;

	/** 在空中的持续时间 (秒)，用于判断轻/重落地 */
	UPROPERTY(BlueprintReadOnly, Category = "Character State Data|Physics")
	float TimeInAir = 0.0f;

	//========================================
	// 动画层类型 (决定使用哪个动画层接口)
	//========================================
	
	/** 
	 * 当前动画层类型
	 * 决定状态机调用哪个接口的函数
	 */
	UPROPERTY(BlueprintReadWrite, Category = "Character State Data|AnimLayer")
	EAnimLayerType AnimLayerType = EAnimLayerType::Melee;

	//========================================
	// 逻辑状态数据 (由 AnimTagSet 系统管理)
	// 使用 AnimTagSet 编辑器创建 TagSet，然后在此处使用宏引入
	//========================================
	
	// AnimTagSet 使用示例:
	// DJ01_ANIM_TAG_SET_COMMONSTATUS_VARS()  // 变量声明
	// 
	// 并在 InitializeWithAbilitySystem 中调用:
	// DJ01_ANIM_TAG_SET_COMMONSTATUS_REGISTER(ASC)  // 注册回调
};
