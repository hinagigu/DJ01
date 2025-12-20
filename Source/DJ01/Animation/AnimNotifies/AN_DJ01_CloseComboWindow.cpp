// Copyright Epic Games, Inc. All Rights Reserved.

#include "AN_DJ01_CloseComboWindow.h"
#include "DJ01/Combo/Public/DJ01ComboManager.h"
#include "Components/SkeletalMeshComponent.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(AN_DJ01_CloseComboWindow)

UAN_DJ01_CloseComboWindow::UAN_DJ01_CloseComboWindow()
{
#if WITH_EDITORONLY_DATA
	NotifyColor = FColor(200, 100, 0); // 橙色，表示关闭窗口
#endif
}

FString UAN_DJ01_CloseComboWindow::GetNotifyName_Implementation() const
{
	return bConsumeInput ? TEXT("Close Combo & Consume") : TEXT("Close Combo Window");
}

void UAN_DJ01_CloseComboWindow::Notify(USkeletalMeshComponent* MeshComp, UAnimSequenceBase* Animation, const FAnimNotifyEventReference& EventReference)
{
	Super::Notify(MeshComp, Animation, EventReference);

	if (!MeshComp)
	{
		return;
	}

	AActor* OwnerActor = MeshComp->GetOwner();
	if (!OwnerActor)
	{
		return;
	}

	// 获取 ComboManager 并关闭连招窗口
	if (UDJ01ComboManager* ComboManager = OwnerActor->FindComponentByClass<UDJ01ComboManager>())
	{
		if (bConsumeInput)
		{
			ComboManager->CloseComboWindowAndConsume();
		}
		else
		{
			ComboManager->CloseComboWindow();
		}
	}
}