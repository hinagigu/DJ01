// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01/Character/Public/DJ01CharacterMovementComponent.h"
#include "Components/CapsuleComponent.h"
#include "GameFramework/Character.h"
#include "Engine/World.h"

// TODO_ABILITY_SYSTEM: GAS 集成后取消注释
// #include "AbilitySystemComponent.h"
// #include "AbilitySystemGlobals.h"
// #include "GameplayTagContainer.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01CharacterMovementComponent)

// 控制台变量：用于调试地面检测距离
namespace DJ01Character
{
	static float GroundTraceDistance = 500.0f;
	FAutoConsoleVariableRef CVar_GroundTraceDistance(
		TEXT("DJ01.Character.GroundTraceDistance"), 
		GroundTraceDistance, 
		TEXT("Distance to trace down when generating ground information (cm)."), 
		ECVF_Cheat
	);
}

UDJ01CharacterMovementComponent::UDJ01CharacterMovementComponent(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
	// ============================================================
	// RPG 角色移动配置
	// ============================================================
	
	// 加速度配置 - RPG 角色通常移动较慢，不需要很高的加速度
	MaxAcceleration = 1800.0f;              // Lyra 使用 2400.0f，适合快节奏射击游戏
	BrakingDecelerationWalking = 1200.0f;   // 行走制动减速度
	BrakingFriction = 6.0f;                 // 制动摩擦力
	GroundFriction = 8.0f;                  // 地面摩擦力
	
	// 旋转配置 - RPG 通常使用"面向移动方向"
	bOrientRotationToMovement = true;       // 角色朝移动方向旋转
	bUseControllerDesiredRotation = false;  // 不使用控制器朝向
	RotationRate = FRotator(0.0f, 540.0f, 0.0f); // 旋转速度（度/秒）
	
	// 跳跃和空中控制
	JumpZVelocity = 600.0f;                 // 跳跃初速度
	AirControl = 0.2f;                      // 空中控制能力（0-1）
	
	// 其他配置
	bAllowPhysicsRotationDuringAnimRootMotion = false; // 动画根骨骼运动时禁止物理旋转
	
	// 蹲伏配置（如果 RPG 需要蹲伏功能）
	GetNavAgentPropertiesRef().bCanCrouch = false; // 默认禁用蹲伏，需要时可改为 true
	bCanWalkOffLedgesWhenCrouching = false;
}

void UDJ01CharacterMovementComponent::InitializeComponent()
{
	Super::InitializeComponent();
	
	// 初始化地面信息缓存
	CachedGroundInfo = FDJ01CharacterGroundInfo();
}

const FDJ01CharacterGroundInfo& UDJ01CharacterMovementComponent::GetGroundInfo()
{
	// 如果这一帧已经更新过，直接返回缓存结果
	if (!CharacterOwner || (GFrameCounter == CachedGroundInfo.LastUpdateFrame))
	{
		return CachedGroundInfo;
	}

	// 情况 1：角色在地面上行走
	if (MovementMode == MOVE_Walking)
	{
		// 直接使用引擎提供的地板信息
		CachedGroundInfo.GroundHitResult = CurrentFloor.HitResult;
		CachedGroundInfo.GroundDistance = 0.0f;
	}
	// 情况 2：角色在空中（跳跃、掉落等）
	else
	{
		const UCapsuleComponent* CapsuleComp = CharacterOwner->GetCapsuleComponent();
		check(CapsuleComp);

		// 计算射线检测的起点和终点
		const float CapsuleHalfHeight = CapsuleComp->GetUnscaledCapsuleHalfHeight();
		const ECollisionChannel CollisionChannel = (UpdatedComponent ? UpdatedComponent->GetCollisionObjectType() : ECC_Pawn);
		const FVector TraceStart = GetActorLocation();
		const FVector TraceEnd = FVector(
			TraceStart.X, 
			TraceStart.Y, 
			TraceStart.Z - DJ01Character::GroundTraceDistance - CapsuleHalfHeight
		);

		// 配置碰撞查询参数
		FCollisionQueryParams QueryParams(SCENE_QUERY_STAT(DJ01CharacterMovementComponent_GetGroundInfo), false, CharacterOwner);
		FCollisionResponseParams ResponseParam;
		InitCollisionParams(QueryParams, ResponseParam);

		// 执行射线检测
		FHitResult HitResult;
		GetWorld()->LineTraceSingleByChannel(HitResult, TraceStart, TraceEnd, CollisionChannel, QueryParams, ResponseParam);

		CachedGroundInfo.GroundHitResult = HitResult;
		CachedGroundInfo.GroundDistance = DJ01Character::GroundTraceDistance;

		// 如果使用导航寻路（AI 角色）
		if (MovementMode == MOVE_NavWalking)
		{
			CachedGroundInfo.GroundDistance = 0.0f;
		}
		// 如果射线命中了地面
		else if (HitResult.bBlockingHit)
		{
			CachedGroundInfo.GroundDistance = FMath::Max((HitResult.Distance - CapsuleHalfHeight), 0.0f);
		}
	}

	// 更新缓存的帧数
	CachedGroundInfo.LastUpdateFrame = GFrameCounter;

	return CachedGroundInfo;
}

// ============================================================
// TODO_ABILITY_SYSTEM: GAS 集成接口
// ============================================================
// 当实现 GAS 后，取消下面代码的注释

/*
float UDJ01CharacterMovementComponent::GetMaxSpeed() const
{
	// 获取角色的 AbilitySystemComponent
	if (UAbilitySystemComponent* ASC = UAbilitySystemGlobals::GetAbilitySystemComponentFromActor(GetOwner()))
	{
		// 检查"移动停止"标签（定身、眩晕、石化等效果）
		if (ASC->HasMatchingGameplayTag(FGameplayTag::RequestGameplayTag(TEXT("Status.MovementStopped"))))
		{
			return 0.0f; // 完全无法移动
		}

		// 检查"移动减速"标签（减速效果）
		if (ASC->HasMatchingGameplayTag(FGameplayTag::RequestGameplayTag(TEXT("Status.MovementSlowed"))))
		{
			// 可以通过 GameplayEffect 的 Magnitude 来动态计算减速比例
			// 这里简单返回 50% 速度作为示例
			return Super::GetMaxSpeed() * 0.5f;
		}

		// 检查"移动加速"标签（加速 Buff、疾跑等）
		if (ASC->HasMatchingGameplayTag(FGameplayTag::RequestGameplayTag(TEXT("Status.MovementHasted"))))
		{
			// 可以通过 GameplayEffect 的 Magnitude 来动态计算加速比例
			// 这里简单返回 150% 速度作为示例
			return Super::GetMaxSpeed() * 1.5f;
		}
	}

	// 没有任何移动相关的标签，返回默认速度
	return Super::GetMaxSpeed();
}

FRotator UDJ01CharacterMovementComponent::GetDeltaRotation(float DeltaTime) const
{
	// 获取角色的 AbilitySystemComponent
	if (UAbilitySystemComponent* ASC = UAbilitySystemGlobals::GetAbilitySystemComponentFromActor(GetOwner()))
	{
		// 检查"旋转锁定"标签（释放技能时、被控制时等）
		if (ASC->HasMatchingGameplayTag(FGameplayTag::RequestGameplayTag(TEXT("Status.RotationLocked"))))
		{
			return FRotator::ZeroRotator; // 不允许旋转
		}

		// 检查"强制朝向"标签（某些技能需要强制面向目标）
		// 这种情况下可能需要从 GameplayEffect 中获取目标朝向
		// 这里仅作为接口预留
	}

	// 没有任何旋转相关的标签，返回默认旋转
	return Super::GetDeltaRotation(DeltaTime);
}
*/