// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class testRuntime : ModuleRules
{
	public testRuntime(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = ModuleRules.PCHUsageMode.UseExplicitOrSharedPCHs;
		
		PublicIncludePaths.AddRange(
			new string[] {
			}
		);
				
		PrivateIncludePaths.AddRange(
			new string[] {
			}
		);
			
		PublicDependencyModuleNames.AddRange(
			new string[]
			{
				"Core",
				"CoreUObject",
				"Engine",
				"InputCore",
				"ModularGameplayActors"
			}
		);
			
		PrivateDependencyModuleNames.AddRange(
			new string[]
			{
				"Slate",
				"SlateCore",
				"GameplayAbilities",
				"GameplayTags",
				"GameplayTasks",
				"EnhancedInput",
				"CommonGame",
				"CommonUser",
				"UIExtension",
				"GameplayMessageRuntime",
				"GameFeatures"
			}
		);
		
		DynamicallyLoadedModuleNames.AddRange(
			new string[]
			{
			}
		);
	}
}
