// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01.h"
#include "Modules/ModuleManager.h"

class FDJ01GameModule : public FDefaultGameModuleImpl
{
public:
    virtual void StartupModule() override
    {
        FDefaultGameModuleImpl::StartupModule();
		
        // 确保 GameplayTags 模块已加载
        FModuleManager::LoadModuleChecked<IModuleInterface>("GameplayTags");
    }
};

IMPLEMENT_PRIMARY_GAME_MODULE( FDJ01GameModule, DJ01, "DJ01" );
