// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Input/Public/DJ01InputComponent.h"

#include "EnhancedInputSubsystems.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01InputComponent)

class UDJ01InputConfig;

UDJ01InputComponent::UDJ01InputComponent(const FObjectInitializer& ObjectInitializer)
{
}

void UDJ01InputComponent::AddInputMappings(const UDJ01InputConfig* InputConfig, UEnhancedInputLocalPlayerSubsystem* InputSubsystem) const
{
	check(InputConfig);
	check(InputSubsystem);

	// Here you can handle any custom logic to add something from your input config if required
}

void UDJ01InputComponent::RemoveInputMappings(const UDJ01InputConfig* InputConfig, UEnhancedInputLocalPlayerSubsystem* InputSubsystem) const
{
	check(InputConfig);
	check(InputSubsystem);

	// Here you can handle any custom logic to remove input mappings that you may have added above
}

void UDJ01InputComponent::RemoveBinds(TArray<uint32>& BindHandles)
{
	for (uint32 Handle : BindHandles)
	{
		RemoveBindingByHandle(Handle);
	}
	BindHandles.Reset();
}
