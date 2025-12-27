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
	 * 应在对象构造时调用，Initialize() 之前
	 * 
	 * @param Tag 要监听的 GameplayTag
	 * @param PropertyName 要更新的属性名（使用 GET_MEMBER_NAME_CHECKED 获取）
	 */
	/**
	 * 添加一个 Tag 到属性的映射
	 * 应在对象构造时调用，Initialize() 之前
	 * 
	 * @param Tag 要监听的 GameplayTag
	 * @param PropertyName 要更新的属性名（使用 GET_MEMBER_NAME_CHECKED 获取）
	 */
	void AddMapping(const FGameplayTag& Tag, FName PropertyName)
	{
		FGameplayTagBlueprintPropertyMapping Mapping;
		Mapping.TagToMap = Tag;
		Mapping.PropertyName = PropertyName;
		// PropertyToEdit 和 PropertyGuid 会在 Initialize() 时由引擎根据 PropertyName 自动解析
		PropertyMappings.Add(Mapping);
	}

	/** 获取当前映射数量（用于调试） */
	int32 GetMappingCount() const
	{
		return PropertyMappings.Num();
	}
};