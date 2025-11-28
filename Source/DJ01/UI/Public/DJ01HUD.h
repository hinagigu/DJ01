// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/HUD.h"
#include "DJ01HUD.generated.h"

class UCommonActivatableWidget;
class UDJ01ActivatableWidgetContainerBase;

/**
 * DJ01 HUD类
 * 
 * 游戏的主HUD类，负责：
 * - 管理UI布局层
 * - 提供UI扩展点
 * - 处理GameFeature添加的UI元素
 * 
 * 使用方式：
 * 1. 在GameMode中设置此类为HUD类
 * 2. GameFeatureAction_AddWidgets会向此HUD添加UI
 */
UCLASS()
class DJ01_API ADJ01HUD : public AHUD
{
	GENERATED_BODY()

public:
	ADJ01HUD(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

protected:
	//~ Begin AActor interface
	virtual void BeginPlay() override;
	virtual void EndPlay(const EEndPlayReason::Type EndPlayReason) override;
	//~ End AActor interface

	//~ Begin AHUD interface
	virtual void GetDebugActorList(TArray<AActor*>& InOutList) override;
	//~ End AHUD interface

private:
	/** 创建UI布局 */
	void CreateLayout();

	/** 主UI布局Widget */
	UPROPERTY(Transient)
	TObjectPtr<UUserWidget> LayoutWidget;
};