// Copyright DJ01. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "GameplayEffectTypes.h"
#include "DJ01GameplayTagPropertyMap.generated.h"

/**
* FDJ01GameplayTagPropertyMap
* 
* 扩展 FGameplayTagBlueprintPropertyMap，提供 C++ 端添加映射的接口
* 这样可以在代码中自动配置 Tag 到变量的映射，无需在蓝图中手动配置
*/
USTRUCT(BlueprintType)
struct DJ01_API FDJ01GameplayTagPropertyMap : public FGameplayTagBlueprintPropertyMap
{
	GENERATED_BODY()

public:
	/**
	 * 添加一个 Tag 到属性的映射
	 * 在构造函数中调用，只记录 Tag 和属性名
	 * 
	 * @param Tag 要监听的 GameplayTag
	 * @param InPropertyName 要更新的属性名
	 */
	void AddMapping(const FGameplayTag& Tag, FName InPropertyName)
	{
		FGameplayTagBlueprintPropertyMapping Mapping;
		Mapping.TagToMap = Tag;
		Mapping.PropertyName = InPropertyName;
		// PropertyToEdit 稍后在 ResolveProperties 中设置
		PropertyMappings.Add(Mapping);
	}

	/**
	 * 解析所有映射的属性引用
	 * 必须在 Initialize() 之前调用，此时类信息已完整可用
	 * 
	 * @param OwnerClass 拥有这些属性的类
	 */
	void ResolveProperties(UClass* OwnerClass)
	{
		if (!OwnerClass)
		{
			return;
		}
		
		for (FGameplayTagBlueprintPropertyMapping& Mapping : PropertyMappings)
		{
			if (Mapping.PropertyName != NAME_None && !Mapping.PropertyToEdit.Get())
			{
				if (FProperty* Property = OwnerClass->FindPropertyByName(Mapping.PropertyName))
				{
					Mapping.PropertyToEdit = Property;
				}
			}
		}
	}

	/** 获取当前映射数量（用于调试） */
	int32 GetMappingCount() const
	{
		return PropertyMappings.Num();
	}
};