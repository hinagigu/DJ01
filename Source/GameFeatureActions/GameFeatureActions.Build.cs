using UnrealBuildTool;

public class GameFeatureActions : ModuleRules
{
    public GameFeatureActions(ReadOnlyTargetRules Target) : base(Target)
    {
        PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

        // 头文件中直接使用到的类型所需的依赖
        PublicDependencyModuleNames.AddRange(new string[] {
            "Core", "CoreUObject", "Engine",
            "GameFeatures", "EnhancedInput","CommonInput",
        });

        // 仅在 cpp 中使用到的类型所需的依赖（可按需精简/增补）
        PrivateDependencyModuleNames.AddRange(new string[] {
            "InputCore",
            "GameplayAbilities", "GameplayTags", "GameplayTasks",
            "ModularGameplay", "ModularGameplayActors",
            "CommonUI", "CommonGame", "UIExtension", "GameplayMessageRuntime",
            "DJ01",  // 添加对 DJ01 模块的依赖
            "UMG",   // 用于 UUserWidget
            "Slate", "SlateCore"  // UI 相关
        });
    }
}