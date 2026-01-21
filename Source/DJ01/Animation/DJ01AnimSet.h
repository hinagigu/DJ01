// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Animation/AnimSequence.h"
#include "Animation/BlendSpace.h"
#include "DJ01AnimSet.generated.h"

/**
 * ============================================================================
 * DJ01 动画集系统 (Anim Set)
 * 
 * 参考 Lyra 设计，将动画资产配置化，方便在 Details 面板中更换动画
 * 无需修改蓝图逻辑即可切换不同的动画资产
 * ============================================================================
 */

// ============================================================================
// 基础移动动画集
// ============================================================================

/**
 * 四方向动画集 (用于 Walk/Jog 等)
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AnimSet_Cardinals
{
	GENERATED_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Cardinals")
	TObjectPtr<UAnimSequence> Forward = nullptr;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Cardinals")
	TObjectPtr<UAnimSequence> Backward = nullptr;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Cardinals")
	TObjectPtr<UAnimSequence> Left = nullptr;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Cardinals")
	TObjectPtr<UAnimSequence> Right = nullptr;
};

/**
 * 待机动画集
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AnimSet_Idle
{
	GENERATED_BODY()

	/** 主待机动画 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Idle")
	TObjectPtr<UAnimSequence> Idle = nullptr;

	/** 待机打断动画数组（站久了随机播放） */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Idle")
	TArray<TObjectPtr<UAnimSequence>> IdleBreaks;

	/** 战斗待机（拔出武器后） */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Idle")
	TObjectPtr<UAnimSequence> IdleCombat = nullptr;
};

/**
 * 移动动画集
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AnimSet_Locomotion
{
	GENERATED_BODY()

	/** 移动 BlendSpace (推荐使用，一个 BS 搞定所有) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "BlendSpace")
	TObjectPtr<UBlendSpace> LocomotionBS = nullptr;

	/** 行走动画 (四方向) - 如果不用 BlendSpace */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Walk")
	FDJ01AnimSet_Cardinals Walk;

	/** 跑步/慢跑动画 (四方向) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Jog")
	FDJ01AnimSet_Cardinals Jog;

	/** 冲刺动画 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Sprint")
	TObjectPtr<UAnimSequence> Sprint = nullptr;
};

/**
 * 蹲伏动画集
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AnimSet_Crouch
{
	GENERATED_BODY()

	/** 蹲伏待机 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Crouch")
	TObjectPtr<UAnimSequence> CrouchIdle = nullptr;

	/** 蹲伏移动 BlendSpace */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Crouch")
	TObjectPtr<UBlendSpace> CrouchLocomotionBS = nullptr;

	/** 蹲伏行走 (四方向) - 如果不用 BlendSpace */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Crouch")
	FDJ01AnimSet_Cardinals CrouchWalk;
};

// ============================================================================
// 跳跃动画集
// ============================================================================

/**
 * 跳跃动画集
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AnimSet_Jump
{
	GENERATED_BODY()

	/** 起跳 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Jump")
	TObjectPtr<UAnimSequence> JumpStart = nullptr;

	/** 上升阶段 (可选) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Jump")
	TObjectPtr<UAnimSequence> JumpApex = nullptr;

	/** 下落循环 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Jump")
	TObjectPtr<UAnimSequence> FallLoop = nullptr;

	/** 轻落地 (低高度) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Jump")
	TObjectPtr<UAnimSequence> LandLight = nullptr;

	/** 重落地 (高高度) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Jump")
	TObjectPtr<UAnimSequence> LandHeavy = nullptr;

	/** 落地恢复/翻滚 (超高高度) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Jump")
	TObjectPtr<UAnimSequence> LandRoll = nullptr;
};

// ============================================================================
// 近战战斗动画集
// ============================================================================

/**
 * 近战战斗动画集
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AnimSet_MeleeCombat
{
	GENERATED_BODY()

	// -------- 格挡 --------
	
	/** 格挡待机 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Block")
	TObjectPtr<UAnimSequence> BlockIdle = nullptr;

	/** 格挡受击 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Block")
	TObjectPtr<UAnimSequence> BlockHit = nullptr;

	/** 完美格挡 (Parry) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Block")
	TObjectPtr<UAnimSequence> Parry = nullptr;

	// -------- 闪避 --------

	/** 前闪避 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Dodge")
	TObjectPtr<UAnimSequence> DodgeForward = nullptr;

	/** 后闪避 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Dodge")
	TObjectPtr<UAnimSequence> DodgeBackward = nullptr;

	/** 左闪避 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Dodge")
	TObjectPtr<UAnimSequence> DodgeLeft = nullptr;

	/** 右闪避 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Dodge")
	TObjectPtr<UAnimSequence> DodgeRight = nullptr;

	// -------- 受击 --------

	/** 受击反应 (前方) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "HitReact")
	TObjectPtr<UAnimSequence> HitReactFront = nullptr;

	/** 受击反应 (后方) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "HitReact")
	TObjectPtr<UAnimSequence> HitReactBack = nullptr;

	/** 受击反应 (左侧) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "HitReact")
	TObjectPtr<UAnimSequence> HitReactLeft = nullptr;

	/** 受击反应 (右侧) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "HitReact")
	TObjectPtr<UAnimSequence> HitReactRight = nullptr;

	// -------- 倒地/起身 --------

	/** 被击倒 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Knockdown")
	TObjectPtr<UAnimSequence> Knockdown = nullptr;

	/** 倒地循环 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Knockdown")
	TObjectPtr<UAnimSequence> KnockdownLoop = nullptr;

	/** 起身 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Knockdown")
	TObjectPtr<UAnimSequence> GetUp = nullptr;
};

/**
 * 武器切换动画集
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AnimSet_WeaponSwitch
{
	GENERATED_BODY()

	/** 拔出武器 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Weapon")
	TObjectPtr<UAnimSequence> DrawWeapon = nullptr;

	/** 收起武器 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Weapon")
	TObjectPtr<UAnimSequence> SheathWeapon = nullptr;
};

// ============================================================================
// 射击战斗动画集
// ============================================================================

/**
 * 射击/瞄准动画集
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AnimSet_RangedCombat
{
	GENERATED_BODY()

	// -------- 瞄准 --------

	/** 瞄准待机 (ADS) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aiming")
	TObjectPtr<UAnimSequence> AimIdle = nullptr;

	/** 瞄准移动 BlendSpace */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aiming")
	TObjectPtr<UBlendSpace> AimLocomotionBS = nullptr;

	/** 髋射待机 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Hipfire")
	TObjectPtr<UAnimSequence> HipfireIdle = nullptr;

	// -------- 换弹 --------

	/** 换弹动画 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Reload")
	TObjectPtr<UAnimSequence> Reload = nullptr;

	/** 快速换弹 (战术换弹) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Reload")
	TObjectPtr<UAnimSequence> ReloadTactical = nullptr;

	/** 空仓换弹 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Reload")
	TObjectPtr<UAnimSequence> ReloadEmpty = nullptr;
};

// ============================================================================
// 高级动画集 (可选)
// ============================================================================

/**
 * 起步/停步动画集 (可选，用于更流畅的移动过渡)
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AnimSet_StartStop
{
	GENERATED_BODY()

	/** 起步动画 (四方向) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Start")
	FDJ01AnimSet_Cardinals Starts;

	/** 停步动画 (四方向) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Stop")
	FDJ01AnimSet_Cardinals Stops;
};

/**
 * 转向动画集 (可选，用于急转弯)
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AnimSet_Pivot
{
	GENERATED_BODY()

	/** 左转 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Pivot")
	TObjectPtr<UAnimSequence> PivotLeft = nullptr;

	/** 右转 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Pivot")
	TObjectPtr<UAnimSequence> PivotRight = nullptr;

	/** 180度转身 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Pivot")
	TObjectPtr<UAnimSequence> TurnInPlace180 = nullptr;
};

// ============================================================================
// 完整动画层配置 (整合所有 AnimSet)
// ============================================================================

/**
 * 近战动画层完整配置
 * 用于 ABP_AnimLayer_Katana 等近战武器动画层
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AnimLayerConfig_Melee
{
	GENERATED_BODY()

	/** 待机动画集 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Anim Sets")
	FDJ01AnimSet_Idle IdleSet;

	/** 移动动画集 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Anim Sets")
	FDJ01AnimSet_Locomotion LocomotionSet;

	/** 蹲伏动画集 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Anim Sets")
	FDJ01AnimSet_Crouch CrouchSet;

	/** 跳跃动画集 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Anim Sets")
	FDJ01AnimSet_Jump JumpSet;

	/** 近战战斗动画集 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Anim Sets")
	FDJ01AnimSet_MeleeCombat CombatSet;

	/** 武器切换动画集 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Anim Sets")
	FDJ01AnimSet_WeaponSwitch WeaponSwitchSet;

	/** 起步/停步动画集 (可选) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Anim Sets|Advanced", meta = (DisplayName = "Start/Stop (Optional)"))
	FDJ01AnimSet_StartStop StartStopSet;

	/** 转向动画集 (可选) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Anim Sets|Advanced", meta = (DisplayName = "Pivot (Optional)"))
	FDJ01AnimSet_Pivot PivotSet;
};

/**
 * 射击动画层完整配置
 * 用于 ABP_AnimLayer_Pistol 等射击武器动画层
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AnimLayerConfig_Ranged
{
	GENERATED_BODY()

	/** 待机动画集 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Anim Sets")
	FDJ01AnimSet_Idle IdleSet;

	/** 移动动画集 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Anim Sets")
	FDJ01AnimSet_Locomotion LocomotionSet;

	/** 蹲伏动画集 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Anim Sets")
	FDJ01AnimSet_Crouch CrouchSet;

	/** 跳跃动画集 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Anim Sets")
	FDJ01AnimSet_Jump JumpSet;

	/** 射击战斗动画集 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Anim Sets")
	FDJ01AnimSet_RangedCombat CombatSet;

	/** 武器切换动画集 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Anim Sets")
	FDJ01AnimSet_WeaponSwitch WeaponSwitchSet;
};