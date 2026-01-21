// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "DJ01AnimationTypes.generated.h"

/**
 * 动画层类型枚举
 * 决定状态机使用哪个动画层接口
 */
UENUM(BlueprintType)
enum class EAnimLayerType : uint8
{
	/** 近战类型 - 使用 ALI_MeleeAnimLayers (空手/刀/剑盾/双剑) */
	Melee		UMETA(DisplayName = "Melee"),
	
	/** 远程类型 - 使用 ALI_RangedAnimLayers (手枪/步枪/弓箭) */
	Ranged		UMETA(DisplayName = "Ranged"),
	
	/** 空中类型 - 使用 ALI_AerialAnimLayers (飞行/滑翔) */
	Aerial		UMETA(DisplayName = "Aerial"),
	
	/** 怪物类型A - 使用 ALI_MonsterAnimLayers_A (四足/爬行) */
	MonsterA	UMETA(DisplayName = "Monster A"),
	
	/** 怪物类型B - 使用 ALI_MonsterAnimLayers_B (巨型/Boss) */
	MonsterB	UMETA(DisplayName = "Monster B"),
	
	/** 载具类型 - 使用 ALI_VehicleAnimLayers (骑乘) */
	Vehicle		UMETA(DisplayName = "Vehicle"),
};