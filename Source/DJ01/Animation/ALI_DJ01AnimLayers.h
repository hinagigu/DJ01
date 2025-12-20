// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Animation/AnimInstance.h"
#include "ALI_DJ01AnimLayers.generated.h"

/**
 * UALI_DJ01AnimLayers
 * 
 * 动画层接口 - 定义可被武器/状态覆盖的动画层
 * 
 * 使用方式：
 * 1. 主动画蓝图 (ABP_DJ01Character_Base) 实现此接口
 * 2. 每种武器的链接层蓝图也实现此接口
 * 3. 运行时通过 LinkAnimClassLayers 切换
 */
UINTERFACE(BlueprintType, meta = (DisplayName = "DJ01 Animation Layers Interface"))
class UALI_DJ01AnimLayers : public UInterface
{
    GENERATED_BODY()
};

class DJ01_API IALI_DJ01AnimLayers
{
    GENERATED_BODY()

public:
    //========================================
    // 全身移动层
    //========================================
    
    /** 
     * 全身移动层 - Idle/Walk/Run 的主要混合逻辑
     * 主动画蓝图在状态机中调用此层
     */
    UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category = "Animation Layers|FullBody", meta = (BlueprintThreadSafe))
    FPoseLink FullBody_IdleState();
    
    UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category = "Animation Layers|FullBody", meta = (BlueprintThreadSafe))
    FPoseLink FullBody_MovingState();
    
    UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category = "Animation Layers|FullBody", meta = (BlueprintThreadSafe))
    FPoseLink FullBody_JumpStartState();
    
    UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category = "Animation Layers|FullBody", meta = (BlueprintThreadSafe))
    FPoseLink FullBody_FallLoopState();
    
    UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category = "Animation Layers|FullBody", meta = (BlueprintThreadSafe))
    FPoseLink FullBody_LandState();

    //========================================
    // 上身覆盖层 (用于边移动边攻击)
    //========================================
    
    /** 
     * 上身攻击覆盖 - 在移动时只覆盖上半身
     * 用于轻攻击等可边走边打的动作
     */
    UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category = "Animation Layers|UpperBody", meta = (BlueprintThreadSafe))
    FPoseLink UpperBody_Overlay();
};