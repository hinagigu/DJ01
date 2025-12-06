#include "DJ01InputBuffer.h"
#include "DJ01/System/Public/DJ01GameplayTags.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01InputBuffer)

UDJ01InputBuffer::UDJ01InputBuffer()
{
    PrimaryComponentTick.bCanEverTick = false;
}

void UDJ01InputBuffer::BufferInput(FGameplayTag AbilityTag, float BufferDuration)
{
    CleanupExpiredInputs();
    
    FBufferedInput NewInput;
    NewInput.AbilityTag = AbilityTag;
    NewInput.InputTime = GetWorld()->GetTimeSeconds();
    NewInput.BufferDuration = BufferDuration > 0.f ? BufferDuration : DefaultBufferDuration;
    
    BufferedInputs.Add(NewInput);
}

bool UDJ01InputBuffer::ConsumeBufferedInput(FGameplayTag& OutAbilityTag)
{
    CleanupExpiredInputs();
    
    if (BufferedInputs.Num() == 0)
    {
        return false;
    }
    
    // 按优先级排序，取最高优先级
    BufferedInputs.Sort([this](const FBufferedInput& A, const FBufferedInput& B)
    {
        return GetPriority(A.AbilityTag) < GetPriority(B.AbilityTag);
    });
    
    OutAbilityTag = BufferedInputs[0].AbilityTag;
    BufferedInputs.RemoveAt(0);
    return true;
}

bool UDJ01InputBuffer::HasBufferedInput(FGameplayTag AbilityTag) const
{
    float CurrentTime = GetWorld()->GetTimeSeconds();
    for (const FBufferedInput& Input : BufferedInputs)
    {
        if (Input.IsValid(CurrentTime) && Input.AbilityTag.MatchesTag(AbilityTag))
        {
            return true;
        }
    }
    return false;
}

void UDJ01InputBuffer::ClearBuffer()
{
    BufferedInputs.Empty();
}

void UDJ01InputBuffer::CleanupExpiredInputs()
{
    float CurrentTime = GetWorld()->GetTimeSeconds();
    BufferedInputs.RemoveAll([CurrentTime](const FBufferedInput& Input)
    {
        return !Input.IsValid(CurrentTime);
    });
}

int32 UDJ01InputBuffer::GetPriority(FGameplayTag AbilityTag) const
{
    // 重攻击优先级高于轻攻击
    if (AbilityTag.MatchesTagExact(DJ01GameplayTags::Ability_Attack_Heavy))
    {
        return 10;
    }
    if (AbilityTag.MatchesTagExact(DJ01GameplayTags::Ability_Attack_Light))
    {
        return 20;
    }
    return 100;
}