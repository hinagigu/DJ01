// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Animation/AnimNotifies/AnimNotify.h"
#include "AN_DJ01_CloseComboWindow.generated.h"

/**
 * UAN_DJ01_CloseComboWindow
 * 
 * 动画通知：关闭连招窗口
 * 在动画的某个时间点触发，关闭连招窗口并尝试消费缓冲的输入
 */
UCLASS(DisplayName = "DJ01 Close Combo Window")
class DJ01_API UAN_DJ01_CloseComboWindow : public UAnimNotify
{
	GENERATED_BODY()

public:

	UAN_DJ01_CloseComboWindow();

	virtual FString GetNotifyName_Implementation() const override;
	virtual void Notify(USkeletalMeshComponent* MeshComp, UAnimSequenceBase* Animation, const FAnimNotifyEventReference& EventReference) override;

public:

	/** 
	 * 是否消费缓冲的输入
	 * true: 关闭窗口时尝试激活下一个技能
	 * false: 仅关闭窗口，不处理缓冲输入
	 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Combo")
	bool bConsumeInput = true;
};