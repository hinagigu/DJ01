// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class DJ01Editor : ModuleRules
{
	public DJ01Editor(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
		
		PublicDependencyModuleNames.AddRange(new string[] { 
			"Core", 
			"CoreUObject", 
			"Engine",
			"DJ01"  // 依赖主模块
		});

		PrivateDependencyModuleNames.AddRange(new string[] { 
			"Slate",
			"SlateCore",
			"UnrealEd",        // 编辑器核心
			"UMG",             // Widget 运行时
			"UMGEditor",       // Widget 编辑器（包含 UWidgetBlueprint、UWidgetTree）
			"Blutility",       // Editor Utility
			"BlueprintGraph",  // 蓝图图表
			"Json",
			"JsonUtilities"
		});
	}
}