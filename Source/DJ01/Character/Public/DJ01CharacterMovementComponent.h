// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/CharacterMovementComponent.h"
#include "DJ01CharacterMovementComponent.generated.h"

class UObject;
struct FFrame;

/**
 * FDJ01CharacterGroundInfo
 *
 * 地面信息结构体
 * 用于播放不同地面材质的脚步声、粒子特效等
 */
USTRUCT(BlueprintType)
struct FDJ01CharacterGroundInfo
{
	GENERATED_BODY()

	FDJ01CharacterGroundInfo()
		: LastUpdateFrame(0)
		, GroundDistance(0.0f)
	{}

	// 上次更新的帧数
	uint64 LastUpdateFrame;

	// 地面检测的命中结果
	UPROPERTY(BlueprintReadOnly)
	FHitResult GroundHitResult;

	// 到地面的距离
	UPROPERTY(BlueprintReadOnly)
	float GroundDistance;
};

/**
 * UDJ01CharacterMovementComponent
 * 
 * 为 RPG 项目优化的角色移动组件
 * 
 * 功能特性：
 * - 基础移动（走/跑/跳跃）
 * - 地面信息检测（用于播放地面特效和音效）
 * - 预留 GAS 集成接口（用于技能系统控制移动）
 * 
 * 设计理念：
 * - 简化的实现，适合 RPG 游戏的移动需求
 * - 相比 Lyra 移除了复杂的网络优化（RPG 通常移动较慢）
 * - 保留可扩展性，便于后续添加冲刺、翻滚等功能
 */
UCLASS()
class DJ01_API UDJ01CharacterMovementComponent : public UCharacterMovementComponent
{
	GENERATED_BODY()

public:
	UDJ01CharacterMovementComponent(const FObjectInitializer& ObjectInitializer);

	/**
	 * 获取当前地面信息
	 * 会自动缓存结果，同一帧内多次调用不会重复检测
	 * 
	 * 使用场景：
	 * - 脚步声系统：根据地面材质播放不同声音
	 * - 粒子特效：根据地面类型生成灰尘、水花等
	 * - 游戏逻辑：检测角色是否在特殊地面上（岩浆、冰面等）
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|CharacterMovement")
	const FDJ01CharacterGroundInfo& GetGroundInfo();

	//~ Begin UMovementComponent Interface
	/** 根据 GameplayTags 计算最终移动速度 */
	virtual float GetMaxSpeed() const override;
	
	/** 根据 GameplayTags 控制旋转 */
	virtual FRotator GetDeltaRotation(float DeltaTime) const override;
	//~ End UMovementComponent Interface

protected:
	virtual void InitializeComponent() override;

private:
	// 缓存的地面信息，通过 GetGroundInfo() 访问
	FDJ01CharacterGroundInfo CachedGroundInfo;

	// 地面检测的最大距离（单位：厘米）
	static constexpr float GroundTraceDistance = 500.0f;
};