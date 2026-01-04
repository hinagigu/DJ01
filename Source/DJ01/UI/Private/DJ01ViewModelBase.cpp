// Copyright DJ01. All Rights Reserved.

#include "DJ01/UI/Public/DJ01ViewModelBase.h"
#include "AbilitySystemComponent.h"

UDJ01ViewModelBase::UDJ01ViewModelBase()
{
}

void UDJ01ViewModelBase::InitializeViewModel_Implementation(UAbilitySystemComponent* ASC)
{
	BoundASC = ASC;
}

void UDJ01ViewModelBase::UninitializeViewModel_Implementation()
{
	BoundASC = nullptr;
}