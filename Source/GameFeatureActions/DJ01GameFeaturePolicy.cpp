// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01GameFeaturePolicy.h"
#include "GameFeaturesSubsystem.h"
#include "GameFeatureData.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01GameFeaturePolicy)

UDJ01GameFeaturePolicy::UDJ01GameFeaturePolicy(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
}

UDJ01GameFeaturePolicy& UDJ01GameFeaturePolicy::Get()
{
	return UGameFeaturesSubsystem::Get().GetPolicy<UDJ01GameFeaturePolicy>();
}

void UDJ01GameFeaturePolicy::InitGameFeatureManager()
{
	// 在这里可以添加自定义的观察者
	// 例如监听 GameFeature 的各种状态变化
	// Observers.Add(NewObject<UYourCustomObserver>());

	UGameFeaturesSubsystem& Subsystem = UGameFeaturesSubsystem::Get();
	for (UObject* Observer : Observers)
	{
		Subsystem.AddObserver(Observer);
	}

	Super::InitGameFeatureManager();
	
	UE_LOG(LogTemp, Log, TEXT("DJ01GameFeaturePolicy: GameFeature Manager initialized"));
}

void UDJ01GameFeaturePolicy::ShutdownGameFeatureManager()
{
	Super::ShutdownGameFeatureManager();

	UGameFeaturesSubsystem& Subsystem = UGameFeaturesSubsystem::Get();
	for (UObject* Observer : Observers)
	{
		Subsystem.RemoveObserver(Observer);
	}
	Observers.Empty();
	
	UE_LOG(LogTemp, Log, TEXT("DJ01GameFeaturePolicy: GameFeature Manager shutdown"));
}

TArray<FPrimaryAssetId> UDJ01GameFeaturePolicy::GetPreloadAssetListForGameFeature(const UGameFeatureData* GameFeatureToLoad, bool bIncludeLoadedAssets) const
{
	// 可以在这里自定义需要预加载的资源
	return Super::GetPreloadAssetListForGameFeature(GameFeatureToLoad, bIncludeLoadedAssets);
}

const TArray<FName> UDJ01GameFeaturePolicy::GetPreloadBundleStateForGameFeature() const
{
	// 可以在这里自定义预加载的 Bundle 状态
	// 例如: return TArray<FName>{FName("Client"), FName("Server")};
	return Super::GetPreloadBundleStateForGameFeature();
}

void UDJ01GameFeaturePolicy::GetGameFeatureLoadingMode(bool& bLoadClientData, bool& bLoadServerData) const
{
	// 决定是否加载客户端和服务器数据
	// 在编辑器中会同时加载两者，这可能会导致卡顿
	bLoadClientData = !IsRunningDedicatedServer();
	bLoadServerData = !IsRunningClientOnly();
}

bool UDJ01GameFeaturePolicy::IsPluginAllowed(const FString& PluginURL) const
{
	// 在这里可以实现插件的黑白名单逻辑
	// 例如：禁止某些插件加载，或者只允许特定插件加载
	
	// 默认允许所有插件
	return Super::IsPluginAllowed(PluginURL);
}