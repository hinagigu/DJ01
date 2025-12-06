#include "DJ01/System/Public/DJ01GameplayTags.h"

#include "GameplayTagsManager.h"

namespace DJ01GameplayTags
{
    // ============================================================
    // 初始化状态 (InitState)
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(InitState_Spawned, "InitState.Spawned", "1: Actor/component has initially spawned and can be extended");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(InitState_DataAvailable, "InitState.DataAvailable", "2: All required data has been loaded/replicated and is ready for initialization");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(InitState_DataInitialized, "InitState.DataInitialized", "3: The available data has been initialized for this actor/component, but it is not ready for full gameplay");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(InitState_GameplayReady, "InitState.GameplayReady", "4: The actor/component is fully ready for active gameplay");

    // ============================================================
    // 输入标签 (InputTag)
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(InputTag_Move, "InputTag.Move", "Move input.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(InputTag_Look_Mouse, "InputTag.Look.Mouse", "Look input with mouse.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(InputTag_Jump, "InputTag.Jump", "Jump input.");

    // ============================================================
    // 属性集标签 (AttributeSet)
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(AttributeSet_Health, "AttributeSet.Health", "Health attribute set identifier.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(AttributeSet_Combat, "AttributeSet.Combat", "Combat attribute set identifier.");

    // ============================================================
    // 技能系统标签 (Ability)
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Ability_ActivateFail_ActivationGroup, "Ability.ActivateFail.ActivationGroup", "Ability failed to activate due to activation group constraints.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Ability_ActivateFail_IsDead, "Ability.ActivateFail.IsDead", "Ability failed to activate because the owner is dead.");

    // ============================================================
    // 攻击技能标签 (Ability.Attack)
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Ability_Attack_Light, "Ability.Attack.Light", "Light attack ability.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Ability_Attack_Heavy, "Ability.Attack.Heavy", "Heavy attack ability.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Ability_Dodge, "Ability.Dodge", "Dodge/roll ability.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Ability_Block, "Ability.Block", "Block/parry ability.");

    // ============================================================
    // 动画事件标签 (Event.Animation)
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Event_Animation_ComboWindow, "Event.Animation.ComboWindow", "Combo window opened - can chain to next attack.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Event_Animation_ComboWindowEnd, "Event.Animation.ComboWindowEnd", "Combo window closed.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Event_Animation_DamageFrame, "Event.Animation.DamageFrame", "Damage frame - perform hit detection.");

    // ============================================================
    // 状态标签 (Status)
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_Death, "Status.Death", "Target is dead.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_AutoRunning, "Status.AutoRunning", "Character is auto-running.");

    // ============================================================
    // 移动状态标签 (Status.Movement)
    // 用于 AnimInstance 的 GameplayTagPropertyMap 映射
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_Movement_Grounded, "Status.Movement.Grounded", "Character is on the ground.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_Movement_InAir, "Status.Movement.InAir", "Character is in the air (jumping/falling).");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_Movement_Sprinting, "Status.Movement.Sprinting", "Character is sprinting.");

    // ============================================================
    // 动作状态标签 (Status.Action)
    // 用于 AnimInstance 的 GameplayTagPropertyMap 映射
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_Action_Attacking, "Status.Action.Attacking", "Character is performing an attack.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_Action_Blocking, "Status.Action.Blocking", "Character is blocking.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_Action_Dodging, "Status.Action.Dodging", "Character is dodging/rolling.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_Action_Casting, "Status.Action.Casting", "Character is casting a spell.");

    // ============================================================
    // 状态条件标签 (Status.Condition)
    // 控制效果，影响移动和动作
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_Condition_Stunned, "Status.Condition.Stunned", "Character is stunned - cannot move or act.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_Condition_Rooted, "Status.Condition.Rooted", "Character is rooted - cannot move but can act.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_Condition_Silenced, "Status.Condition.Silenced", "Character is silenced - cannot use abilities.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_Condition_Slowed, "Status.Condition.Slowed", "Character is slowed - reduced movement speed.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Status_Condition_Hasted, "Status.Condition.Hasted", "Character is hasted - increased movement speed.");

    // ============================================================
    // 伤害类型标签 (Damage.Type)
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Damage_Type_Physical, "Damage.Type.Physical", "Physical damage - reduced by Defense.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Damage_Type_Magical, "Damage.Type.Magical", "Magical damage - reduced by MagicDefense.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Damage_Type_True, "Damage.Type.True", "True damage - ignores all defenses.");

    // ============================================================
    // 伤害元素标签 (Damage.Element)
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Damage_Element_Fire, "Damage.Element.Fire", "Fire elemental damage.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Damage_Element_Ice, "Damage.Element.Ice", "Ice elemental damage.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Damage_Element_Thunder, "Damage.Element.Thunder", "Thunder/Lightning elemental damage.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Damage_Element_Water, "Damage.Element.Water", "Water elemental damage.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Damage_Element_Wind, "Damage.Element.Wind", "Wind elemental damage.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Damage_Element_Light, "Damage.Element.Light", "Light/Holy elemental damage.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Damage_Element_Dark, "Damage.Element.Dark", "Dark/Shadow elemental damage.");

    // ============================================================
    // 元素弱点标签 (Weakness.Element)
    // 挂在角色/敌人身上，命中弱点时伤害 +50%
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Weakness_Element_Fire, "Weakness.Element.Fire", "Weak to Fire - takes +50% fire damage.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Weakness_Element_Ice, "Weakness.Element.Ice", "Weak to Ice - takes +50% ice damage.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Weakness_Element_Thunder, "Weakness.Element.Thunder", "Weak to Thunder - takes +50% thunder damage.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Weakness_Element_Water, "Weakness.Element.Water", "Weak to Water - takes +50% water damage.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Weakness_Element_Wind, "Weakness.Element.Wind", "Weak to Wind - takes +50% wind damage.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Weakness_Element_Light, "Weakness.Element.Light", "Weak to Light - takes +50% light damage.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Weakness_Element_Dark, "Weakness.Element.Dark", "Weak to Dark - takes +50% dark damage.");

    // ============================================================
    // 伤害事件标签 (GameplayCue)
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(GameplayCue_Damage, "GameplayCue.Damage", "Generic damage feedback cue.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(GameplayCue_Damage_Weakness, "GameplayCue.Damage.Weakness", "Weakness hit damage feedback cue (extra visual/audio).");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(GameplayCue_Heal, "GameplayCue.Heal", "Heal feedback cue.");

    // ============================================================
    // 作弊标签 (Cheat) - 仅非 Shipping 构建
    // ============================================================
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Cheat_GodMode, "Cheat.GodMode", "God mode - makes the player invincible.");
    UE_DEFINE_GAMEPLAY_TAG_COMMENT(Cheat_UnlimitedHealth, "Cheat.UnlimitedHealth", "Unlimited health - health cannot drop below 1.");
}