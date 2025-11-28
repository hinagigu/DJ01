// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "GameFeaturesProjectPolicies.h"
#include "GameFeatureStateChangeObserver.h"

#include "DJ01GameFeaturePolicy.generated.h"

class UGameFeatureData;
struct FPrimaryAssetId;

/**
 * DJ01 游戏功能策略类
 * 
 * 负责管理 GameFeature 插件的生命周期，包括：
 * - 控制插件的加载、激活、停用流程
 * - 决定哪些插件可以被加载
 * - 管理插件的预加载资源
 * - 配置客户端/服务器的加载模式
 */
UCLASS(MinimalAPI, Config = Game)
class UDJ01GameFeaturePolicy : public UDefaultGameFeaturesProjectPolicies
{
	GENERATED_BODY()

public:
	/** 获取全局策略实例 */
	static UDJ01GameFeaturePolicy& Get();

	UDJ01GameFeaturePolicy(const FObjectInitializer& ObjectInitializer);

	//~UGameFeaturesProjectPolicies interface
	
	/** 初始化 GameFeature 管理器，注册观察者 */
	virtual void InitGameFeatureManager() override;
	
	/** 关闭 GameFeature 管理器，清理观察者 */
	virtual void ShutdownGameFeatureManager() override;
	
	/** 获取指定 GameFeature 需要预加载的资源列表 */
	virtual TArray<FPrimaryAssetId> GetPreloadAssetListForGameFeature(const UGameFeatureData* GameFeatureToLoad, bool bIncludeLoadedAssets = false) const override;
	
	/** 判断指定插件是否允许加载 */
	virtual bool IsPluginAllowed(const FString& PluginURL) const override;
	
	/** 获取 GameFeature 预加载的 Bundle 状态 */
	virtual const TArray<FName> GetPreloadBundleStateForGameFeature() const override;
	
	/** 获取 GameFeature 的加载模式（客户端/服务器） */
	virtual void GetGameFeatureLoadingMode(bool& bLoadClientData, bool& bLoadServerData) const override;
	
	//~End of UGameFeaturesProjectPolicies interface

private:
	/** 注册的状态观察者列表 */
	UPROPERTY(Transient)
	TArray<TObjectPtr<UObject>> Observers;
};