// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01/AbilitySystem/Attributes/Public/DJ01AttributeSet.h"

#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"
#include "Net/UnrealNetwork.h"

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

void UDJ01AttributeSet::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
	Super::GetLifetimeReplicatedProps(OutLifetimeProps);
	// 基类不注册任何属性，由子类处理
}

