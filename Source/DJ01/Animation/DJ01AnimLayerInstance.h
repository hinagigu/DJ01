// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Animation/AnimInstance.h"
#include "DJ01AnimSet.h"
#include "DJ01AnimLayerInstance.generated.h"

/**
 * 近战动画层基类
 * ABP_AnimLayer_Katana 等蓝图继承此类
 */
UCLASS()
class DJ01_API UDJ01MeleeAnimLayerInstance : public UAnimInstance
{
	GENERATED_BODY()

public:

	/** 近战动画配置 - 在蓝图 Details 面板中配置 */
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Animation Config")
	FDJ01AnimLayerConfig_Melee AnimConfig;
};

/**
 * 射击动画层基类
 * ABP_AnimLayer_Pistol 等蓝图继承此类
 */
UCLASS()
class DJ01_API UDJ01RangedAnimLayerInstance : public UAnimInstance
{
	GENERATED_BODY()

public:

	/** 射击动画配置 - 在蓝图 Details 面板中配置 */
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Animation Config")
	FDJ01AnimLayerConfig_Ranged AnimConfig;
};