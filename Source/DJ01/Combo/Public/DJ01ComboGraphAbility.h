// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "DJ01/AbilitySystem/Abilities/Public/DJ01GameplayAbility.h"
#include "DJ01ComboGraphAbility.generated.h"

class UComboGraph;
class UInputAction;
class UComboGraphAbilityTask_StartGraph;
class UComboGraphNodeAnimBase;

/**
 * UDJ01ComboGraphAbility
 * 
 * 连招技能中间层
 * - 继承自 UDJ01GameplayAbility，保留项目技能系统的所有特性
 * - 封装 ComboGraph 插件的使用，提供简洁的接口
 * 
 * 使用方式：
 * 1. 创建蓝图子类
 * 2. 设置 ComboGraph 资产
 * 3. 像普通 GA 一样授予和触发
 */
UCLASS(Abstract, Meta = (ShortTooltip = "Base class for combo abilities using ComboGraph"))
class DJ01_API UDJ01ComboGraphAbility : public UDJ01GameplayAbility
{
    GENERATED_BODY()

public:
    UDJ01ComboGraphAbility(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

    //~============================================================================
    // 运行时查询
    //~============================================================================
    
    /** 获取当前正在执行的节点 */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "DJ01|ComboGraph")
    UComboGraphNodeAnimBase* GetCurrentComboNode() const;

    /** 获取上一个执行的节点 */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "DJ01|ComboGraph")
    UComboGraphNodeAnimBase* GetPreviousComboNode() const;

    /** ComboGraph 是否正在运行 */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "DJ01|ComboGraph")
    bool IsComboGraphRunning() const;

protected:
    //~UGameplayAbility interface
    virtual void ActivateAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilityActivationInfo ActivationInfo, const FGameplayEventData* TriggerEventData) override;
    virtual void EndAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilityActivationInfo ActivationInfo, bool bReplicateEndAbility, bool bWasCancelled) override;
    //~End of UGameplayAbility interface

    //~============================================================================
    // 蓝图可覆写事件
    //~============================================================================

    /** 当 ComboGraph 开始执行时调用 */
    UFUNCTION(BlueprintImplementableEvent, Category = "DJ01|ComboGraph", DisplayName = "OnComboGraphStarted")
    void K2_OnComboGraphStarted();

    /** 当 ComboGraph 结束时调用 */
    UFUNCTION(BlueprintImplementableEvent, Category = "DJ01|ComboGraph", DisplayName = "OnComboGraphEnded")
    void K2_OnComboGraphEnded(bool bWasCancelled);

    /** 当节点切换时调用 */
    UFUNCTION(BlueprintImplementableEvent, Category = "DJ01|ComboGraph", DisplayName = "OnComboNodeChanged")
    void K2_OnComboNodeChanged(UComboGraphNodeAnimBase* PreviousNode, UComboGraphNodeAnimBase* NewNode);

    /** 当接收到 Gameplay Event 时调用 */
    UFUNCTION(BlueprintImplementableEvent, Category = "DJ01|ComboGraph", DisplayName = "OnComboEventReceived")
    void K2_OnComboEventReceived(FGameplayTag EventTag, FGameplayEventData EventData);

    //~============================================================================
    // Native 可覆写方法（供 C++ 子类使用）
    //~============================================================================

    /** Native: ComboGraph 开始 */
    virtual void OnComboGraphStarted();
    
    /** Native: ComboGraph 结束 */
    virtual void OnComboGraphEnded(bool bWasCancelled);
    
    /** Native: 节点切换 */
    virtual void OnComboNodeChanged(UComboGraphNodeAnimBase* PreviousNode, UComboGraphNodeAnimBase* NewNode);

protected:
    //~============================================================================
    // 配置属性
    //~============================================================================

    /** 要运行的 ComboGraph 资产 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DJ01|ComboGraph")
    TObjectPtr<UComboGraph> ComboGraph;

    /** 
     * 初始输入 Action（用于 Conduit 节点分支）
     * 如果 ComboGraph 使用 Conduit 入口节点，需要设置此项
     */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DJ01|ComboGraph")
    TObjectPtr<UInputAction> InitialInputAction;

    /** 是否广播内部事件（如 ComboWindow 开关、状态切换） */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DJ01|ComboGraph|Advanced")
    bool bBroadcastInternalEvents = false;

    /** ComboGraph 结束时是否自动结束技能 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DJ01|ComboGraph|Advanced")
    bool bEndAbilityOnGraphEnd = true;

private:
    UFUNCTION()
    void HandleGraphStart(FGameplayTag EventTag, FGameplayEventData EventData);

    UFUNCTION()
    void HandleGraphEnd(FGameplayTag EventTag, FGameplayEventData EventData);

    UFUNCTION()
    void HandleEventReceived(FGameplayTag EventTag, FGameplayEventData EventData);

private:
    UPROPERTY()
    TObjectPtr<UComboGraphAbilityTask_StartGraph> ComboTask;

    UPROPERTY()
    TObjectPtr<UComboGraphNodeAnimBase> CachedPreviousNode;
};