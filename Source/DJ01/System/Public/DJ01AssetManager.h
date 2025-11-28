// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Engine/AssetManager.h"
#include "DJ01/Character/Public/DJ01PawnData.h"
#include  "DJ01GameData.h"
#include "DJ01AssetManager.generated.h"
/**
 * DJ01 资产管理器
 * 
 * 游戏的资产管理器，负责：
 * - 管理PrimaryAssets的加载和卸载
 * - 处理Bundle的加载策略
 * - 管理GameFeature的资产
 * 
 * 使用方式：
 * 1. 在DefaultEngine.ini中配置: AssetManagerClassName=/Script/DJ01.DJ01AssetManager
 * 2. 配置PrimaryAssetTypes和PrimaryAssetRules
 */
UCLASS(Config = Game)
class DJ01_API UDJ01AssetManager : public UAssetManager
{
	GENERATED_BODY()

public:
	UDJ01AssetManager();
	
	/** 获取AssetManager的单例 */
	static UDJ01AssetManager& Get();

	/** 
	 * 同步加载PrimaryAsset
	 * @param AssetId 要加载的资产ID
	 * @param bLogWarning 加载失败时是否输出警告
	 * @return 加载的资产对象
	 */
	template<typename AssetType>
	static AssetType* GetAsset(const TSoftObjectPtr<AssetType>& AssetPointer, bool bKeepInMemory = true);
	const UDJ01GameData& GetGameData() const;
	const UDJ01GameData* GetGameDataPtr() const;

	/** 
	 * 同步加载子对象
	 * @param AssetPointer 资产的软引用
	 * @param bKeepInMemory 是否保持在内存中
	 * @return 加载的资产
	 */
	template<typename AssetType>
	static TSubclassOf<AssetType> GetSubclass(const TSoftClassPtr<AssetType>& AssetPointer, bool bKeepInMemory = true);
	const UDJ01PawnData* GetDefaultPawnData() const;

protected:
	//~ Begin UAssetManager interface
	virtual void StartInitialLoading() override;
	//~ End UAssetManager interface

	/** 初始化GameFeature相关设置 */
	void InitializeGameFeatures();

	/** 同步加载资产的内部实现 */
	static UObject* SynchronousLoadAsset(const FSoftObjectPath& AssetPath);

	/** 添加已加载资产到追踪列表 */
	void AddLoadedAsset(const UObject* Asset);

private:
	/** 已加载的资产列表 */
	UPROPERTY()
	TSet<TObjectPtr<const UObject>> LoadedAssets;

	/** 用于修改已加载资产列表时的线程安全锁 */
	FCriticalSection LoadedAssetsCritical;

	UPROPERTY(Config)
	TSoftObjectPtr<UDJ01PawnData> DefaultPawnData;

	// Game data asset to use.
	UPROPERTY(Config)
	TSoftObjectPtr<UDJ01GameData> GameDataPath;

};

template<typename AssetType>
AssetType* UDJ01AssetManager::GetAsset(const TSoftObjectPtr<AssetType>& AssetPointer, bool bKeepInMemory)
{
	AssetType* LoadedAsset = nullptr;

	const FSoftObjectPath& AssetPath = AssetPointer.ToSoftObjectPath();

	if (AssetPath.IsValid())
	{
		LoadedAsset = AssetPointer.Get();
		if (!LoadedAsset)
		{
			LoadedAsset = Cast<AssetType>(SynchronousLoadAsset(AssetPath));
			ensureAlwaysMsgf(LoadedAsset, TEXT("加载资产失败 [%s]"), *AssetPointer.ToString());
		}

		if (LoadedAsset && bKeepInMemory)
		{
			// 添加到已加载资产列表
			Get().AddLoadedAsset(Cast<UObject>(LoadedAsset));
		}
	}

	return LoadedAsset;
}

template<typename AssetType>
TSubclassOf<AssetType> UDJ01AssetManager::GetSubclass(const TSoftClassPtr<AssetType>& AssetPointer, bool bKeepInMemory)
{
	TSubclassOf<AssetType> LoadedSubclass;

	const FSoftObjectPath& AssetPath = AssetPointer.ToSoftObjectPath();

	if (AssetPath.IsValid())
	{
		LoadedSubclass = AssetPointer.Get();
		if (!LoadedSubclass)
		{
			LoadedSubclass = Cast<UClass>(AssetPath.TryLoad());
			ensureAlwaysMsgf(LoadedSubclass, TEXT("加载类失败 [%s]"), *AssetPointer.ToString());
		}

		if (LoadedSubclass && bKeepInMemory)
		{
			// 添加到已加载资产列表，防止被卸载
			Get().GetStreamableManager().RequestAsyncLoad(AssetPath, FStreamableDelegate(), FStreamableManager::AsyncLoadHighPriority);
		}
	}

	return LoadedSubclass;
}