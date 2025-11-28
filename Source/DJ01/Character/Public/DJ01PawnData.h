// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Engine/DataAsset.h"
#include "DJ01PawnData.generated.h"

class APawn;
class UDJ01InputConfig;
class UDJ01CameraMode;
class UDJ01AbilitySet;

// TODO_ABILITY_SYSTEM: 以下是 AbilitySystem 相关的类，后续需要实现
// class UDJ01AbilityTagRelationshipMapping;

/**
 * UDJ01PawnData
 *
 * 定义 Pawn 属性的不可变数据资产
 * 仿照 Lyra 的 PawnData 系统，用于配置角色的各种属性
 */
UCLASS(BlueprintType, Const, Meta = (DisplayName = "DJ01 Pawn Data", ShortTooltip = "Data asset used to define a Pawn."))
class DJ01_API UDJ01PawnData : public UPrimaryDataAsset
{
	GENERATED_BODY()

public:
	UDJ01PawnData(const FObjectInitializer& ObjectInitializer);

public:
	// 要为此 Pawn 实例化的类（通常应该继承自 ADJ01Character）
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DJ01|Pawn")
	TSubclassOf<APawn> PawnClass;

	// 授予此 Pawn 的能力系统的 Ability Sets
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DJ01|Abilities")
	TArray<TObjectPtr<UDJ01AbilitySet>> AbilitySets;

	// TODO_ABILITY_SYSTEM: 此 Pawn 执行操作时使用的能力标签映射
	// UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DJ01|Abilities")
	// TObjectPtr<UDJ01AbilityTagRelationshipMapping> TagRelationshipMapping;

	// 玩家控制的 Pawn 使用的输入配置，用于创建输入映射和绑定输入操作
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DJ01|Input")
	TObjectPtr<UDJ01InputConfig> InputConfig;

	// 玩家控制的 Pawn 使用的默认相机模式
	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DJ01|Camera")
	TSubclassOf<UDJ01CameraMode> DefaultCameraMode;
};