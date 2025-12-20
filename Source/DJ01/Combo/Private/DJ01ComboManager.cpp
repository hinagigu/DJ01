// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Combo/Public/DJ01ComboManager.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"
#include "DJ01/System/Public/DJ01GameplayTags.h"
#include "AbilitySystemBlueprintLibrary.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01ComboManager)

UDJ01ComboManager::UDJ01ComboManager()
{
    PrimaryComponentTick.bCanEverTick = false;
}

void UDJ01ComboManager::BeginPlay()
{
    Super::BeginPlay();
    
    // 预缓存 ASC
    GetASC();
}

//========================================
// 输入缓冲
//========================================

void UDJ01ComboManager::BufferInput(FGameplayTag AbilityTag, int32 Priority)
{
    InputBuffer.BufferInput(AbilityTag, Priority, GetCurrentTime(), CurrentComboIndex);
}

bool UDJ01ComboManager::TryActivateOrBuffer(FGameplayTag AbilityTag, int32 Priority)
{
    // 如果没有连招进行中，尝试直接激活
    if (!bComboWindowOpen && CurrentComboIndex == 0)
    {
        if (TryActivateAbilityByTag(AbilityTag))
        {
            return true;
        }
    }
    
    // 否则缓冲输入
    BufferInput(AbilityTag, Priority);
    return false;
}

bool UDJ01ComboManager::HasBufferedInput() const
{
    return InputBuffer.HasAnyInput(GetCurrentTime());
}

void UDJ01ComboManager::ClearInputBuffer()
{
    InputBuffer.Clear();
}

//========================================
// 连招窗口控制
//========================================

void UDJ01ComboManager::OpenComboWindow(FGameplayTag ComboChainTag)
{
    bComboWindowOpen = true;
	
    if (ComboChainTag.IsValid())
    {
        CurrentComboChainTag = ComboChainTag;
        // 同步连招链 Tag
        SyncComboChainTag(ComboChainTag);
    }
	
    // 同步连招窗口 Tag 到 ASC
    SyncComboWindowTag(true);
	
    OnComboWindowStateChanged.Broadcast(true);
}

bool UDJ01ComboManager::CloseComboWindowAndConsume()
{
    bComboWindowOpen = false;
	
    // 同步 Tag 到 ASC
    SyncComboWindowTag(false);
	
    OnComboWindowStateChanged.Broadcast(false);
	
    // 尝试消费缓冲输入
    FDJ01ComboBufferedInput ConsumedInput;
    if (InputBuffer.ConsumeAndClear(GetCurrentTime(), ConsumedInput))
    {
        // 推进连招
        AdvanceComboIndex();
		
        // 激活下一个技能
        if (TryActivateAbilityByTag(ConsumedInput.AbilityTag))
        {
            OnComboAdvanced.Broadcast(CurrentComboIndex, ConsumedInput.AbilityTag);
            return true;
        }
    }
	
    return false;
}

void UDJ01ComboManager::CloseComboWindow()
{
    bComboWindowOpen = false;
	
    // 同步 Tag 到 ASC
    SyncComboWindowTag(false);
	
    OnComboWindowStateChanged.Broadcast(false);
}

//========================================
// 连招状态
//========================================

void UDJ01ComboManager::AdvanceComboIndex()
{
    CurrentComboIndex++;
}

void UDJ01ComboManager::ResetComboState()
{
    bComboWindowOpen = false;
    CurrentComboIndex = 0;
    InputBuffer.Clear();
	
    // 清除所有连招相关 Tag
    SyncComboWindowTag(false);
    SyncComboChainTag(FGameplayTag()); // 传空 Tag 会清除所有 Chain Tag
	
    CurrentComboChainTag = FGameplayTag();
}

//========================================
// 自动衔接
//========================================

void UDJ01ComboManager::RequestAutoChain(FGameplayTag NextAbilityTag)
{
    if (!NextAbilityTag.IsValid())
    {
        return;
    }
    
    AdvanceComboIndex();
    
    if (TryActivateAbilityByTag(NextAbilityTag))
    {
        OnComboAdvanced.Broadcast(CurrentComboIndex, NextAbilityTag);
    }
}

//========================================
// 内部方法
//========================================

UDJ01AbilitySystemComponent* UDJ01ComboManager::GetASC()
{
    if (!CachedASC.IsValid())
    {
        if (AActor* Owner = GetOwner())
        {
            // 尝试从 Owner 获取 ASC
            CachedASC = Owner->FindComponentByClass<UDJ01AbilitySystemComponent>();
        }
    }
    
    return CachedASC.Get();
}

float UDJ01ComboManager::GetCurrentTime() const
{
    if (const UWorld* World = GetWorld())
    {
        return World->GetTimeSeconds();
    }
    return 0.f;
}

bool UDJ01ComboManager::TryActivateAbilityByTag(FGameplayTag AbilityTag)
{
    if (UDJ01AbilitySystemComponent* ASC = GetASC())
    {
        // 使用 GameplayTag 激活技能
        FGameplayTagContainer TagContainer;
        TagContainer.AddTag(AbilityTag);
		
        return ASC->TryActivateAbilitiesByTag(TagContainer);
    }
	
    return false;
}

void UDJ01ComboManager::SyncComboWindowTag(bool bOpen)
{
    UDJ01AbilitySystemComponent* ASC = GetASC();
    if (!ASC)
    {
        return;
    }
	
    if (bOpen)
    {
        // 添加连招窗口 Tag
        ASC->AddLooseGameplayTag(DJ01GameplayTags::State_Combo_WindowOpen);
    }
    else
    {
        // 移除连招窗口 Tag
        ASC->RemoveLooseGameplayTag(DJ01GameplayTags::State_Combo_WindowOpen);
    }
}

void UDJ01ComboManager::SyncComboChainTag(FGameplayTag NewChainTag)
{
    UDJ01AbilitySystemComponent* ASC = GetASC();
    if (!ASC)
    {
        return;
    }
	
    // 先移除所有可能的连招链 Tag
    ASC->RemoveLooseGameplayTag(DJ01GameplayTags::State_Combo_Chain_Light);
    ASC->RemoveLooseGameplayTag(DJ01GameplayTags::State_Combo_Chain_Heavy);
    ASC->RemoveLooseGameplayTag(DJ01GameplayTags::State_Combo_Chain_Special);
	
    // 添加新的连招链 Tag
    if (NewChainTag.IsValid())
    {
        ASC->AddLooseGameplayTag(NewChainTag);
    }
}