// ============================================================
// DJ01 Generated GameplayTags
// 自动生成的文件，请勿手动修改！
// 生成时间: 2025-12-20 19:36:12
// ============================================================

#pragma once

#include "NativeGameplayTags.h"

namespace DJ01GameplayTags
{
    // ========== InitState ==========
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InitState_Spawned);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InitState_DataAvailable);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InitState_DataInitialized);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InitState_GameplayReady);

    // ========== InputTag ==========
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InputTag_Move);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InputTag_Look_Mouse);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InputTag_Jump);

    // ========== AttributeSet ==========
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(AttributeSet_Health);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(AttributeSet_Combat);

    // ========== Ability ==========
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_ActivateFail_ActivationGroup);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_ActivateFail_IsDead);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_Attack_Light);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_Attack_Heavy);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_Dodge);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_Block);

    // ========== Event ==========
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Event_Animation_ComboWindow);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Event_Animation_ComboWindowEnd);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Event_Animation_DamageFrame);

    // ========== Status ==========
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Death);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_AutoRunning);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Movement_Grounded);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Movement_InAir);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Movement_Sprinting);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Action_Attacking);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Action_Blocking);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Action_Dodging);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Action_Casting);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Condition_Stunned);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Condition_Rooted);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Condition_Silenced);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Condition_Slowed);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Condition_Hasted);

    // ========== Damage ==========
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Type_Physical);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Type_Magical);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Type_True);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Element_Fire);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Element_Ice);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Element_Thunder);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Element_Water);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Element_Wind);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Element_Light);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Element_Dark);

    // ========== Weakness ==========
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Weakness_Element_Fire);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Weakness_Element_Ice);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Weakness_Element_Thunder);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Weakness_Element_Water);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Weakness_Element_Wind);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Weakness_Element_Light);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Weakness_Element_Dark);

    // ========== GameplayCue ==========
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(GameplayCue_Damage);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(GameplayCue_Damage_Weakness);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(GameplayCue_Heal);

    // ========== State ==========
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(State_Combo_WindowOpen);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(State_Combo_Chain_Light);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(State_Combo_Chain_Heavy);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(State_Combo_Chain_Special);

    // ========== Cheat ==========
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Cheat_GodMode);
    DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Cheat_UnlimitedHealth);

}
