#pragma once

#include "NativeGameplayTags.h"

namespace DJ01GameplayTags
{
	// 初始化状态
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InitState_Spawned);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InitState_DataAvailable);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InitState_DataInitialized);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InitState_GameplayReady);

	// 输入
	// Input Tags
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InputTag_Move);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InputTag_Look_Mouse);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InputTag_Jump);

	// AttributeSet Tags - 用于通过 Tag 查找属性集
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(AttributeSet_Health);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(AttributeSet_Combat);

	// Ability System Tags
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_ActivateFail_ActivationGroup);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_ActivateFail_IsDead);

	// Status Tags
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Death);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_AutoRunning);

	// Cheat Tags (仅非 Shipping 构建)
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Cheat_GodMode);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Cheat_UnlimitedHealth);
}