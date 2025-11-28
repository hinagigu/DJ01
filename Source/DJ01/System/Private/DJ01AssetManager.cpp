#include "DJ01/System/Public/DJ01AssetManager.h"

#include "DJ01/Character/Public/DJ01PawnData.h"


UObject* UDJ01AssetManager::SynchronousLoadAsset(const FSoftObjectPath& AssetPath)
{
	if (AssetPath.IsValid())
	{
		TUniquePtr<FScopeLogTime> LogTimePtr;
		
		// 如果需要，可以在这里添加资产加载日志
		
		return AssetPath.TryLoad();
	}
	return nullptr;
}

void UDJ01AssetManager::AddLoadedAsset(const UObject* Asset)
{
	if (Asset)
	{
		FScopeLock LoadedAssetsLock(&LoadedAssetsCritical);
		LoadedAssets.Add(Asset);
	}
}// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/System/Public/DJ01AssetManager.h"
#include "Misc/App.h"
#include "Stats/StatsMisc.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01AssetManager)

UDJ01AssetManager::UDJ01AssetManager()
{
}

UDJ01AssetManager& UDJ01AssetManager::Get()
{
	check(GEngine);

	if (UDJ01AssetManager* Singleton = Cast<UDJ01AssetManager>(GEngine->AssetManager))
	{
		return *Singleton;
	}

	UE_LOG(LogTemp, Fatal, TEXT("无效的AssetManagerClassName配置，必须设置为DJ01AssetManager!"));

	// 永远不会到这里
	return *NewObject<UDJ01AssetManager>();
}

void UDJ01AssetManager::StartInitialLoading()
{
	SCOPED_BOOT_TIMING("UDJ01AssetManager::StartInitialLoading");

	Super::StartInitialLoading();

	// 初始化GameFeature相关
	InitializeGameFeatures();
	
	UE_LOG(LogTemp, Log, TEXT("[UDJ01AssetManager::StartInitialLoading] 资产管理器初始化完成"));

	// 临时检查
	TArray<FPrimaryAssetId> IdList;
	GetPrimaryAssetIdList(FPrimaryAssetType("DJ01ExperienceDefinition"), IdList);
	UE_LOG(LogTemp, Warning, TEXT("[DEBUG] StartInitialLoading found %d Experiences:"), IdList.Num());

}

void UDJ01AssetManager::InitializeGameFeatures()
{
	// 这里可以添加GameFeature相关的初始化逻辑
	// 例如预加载某些GameFeature资产等

	UE_LOG(LogTemp, Log, TEXT("[UDJ01AssetManager::InitializeGameFeatures] GameFeature初始化完成"));
}

const UDJ01PawnData* UDJ01AssetManager::GetDefaultPawnData() const
{
	return GetAsset(DefaultPawnData);
}

const UDJ01GameData& UDJ01AssetManager::GetGameData() const
{
	const UDJ01GameData* GameData = GetAsset(GameDataPath);
	check(GameData);
	return *GameData;
}

const UDJ01GameData* UDJ01AssetManager::GetGameDataPtr() const
{
	return GetAsset(GameDataPath);
}

