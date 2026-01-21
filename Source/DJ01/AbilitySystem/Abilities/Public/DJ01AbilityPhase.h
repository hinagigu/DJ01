// ============================================================
// DJ01AbilityPhase.h
// 技能阶段状态机定义
// ============================================================

#pragma once

#include "CoreMinimal.h"
#include "GameplayTagContainer.h"

#include "DJ01AbilityPhase.generated.h"

/**
* EDJ01PhaseTimingMode
* 阶段计时模式 - 控制阶段如何切换到下一阶段
*/
UENUM(BlueprintType)
enum class EDJ01PhaseTimingMode : uint8
{
	/** 按 Duration 自动切换 (Duration=0 时立即切换) */
	Automatic		UMETA(DisplayName = "Automatic / 自动"),

	/** 按 Montage 长度切换 (未配置 Montage 时回退到 Automatic) */
	UseMontageLength	UMETA(DisplayName = "Use Montage Length / 动画长度"),

	/** 完全手动控制 (需要脚本调用 TransitionToPhase 或 SkipCurrentPhase) */
	Manual			UMETA(DisplayName = "Manual / 手动")
};

/**
 * EDJ01AbilityPhase
 * 技能阶段状态机 - 定义技能执行的各个阶段
 */
UENUM(BlueprintType)
enum class EDJ01AbilityPhase : uint8
{
	// 未激活/空闲
	None = 0				UMETA(DisplayName = "None"),

	// 前摇阶段 - 技能激活后的准备动作（可被打断）
	Startup					UMETA(DisplayName = "Startup / 前摇"),

	// 激活阶段 - 技能效果生效的主要阶段
	Active					UMETA(DisplayName = "Active / 激活"),

	// 后摇阶段 - 技能效果结束后的硬直
	Recovery				UMETA(DisplayName = "Recovery / 后摇"),

	// 冷却阶段 - 技能进入冷却
	Cooldown				UMETA(DisplayName = "Cooldown / 冷却"),

	// 结束
	Ended					UMETA(DisplayName = "Ended / 结束"),

	MAX						UMETA(Hidden)
};

class UAnimMontage;

/**
* FDJ01AbilityPhaseInfo
* 阶段配置信息
*/
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AbilityPhaseInfo
{
	GENERATED_BODY()

	// ========== 计时配置 ==========

	/** 阶段计时模式 */
	UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Phase|Timing")
	EDJ01PhaseTimingMode TimingMode = EDJ01PhaseTimingMode::Automatic;

	/** 阶段持续时间 (仅 Automatic 模式生效，0 表示瞬时切换) */
	UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Phase|Timing", 
		meta = (EditCondition = "TimingMode == EDJ01PhaseTimingMode::Automatic", EditConditionHides))
	float Duration = 0.0f;

	// ========== 控制配置 ==========

	/** 该阶段是否可被打断 */
	UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Phase|Control")
	bool bCanBeInterrupted = true;

	/** 该阶段是否可取消到其他技能 */
	UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Phase|Control")
	bool bCanCancelInto = false;

	/** 进入此阶段时添加的 Tag */
	UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Phase|Tags")
	FGameplayTagContainer PhaseTags;

	// ========== 动画配置 ==========

	/** 该阶段播放的 Montage (可选) */
	UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Phase|Animation")
	TObjectPtr<UAnimMontage> Montage = nullptr;

	/** Montage 播放速率 */
	UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Phase|Animation", 
		meta = (ClampMin = "0.1", ClampMax = "5.0", EditCondition = "Montage != nullptr", EditConditionHides))
	float MontagePlayRate = 1.0f;

	/** Montage 起始 Section 名称 (留空则从头播放) */
	UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Phase|Animation",
		meta = (EditCondition = "Montage != nullptr", EditConditionHides))
	FName MontageStartSection = NAME_None;

	// ========== 辅助方法 ==========

	/** 是否有有效的 Montage */
	bool HasMontage() const { return Montage != nullptr; }

	/** 获取实际持续时间 (根据 TimingMode 计算) */
	float GetEffectiveDuration() const;

	/** 是否需要设置定时器自动切换 */
	bool ShouldAutoTransition() const { return TimingMode != EDJ01PhaseTimingMode::Manual; }
};

/**
 * FDJ01AbilityPhaseConfig
 * 技能的完整阶段配置
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AbilityPhaseConfig
{
	GENERATED_BODY()

	/** 前摇配置 */
	UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Phases")
	FDJ01AbilityPhaseInfo Startup;

	/** 激活阶段配置 */
	UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Phases")
	FDJ01AbilityPhaseInfo Active;

	/** 后摇配置 */
	UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Phases")
	FDJ01AbilityPhaseInfo Recovery;

	/** 获取指定阶段的配置 */
	const FDJ01AbilityPhaseInfo* GetPhaseInfo(EDJ01AbilityPhase Phase) const
	{
		switch (Phase)
		{
		case EDJ01AbilityPhase::Startup:	return &Startup;
		case EDJ01AbilityPhase::Active:		return &Active;
		case EDJ01AbilityPhase::Recovery:	return &Recovery;
		default: return nullptr;
		}
	}
};

// 阶段转换验证辅助函数
inline bool IsValidPhaseTransition(EDJ01AbilityPhase From, EDJ01AbilityPhase To)
{
	// 定义有效的状态转换
	switch (From)
	{
	case EDJ01AbilityPhase::None:
		return To == EDJ01AbilityPhase::Startup || To == EDJ01AbilityPhase::Active;

	case EDJ01AbilityPhase::Startup:
		return To == EDJ01AbilityPhase::Active || To == EDJ01AbilityPhase::Ended;

	case EDJ01AbilityPhase::Active:
		return To == EDJ01AbilityPhase::Recovery || To == EDJ01AbilityPhase::Ended;

	case EDJ01AbilityPhase::Recovery:
		return To == EDJ01AbilityPhase::Cooldown || To == EDJ01AbilityPhase::Ended;

	case EDJ01AbilityPhase::Cooldown:
		return To == EDJ01AbilityPhase::Ended || To == EDJ01AbilityPhase::None;

	case EDJ01AbilityPhase::Ended:
		return To == EDJ01AbilityPhase::None;

	default:
		return false;
	}
}

// 获取阶段名称（用于调试）
inline FString GetAbilityPhaseName(EDJ01AbilityPhase Phase)
{
	switch (Phase)
	{
	case EDJ01AbilityPhase::None:		return TEXT("None");
	case EDJ01AbilityPhase::Startup:	return TEXT("Startup");
	case EDJ01AbilityPhase::Active:		return TEXT("Active");
	case EDJ01AbilityPhase::Recovery:	return TEXT("Recovery");
	case EDJ01AbilityPhase::Cooldown:	return TEXT("Cooldown");
	case EDJ01AbilityPhase::Ended:		return TEXT("Ended");
	default:							return TEXT("Unknown");
	}
}

// 获取实际持续时间 (根据 TimingMode 计算)
inline float FDJ01AbilityPhaseInfo::GetEffectiveDuration() const
{
	switch (TimingMode)
	{
	case EDJ01PhaseTimingMode::UseMontageLength:
		if (Montage)
		{
			const float MontageLength = Montage->GetPlayLength();
			const float Rate = FMath::Max(MontagePlayRate, 0.1f);
			return MontageLength / Rate;
		}
		// 回退到 Duration
		return Duration;

	case EDJ01PhaseTimingMode::Automatic:
		return Duration;

	case EDJ01PhaseTimingMode::Manual:
	default:
		// Manual 模式不需要时长
		return -1.0f;
	}
}