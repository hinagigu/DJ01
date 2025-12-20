// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Animation/AnimNotifies/AnimNotify.h"
#include "GameplayTagContainer.h"
#include "AN_DJ01_OpenComboWindow.generated.h"

/**
 * UAN_DJ01_OpenComboWindow
 * 
 * 动画通知：打开连招窗口
 * 在动画的某个时间点触发，标记可以接受下一段连招输入
 */
UCLASS(DisplayName = "DJ01 Open Combo Window")
class DJ01_API UAN_DJ01_OpenComboWindow : public UAnimNotify
{
	GENERATED_BODY()

public:

	UAN_DJ01_OpenComboWindow();

	virtual FString GetNotifyName_Implementation() const override;
	virtual void Notify(USkeletalMeshComponent* MeshComp, UAnimSequenceBase* Animation, const FAnimNotifyEventReference& EventReference) override;

public:

	/** 
	 * 连招链标识（可选）
	 * 用于区分不同的连招链，如 Combo.Sword.Light / Combo.Sword.Heavy
	 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Combo")
	FGameplayTag ComboChainTag;
};