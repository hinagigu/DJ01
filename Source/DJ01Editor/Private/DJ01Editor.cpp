// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01Editor.h"

#define LOCTEXT_NAMESPACE "FDJ01EditorModule"

void FDJ01EditorModule::StartupModule()
{
	// 模块启动时的初始化
	UE_LOG(LogTemp, Log, TEXT("DJ01Editor Module Started"));
}

void FDJ01EditorModule::ShutdownModule()
{
	// 模块关闭时的清理
}

#undef LOCTEXT_NAMESPACE
	
IMPLEMENT_MODULE(FDJ01EditorModule, DJ01Editor)