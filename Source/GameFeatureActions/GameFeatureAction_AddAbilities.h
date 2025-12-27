// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "GameFeatureAction_WorldActionBase.h"
#include "Abilities/GameplayAbility.h"

#include "GameFeatureAction_AddAbilities.generated.h"

struct FWorldContext;
class UInputAction;
class UAttributeSet;
class UDataTable;
struct FComponentRequestHandle;
class UDJ01AbilitySet;
struct FDJ01AbilitySet_GrantedHandles;

/**
 * FDJ01AbilityGrant
 * 用于在 GameFeature 中授予单个 Gameplay Ability 的数据结构
 */
USTRUCT(BlueprintType)
struct FDJ01AbilityGrant
{
	GENERATED_BODY()

	// 要授予的 Ability 类型
	UPROPERTY(EditAnywhere, BlueprintReadOnly, meta=(AssetBundles="Client,Server"))
	TSoftClassPtr<UGameplayAbility> AbilityType;
};

/**
* FDJ01AttributeSetGrant
* 用于在 GameFeature 中授予单个 Attribute Set 的数据结构
*/
USTRUCT(BlueprintType)
struct FDJ01AttributeSetGrant
{
	GENERATED_BODY()

	// 要授予的 AttributeSet 类型
	UPROPERTY(EditAnywhere, BlueprintReadOnly, meta=(AssetBundles="Client,Server"))
	TSoftClassPtr<UAttributeSet> AttributeSetType;

	// 属性集的标识 Tag（用于通过 Tag 查找属性集）
	// 例如：AttributeSet.Health, AttributeSet.Combat, AttributeSet.Stamina
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Meta = (Categories = "AttributeSet"))
	FGameplayTag AttributeSetTag;

	// 用于初始化属性的数据表（可选）
	UPROPERTY(EditAnywhere, BlueprintReadOnly, meta=(AssetBundles="Client,Server"))
	TSoftObjectPtr<UDataTable> InitializationData;
};

/**
* FGameFeatureAbilitiesEntry
* GameFeature 中添加 Abilities 的配置条目
*/
USTRUCT(BlueprintType)
struct FGameFeatureAbilitiesEntry
{
	GENERATED_BODY()

	// 目标 Actor 类
	UPROPERTY(EditAnywhere, Category="Abilities")
	TSoftClassPtr<AActor> ActorClass;

	// 要授予的 Ability 列表
	UPROPERTY(EditAnywhere, Category="Abilities")
	TArray<FDJ01AbilityGrant> GrantedAbilities;

	// 要授予的 AttributeSet 列表
	UPROPERTY(EditAnywhere, Category="Attributes")
	TArray<FDJ01AttributeSetGrant> GrantedAttributes;

	// 要授予的 AbilitySet 列表
	UPROPERTY(EditAnywhere, Category="Attributes", meta=(AssetBundles="Client,Server"))
	TArray<TSoftObjectPtr<const UDJ01AbilitySet>> GrantedAbilitySets;
};

//////////////////////////////////////////////////////////////////////
// UGameFeatureAction_AddAbilities

/**
 * UGameFeatureAction_AddAbilities
 * 
 * 负责向指定类型的 Actor 授予 Abilities、AttributeSets 和 AbilitySets 的 GameFeatureAction。
 * 这样可以通过 GameFeature 动态配置角色的技能和属性，而非在代码中硬编码。
 */
UCLASS(MinimalAPI, meta = (DisplayName = "Add Abilities"))
class UGameFeatureAction_AddAbilities final : public UGameFeatureAction_WorldActionBase
{
	GENERATED_BODY()

public:
	//~ Begin UGameFeatureAction interface
	virtual void OnGameFeatureActivating(FGameFeatureActivatingContext& Context) override;
	virtual void OnGameFeatureDeactivating(FGameFeatureDeactivatingContext& Context) override;
	//~ End UGameFeatureAction interface

	//~ Begin UObject interface
#if WITH_EDITOR
	virtual EDataValidationResult IsDataValid(class FDataValidationContext& Context) const override;
#endif
	//~ End UObject interface

	/** 要处理的 Abilities 列表配置 */
	UPROPERTY(EditAnywhere, Category="Abilities", meta=(TitleProperty="ActorClass", ShowOnlyInnerProperties))
	TArray<FGameFeatureAbilitiesEntry> AbilitiesList;

private:
	/** 已添加的扩展信息 */
	struct FActorExtensions
	{
		TArray<FGameplayAbilitySpecHandle> Abilities;
		TArray<UAttributeSet*> Attributes;
		TArray<FDJ01AbilitySet_GrantedHandles> AbilitySetHandles;
	};

	/** 每个 Context 的数据 */
	struct FPerContextData
	{
		TMap<AActor*, FActorExtensions> ActiveExtensions;
		TArray<TSharedPtr<FComponentRequestHandle>> ComponentRequests;
	};
	
	TMap<FGameFeatureStateChangeContext, FPerContextData> ContextData;	

	//~ Begin UGameFeatureAction_WorldActionBase interface
	virtual void AddToWorld(const FWorldContext& WorldContext, const FGameFeatureStateChangeContext& ChangeContext) override;
	//~ End UGameFeatureAction_WorldActionBase interface

	void Reset(FPerContextData& ActiveData);
	void HandleActorExtension(AActor* Actor, FName EventName, int32 EntryIndex, FGameFeatureStateChangeContext ChangeContext);
	void AddActorAbilities(AActor* Actor, const FGameFeatureAbilitiesEntry& AbilitiesEntry, FPerContextData& ActiveData);
	void RemoveActorAbilities(AActor* Actor, FPerContextData& ActiveData);

	template<class ComponentType>
	ComponentType* FindOrAddComponentForActor(AActor* Actor, const FGameFeatureAbilitiesEntry& AbilitiesEntry, FPerContextData& ActiveData)
	{
		return Cast<ComponentType>(FindOrAddComponentForActor(ComponentType::StaticClass(), Actor, AbilitiesEntry, ActiveData));
	}
	UActorComponent* FindOrAddComponentForActor(UClass* ComponentType, AActor* Actor, const FGameFeatureAbilitiesEntry& AbilitiesEntry, FPerContextData& ActiveData);
};