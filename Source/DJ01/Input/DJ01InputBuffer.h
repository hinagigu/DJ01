#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "GameplayTagContainer.h"
#include "DJ01InputBuffer.generated.h"

/** 缓冲的输入条目 */
USTRUCT(BlueprintType)
struct FBufferedInput
{
    GENERATED_BODY()
    
    /** 输入对应的技能Tag */
    UPROPERTY()
    FGameplayTag AbilityTag;
    
    /** 输入时间戳 */
    UPROPERTY()
    float InputTime = 0.f;
    
    /** 缓冲有效期 (秒) */
    UPROPERTY()
    float BufferDuration = 0.2f;
    
    bool IsValid(float CurrentTime) const
    {
        return (CurrentTime - InputTime) < BufferDuration;
    }
};

/**
 * UDJ01InputBuffer
 * 
 * 输入缓冲组件 - 用于连招系统的预输入
 * 添加到角色身上，缓存玩家在攻击动画中的输入
 */
UCLASS(BlueprintType, meta = (BlueprintSpawnableComponent))
class DJ01_API UDJ01InputBuffer : public UActorComponent
{
    GENERATED_BODY()

public:
    UDJ01InputBuffer();

    /** 添加缓冲输入 */
    UFUNCTION(BlueprintCallable, Category = "Input Buffer")
    void BufferInput(FGameplayTag AbilityTag, float BufferDuration = 0.2f);
    
    /** 消费缓冲输入 (返回最高优先级的有效输入) */
    UFUNCTION(BlueprintCallable, Category = "Input Buffer")
    bool ConsumeBufferedInput(FGameplayTag& OutAbilityTag);
    
    /** 检查是否有特定类型的缓冲输入 */
    UFUNCTION(BlueprintCallable, Category = "Input Buffer")
    bool HasBufferedInput(FGameplayTag AbilityTag) const;
    
    /** 清空所有缓冲 */
    UFUNCTION(BlueprintCallable, Category = "Input Buffer")
    void ClearBuffer();

    /** 默认缓冲有效期 */
    UPROPERTY(EditDefaultsOnly, Category = "Input Buffer")
    float DefaultBufferDuration = 0.2f;

private:
    UPROPERTY()
    TArray<FBufferedInput> BufferedInputs;
    
    void CleanupExpiredInputs();
    int32 GetPriority(FGameplayTag AbilityTag) const;
};