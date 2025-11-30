// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "AttributeSet.h"

#include "DJ01AttributeSet.generated.h"

class AActor;
class UDJ01AbilitySystemComponent;
class UObject;
class UWorld;
struct FGameplayEffectSpec;


/**
 * 属性访问器宏
 * 
 * 为属性创建一组辅助函数，例如：
 *		ATTRIBUTE_ACCESSORS(UDJ01HealthSet, Health)
 * 将创建以下函数：
 *		static FGameplayAttribute GetHealthAttribute();
 *		float GetHealth() const;
 *		void SetHealth(float NewVal);
 *		void InitHealth(float NewVal);
 */
#define ATTRIBUTE_ACCESSORS(ClassName, PropertyName) \
    GAMEPLAYATTRIBUTE_PROPERTY_GETTER(ClassName, PropertyName) \
    GAMEPLAYATTRIBUTE_VALUE_GETTER(PropertyName) \
    GAMEPLAYATTRIBUTE_VALUE_SETTER(PropertyName) \
    GAMEPLAYATTRIBUTE_VALUE_INITTER(PropertyName)

/** 
 * 属性事件委托
 * 用于广播属性变化事件，部分参数在客户端可能为空：
 * @param EffectInstigator	效果发起者
 * @param EffectCauser		造成变化的物理 Actor
 * @param EffectSpec		完整的效果规格
 * @param EffectMagnitude	原始数值（clamp 之前）
 * @param OldValue			变化前的值
 * @param NewValue			变化后的值
*/
DECLARE_MULTICAST_DELEGATE_SixParams(FDJ01AttributeEvent, AActor* /*EffectInstigator*/, AActor* /*EffectCauser*/, const FGameplayEffectSpec* /*EffectSpec*/, float /*EffectMagnitude*/, float /*OldValue*/, float /*NewValue*/);

/**
 * UDJ01AttributeSet
 *
 * 项目的基础属性集类
 * 所有游戏属性集都应该继承自此类
 */
UCLASS()
class DJ01_API UDJ01AttributeSet : public UAttributeSet
{
    GENERATED_BODY()

public:

    UDJ01AttributeSet();

    UWorld* GetWorld() const override;

    UDJ01AbilitySystemComponent* GetDJ01AbilitySystemComponent() const;
};
