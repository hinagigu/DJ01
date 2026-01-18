// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "GameplayEffectTypes.h"

#include "DJ01GameplayEffectContext.generated.h"

class AActor;
class FArchive;
class IDJ01AbilitySourceInterface;
class UObject;
class UPhysicalMaterial;

USTRUCT()
struct FDJ01GameplayEffectContext : public FGameplayEffectContext
{
	GENERATED_BODY()

	FDJ01GameplayEffectContext()
		: FGameplayEffectContext()
	{
	}

	FDJ01GameplayEffectContext(AActor* InInstigator, AActor* InEffectCauser)
		: FGameplayEffectContext(InInstigator, InEffectCauser)
	{
	}

	/** Returns the wrapped FDJ01GameplayEffectContext from the handle, or nullptr if it doesn't exist or is the wrong type */
	static FDJ01GameplayEffectContext* ExtractEffectContext(struct FGameplayEffectContextHandle Handle);

	/** Sets the object used as the ability source */
	void SetAbilitySource(const IDJ01AbilitySourceInterface* InObject, float InSourceLevel);

	/** Returns the ability source interface associated with the source object. Only valid on the authority. */
	const IDJ01AbilitySourceInterface* GetAbilitySource() const;

	virtual FGameplayEffectContext* Duplicate() const override
	{
		FDJ01GameplayEffectContext* NewContext = new FDJ01GameplayEffectContext();
		*NewContext = *this;
		NewContext->AddActors(Actors);
		if (GetHitResult())
		{
			// Does a deep copy of the hit result
			NewContext->AddHitResult(*GetHitResult(), true);
		}
		// ComboGraph 兼容
		NewContext->CueParamsObjects = CueParamsObjects;
		NewContext->CueParamsObjectsPaths = CueParamsObjectsPaths;
		return NewContext;
	}

	virtual UScriptStruct* GetScriptStruct() const override
	{
		return FDJ01GameplayEffectContext::StaticStruct();
	}

	/** Overridden to serialize new fields */
	virtual bool NetSerialize(FArchive& Ar, class UPackageMap* Map, bool& bOutSuccess) override;

	/** Returns the physical material from the hit result if there is one */
	const UPhysicalMaterial* GetPhysicalMaterial() const;

	//~============================================================================
	// ComboGraph 兼容 - Gameplay Cue 参数传递
	//~============================================================================

	/** 获取 Cue 参数对象数组（用于 ComboGraph Gameplay Cue） */
	TArray<TWeakObjectPtr<UObject>> GetCueParamsObjects() const { return CueParamsObjects; }
	
	/** 设置 Cue 参数对象数组 */
	void SetCueParamsObjects(const TArray<TWeakObjectPtr<UObject>>& InCueParamsObjects) { CueParamsObjects = InCueParamsObjects; }

	/** 获取 Cue 参数对象路径数组 */
	TArray<FSoftObjectPath> GetCueParamsObjectsPaths() const { return CueParamsObjectsPaths; }
	
	/** 设置 Cue 参数对象路径数组 */
	void SetCueParamsObjectsPath(const TArray<FSoftObjectPath>& InCueParamsObjectsPaths) { CueParamsObjectsPaths = InCueParamsObjectsPaths; }

public:
	/** ID to allow the identification of multiple bullets that were part of the same cartridge */
	UPROPERTY()
	int32 CartridgeID = -1;

protected:
	/** Ability Source object (should implement IDJ01AbilitySourceInterface). NOT replicated currently */
	UPROPERTY()
	TWeakObjectPtr<const UObject> AbilitySourceObject;

	//~============================================================================
	// ComboGraph 兼容数据
	//~============================================================================

	/** ComboGraph Gameplay Cue 使用的参数对象 */
	UPROPERTY()
	TArray<TWeakObjectPtr<UObject>> CueParamsObjects;

	/** ComboGraph Gameplay Cue 使用的参数对象路径（用于序列化） */
	UPROPERTY()
	TArray<FSoftObjectPath> CueParamsObjectsPaths;
};

template<>
struct TStructOpsTypeTraits<FDJ01GameplayEffectContext> : public TStructOpsTypeTraitsBase2<FDJ01GameplayEffectContext>
{
	enum
	{
		WithNetSerializer = true,
		WithCopy = true
	};
};


