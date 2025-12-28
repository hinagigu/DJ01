// Copyright Epic Games, Inc. All Rights Reserved.

#include "TestAnimInstance.h"
#include "AbilitySystemComponent.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(TestAnimInstance)


UTestAnimInstance::UTestAnimInstance(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
}

void UTestAnimInstance::InitializeWithAbilitySystem(UAbilitySystemComponent* ASC)
{
	if (!ASC)
	{
		return;
	}

	// 初始化 BindingSet，注册监听器并获取当前值
	DJ01_INIT_BINDING_SET(Test, ASC)
}

void UTestAnimInstance::NativeInitializeAnimation()
{
	Super::NativeInitializeAnimation();
}

void UTestAnimInstance::NativeUpdateAnimation(float DeltaSeconds)
{
	Super::NativeUpdateAnimation();

	// 测试用：可以在这里更新属性值用于调试
}