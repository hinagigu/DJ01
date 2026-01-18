// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/AbilitySystem/Public/DJ01GameplayEffectContext.h"

#include "DJ01/AbilitySystem/Public/DJ01AbilitySourceInterface.h"
#include "Engine/HitResult.h"
#include "PhysicalMaterials/PhysicalMaterial.h"

#if UE_WITH_IRIS
#include "Iris/ReplicationState/PropertyNetSerializerInfoRegistry.h"
#include "Serialization/GameplayEffectContextNetSerializer.h"
#endif

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01GameplayEffectContext)

class FArchive;

FDJ01GameplayEffectContext* FDJ01GameplayEffectContext::ExtractEffectContext(struct FGameplayEffectContextHandle Handle)
{
	FGameplayEffectContext* BaseEffectContext = Handle.Get();
	if ((BaseEffectContext != nullptr) && BaseEffectContext->GetScriptStruct()->IsChildOf(FDJ01GameplayEffectContext::StaticStruct()))
	{
		return (FDJ01GameplayEffectContext*)BaseEffectContext;
	}

	return nullptr;
}

bool FDJ01GameplayEffectContext::NetSerialize(FArchive& Ar, class UPackageMap* Map, bool& bOutSuccess)
{
	FGameplayEffectContext::NetSerialize(Ar, Map, bOutSuccess);

	// Not serialized for post-activation use:
	// CartridgeID

	//~============================================================================
	// ComboGraph 兼容 - 序列化 Cue 参数
	//~============================================================================
	
	uint8 bHasCueParamsObjects = (CueParamsObjects.Num() > 0) ? 1 : 0;
	uint8 bHasCueParamsPaths = (CueParamsObjectsPaths.Num() > 0) ? 1 : 0;
	
	Ar.SerializeBits(&bHasCueParamsObjects, 1);
	Ar.SerializeBits(&bHasCueParamsPaths, 1);
	
	if (bHasCueParamsObjects)
	{
		SafeNetSerializeTArray_Default<31>(Ar, CueParamsObjects);
	}
	
	if (bHasCueParamsPaths)
	{
		SafeNetSerializeTArray_Default<31>(Ar, CueParamsObjectsPaths);
	}

	return true;
}

#if UE_WITH_IRIS
namespace UE::Net
{
	// Forward to FGameplayEffectContextNetSerializer
	// Note: If FDJ01GameplayEffectContext::NetSerialize() is modified, a custom NetSerializesr must be implemented as the current fallback will no longer be sufficient.
	UE_NET_IMPLEMENT_FORWARDING_NETSERIALIZER_AND_REGISTRY_DELEGATES(DJ01GameplayEffectContext, FGameplayEffectContextNetSerializer);
}
#endif

void FDJ01GameplayEffectContext::SetAbilitySource(const IDJ01AbilitySourceInterface* InObject, float InSourceLevel)
{
	AbilitySourceObject = MakeWeakObjectPtr(Cast<const UObject>(InObject));
	//SourceLevel = InSourceLevel;
}

const IDJ01AbilitySourceInterface* FDJ01GameplayEffectContext::GetAbilitySource() const
{
	return Cast<IDJ01AbilitySourceInterface>(AbilitySourceObject.Get());
}

const UPhysicalMaterial* FDJ01GameplayEffectContext::GetPhysicalMaterial() const
{
	if (const FHitResult* HitResultPtr = GetHitResult())
	{
		return HitResultPtr->PhysMaterial.Get();
	}
	return nullptr;
}


