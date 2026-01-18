// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "DJ01/AbilitySystem/Attributes/BindingSets/Generated/BindingSets.h"
#include "CoreMinimal.h"
#include "Animation/AnimInstance.h"
#include "TestAnimInstance.generated.h"

class UAbilitySystemComponent;

/**
* UTestAnimInstance
*
* 测试用动画实例类
* 用于测试 BindingSet 功能和属性监听
*/
UCLASS(Config = Game)
class DJ01_API UTestAnimInstance : public UAnimInstance
{
	GENERATED_BODY()







public:

	UTestAnimInstance(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

protected:

	virtual void NativeInitializeAnimation() override;
	virtual void NativeUpdateAnimation(float DeltaSeconds) override;
};