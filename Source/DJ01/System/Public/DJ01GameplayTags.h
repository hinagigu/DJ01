#pragma once

#include "NativeGameplayTags.h"

namespace DJ01GameplayTags
{
	// ============================================================
	// 初始化状态 (InitState)
	// ============================================================
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InitState_Spawned);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InitState_DataAvailable);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InitState_DataInitialized);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InitState_GameplayReady);

	// ============================================================
	// 输入标签 (InputTag)
	// ============================================================
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InputTag_Move);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InputTag_Look_Mouse);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(InputTag_Jump);

	// ============================================================
	// 属性集标签 (AttributeSet)
	// ============================================================
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(AttributeSet_Health);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(AttributeSet_Combat);

	// ============================================================
	// 技能系统标签 (Ability)
	// ============================================================
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_ActivateFail_ActivationGroup);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_ActivateFail_IsDead);

	// ============================================================
	// 状态标签 (Status)
	// ============================================================
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Death);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_AutoRunning);

	// ============================================================
	// 移动状态标签 (Status.Movement)
	// 用于 AnimInstance 的 GameplayTagPropertyMap 映射
	// ============================================================
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Movement_Grounded);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Movement_InAir);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Movement_Sprinting);

	// ============================================================
	// 动作状态标签 (Status.Action)
	// 用于 AnimInstance 的 GameplayTagPropertyMap 映射
	// ============================================================
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Action_Attacking);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Action_Blocking);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Action_Dodging);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Action_Casting);

	// ============================================================
	// 状态条件标签 (Status.Condition)
	// 控制效果，影响移动和动作
	// ============================================================
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Condition_Stunned);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Condition_Rooted);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Condition_Silenced);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Condition_Slowed);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Status_Condition_Hasted);

	// ============================================================
	// 伤害类型标签 (Damage.Type)
	// 用于 DamageExecution 区分物理/魔法/真实伤害
	// ============================================================
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Type_Physical);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Type_Magical);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Type_True);

	// ============================================================
	// 伤害元素标签 (Damage.Element)
	// 技能携带的元素类型，用于触发弱点机制
	// ============================================================
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Element_Fire);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Element_Ice);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Element_Thunder);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Element_Water);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Element_Wind);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Element_Light);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Damage_Element_Dark);

	// ============================================================
	// 元素弱点标签 (Weakness.Element)
	// 挂在角色/敌人身上，表示对某元素有弱点
	// 命中弱点时伤害 +50%
	// ============================================================
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Weakness_Element_Fire);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Weakness_Element_Ice);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Weakness_Element_Thunder);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Weakness_Element_Water);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Weakness_Element_Wind);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Weakness_Element_Light);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Weakness_Element_Dark);

	// ============================================================
	// 伤害事件标签 (GameplayCue)
	// 用于触发伤害/治疗的视觉和音效反馈
	// ============================================================
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(GameplayCue_Damage);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(GameplayCue_Damage_Weakness);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(GameplayCue_Heal);

	// ============================================================
	// 作弊标签 (Cheat) - 仅非 Shipping 构建
	// ============================================================
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Cheat_GodMode);
	DJ01_API UE_DECLARE_GAMEPLAY_TAG_EXTERN(Cheat_UnlimitedHealth);
}