// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "GameplayTagContainer.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "DJ01AbilitySystemStatics.generated.h"

class UAbilitySystemComponent;
class UDJ01AbilitySystemComponent;
class UAttributeSet;

/**
 * UDJ01AbilitySystemStatics
 * 
 * 提供与 AbilitySystem 相关的静态蓝图工具函数。
 * 支持从任意拥有 ASC 的 Actor 通过 Tag 获取属性集。
 */
UCLASS()
class DJ01_API UDJ01AbilitySystemStatics : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

public:
	//~============================================================================
	// AbilitySystemComponent 获取
	//~============================================================================
	
	/**
	 * 从 Actor 获取 AbilitySystemComponent
	 * 支持直接实现 IAbilitySystemInterface 的 Actor 或通过 PlayerState 持有 ASC 的 Pawn
	 */
	UFUNCTION(BlueprintPure, Category = "DJ01|AbilitySystem", meta = (DefaultToSelf = "Actor"))
	static UAbilitySystemComponent* GetAbilitySystemComponent(AActor* Actor);

	/**
	 * 从 Actor 获取 DJ01AbilitySystemComponent
	 */
	UFUNCTION(BlueprintPure, Category = "DJ01|AbilitySystem", meta = (DefaultToSelf = "Actor"))
	static UDJ01AbilitySystemComponent* GetDJ01AbilitySystemComponent(AActor* Actor);
	
	//~============================================================================
	// 通过 Tag 获取属性集（核心功能）
	//~============================================================================
	
	/**
	 * 通过 Tag 从 Actor 获取属性集
	 * @param Actor - 拥有 ASC 的 Actor（角色、PlayerState 等）
	 * @param AttributeSetTag - 属性集的标识 Tag（如 AttributeSet.Health）
	 * @return 对应的属性集实例，如果不存在则返回 nullptr
	 */
	UFUNCTION(BlueprintPure, Category = "DJ01|AbilitySystem|Attributes", meta = (DefaultToSelf = "Actor"))
	static const UAttributeSet* GetAttributeSetByTag(AActor* Actor, FGameplayTag AttributeSetTag);

	/**
	 * 通过 Tag 从 ASC 获取属性集
	 */
	UFUNCTION(BlueprintPure, Category = "DJ01|AbilitySystem|Attributes")
	static const UAttributeSet* GetAttributeSetByTagFromASC(UDJ01AbilitySystemComponent* ASC, FGameplayTag AttributeSetTag);
};