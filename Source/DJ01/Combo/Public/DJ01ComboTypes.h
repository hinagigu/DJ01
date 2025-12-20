// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "GameplayTagContainer.h"
#include "DJ01ComboTypes.generated.h"

/**
 * FDJ01ComboBufferedInput
 * 
 * 缓冲的输入条目 - 用于连招系统
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01ComboBufferedInput
{
    GENERATED_BODY()
    
    FDJ01ComboBufferedInput() = default;
    
    FDJ01ComboBufferedInput(FGameplayTag InAbilityTag, int32 InPriority, float InInputTime, float InBufferDuration)
        : AbilityTag(InAbilityTag)
        , Priority(InPriority)
        , InputTime(InInputTime)
        , BufferDuration(InBufferDuration)
    {
    }
    
    /** 请求激活的技能Tag */
    UPROPERTY(BlueprintReadOnly, Category = "Combo")
    FGameplayTag AbilityTag;
    
    /** 技能优先级 (数值越小优先级越高) */
    UPROPERTY(BlueprintReadOnly, Category = "Combo")
    int32 Priority = 100;
    
    /** 输入时间戳 */
    UPROPERTY(BlueprintReadOnly, Category = "Combo")
    float InputTime = 0.f;
    
    /** 缓冲有效期 (秒) */
    UPROPERTY(BlueprintReadOnly, Category = "Combo")
    float BufferDuration = 0.3f;
    
    /** 当前连段索引 */
    UPROPERTY(BlueprintReadOnly, Category = "Combo")
    int32 ComboIndex = 0;
    
    /** 输入方向 (用于方向技) */
    UPROPERTY(BlueprintReadOnly, Category = "Combo")
    FVector2D InputDirection = FVector2D::ZeroVector;
    
    /** 检查此缓冲是否仍然有效 */
    bool IsValid(float CurrentTime) const
    {
        return AbilityTag.IsValid() && (CurrentTime - InputTime) < BufferDuration;
    }
    
    /** 检查是否为空槽位 */
    bool IsEmpty() const
    {
        return !AbilityTag.IsValid();
    }
    
    /** 重置为无效状态 */
    void Invalidate()
    {
        AbilityTag = FGameplayTag();
        Priority = 100;
        ComboIndex = 0;
    }
};

/**
 * FDJ01ComboInputBuffer
 * 
 * 环形输入缓冲 - 用于连招系统
 * 作为 ComboManager 的成员使用，非独立组件
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01ComboInputBuffer
{
    GENERATED_BODY()
    
    FDJ01ComboInputBuffer();
    
    //========================================
    // 缓冲操作
    //========================================
    
    /** 添加缓冲输入 */
    void BufferInput(FGameplayTag AbilityTag, int32 Priority, float CurrentTime, int32 CurrentComboIndex = 0);
    
    /** 
     * 消费最高优先级的有效输入并清空缓冲
     * @param CurrentTime 当前时间
     * @param OutInput 输出消费的输入
     * @return 是否成功消费
     */
    bool ConsumeAndClear(float CurrentTime, FDJ01ComboBufferedInput& OutInput);
    
    /** 
     * 消费满足 Tag 过滤的输入
     * @param CurrentTime 当前时间
     * @param TagFilter 只消费匹配此 Tag 的输入
     * @param OutInput 输出消费的输入
     * @return 是否成功消费
     */
    bool ConsumeWithTag(float CurrentTime, const FGameplayTag& TagFilter, FDJ01ComboBufferedInput& OutInput);
    
    /** 查看但不消费 */
    bool Peek(float CurrentTime, FDJ01ComboBufferedInput& OutInput) const;
    
    /** 检查是否有任何有效缓冲 */
    bool HasAnyInput(float CurrentTime) const;
    
    /** 清空所有缓冲 */
    void Clear();
    
    //========================================
    // 配置
    //========================================
    
    /** 默认缓冲有效期 (秒) */
    UPROPERTY(EditDefaultsOnly, BlueprintReadWrite, Category = "Combo")
    float DefaultBufferDuration = 0.3f;
    
    /** 环形缓冲容量 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Combo", meta = (ClampMin = "1", ClampMax = "16"))
    int32 Capacity = 8;
    
private:
    /** 环形缓冲数组 */
    UPROPERTY()
    TArray<FDJ01ComboBufferedInput> RingBuffer;
    
    /** 下一个写入位置 */
    int32 WriteIndex = 0;
    
    /** 初始化环形缓冲 */
    void EnsureInitialized();
    
    /** 查找最高优先级的有效输入，返回索引 */
    int32 FindBestInputIndex(float CurrentTime) const;
    
    /** 查找满足条件的最高优先级输入 */
    template<typename Predicate>
    int32 FindBestInputIndexWithPredicate(float CurrentTime, Predicate Pred) const;
};

//========================================
// 模板实现
//========================================

template<typename Predicate>
int32 FDJ01ComboInputBuffer::FindBestInputIndexWithPredicate(float CurrentTime, Predicate Pred) const
{
    int32 BestIndex = INDEX_NONE;
    int32 BestPriority = INT_MAX;
    
    for (int32 i = 0; i < RingBuffer.Num(); ++i)
    {
        const FDJ01ComboBufferedInput& Input = RingBuffer[i];
        
        if (Input.IsValid(CurrentTime) && Pred(Input))
        {
            if (Input.Priority < BestPriority)
            {
                BestPriority = Input.Priority;
                BestIndex = i;
            }
        }
    }
    
    return BestIndex;
}