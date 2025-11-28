// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/UI/Public/DJ01HUD.h"
#include "Components/GameFrameworkComponentManager.h"
#include "Blueprint/UserWidget.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01HUD)

ADJ01HUD::ADJ01HUD(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
	PrimaryActorTick.bStartWithTickEnabled = false;
}

void ADJ01HUD::BeginPlay()
{
	Super::BeginPlay();

	// 通知GameFrameworkComponentManager此HUD已准备好
	UGameFrameworkComponentManager::AddGameFrameworkComponentReceiver(this);

	// 创建UI布局
	CreateLayout();

	UE_LOG(LogTemp, Log, TEXT("[ADJ01HUD::BeginPlay] HUD已初始化"));
}

void ADJ01HUD::EndPlay(const EEndPlayReason::Type EndPlayReason)
{
	UGameFrameworkComponentManager::RemoveGameFrameworkComponentReceiver(this);
	
	Super::EndPlay(EndPlayReason);
}

void ADJ01HUD::GetDebugActorList(TArray<AActor*>& InOutList)
{
	Super::GetDebugActorList(InOutList);
}

void ADJ01HUD::CreateLayout()
{
	// 这里可以创建主UI布局
	// 例如加载一个包含所有UI层的Widget
	
	if (APlayerController* PC = GetOwningPlayerController())
	{
		// 示例：创建UI根容器
		// LayoutWidget = CreateWidget<UUserWidget>(PC, LayoutWidgetClass);
		// if (LayoutWidget)
		// {
		//     LayoutWidget->AddToViewport();
		// }
	}

	UE_LOG(LogTemp, Log, TEXT("[ADJ01HUD::CreateLayout] UI布局已创建"));
}