// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class DJ01 : ModuleRules
{
	public DJ01(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
	
		PublicDependencyModuleNames.AddRange(new string[] { 
			"Core", 
			"CoreOnline",  // 在线功能核心（FUniqueNetIdWrapper等）
			"CoreUObject", 
			"Engine", 
			"InputCore", 
			"EnhancedInput",
			"GameplayAbilities", 
			"GameplayTags", 
			"GameplayTasks",
			"GameFeatures",
			"ModularGameplay",
			"GameplayMessageRuntime",  // 游戏消息路由系统
			"UMG",  // UI相关
			"CommonUI", // CommonUI插件
			"CommonInput",
			"CommonUser",  // CommonUser插件（用于会话管理）
			"NetCore",  // 网络复制支持
			"IrisCore",  // Iris网络序列化系统（用于GameplayEffectContext等）
			"PhysicsCore",  // 物理核心（UPhysicalMaterial等）
			"LoadingScreen",  // 加载屏幕插件
			"AIModule", // AI系统（GenericTeamAgentInterface等）
			"AudioMixer" // 音频混合器（SwapAudioOutputDevice等）
		});

		PrivateDependencyModuleNames.AddRange(new string[] { 
			"Slate",
			"SlateCore",
			"GameFeatureActions",
			"ModularGameplayActors",
			"CommonGame",
			"UIExtension",
			"EngineSettings",  // 用于 UGameMapsSettings
			"AngelscriptCode"  // AngelScript 集成 - 用于检测 AS 类覆盖的 K2 函数
		});

		// Uncomment if you are using online features
		// PrivateDependencyModuleNames.Add("OnlineSubsystem");

		// To include OnlineSubsystemSteam, add it to the plugins section in your uproject file with the Enabled attribute set to true
	}
}
