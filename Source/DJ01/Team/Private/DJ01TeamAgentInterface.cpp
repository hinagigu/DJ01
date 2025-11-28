// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Team/Public/DJ01TeamAgentInterface.h"

#include "DJ01/System/Public/DJ01LogChannels.h"
#include "UObject/ScriptInterface.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01TeamAgentInterface)

UDJ01TeamAgentInterface::UDJ01TeamAgentInterface(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
}

void IDJ01TeamAgentInterface::ConditionalBroadcastTeamChanged(TScriptInterface<IDJ01TeamAgentInterface> This, FGenericTeamId OldTeamID, FGenericTeamId NewTeamID)
{
	if (OldTeamID != NewTeamID)
	{
		const int32 OldTeamIndex = GenericTeamIdToInteger(OldTeamID); 
		const int32 NewTeamIndex = GenericTeamIdToInteger(NewTeamID);

		UObject* ThisObj = This.GetObject();
		UE_LOG(LogDJ01Teams, Verbose, TEXT("[%s] %s assigned team %d"), *GetClientServerContextString(ThisObj), *GetPathNameSafe(ThisObj), NewTeamIndex);

		This.GetInterface()->GetTeamChangedDelegateChecked().Broadcast(ThisObj, OldTeamIndex, NewTeamIndex);
	}
}

void IDJ01TeamAgentInterface::SetGenericTeamId(const FGenericTeamId& NewTeamID)
{
	// 将 GenericTeamId 转换为我们的 Config 并设置
	// 注意：这里只能设置 MyTeam，AttackMask 需要保持不变或由具体实现处理
	FDJ01TeamConfig NewConfig = GetTeamConfig();
	NewConfig.MyTeam = DJ01Team::FromGenericTeamId(NewTeamID);
	SetTeamConfig(NewConfig);
}

FGenericTeamId IDJ01TeamAgentInterface::GetGenericTeamId() const
{
	return DJ01Team::ToGenericTeamId(GetTeamConfig().MyTeam);
}

ETeamAttitude::Type IDJ01TeamAgentInterface::GetTeamAttitudeTowards(const AActor& Other) const
{
	if (const IDJ01TeamAgentInterface* OtherTeamAgent = Cast<const IDJ01TeamAgentInterface>(&Other))
	{
		return DJ01Team::GetAttitude(GetTeamConfig(), OtherTeamAgent->GetTeamConfig().MyTeam);
	}
	// 尝试回退到标准的 GenericTeamAgent
	else if (const IGenericTeamAgentInterface* OtherGenericAgent = Cast<const IGenericTeamAgentInterface>(&Other))
	{
		return DJ01Team::GetAttitude(GetTeamConfig(), DJ01Team::FromGenericTeamId(OtherGenericAgent->GetGenericTeamId()));
	}

	return ETeamAttitude::Neutral;
}

