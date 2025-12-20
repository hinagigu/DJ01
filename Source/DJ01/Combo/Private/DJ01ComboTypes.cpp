// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Combo/Public/DJ01ComboTypes.h"

//========================================
// FDJ01ComboInputBuffer
//========================================

FDJ01ComboInputBuffer::FDJ01ComboInputBuffer()
{
    // 延迟初始化，在首次使用时进行
}

void FDJ01ComboInputBuffer::EnsureInitialized()
{
    if (RingBuffer.Num() != Capacity)
    {
        RingBuffer.SetNum(Capacity);
        WriteIndex = 0;
        
        for (FDJ01ComboBufferedInput& Slot : RingBuffer)
        {
            Slot.Invalidate();
        }
    }
}

void FDJ01ComboInputBuffer::BufferInput(FGameplayTag AbilityTag, int32 Priority, float CurrentTime, int32 CurrentComboIndex)
{
    if (!AbilityTag.IsValid())
    {
        return;
    }
    
    EnsureInitialized();
    
    // 写入当前位置
    FDJ01ComboBufferedInput& Slot = RingBuffer[WriteIndex];
    Slot.AbilityTag = AbilityTag;
    Slot.Priority = Priority;
    Slot.InputTime = CurrentTime;
    Slot.BufferDuration = DefaultBufferDuration;
    Slot.ComboIndex = CurrentComboIndex;
    
    // 移动写入指针
    WriteIndex = (WriteIndex + 1) % RingBuffer.Num();
}

bool FDJ01ComboInputBuffer::ConsumeAndClear(float CurrentTime, FDJ01ComboBufferedInput& OutInput)
{
    const int32 BestIndex = FindBestInputIndex(CurrentTime);
    
    if (BestIndex != INDEX_NONE)
    {
        OutInput = RingBuffer[BestIndex];
        Clear(); // 消费后清空
        return true;
    }
    
    return false;
}

bool FDJ01ComboInputBuffer::ConsumeWithTag(float CurrentTime, const FGameplayTag& TagFilter, FDJ01ComboBufferedInput& OutInput)
{
    const int32 BestIndex = FindBestInputIndexWithPredicate(CurrentTime, 
        [&TagFilter](const FDJ01ComboBufferedInput& Input)
        {
            return Input.AbilityTag.MatchesTag(TagFilter);
        });
    
    if (BestIndex != INDEX_NONE)
    {
        OutInput = RingBuffer[BestIndex];
        Clear();
        return true;
    }
    
    return false;
}

bool FDJ01ComboInputBuffer::Peek(float CurrentTime, FDJ01ComboBufferedInput& OutInput) const
{
    const int32 BestIndex = FindBestInputIndex(CurrentTime);
    
    if (BestIndex != INDEX_NONE)
    {
        OutInput = RingBuffer[BestIndex];
        return true;
    }
    
    return false;
}

bool FDJ01ComboInputBuffer::HasAnyInput(float CurrentTime) const
{
    for (const FDJ01ComboBufferedInput& Input : RingBuffer)
    {
        if (Input.IsValid(CurrentTime))
        {
            return true;
        }
    }
    return false;
}

void FDJ01ComboInputBuffer::Clear()
{
    for (FDJ01ComboBufferedInput& Input : RingBuffer)
    {
        Input.Invalidate();
    }
    WriteIndex = 0;
}

int32 FDJ01ComboInputBuffer::FindBestInputIndex(float CurrentTime) const
{
    return FindBestInputIndexWithPredicate(CurrentTime, [](const FDJ01ComboBufferedInput&) { return true; });
}