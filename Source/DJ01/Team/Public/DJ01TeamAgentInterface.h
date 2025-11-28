// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "GenericTeamAgentInterface.h"
#include "DJ01TeamTypes.h"
#include "UObject/Object.h"

#include "UObject/WeakObjectPtr.h"
#include "DJ01TeamAgentInterface.generated.h"

template <typename InterfaceType> class TScriptInterface;

DECLARE_DYNAMIC_MULTICAST_DELEGATE_ThreeParams(FOnDJ01TeamIndexChangedDelegate, UObject*, ObjectChangingTeam, int32, OldTeamID, int32, NewTeamID);

DECLARE_DYNAMIC_MULTICAST_DELEGATE_ThreeParams(FDJ01TeamConfigChangedDelegate, UObject*, Agent, FDJ01TeamConfig, OldConfig, FDJ01TeamConfig, NewConfig);

inline int32 GenericTeamIdToInteger(FGenericTeamId ID)
{
	return (ID == FGenericTeamId::NoTeam) ? INDEX_NONE : (int32)ID;
}

inline FGenericTeamId IntegerToGenericTeamId(int32 ID)
{
	return (ID == INDEX_NONE) ? FGenericTeamId::NoTeam : FGenericTeamId((uint8)ID);
}

/** Interface for actors which can be associated with teams */
UINTERFACE(meta=(CannotImplementInterfaceInBlueprint))
class UDJ01TeamAgentInterface : public UGenericTeamAgentInterface
{
	GENERATED_UINTERFACE_BODY()
};

class DJ01_API IDJ01TeamAgentInterface : public IGenericTeamAgentInterface
{
	GENERATED_IINTERFACE_BODY()

public:
	// === RPG 战斗接口 ===

	/** 获取当前团队配置 */
	virtual FDJ01TeamConfig GetTeamConfig() const = 0;

	/** 设置团队配置 */
	virtual void SetTeamConfig(const FDJ01TeamConfig& NewConfig) = 0;

	/** 获取团队变化委托 (RPG) */
	virtual FDJ01TeamConfigChangedDelegate* GetTeamChangedDelegate() { return nullptr; }

	/** 便捷方法：判断是否可以攻击目标 */
	virtual bool CanAttackTeam(EDJ01Team TargetTeam) const
	{
		return GetTeamConfig().CanAttack(TargetTeam);
	}

	/** 便捷方法：判断是否是友军 */
	virtual bool IsFriendlyToTeam(EDJ01Team TargetTeam) const
	{
		return GetTeamConfig().IsFriendly(TargetTeam);
	}

	// === Lyra 广播接口 ===

	virtual FOnDJ01TeamIndexChangedDelegate* GetOnTeamIndexChangedDelegate() { return nullptr; }

	static void ConditionalBroadcastTeamChanged(TScriptInterface<IDJ01TeamAgentInterface> This, FGenericTeamId OldTeamID, FGenericTeamId NewTeamID);
	
	FOnDJ01TeamIndexChangedDelegate& GetTeamChangedDelegateChecked()
	{
		FOnDJ01TeamIndexChangedDelegate* Result = GetOnTeamIndexChangedDelegate();
		check(Result);
		return *Result;
	}

	// === IGenericTeamAgentInterface 实现 ===

	virtual void SetGenericTeamId(const FGenericTeamId& NewTeamID) override;
	virtual FGenericTeamId GetGenericTeamId() const override;
	virtual ETeamAttitude::Type GetTeamAttitudeTowards(const AActor& Other) const override;
};
