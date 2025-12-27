// ============================================================
// DJ01 Generated AnimInstance Variables & Tag Mappings
// 自动生成的文件，请勿手动修改！
// 生成时间: 2025-12-27 15:05:00
// ============================================================
//
// 使用方式：
// 1. 在 DJ01AnimInstance.h 顶部 #include 此文件
// 2. 在类的 protected 区域使用 DJ01_ANIM_INSTANCE_GENERATED_VARS
// 3. 在构造函数中使用 DJ01_ANIM_INSTANCE_INIT_TAG_MAPPINGS()
//    映射会自动完成，无需在蓝图中配置！
//

#pragma once

#include "NativeGameplayTags.h"
#include "DJ01/System/Public/DJ01GameplayTags.h"

// ========== 变量声明宏 (用于头文件 protected 区域) ==========
#define DJ01_ANIM_INSTANCE_GENERATED_VARS \
    /** Character is stunned - cannot move or act (映射自 Status.Condition.Stunned) */ \
    UPROPERTY(BlueprintReadOnly, Category = "Character State Data|Status") \
    bool bStunned = false; \
    /** Character is rooted - cannot move but can act (映射自 Status.Condition.Rooted) */ \
    UPROPERTY(BlueprintReadOnly, Category = "Character State Data|Status") \
    bool bRooted = false; \
    /** Character is silenced - cannot use abilities (映射自 Status.Condition.Silenced) */ \
    UPROPERTY(BlueprintReadOnly, Category = "Character State Data|Status") \
    bool bSlienced = false; \
    /** Character is slowed - reduced movement speed (映射自 Status.Condition.Slowed) */ \
    UPROPERTY(BlueprintReadOnly, Category = "Character State Data|Status") \
    bool bSlowed = false; \
    /** Character is hasted - increased movement speed (映射自 Status.Condition.Hasted) */ \
    UPROPERTY(BlueprintReadOnly, Category = "Character State Data|Status") \
    bool bHasted = false; \
    /** Character will immunity damage (映射自 Status.Immunity.Damage) */ \
    UPROPERTY(BlueprintReadOnly, Category = "Character State Data|Status") \
    bool bDamaged = false;


// ========== 映射初始化宏 (用于构造函数) ==========
// 自动配置 GameplayTagPropertyMap，无需在蓝图中手动配置
#define DJ01_ANIM_INSTANCE_INIT_TAG_MAPPINGS() \
    { \
        /* Status.Condition.Stunned -> bStunned */ \
        { \
            FGameplayTagBlueprintPropertyMapping Mapping; \
            Mapping.TagToMap = DJ01GameplayTags::Status_Condition_Stunned; \
            Mapping.PropertyName = GET_MEMBER_NAME_CHECKED(ThisClass, bStunned); \
            GameplayTagPropertyMap.PropertyMappings.Add(Mapping); \
        } \
        /* Status.Condition.Rooted -> bRooted */ \
        { \
            FGameplayTagBlueprintPropertyMapping Mapping; \
            Mapping.TagToMap = DJ01GameplayTags::Status_Condition_Rooted; \
            Mapping.PropertyName = GET_MEMBER_NAME_CHECKED(ThisClass, bRooted); \
            GameplayTagPropertyMap.PropertyMappings.Add(Mapping); \
        } \
        /* Status.Condition.Silenced -> bSlienced */ \
        { \
            FGameplayTagBlueprintPropertyMapping Mapping; \
            Mapping.TagToMap = DJ01GameplayTags::Status_Condition_Silenced; \
            Mapping.PropertyName = GET_MEMBER_NAME_CHECKED(ThisClass, bSlienced); \
            GameplayTagPropertyMap.PropertyMappings.Add(Mapping); \
        } \
        /* Status.Condition.Slowed -> bSlowed */ \
        { \
            FGameplayTagBlueprintPropertyMapping Mapping; \
            Mapping.TagToMap = DJ01GameplayTags::Status_Condition_Slowed; \
            Mapping.PropertyName = GET_MEMBER_NAME_CHECKED(ThisClass, bSlowed); \
            GameplayTagPropertyMap.PropertyMappings.Add(Mapping); \
        } \
        /* Status.Condition.Hasted -> bHasted */ \
        { \
            FGameplayTagBlueprintPropertyMapping Mapping; \
            Mapping.TagToMap = DJ01GameplayTags::Status_Condition_Hasted; \
            Mapping.PropertyName = GET_MEMBER_NAME_CHECKED(ThisClass, bHasted); \
            GameplayTagPropertyMap.PropertyMappings.Add(Mapping); \
        } \
        /* Status.Immunity.Damage -> bDamaged */ \
        { \
            FGameplayTagBlueprintPropertyMapping Mapping; \
            Mapping.TagToMap = DJ01GameplayTags::Status_Immunity_Damage; \
            Mapping.PropertyName = GET_MEMBER_NAME_CHECKED(ThisClass, bDamaged); \
            GameplayTagPropertyMap.PropertyMappings.Add(Mapping); \
        } \
    }

// ========== 宏结束 ==========
