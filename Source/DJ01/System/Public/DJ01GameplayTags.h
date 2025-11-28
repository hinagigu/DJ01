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
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InputTag_Move);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InputTag_Look_Mouse);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InputTag_Jump);

	// Ability System Tags
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_ActivateFail_ActivationGroup);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_ActivateFail_IsDead);

	// Status Tags
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Death);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_AutoRunning);
}