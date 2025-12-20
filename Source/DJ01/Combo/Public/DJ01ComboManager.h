// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "GameplayTagContainer.h"
#include "DJ01/Combo/Public/DJ01ComboTypes.h"
#include "DJ01ComboManager.generated.h"

class UDJ01AbilitySystemComponent;

/**
 * 连招窗口状态变化委托
 */
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnComboWindowStateChanged, bool, bIsOpen);

/**
 * 连招推进委托
 */
DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(FOnComboAdvanced, int32, NewComboIndex, FGameplayTag, AbilityTag);

/**
 * UDJ01ComboManager
 * 
 * 连招管理器 - 协调输入缓冲、GAS、动画系统
 * 
 * 职责：
 * - 管理输入缓冲
 * - 控制连招窗口（是否可接受输入）
 * - 追踪当前连招状态
 * - 与 ASC 协调技能激活
 */
UCLASS(BlueprintType, meta = (BlueprintSpawnableComponent))
class DJ01_API UDJ01ComboManager : public UActorComponent
{
    GENERATED_BODY()

public:
    UDJ01ComboManager();
    
    virtual void BeginPlay() override;

    //========================================
    // 输入缓冲
    //========================================
    
    /**
     * 缓冲输入
     * 由输入系统调用（EnhancedInput / AngelScript）
     * 
     * @param AbilityTag 技能标签
     * @param Priority 优先级（越小越高）
     */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Combo")
    void BufferInput(FGameplayTag AbilityTag, int32 Priority = 50);
    
    /**
     * 尝试立即激活或缓冲输入
     * 如果当前无技能执行，立即激活；否则缓冲
     * 
     * @param AbilityTag 技能标签
     * @param Priority 优先级
     * @return 是否立即激活成功
     */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Combo")
    bool TryActivateOrBuffer(FGameplayTag AbilityTag, int32 Priority = 50);
    
    /** 检查是否有缓冲输入 */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "DJ01|Combo")
    bool HasBufferedInput() const;
    
    /** 清空输入缓冲 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Combo")
    void ClearInputBuffer();

    //========================================
    // 连招窗口控制（由 AnimNotify 调用）
    //========================================
    
    /**
     * 打开连招窗口
     * 由 AnimNotify 调用，标记可以接受下一段输入
     * 
     * @param ComboChainTag 当前连招链标识（可选）
     */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Combo")
    void OpenComboWindow(FGameplayTag ComboChainTag = FGameplayTag());
    
    /**
     * 关闭连招窗口并尝试消费输入
     * 由 AnimNotify 调用
     * 
     * @return 是否成功消费输入并激活下一段
     */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Combo")
    bool CloseComboWindowAndConsume();
    
    /**
     * 仅关闭连招窗口（不消费输入）
     */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Combo")
    void CloseComboWindow();
    
    /** 连招窗口是否打开 */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "DJ01|Combo")
    bool IsComboWindowOpen() const { return bComboWindowOpen; }

    //========================================
    // 连招状态
    //========================================
    
    /** 获取当前连招索引 */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "DJ01|Combo")
    int32 GetCurrentComboIndex() const { return CurrentComboIndex; }
    
    /** 获取当前连招链 Tag */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "DJ01|Combo")
    FGameplayTag GetCurrentComboChainTag() const { return CurrentComboChainTag; }
    
    /** 推进连招索引 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Combo")
    void AdvanceComboIndex();
    
    /** 重置连招状态 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Combo")
    void ResetComboState();
    
    //========================================
    // 自动衔接（由 AnimNotify 调用）
    //========================================
    
    /**
     * 请求自动衔接下一段
     * 无需玩家输入，自动触发下一个技能
     * 
     * @param NextAbilityTag 下一个技能的 Tag
     */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Combo")
    void RequestAutoChain(FGameplayTag NextAbilityTag);

    //========================================
    // 事件委托
    //========================================
    
    /** 连招窗口状态变化 */
    UPROPERTY(BlueprintAssignable, Category = "DJ01|Combo")
    FOnComboWindowStateChanged OnComboWindowStateChanged;
    
    /** 连招推进 */
    UPROPERTY(BlueprintAssignable, Category = "DJ01|Combo")
    FOnComboAdvanced OnComboAdvanced;

    //========================================
    // 配置
    //========================================
	
    /** 输入缓冲配置 */
    UPROPERTY(EditDefaultsOnly, Category = "DJ01|Combo")
    FDJ01ComboInputBuffer InputBuffer;

protected:
	
    /** 获取 ASC（缓存） */
    UDJ01AbilitySystemComponent* GetASC();
	
    /** 同步连招窗口 Tag 到 ASC (State.Combo.WindowOpen) */
    void SyncComboWindowTag(bool bOpen);
    
    /** 同步连招链 Tag 到 ASC (State.Combo.Chain.*) */
    void SyncComboChainTag(FGameplayTag NewChainTag);
    
    /** 获取当前时间 */
    float GetCurrentTime() const;
    
    /** 尝试通过 Tag 激活技能 */
    bool TryActivateAbilityByTag(FGameplayTag AbilityTag);

private:
    
    /** 缓存的 ASC 引用 */
    UPROPERTY()
    TWeakObjectPtr<UDJ01AbilitySystemComponent> CachedASC;
    
    /** 连招窗口是否打开 */
    bool bComboWindowOpen = false;
    
    /** 当前连招链标识 */
    FGameplayTag CurrentComboChainTag;
    
    /** 当前连招索引 (0-based) */
    int32 CurrentComboIndex = 0;
};