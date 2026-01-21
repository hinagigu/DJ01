// ============================================================
// DJ01AbilityPhaseStateMachine.h
// 技能阶段状态机 - 独立组件
// ============================================================

#pragma once

#include "CoreMinimal.h"
#include "UObject/NoExportTypes.h"
#include "DJ01AbilityPhase.h"

#include "DJ01AbilityPhaseStateMachine.generated.h"

class UDJ01GameplayAbility;
class UAbilitySystemComponent;

// ============================================================
// 状态机委托
// ============================================================

/** 阶段变化委托 */
DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(FOnAbilityPhaseChanged, EDJ01AbilityPhase, OldPhase, EDJ01AbilityPhase, NewPhase);

/** 阶段进入委托 */
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnAbilityPhaseEnter, EDJ01AbilityPhase, Phase);

/** 阶段退出委托 */
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnAbilityPhaseExit, EDJ01AbilityPhase, Phase);

/** 状态机结束委托 */
DECLARE_DYNAMIC_MULTICAST_DELEGATE(FOnPhaseStateMachineFinished);

// ============================================================
// UDJ01AbilityPhaseStateMachine
// ============================================================

/**
 * 技能阶段状态机
 * 
 * 独立于技能类的状态机实现，负责管理技能的执行阶段。
 * 技能类持有状态机实例，通过委托接收阶段变化通知。
 * 
 * 使用方式：
 * 1. 技能激活时调用 Initialize()
 * 2. 状态机自动按配置推进阶段
 * 3. 技能可以手动调用 TransitionToPhase() 控制阶段
 * 4. 技能结束时调用 Shutdown()
 */
UCLASS(BlueprintType, Blueprintable)
class DJ01_API UDJ01AbilityPhaseStateMachine : public UObject
{
    GENERATED_BODY()

public:
    UDJ01AbilityPhaseStateMachine();

    // ========== 生命周期 ==========

    /**
     * 初始化状态机
     * @param InOwnerAbility - 拥有此状态机的技能
     * @param InConfig - 阶段配置
     */
    UFUNCTION(BlueprintCallable, Category = "Phase")
    void Initialize(UDJ01GameplayAbility* InOwnerAbility, const FDJ01AbilityPhaseConfig& InConfig);

    /**
     * 启动状态机（进入第一个阶段）
     */
    UFUNCTION(BlueprintCallable, Category = "Phase")
    void Start();

    /**
     * 关闭状态机（清理资源）
     */
    UFUNCTION(BlueprintCallable, Category = "Phase")
    void Shutdown();

    /**
     * 状态机是否正在运行
     */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Phase")
    bool IsRunning() const { return bIsRunning; }

    // ========== 阶段控制 ==========

    /**
     * 切换到指定阶段
     * @param NewPhase - 目标阶段
     * @param bForce - 是否强制转换（忽略验证）
     * @return 是否成功切换
     */
    UFUNCTION(BlueprintCallable, Category = "Phase")
    bool TransitionToPhase(EDJ01AbilityPhase NewPhase, bool bForce = false);

    /**
     * 获取当前阶段
     */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Phase")
    EDJ01AbilityPhase GetCurrentPhase() const { return CurrentPhase; }

    /**
     * 获取上一个阶段
     */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Phase")
    EDJ01AbilityPhase GetPreviousPhase() const { return PreviousPhase; }

    /**
     * 当前阶段是否可被打断
     */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Phase")
    bool CanCurrentPhaseBeInterrupted() const;

    /**
     * 当前阶段是否可取消到其他技能
     */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Phase")
    bool CanCurrentPhaseCancelInto() const;

    /**
     * 获取当前阶段剩余时间
     */
    UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Phase")
    float GetCurrentPhaseRemainingTime() const;

    /**
     * 跳过当前阶段（立即进入下一阶段）
     */
    UFUNCTION(BlueprintCallable, Category = "Phase")
    void SkipCurrentPhase();

    // ========== 委托 ==========

    /** 阶段变化时触发 */
    UPROPERTY(BlueprintAssignable, Category = "Phase|Events")
    FOnAbilityPhaseChanged OnPhaseChanged;

    /** 进入阶段时触发 */
    UPROPERTY(BlueprintAssignable, Category = "Phase|Events")
    FOnAbilityPhaseEnter OnPhaseEnter;

    /** 退出阶段时触发 */
    UPROPERTY(BlueprintAssignable, Category = "Phase|Events")
    FOnAbilityPhaseExit OnPhaseExit;

    /** 状态机运行结束时触发 */
    UPROPERTY(BlueprintAssignable, Category = "Phase|Events")
    FOnPhaseStateMachineFinished OnFinished;

protected:
    // ========== 内部方法 ==========

    /** 处理阶段进入 */
    virtual void HandlePhaseEnter(EDJ01AbilityPhase Phase);

    /** 处理阶段退出 */
    virtual void HandlePhaseExit(EDJ01AbilityPhase Phase);

    /** 阶段计时器到期 */
    UFUNCTION()
    void OnPhaseTimerExpired();

    /** 清理计时器 */
    void ClearPhaseTimer();

    /** 获取下一个自动阶段 */
    EDJ01AbilityPhase GetNextAutoPhase() const;

    /** 应用阶段 Tag */
    void ApplyPhaseTags(EDJ01AbilityPhase Phase, bool bAdd);

    /** 获取 World */
    UWorld* GetWorld() const;

    /** 验证转换是否有效（公开给技能类使用） */
    bool IsTransitionValid(EDJ01AbilityPhase From, EDJ01AbilityPhase To) const;

protected:
    // ========== 状态 ==========

    /** 当前阶段 */
    UPROPERTY(BlueprintReadOnly, Category = "Phase")
    EDJ01AbilityPhase CurrentPhase = EDJ01AbilityPhase::None;

    /** 上一个阶段 */
    UPROPERTY(BlueprintReadOnly, Category = "Phase")
    EDJ01AbilityPhase PreviousPhase = EDJ01AbilityPhase::None;

    /** 阶段配置 */
    UPROPERTY(BlueprintReadOnly, Category = "Phase")
    FDJ01AbilityPhaseConfig Config;

    /** 拥有者技能 */
    UPROPERTY()
    TWeakObjectPtr<UDJ01GameplayAbility> OwnerAbility;

    /** 阶段计时器句柄 */
    FTimerHandle PhaseTimerHandle;

    /** 当前阶段开始时间 */
    float CurrentPhaseStartTime = 0.0f;

    /** 是否正在运行 */
    bool bIsRunning = false;
};