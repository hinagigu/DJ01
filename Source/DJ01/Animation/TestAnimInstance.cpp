// Copyright Epic Games, Inc. All Rights Reserved.

#include "TestAnimInstance.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(TestAnimInstance)


UTestAnimInstance::UTestAnimInstance(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
}

void UTestAnimInstance::NativeInitializeAnimation()
{
	Super::NativeInitializeAnimation();
}

void UTestAnimInstance::NativeUpdateAnimation(float DeltaSeconds)
{
	Super::NativeUpdateAnimation(DeltaSeconds);
}