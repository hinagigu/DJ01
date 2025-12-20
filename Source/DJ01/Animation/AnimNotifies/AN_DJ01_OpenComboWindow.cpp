// Copyright Epic Games, Inc. All Rights Reserved.

#include "AN_DJ01_OpenComboWindow.h"
#include "DJ01/Combo/Public/DJ01ComboManager.h"
#include "Components/SkeletalMeshComponent.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(AN_DJ01_OpenComboWindow)

UAN_DJ01_OpenComboWindow::UAN_DJ01_OpenComboWindow()
{
#if WITH_EDITORONLY_DATA
	NotifyColor = FColor(0, 200, 100); // 绿色，表示开始窗口
#endif
}

FString UAN_DJ01_OpenComboWindow::GetNotifyName_Implementation() const
{
	if (ComboChainTag.IsValid())
	{
		return FString::Printf(TEXT("Open Combo [%s]"), *ComboChainTag.ToString());
	}
	return TEXT("Open Combo Window");
}

void UAN_DJ01_OpenComboWindow::Notify(USkeletalMeshComponent* MeshComp, UAnimSequenceBase* Animation, const FAnimNotifyEventReference& EventReference)
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

	// 获取 ComboManager 并打开连招窗口
	if (UDJ01ComboManager* ComboManager = OwnerActor->FindComponentByClass<UDJ01ComboManager>())
	{
		ComboManager->OpenComboWindow(ComboChainTag);
	}
}