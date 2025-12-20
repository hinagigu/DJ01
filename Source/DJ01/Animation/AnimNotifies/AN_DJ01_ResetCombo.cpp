// Copyright Epic Games, Inc. All Rights Reserved.

#include "AN_DJ01_ResetCombo.h"
#include "DJ01/Combo/Public/DJ01ComboManager.h"
#include "Components/SkeletalMeshComponent.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(AN_DJ01_ResetCombo)

UAN_DJ01_ResetCombo::UAN_DJ01_ResetCombo()
{
#if WITH_EDITORONLY_DATA
	NotifyColor = FColor(200, 50, 50); // 红色，表示重置
#endif
}

FString UAN_DJ01_ResetCombo::GetNotifyName_Implementation() const
{
	return TEXT("Reset Combo");
}

void UAN_DJ01_ResetCombo::Notify(USkeletalMeshComponent* MeshComp, UAnimSequenceBase* Animation, const FAnimNotifyEventReference& EventReference)
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

	// 获取 ComboManager 并重置连招状态
	if (UDJ01ComboManager* ComboManager = OwnerActor->FindComponentByClass<UDJ01ComboManager>())
	{
		ComboManager->ResetComboState();
	}
}