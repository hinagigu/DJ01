// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/System/Public/DJ01GameData.h"
#include "DJ01/System/Public/DJ01AssetManager.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01GameData)

UDJ01GameData::UDJ01GameData()
{
}

const UDJ01GameData& UDJ01GameData::Get()
{
	return UDJ01AssetManager::Get().GetGameData();
}
