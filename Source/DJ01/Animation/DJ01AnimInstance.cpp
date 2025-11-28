// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01AnimInstance.h"
#include "AbilitySystemGlobals.h"
#include "DJ01/Character/Public/DJ01Character.h"
#include "DJ01/Character/Public/DJ01CharacterMovementComponent.h"

#if WITH_EDITOR
#include "Misc/DataValidation.h"
#endif

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01AnimInstance)


UDJ01AnimInstance::UDJ01AnimInstance(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
}

void UDJ01AnimInstance::InitializeWithAbilitySystem(UAbilitySystemComponent* ASC)
{
	check(ASC);

	GameplayTagPropertyMap.Initialize(this, ASC);
}

#if WITH_EDITOR
EDataValidationResult UDJ01AnimInstance::IsDataValid(FDataValidationContext& Context) const
{
	Super::IsDataValid(Context);

	GameplayTagPropertyMap.IsDataValid(this, Context);

	return ((Context.GetNumErrors() > 0) ? EDataValidationResult::Invalid : EDataValidationResult::Valid);
}
#endif // WITH_EDITOR

void UDJ01AnimInstance::NativeInitializeAnimation()
{
	Super::NativeInitializeAnimation();

	if (AActor* OwningActor = GetOwningActor())
	{
		if (UAbilitySystemComponent* ASC = UAbilitySystemGlobals::GetAbilitySystemComponentFromActor(OwningActor))
		{
			InitializeWithAbilitySystem(ASC);
		}
	}
}

void UDJ01AnimInstance::NativeUpdateAnimation(float DeltaSeconds)
{
	Super::NativeUpdateAnimation(DeltaSeconds);

	const ADJ01Character* Character = Cast<ADJ01Character>(GetOwningActor());
	if (!Character)
	{
		return;
	}

	UDJ01CharacterMovementComponent* CharMoveComp = CastChecked<UDJ01CharacterMovementComponent>(Character->GetCharacterMovement());
	const FDJ01CharacterGroundInfo& GroundInfo = CharMoveComp->GetGroundInfo();
	GroundDistance = GroundInfo.GroundDistance;
}
