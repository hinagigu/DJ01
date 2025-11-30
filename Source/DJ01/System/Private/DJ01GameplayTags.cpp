#include "DJ01/System/Public/DJ01GameplayTags.h"

#include "GameplayTagsManager.h"

namespace DJ01GameplayTags
{
    // 初始化状态
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(InitState_Spawned, "InitState.Spawned", "1: Actor/component has initially spawned and can be extended");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(InitState_DataAvailable, "InitState.DataAvailable", "2: All required data has been loaded/replicated and is ready for initialization");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(InitState_DataInitialized, "InitState.DataInitialized", "3: The available data has been initialized for this actor/component, but it is not ready for full gameplay");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(InitState_GameplayReady, "InitState.GameplayReady", "4: The actor/component is fully ready for active gameplay");

    // 输入
    // Input Tags
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(InputTag_Move, "InputTag.Move", "Move input.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(InputTag_Look_Mouse, "InputTag.Look.Mouse", "Look input with mouse.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(InputTag_Jump, "InputTag.Jump", "Jump input.");

    // AttributeSet Tags
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(AttributeSet_Health, "AttributeSet.Health", "Health attribute set identifier.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(AttributeSet_Combat, "AttributeSet.Combat", "Combat attribute set identifier.");

    // Ability System Tags
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Ability_ActivateFail_ActivationGroup, "Ability.ActivateFail.ActivationGroup", "Ability failed to activate due to activation group constraints.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Ability_ActivateFail_IsDead, "Ability.ActivateFail.IsDead", "Ability failed to activate because the owner is dead.");

    // Status Tags
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_Death, "Status.Death", "Target is dead.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_AutoRunning, "Status.AutoRunning", "Character is auto-running.");

    // Cheat Tags (仅非 Shipping 构建使用)
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Cheat_GodMode, "Cheat.GodMode", "God mode - makes the player invincible.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Cheat_UnlimitedHealth, "Cheat.UnlimitedHealth", "Unlimited health - health cannot drop below 1.");
}