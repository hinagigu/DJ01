// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Animation/AnimNotifies/AnimNotify.h"
#include "AN_DJ01_ResetCombo.generated.h"

/**
 * UAN_DJ01_ResetCombo
 * 
 * 动画通知：重置连招状态
 * 在连招结束动画的末尾触发，将连招状态重置为初始状态
 */
UCLASS(DisplayName = "DJ01 Reset Combo")
class DJ01_API UAN_DJ01_ResetCombo : public UAnimNotify
{
	GENERATED_BODY()

public:

	UAN_DJ01_ResetCombo();

	virtual FString GetNotifyName_Implementation() const override;
	virtual void Notify(USkeletalMeshComponent* MeshComp, UAnimSequenceBase* Animation, const FAnimNotifyEventReference& EventReference) override;
};