// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01AttributeSet.h"

#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01AttributeSet)

class UWorld;


UDJ01AttributeSet::UDJ01AttributeSet()
{
}

UWorld* UDJ01AttributeSet::GetWorld() const
{
	const UObject* Outer = GetOuter();
	check(Outer);

	return Outer->GetWorld();
}

UDJ01AbilitySystemComponent* UDJ01AttributeSet::GetDJ01AbilitySystemComponent() const
{
	return Cast<UDJ01AbilitySystemComponent>(GetOwningAbilitySystemComponent());
}

