		// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "GenericTeamAgentInterface.h"
#include "DJ01TeamTypes.generated.h"

/**
 * EDJ01Team - 基于位标志的团队系统
 * 
 * 设计理念：
 * 1. 每个Team是一个独立的bit
 * 2. 通过位掩码定义"攻击目标"关系
 * 3. 一行代码判断敌对：(MyAttackMask & TargetTeam) != 0
 * 
 * 优势：
 * - 极简：只需要位运算，不需要复杂的子系统
 * - 高效：位运算性能极高
 * - 灵活：支持"一对多"关系（一个单位可以同时属于多个阵营）
 * - 可扩展：最多支持32个阵营（uint32）
 */
UENUM(BlueprintType, Meta = (Bitflags, UseEnumValuesAsMaskValuesInEditor = "true", ScriptName = "EDJ01Team"))
enum class EDJ01Team : uint8
{
	// === 基础阵营（每个是一个bit）===
	
	None        = 0,          // 0b00000000 - 无阵营
	
	Player      = 1 << 0,     // 0b00000001 - 玩家
	Monster     = 1 << 1,     // 0b00000010 - 怪物
	NPC         = 1 << 2,     // 0b00000100 - NPC
	Boss        = 1 << 3,     // 0b00001000 - Boss
	Neutral     = 1 << 4,     // 0b00010000 - 中立生物
	
	// === PvP阵营（可选）===
	TeamRed     = 1 << 5,     // 0b00100000 - 红队
	TeamBlue    = 1 << 6,     // 0b01000000 - 蓝队
	TeamGreen   = 1 << 7,     // 0b10000000 - 绿队
};
ENUM_CLASS_FLAGS(EDJ01Team);

/**
 * FDJ01TeamConfig - 团队配置
 * 
 * 只需两个字段就能定义完整的团队行为！
 */
USTRUCT(BlueprintType)
struct FDJ01TeamConfig
{
	GENERATED_BODY()

	/** 我的阵营标识 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Team")
	EDJ01Team MyTeam = EDJ01Team::None;

	/** 
	 * 我可以攻击的目标阵营（位掩码）
	 * 
	 * 例如：
	 * - 玩家：Monster | Boss (可以攻击怪物和Boss)
	 * - 怪物：Player | NPC (可以攻击玩家和NPC)
	 * - NPC：Monster (只攻击怪物，不攻击玩家)
	 * - 中立生物：None (不攻击任何人)
	 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Team", Meta = (Bitmask, BitmaskEnum = "/Script/DJ01.EDJ01Team"))
	uint8 AttackMask = 0;

	/** 快捷方法：判断是否可以攻击目标 */
	bool CanAttack(EDJ01Team TargetTeam) const
	{
		return (AttackMask & static_cast<uint8>(TargetTeam)) != 0;
	}

	/** 快捷方法：判断是否是友军 */
	bool IsFriendly(EDJ01Team TargetTeam) const
	{
		// 同阵营 或 不能攻击对方
		return MyTeam == TargetTeam || !CanAttack(TargetTeam);
	}

	/** 预设配置 */
	static FDJ01TeamConfig MakePlayer()
	{
		FDJ01TeamConfig Config;
		Config.MyTeam = EDJ01Team::Player;
		Config.AttackMask = static_cast<uint8>(EDJ01Team::Monster) | static_cast<uint8>(EDJ01Team::Boss);
		return Config;
	}

	static FDJ01TeamConfig MakeMonster()
	{
		FDJ01TeamConfig Config;
		Config.MyTeam = EDJ01Team::Monster;
		Config.AttackMask = static_cast<uint8>(EDJ01Team::Player) | static_cast<uint8>(EDJ01Team::NPC);
		return Config;
	}

	static FDJ01TeamConfig MakeFriendlyNPC()
	{
		FDJ01TeamConfig Config;
		Config.MyTeam = EDJ01Team::NPC;
		Config.AttackMask = static_cast<uint8>(EDJ01Team::Monster) | static_cast<uint8>(EDJ01Team::Boss);
		return Config;
	}

	static FDJ01TeamConfig MakeNeutral()
	{
		FDJ01TeamConfig Config;
		Config.MyTeam = EDJ01Team::Neutral;
		Config.AttackMask = 0; // 不攻击任何人
		return Config;
	}
};

/**
 * DJ01TeamStatics - 静态工具函数
 */
namespace DJ01Team
{
	/** 判断A是否可以攻击B */
	inline bool CanAttack(const FDJ01TeamConfig& AttackerConfig, EDJ01Team TargetTeam)
	{
		return AttackerConfig.CanAttack(TargetTeam);
	}

	/** 判断A和B是否是敌对关系（双向） */
	inline bool AreEnemies(const FDJ01TeamConfig& ConfigA, const FDJ01TeamConfig& ConfigB)
	{
		return ConfigA.CanAttack(ConfigB.MyTeam) || ConfigB.CanAttack(ConfigA.MyTeam);
	}

	/** 判断A和B是否是友军（双向） */
	inline bool AreFriends(const FDJ01TeamConfig& ConfigA, const FDJ01TeamConfig& ConfigB)
	{
		// 同阵营 或 双方都不攻击对方
		return (ConfigA.MyTeam == ConfigB.MyTeam) || 
		       (!ConfigA.CanAttack(ConfigB.MyTeam) && !ConfigB.CanAttack(ConfigA.MyTeam));
	}

	/** EDJ01Team -> FGenericTeamId（用于UE AI系统） */
	inline FGenericTeamId ToGenericTeamId(EDJ01Team Team)
	{
		return FGenericTeamId(static_cast<uint8>(Team));
	}

	/** FGenericTeamId -> EDJ01Team */
	inline EDJ01Team FromGenericTeamId(FGenericTeamId TeamId)
	{
		return static_cast<EDJ01Team>(TeamId.GetId());
	}

	/** 
	 * 计算ETeamAttitude（用于UE AI系统）
	 * 基于位掩码自动计算态度
	 */
	inline ETeamAttitude::Type GetAttitude(const FDJ01TeamConfig& ObserverConfig, EDJ01Team TargetTeam)
	{
		// 同阵营 -> 友好
		if (ObserverConfig.MyTeam == TargetTeam)
		{
			return ETeamAttitude::Friendly;
		}
		
		// 可以攻击 -> 敌对
		if (ObserverConfig.CanAttack(TargetTeam))
		{
			return ETeamAttitude::Hostile;
		}
		
		// 否则 -> 中立
		return ETeamAttitude::Neutral;
	}
}