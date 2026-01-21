# 09 - 实战练习与项目整合

## 概述

本文档将前面所有学习内容整合为具体的实战练习，帮助你在DJ01项目中逐步实现MMO级别的网络同步系统。每个练习都包含明确的目标、步骤和验证方法。

---

## 学习路线图

```mermaid
graph TB
    subgraph 第一阶段：基础网络
        A1[练习1: 基础属性复制] --> A2[练习2: 条件复制优化]
        A2 --> A3[练习3: Push Model实现]
    end
    
    subgraph 第二阶段：GAS网络同步
        B1[练习4: Ability预测] --> B2[练习5: GE同步优化]
        B2 --> B3[练习6: GameplayCue分离]
    end
    
    subgraph 第三阶段：移动与战斗
        C1[练习7: 移动预测回滚] --> C2[练习8: 延迟补偿]
        C2 --> C3[练习9: 权威伤害计算]
    end
    
    subgraph 第四阶段：高级架构
        D1[练习10: AOI相关性] --> D2[练习11: 负载优化]
        D2 --> D3[练习12: 分布式架构]
    end
    
    A3 --> B1
    B3 --> C1
    C3 --> D1
```

---

## 第一阶段：基础网络同步

### 练习1：基础属性复制

**目标**：理解UE5的属性复制机制

**任务**：
1. 创建一个可复制的Actor，包含Health和Mana属性
2. 实现OnRep回调，在属性变化时更新UI
3. 验证Server→Client的单向复制

**步骤**：

```cpp filePath=Source/DJ01/Exercises/Ex01_BasicReplication.h
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Ex01_BasicReplication.generated.h"

UCLASS()
class AEx01_BasicReplication : public AActor
{
    GENERATED_BODY()
    
public:
    AEx01_BasicReplication();
    
    virtual void GetLifetimeReplicatedProps(
        TArray<FLifetimeProperty>& OutLifetimeProps) const override;
    
    // === 练习任务 ===
    
    // 任务1: 添加UPROPERTY(Replicated)
    UPROPERTY(ReplicatedUsing = OnRep_Health, BlueprintReadOnly, Category = "Stats")
    float Health = 100.0f;
    
    // 任务2: 实现OnRep回调
    UFUNCTION()
    void OnRep_Health();
    
    // 任务3: Server端修改函数
    UFUNCTION(BlueprintCallable, Category = "Stats")
    void ServerSetHealth(float NewHealth);
    
protected:
    // 用于验证的UI更新
    void UpdateHealthDisplay();
};
```

```cpp filePath=Source/DJ01/Exercises/Ex01_BasicReplication.cpp
#include "Ex01_BasicReplication.h"
#include "Net/UnrealNetwork.h"

AEx01_BasicReplication::AEx01_BasicReplication()
{
    // 启用复制
    bReplicates = true;
}

void AEx01_BasicReplication::GetLifetimeReplicatedProps(
    TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    
    // 练习: 注册属性复制
    DOREPLIFETIME(AEx01_BasicReplication, Health);
}

void AEx01_BasicReplication::OnRep_Health()
{
    // 练习: 客户端收到新值后的处理
    UE_LOG(LogTemp, Log, TEXT("[Client] Health updated to: %.1f"), Health);
    UpdateHealthDisplay();
}

void AEx01_BasicReplication::ServerSetHealth(float NewHealth)
{
    // 练习: 仅服务器可以修改权威值
    if (HasAuthority())
    {
        Health = FMath::Clamp(NewHealth, 0.0f, 100.0f);
        UE_LOG(LogTemp, Log, TEXT("[Server] Health set to: %.1f"), Health);
    }
}

void AEx01_BasicReplication::UpdateHealthDisplay()
{
    // TODO: 更新UI显示
}
```

**验证方法**：
1. 在PIE中使用"Play As Listen Server" + 1个Client
2. 在Server上调用`ServerSetHealth(50.0f)`
3. 观察Client的日志是否输出"Health updated to: 50.0"

---

### 练习2：条件复制优化

**目标**：使用COND_减少不必要的网络流量

**任务**：
1. 使用`COND_OwnerOnly`复制仅Owner需要的属性
2. 使用`COND_SkipOwner`复制Owner不需要的属性
3. 测量带宽差异

```cpp filePath=Source/DJ01/Exercises/Ex02_ConditionalReplication.h
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "Ex02_ConditionalReplication.generated.h"

UCLASS()
class AEx02_ConditionalCharacter : public ACharacter
{
    GENERATED_BODY()
    
public:
    virtual void GetLifetimeReplicatedProps(
        TArray<FLifetimeProperty>& OutLifetimeProps) const override;
    
    // === 练习任务 ===
    
    // 任务1: 只同步给Owner（如背包信息）
    UPROPERTY(Replicated, BlueprintReadOnly, Category = "Private")
    int32 Gold = 0;
    
    // 任务2: 不同步给Owner（Owner从本地获取）
    UPROPERTY(Replicated, BlueprintReadOnly, Category = "Public")
    float VisibleHealth = 100.0f;
    
    // 任务3: 只在初始化时同步
    UPROPERTY(Replicated, BlueprintReadOnly, Category = "Init")
    FString CharacterName;
};
```

```cpp filePath=Source/DJ01/Exercises/Ex02_ConditionalReplication.cpp
#include "Ex02_ConditionalReplication.h"
#include "Net/UnrealNetwork.h"

void AEx02_ConditionalCharacter::GetLifetimeReplicatedProps(
    TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    
    // 练习1: 只同步给Owner
    // 类似逆水寒的私有属性同步策略
    DOREPLIFETIME_CONDITION(AEx02_ConditionalCharacter, Gold, COND_OwnerOnly);
    
    // 练习2: 不同步给Owner（Owner本地已有）
    DOREPLIFETIME_CONDITION(AEx02_ConditionalCharacter, VisibleHealth, COND_SkipOwner);
    
    // 练习3: 只在初始化时同步
    DOREPLIFETIME_CONDITION(AEx02_ConditionalCharacter, CharacterName, COND_InitialOnly);
}
```

**验证方法**：
1. 使用`stat net`命令观察网络流量
2. 频繁修改Gold，验证只有Owner收到更新
3. 频繁修改VisibleHealth，验证Owner不收到更新

---

### 练习3：Push Model实现

**目标**：实现UE5的Push Model优化（类似逆水寒MarkDirty）

**任务**：
1. 启用Actor的Push Model
2. 使用`MARK_PROPERTY_DIRTY_FROM_NAME`手动标记脏属性
3. 比较Push Model开启前后的性能

```cpp filePath=Source/DJ01/Exercises/Ex03_PushModel.h
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Ex03_PushModel.generated.h"

UCLASS()
class AEx03_PushModelActor : public AActor
{
    GENERATED_BODY()
    
public:
    AEx03_PushModelActor();
    
    virtual void GetLifetimeReplicatedProps(
        TArray<FLifetimeProperty>& OutLifetimeProps) const override;
    
    // === 练习任务 ===
    
    // 使用Push Model的属性
    UPROPERTY(Replicated, BlueprintReadOnly)
    int32 Score = 0;
    
    UPROPERTY(Replicated, BlueprintReadOnly)
    FVector Position = FVector::ZeroVector;
    
    // 类似逆水寒MarkDirty的Setter
    UFUNCTION(BlueprintCallable)
    void SetScore(int32 NewScore);
    
    UFUNCTION(BlueprintCallable)
    void SetPosition(const FVector& NewPosition);
};
```

```cpp filePath=Source/DJ01/Exercises/Ex03_PushModel.cpp
#include "Ex03_PushModel.h"
#include "Net/UnrealNetwork.h"

AEx03_PushModelActor::AEx03_PushModelActor()
{
    bReplicates = true;
    
    // 练习: 启用Push Model
    // 这告诉引擎不要自动检测属性变化，而是等待手动标记
    bReplicateUsingRegisteredSubObjectList = true;
}

void AEx03_PushModelActor::GetLifetimeReplicatedProps(
    TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    
    // 使用FDoRepLifetimeParams启用Push Model
    FDoRepLifetimeParams Params;
    Params.bIsPushBased = true;
    
    DOREPLIFETIME_WITH_PARAMS_FAST(AEx03_PushModelActor, Score, Params);
    DOREPLIFETIME_WITH_PARAMS_FAST(AEx03_PushModelActor, Position, Params);
}

void AEx03_PushModelActor::SetScore(int32 NewScore)
{
    // 类似逆水寒的 MarkDirty 机制
    if (Score != NewScore)
    {
        Score = NewScore;
        
        // 手动标记属性为脏
        // 只有标记后才会在下次复制时发送
        MARK_PROPERTY_DIRTY_FROM_NAME(AEx03_PushModelActor, Score, this);
    }
}

void AEx03_PushModelActor::SetPosition(const FVector& NewPosition)
{
    if (!Position.Equals(NewPosition, 0.1f))
    {
        Position = NewPosition;
        MARK_PROPERTY_DIRTY_FROM_NAME(AEx03_PushModelActor, Position, this);
    }
}
```

**验证方法**：
1. 创建1000个该Actor
2. 每帧调用SetScore但传入相同的值
3. 观察网络流量是否为0（因为值没变化，没有标记脏）

---

## 第二阶段：GAS网络同步

### 练习4：Ability预测

**目标**：实现客户端预测的Gameplay Ability

**任务**：
1. 创建一个预测激活的冲刺Ability
2. 正确使用Prediction Key
3. 处理服务器拒绝的情况

```cpp filePath=Source/DJ01/Exercises/Ex04_PredictedAbility.h
#pragma once

#include "Abilities/GameplayAbility.h"
#include "Ex04_PredictedAbility.generated.h"

/**
 * 练习: 实现预测冲刺Ability
 */
UCLASS()
class UEx04_DashAbility : public UGameplayAbility
{
    GENERATED_BODY()
    
public:
    UEx04_DashAbility();
    
    virtual void ActivateAbility(
        const FGameplayAbilitySpecHandle Handle,
        const FGameplayAbilityActorInfo* ActorInfo,
        const FGameplayAbilityActivationInfo ActivationInfo,
        const FGameplayEventData* TriggerEventData) override;
    
    virtual bool CanActivateAbility(
        const FGameplayAbilitySpecHandle Handle,
        const FGameplayAbilityActorInfo* ActorInfo,
        const FGameplayTagContainer* SourceTags,
        const FGameplayTagContainer* TargetTags,
        FGameplayTagContainer* OptionalRelevantTags) const override;
    
protected:
    UPROPERTY(EditDefaultsOnly)
    float DashDistance = 500.0f;
    
    UPROPERTY(EditDefaultsOnly)
    float DashDuration = 0.2f;
    
    // 执行冲刺
    void PerformDash(AActor* AvatarActor);
    
    // 冲刺结束
    UFUNCTION()
    void OnDashComplete();
};
```

```cpp filePath=Source/DJ01/Exercises/Ex04_PredictedAbility.cpp
#include "Ex04_PredictedAbility.h"
#include "AbilitySystemComponent.h"
#include "GameFramework/Character.h"
#include "GameFramework/CharacterMovementComponent.h"

UEx04_DashAbility::UEx04_DashAbility()
{
    // 练习: 配置预测策略
    InstancingPolicy = EGameplayAbilityInstancingPolicy::InstancedPerActor;
    
    // 关键: 允许客户端预测
    NetExecutionPolicy = EGameplayAbilityNetExecutionPolicy::LocalPredicted;
    
    // 允许服务器取消客户端的预测
    NetSecurityPolicy = EGameplayAbilityNetSecurityPolicy::ServerOnlyTermination;
}

void UEx04_DashAbility::ActivateAbility(
    const FGameplayAbilitySpecHandle Handle,
    const FGameplayAbilityActorInfo* ActorInfo,
    const FGameplayAbilityActivationInfo ActivationInfo,
    const FGameplayEventData* TriggerEventData)
{
    // 练习: 检查预测状态
    if (!CommitAbility(Handle, ActorInfo, ActivationInfo))
    {
        EndAbility(Handle, ActorInfo, ActivationInfo, true, true);
        return;
    }
    
    AActor* AvatarActor = ActorInfo->AvatarActor.Get();
    if (!AvatarActor)
    {
        EndAbility(Handle, ActorInfo, ActivationInfo, true, true);
        return;
    }
    
    // 练习: 客户端和服务器都执行冲刺
    // 客户端立即执行（预测），服务器验证后也执行
    PerformDash(AvatarActor);
    
    // 设置定时器结束Ability
    FTimerHandle TimerHandle;
    GetWorld()->GetTimerManager().SetTimer(
        TimerHandle, this, &UEx04_DashAbility::OnDashComplete, DashDuration, false);
}

bool UEx04_DashAbility::CanActivateAbility(
    const FGameplayAbilitySpecHandle Handle,
    const FGameplayAbilityActorInfo* ActorInfo,
    const FGameplayTagContainer* SourceTags,
    const FGameplayTagContainer* TargetTags,
    FGameplayTagContainer* OptionalRelevantTags) const
{
    if (!Super::CanActivateAbility(Handle, ActorInfo, SourceTags, TargetTags, OptionalRelevantTags))
    {
        return false;
    }
    
    // 练习: 添加自定义验证逻辑
    // 例如：检查是否在地面上
    if (ACharacter* Character = Cast<ACharacter>(ActorInfo->AvatarActor.Get()))
    {
        return Character->GetCharacterMovement()->IsMovingOnGround();
    }
    
    return false;
}

void UEx04_DashAbility::PerformDash(AActor* AvatarActor)
{
    if (ACharacter* Character = Cast<ACharacter>(AvatarActor))
    {
        FVector DashDirection = Character->GetActorForwardVector();
        FVector DashVelocity = DashDirection * (DashDistance / DashDuration);
        
        Character->LaunchCharacter(DashVelocity, true, false);
        
        UE_LOG(LogTemp, Log, TEXT("[%s] Dash performed: %s"), 
            HasAuthority() ? TEXT("Server") : TEXT("Client"),
            *DashDirection.ToString());
    }
}

void UEx04_DashAbility::OnDashComplete()
{
    EndAbility(CurrentSpecHandle, CurrentActorInfo, CurrentActivationInfo, true, false);
}
```

**验证方法**：
1. 在200ms延迟下测试冲刺
2. 验证客户端立即开始冲刺
3. 验证服务器确认后没有明显回拉

---

### 练习5：GameplayEffect同步优化

**目标**：优化GE的网络同步

**任务**：
1. 创建Duration GE并观察同步行为
2. 使用Minimal Replication优化
3. 实现GE的预测应用

```cpp filePath=Source/DJ01/Exercises/Ex05_GEOptimization.h
#pragma once

#include "GameplayEffect.h"
#include "Ex05_GEOptimization.generated.h"

/**
 * 练习: 优化过的持续性GE
 */
UCLASS()
class UEx05_OptimizedDOTEffect : public UGameplayEffect
{
    GENERATED_BODY()
    
public:
    UEx05_OptimizedDOTEffect();
};

/**
 * 练习: GE应用组件
 */
UCLASS()
class UEx05_GEApplierComponent : public UActorComponent
{
    GENERATED_BODY()
    
public:
    // 预测应用GE
    UFUNCTION(BlueprintCallable)
    void ApplyEffectWithPrediction(AActor* Target, 
        TSubclassOf<UGameplayEffect> EffectClass);
    
    // 服务器确认应用
    UFUNCTION(Server, Reliable)
    void ServerConfirmEffect(AActor* Target, 
        TSubclassOf<UGameplayEffect> EffectClass);
};
```

---

### 练习6：GameplayCue分离

**目标**：将视觉表现与逻辑分离

**任务**：
1. 创建一个攻击Ability，伤害逻辑和特效分离
2. 使用GameplayCue执行客户端特效
3. 在高负载时跳过非必要Cue

```cpp filePath=Source/DJ01/Exercises/Ex06_GameplayCueSeparation.h
#pragma once

#include "Abilities/GameplayAbility.h"
#include "Ex06_GameplayCueSeparation.generated.h"

/**
 * 练习: 攻击Ability - 逻辑与表现分离
 */
UCLASS()
class UEx06_AttackAbility : public UGameplayAbility
{
    GENERATED_BODY()
    
public:
    virtual void ActivateAbility(
        const FGameplayAbilitySpecHandle Handle,
        const FGameplayAbilityActorInfo* ActorInfo,
        const FGameplayAbilityActivationInfo ActivationInfo,
        const FGameplayEventData* TriggerEventData) override;
    
protected:
    // 伤害GE（服务器权威）
    UPROPERTY(EditDefaultsOnly)
    TSubclassOf<UGameplayEffect> DamageEffectClass;
    
    // 攻击特效Cue（客户端表现）
    UPROPERTY(EditDefaultsOnly)
    FGameplayTag AttackCueTag;
    
    // 命中特效Cue
    UPROPERTY(EditDefaultsOnly)
    FGameplayTag HitCueTag;
    
    // 执行伤害（仅服务器）
    void ApplyDamage(AActor* Target);
    
    // 播放特效（所有客户端）
    void PlayAttackEffects(AActor* Target);
};
```

```cpp filePath=Source/DJ01/Exercises/Ex06_GameplayCueSeparation.cpp
#include "Ex06_GameplayCueSeparation.h"
#include "AbilitySystemComponent.h"
#include "AbilitySystemBlueprintLibrary.h"

void UEx06_AttackAbility::ActivateAbility(
    const FGameplayAbilitySpecHandle Handle,
    const FGameplayAbilityActorInfo* ActorInfo,
    const FGameplayAbilityActivationInfo ActivationInfo,
    const FGameplayEventData* TriggerEventData)
{
    if (!CommitAbility(Handle, ActorInfo, ActivationInfo))
    {
        EndAbility(Handle, ActorInfo, ActivationInfo, true, true);
        return;
    }
    
    // 获取目标
    AActor* Target = GetAvatarActorFromActorInfo(); // 简化：攻击自己作为演示
    
    // 练习: 分离伤害逻辑和视觉表现
    
    // 1. 服务器执行伤害（权威）
    if (HasAuthority())
    {
        ApplyDamage(Target);
    }
    
    // 2. 所有端播放特效（通过Cue）
    PlayAttackEffects(Target);
    
    EndAbility(Handle, ActorInfo, ActivationInfo, true, false);
}

void UEx06_AttackAbility::ApplyDamage(AActor* Target)
{
    // 仅服务器执行
    if (!HasAuthority()) return;
    
    UAbilitySystemComponent* TargetASC = 
        UAbilitySystemBlueprintLibrary::GetAbilitySystemComponent(Target);
    
    if (TargetASC && DamageEffectClass)
    {
        FGameplayEffectContextHandle Context = MakeEffectContext(
            CurrentSpecHandle, CurrentActorInfo);
        FGameplayEffectSpecHandle SpecHandle = MakeOutgoingGameplayEffectSpec(
            DamageEffectClass, GetAbilityLevel());
        
        ApplyGameplayEffectSpecToTarget(CurrentSpecHandle, CurrentActorInfo, 
            CurrentActivationInfo, SpecHandle, 
            FGameplayAbilityTargetDataHandle());
        
        UE_LOG(LogTemp, Log, TEXT("[Server] Damage applied to %s"), *Target->GetName());
    }
}

void UEx06_AttackAbility::PlayAttackEffects(AActor* Target)
{
    // 通过GameplayCue播放特效
    // Cue会自动复制到所有相关客户端
    
    UAbilitySystemComponent* ASC = GetAbilitySystemComponentFromActorInfo();
    if (ASC && AttackCueTag.IsValid())
    {
        FGameplayCueParameters CueParams;
        CueParams.Location = Target->GetActorLocation();
        CueParams.Normal = GetAvatarActorFromActorInfo()->GetActorForwardVector();
        
        // 执行Cue - 引擎会自动处理网络复制
        ASC->ExecuteGameplayCue(AttackCueTag, CueParams);
        
        UE_LOG(LogTemp, Log, TEXT("Attack Cue executed: %s"), *AttackCueTag.ToString());
    }
}
```

---

## 第三阶段：移动与战斗

### 练习7：移动预测与回滚

**目标**：理解CMC的预测机制

**任务**：
1. 添加自定义移动能力（双跳）
2. 实现SavedMove保存额外状态
3. 处理服务器校正后的回放

```cpp filePath=Source/DJ01/Exercises/Ex07_MovementPrediction.h
#pragma once

#include "GameFramework/CharacterMovementComponent.h"
#include "Ex07_MovementPrediction.generated.h"

/**
 * 练习: 支持双跳预测的移动组件
 */
UCLASS()
class UEx07_DoubleJumpMovement : public UCharacterMovementComponent
{
    GENERATED_BODY()
    
public:
    UEx07_DoubleJumpMovement();
    
    // 双跳次数
    UPROPERTY(EditDefaultsOnly, Category = "DoubleJump")
    int32 MaxJumpCount = 2;
    
    // 当前跳跃次数
    int32 CurrentJumpCount = 0;
    
    // 重载跳跃检查
    virtual bool CanAttemptJump() const override;
    
    // 重载跳跃执行
    virtual bool DoJump(bool bReplayingMoves) override;
    
    // 落地时重置
    virtual void ProcessLanded(const FHitResult& Hit, 
        float remainingTime, int32 Iterations) override;
    
protected:
    // 练习: 创建自定义SavedMove
    virtual class FNetworkPredictionData_Client* GetPredictionData_Client() const override;
};

/**
 * 自定义SavedMove - 保存双跳状态
 */
class FEx07_SavedMove : public FSavedMove_Character
{
public:
    typedef FSavedMove_Character Super;
    
    // 保存的双跳计数
    int32 SavedJumpCount = 0;
    
    // 重载：清除
    virtual void Clear() override;
    
    // 重载：保存状态
    virtual void SetMoveFor(ACharacter* C, float InDeltaTime, 
        FVector const& NewAccel, class FNetworkPredictionData_Client_Character& ClientData) override;
    
    // 重载：准备重放
    virtual void PrepMoveFor(ACharacter* C) override;
    
    // 重载：合并检查
    virtual bool CanCombineWith(const FSavedMovePtr& NewMove, 
        ACharacter* InCharacter, float MaxDelta) const override;
};

class FEx07_NetworkPredictionData_Client : public FNetworkPredictionData_Client_Character
{
public:
    typedef FNetworkPredictionData_Client_Character Super;
    
    FEx07_NetworkPredictionData_Client(const UCharacterMovementComponent& ClientMovement);
    
    virtual FSavedMovePtr AllocateNewMove() override;
};
```

```cpp filePath=Source/DJ01/Exercises/Ex07_MovementPrediction.cpp
#include "Ex07_MovementPrediction.h"
#include "GameFramework/Character.h"

UEx07_DoubleJumpMovement::UEx07_DoubleJumpMovement()
{
    // 启用网络预测
    SetNetworkMoveDataContainer(FEx07_NetworkPredictionData_Client(*this));
}

bool UEx07_DoubleJumpMovement::CanAttemptJump() const
{
    // 练习: 允许多次跳跃
    return IsJumpAllowed() && 
           (IsMovingOnGround() || CurrentJumpCount < MaxJumpCount);
}

bool UEx07_DoubleJumpMovement::DoJump(bool bReplayingMoves)
{
    if (CanAttemptJump())
    {
        // 练习: 增加跳跃计数
        CurrentJumpCount++;
        
        // 执行跳跃
        Velocity.Z = JumpZVelocity;
        SetMovementMode(MOVE_Falling);
        
        UE_LOG(LogTemp, Log, TEXT("Jump %d/%d (Replaying: %s)"), 
            CurrentJumpCount, MaxJumpCount,
            bReplayingMoves ? TEXT("Yes") : TEXT("No"));
        
        return true;
    }
    return false;
}

void UEx07_DoubleJumpMovement::ProcessLanded(const FHitResult& Hit, 
    float remainingTime, int32 Iterations)
{
    Super::ProcessLanded(Hit, remainingTime, Iterations);
    
    // 练习: 落地时重置跳跃计数
    CurrentJumpCount = 0;
}

FNetworkPredictionData_Client* UEx07_DoubleJumpMovement::GetPredictionData_Client() const
{
    if (ClientPredictionData == nullptr)
    {
        UEx07_DoubleJumpMovement* MutableThis = 
            const_cast<UEx07_DoubleJumpMovement*>(this);
        MutableThis->ClientPredictionData = 
            new FEx07_NetworkPredictionData_Client(*this);
    }
    return ClientPredictionData;
}

// === SavedMove 实现 ===

void FEx07_SavedMove::Clear()
{
    Super::Clear();
    SavedJumpCount = 0;
}

void FEx07_SavedMove::SetMoveFor(ACharacter* C, float InDeltaTime, 
    FVector const& NewAccel, FNetworkPredictionData_Client_Character& ClientData)
{
    Super::SetMoveFor(C, InDeltaTime, NewAccel, ClientData);
    
    // 练习: 保存双跳状态
    if (UEx07_DoubleJumpMovement* Movement = 
            Cast<UEx07_DoubleJumpMovement>(C->GetCharacterMovement()))
    {
        SavedJumpCount = Movement->CurrentJumpCount;
    }
}

void FEx07_SavedMove::PrepMoveFor(ACharacter* C)
{
    Super::PrepMoveFor(C);
    
    // 练习: 回放前恢复状态
    if (UEx07_DoubleJumpMovement* Movement = 
            Cast<UEx07_DoubleJumpMovement>(C->GetCharacterMovement()))
    {
        Movement->CurrentJumpCount = SavedJumpCount;
    }
}

bool FEx07_SavedMove::CanCombineWith(const FSavedMovePtr& NewMove, 
    ACharacter* InCharacter, float MaxDelta) const
{
    // 练习: 跳跃状态不同时不能合并
    if (FEx07_SavedMove* OtherMove = static_cast<FEx07_SavedMove*>(NewMove.Get()))
    {
        if (SavedJumpCount != OtherMove->SavedJumpCount)
        {
            return false;
        }
    }
    return Super::CanCombineWith(NewMove, InCharacter, MaxDelta);
}

// === NetworkPredictionData 实现 ===

FEx07_NetworkPredictionData_Client::FEx07_NetworkPredictionData_Client(
    const UCharacterMovementComponent& ClientMovement)
    : Super(ClientMovement)
{
}

FSavedMovePtr FEx07_NetworkPredictionData_Client::AllocateNewMove()
{
    return FSavedMovePtr(new FEx07_SavedMove());
}
```

---

### 练习8：延迟补偿

**目标**：实现射击命中的延迟补偿

**任务**：
1. 记录玩家位置历史
2. 服务器回溯到客户端射击时刻
3. 验证命中判定

```cpp filePath=Source/DJ01/Exercises/Ex08_LagCompensation.h
#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "Ex08_LagCompensation.generated.h"

USTRUCT()
struct FEx08_PositionSnapshot
{
    GENERATED_BODY()
    
    UPROPERTY()
    FVector Location = FVector::ZeroVector;
    
    UPROPERTY()
    FRotator Rotation = FRotator::ZeroRotator;
    
    UPROPERTY()
    double ServerTime = 0.0;
};

/**
 * 练习: 位置历史记录组件
 */
UCLASS()
class UEx08_PositionHistoryComponent : public UActorComponent
{
    GENERATED_BODY()
    
public:
    virtual void TickComponent(float DeltaTime, ELevelTick TickType, 
        FActorComponentTickFunction* ThisTickFunction) override;
    
    // 获取指定时间的位置
    bool GetPositionAtTime(double Time, FVector& OutLocation, FRotator& OutRotation) const;
    
    // 历史记录长度（秒）
    UPROPERTY(EditDefaultsOnly)
    float HistoryDuration = 1.0f;
    
protected:
    TArray<FEx08_PositionSnapshot> PositionHistory;
    
    void RecordPosition();
    void CleanupOldHistory();
};

/**
 * 练习: 延迟补偿射击验证
 */
UCLASS()
class UEx08_LagCompensatedWeapon : public UActorComponent
{
    GENERATED_BODY()
    
public:
    // 客户端请求射击
    UFUNCTION(Server, Reliable)
    void ServerFire(FVector_NetQuantize StartLocation, 
        FVector_NetQuantizeNormal Direction, 
        double ClientFireTime);
    
protected:
    // 服务器验证命中
    bool ValidateHit(const FVector& Start, const FVector& Direction, 
        double ClientTime, FHitResult& OutHit);
    
    // 回溯所有目标位置
    void RewindTargets(double ToTime, TArray<TTuple<AActor*, FTransform>>& OutOriginalTransforms);
    
    // 恢复目标位置
    void RestoreTargets(const TArray<TTuple<AActor*, FTransform>>& OriginalTransforms);
};
```

---

### 练习9：权威伤害计算

**目标**：实现服务器权威的伤害系统

**任务**：
1. 创建伤害计算器（GameplayEffectExecutionCalculation）
2. 所有伤害仅在服务器计算
3. 同步伤害结果到客户端

```cpp filePath=Source/DJ01/Exercises/Ex09_AuthoritativeDamage.h
#pragma once

#include "GameplayEffectExecutionCalculation.h"
#include "Ex09_AuthoritativeDamage.generated.h"

/**
 * 练习: 服务器权威伤害计算
 */
UCLASS()
class UEx09_DamageCalculation : public UGameplayEffectExecutionCalculation
{
    GENERATED_BODY()
    
public:
    UEx09_DamageCalculation();
    
    virtual void Execute_Implementation(
        const FGameplayEffectCustomExecutionParameters& ExecutionParams,
        FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const override;
    
protected:
    // 捕获的属性
    FGameplayEffectAttributeCaptureDefinition AttackDef;
    FGameplayEffectAttributeCaptureDefinition DefenseDef;
    FGameplayEffectAttributeCaptureDefinition HealthDef;
};
```

```cpp filePath=Source/DJ01/Exercises/Ex09_AuthoritativeDamage.cpp
#include "Ex09_AuthoritativeDamage.h"
#include "AbilitySystemComponent.h"
// 假设有DJ01AttributeSet定义

UEx09_DamageCalculation::UEx09_DamageCalculation()
{
    // 配置属性捕获
    // AttackDef.AttributeToCapture = UDJ01AttributeSet::GetAttackAttribute();
    // ...
}

void UEx09_DamageCalculation::Execute_Implementation(
    const FGameplayEffectCustomExecutionParameters& ExecutionParams,
    FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const
{
    // 练习: 仅在服务器执行
    UAbilitySystemComponent* TargetASC = ExecutionParams.GetTargetAbilitySystemComponent();
    if (!TargetASC || !TargetASC->GetOwnerActor()->HasAuthority())
    {
        // 非服务器端不执行任何计算
        return;
    }
    
    // 获取捕获的属性值
    float AttackPower = 0.0f;
    float Defense = 0.0f;
    
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(AttackDef, 
        FAggregatorEvaluateParameters(), AttackPower);
    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(DefenseDef, 
        FAggregatorEvaluateParameters(), Defense);
    
    // 练习: 服务器权威的伤害公式
    float BaseDamage = AttackPower * 2.0f;
    float DamageReduction = Defense / (Defense + 100.0f);
    float FinalDamage = BaseDamage * (1.0f - DamageReduction);
    
    // 添加随机浮动
    FinalDamage *= FMath::RandRange(0.9f, 1.1f);
    
    // 输出伤害
    // OutExecutionOutput.AddOutputModifier(
    //     FGameplayModifierEvaluatedData(
    //         UDJ01AttributeSet::GetHealthAttribute(),
    //         EGameplayModOp::Additive,
    //         -FinalDamage));
    
    UE_LOG(LogTemp, Log, TEXT("[Server] Damage calculated: %.1f (Attack: %.1f, Defense: %.1f)"),
        FinalDamage, AttackPower, Defense);
}
```

---

## 第四阶段：高级架构

### 练习10：AOI相关性系统

**目标**：实现自定义网络相关性

**任务**：
1. 重载IsNetRelevantFor
2. 实现距离+扇形视野的复合判定
3. 添加AOI分组优化

（参考06_AOI_Relevancy.md中的实现）

---

### 练习11：负载优化系统

**目标**：实现动态负载优化

**任务**：
1. 实现UDJ01NetworkOptimizer
2. 根据CPU/玩家数自动切换优化等级
3. 各系统响应优化等级变化

（参考07_HighLoadOptimization.md中的实现）

---

### 练习12：分布式架构原型

**目标**：实现多服务器协调

**任务**：
1. 实现MasterServer子系统
2. 实现GameServer自注册
3. 实现玩家跨服传送

（参考08_DistributedArchitecture.md中的实现）

---

## 项目整合清单

### 文件结构

```
Source/DJ01/
├── Network/
│   ├── DJ01NetworkOptimizer.h/.cpp       # 负载优化
│   ├── DJ01ReplicationGraph.h/.cpp       # 自定义复制图
│   └── Distributed/
│       ├── DJ01DistributedTypes.h        # 分布式类型定义
│       ├── DJ01MasterServer.h/.cpp       # Master服务器
│       ├── DJ01MessageBroker.h/.cpp      # 消息总线
│       ├── DJ01ServerTransfer.h/.cpp     # 跨服传送
│       └── DJ01GameServerComponent.h/.cpp # GameServer组件
├── GAS/
│   ├── DJ01GameplayCueManager.h/.cpp     # Cue管理器优化
│   ├── Abilities/
│   │   └── DJ01PredictedAbility.h/.cpp   # 预测Ability基类
│   └── Effects/
│       └── DJ01DamageCalculation.h/.cpp  # 伤害计算
├── Characters/
│   ├── DJ01CharacterMovementComponent.h/.cpp # 移动组件
│   └── DJ01CharacterBase.h/.cpp          # 角色基类
├── Actors/
│   ├── DJ01RelevancyActor.h/.cpp         # 相关性Actor
│   └── DJ01DormantActor.h/.cpp           # 休眠Actor
└── Triggers/
    └── DJ01AOITrigger.h/.cpp             # AOI触发器
```

### 配置检查清单

```
□ Project Settings → Network
  □ 启用 Push Model
  □ 配置 NetCullDistanceSquared 默认值
  □ 设置 NetUpdateFrequency

□ DefaultEngine.ini
  □ 配置 ReplicationGraph
  □ 设置网络优化参数

□ GameMode
  □ 附加 DJ01GameServerComponent
  □ 配置 GameplayCueManager

□ 角色蓝图
  □ 使用 DJ01CharacterMovementComponent
  □ 配置 NetCullDistanceSquared
```

---

## 性能测试建议

### 测试场景

1. **基础同步测试**
   - 100个客户端连接
   - 观察带宽和CPU使用率

2. **高负载测试**
   - 逐步增加客户端至系统极限
   - 验证优化系统自动启用

3. **延迟测试**
   - 模拟200ms网络延迟
   - 验证预测和回滚效果

4. **跨服测试**
   - 启动多个DS实例
   - 测试玩家传送流程

### 监控指标

| 指标 | 正常范围 | 告警阈值 |
|------|---------|---------|
| 网络更新频率 | 60-100Hz | <30Hz |
| 复制Actor数量 | <500 | >800 |
| 服务器Tick时间 | <16ms | >33ms |
| 客户端RTT | <100ms | >200ms |
| 预测失败率 | <5% | >10% |

---

## 学习资源

### 官方文档
- [UE5 Networking Overview](https://docs.unrealengine.com/5.0/en-US/networking-overview-for-unreal-engine/)
- [Gameplay Ability System](https://docs.unrealengine.com/5.0/en-US/gameplay-ability-system-for-unreal-engine/)
- [Character Movement Component](https://docs.unrealengine.com/5.0/en-US/character-movement-component-in-unreal-engine/)

### 推荐视频
- GDC: "Overwatch Gameplay Architecture and Netcode"
- Unreal Fest: "Replication Graph Deep Dive"
- UE5 官方: "Lyra Sample Game Breakdown"

### 相关项目
- Lyra Starter Game（UE5官方示例）
- Action RPG Sample
- ShooterGame Sample

---

## 总结

通过完成这12个练习，你将掌握：

1. **基础网络**：属性复制、条件同步、Push Model
2. **GAS网络**：Ability预测、GE同步、Cue分离
3. **移动战斗**：移动预测、延迟补偿、权威伤害
4. **高级架构**：AOI相关性、负载优化、分布式设计

这些技能将帮助你理解和实现MMO级别的网络同步系统，在就业市场上展示高级技术能力。

---

## 完整文档索引

1. [00_Overview.md](./00_Overview.md) - 学习路线图与概念映射
2. [01_UE_NetworkArchitecture.md](./01_UE_NetworkArchitecture.md) - UE5网络架构基础
3. [02_GAS_NetworkSync.md](./02_GAS_NetworkSync.md) - GAS网络同步机制
4. [03_PropertyReplication.md](./03_PropertyReplication.md) - 属性复制与优化
5. [04_MovementPrediction.md](./04_MovementPrediction.md) - 移动预测与回滚
6. [05_CombatSync.md](./05_CombatSync.md) - 战斗同步机制
7. [06_AOI_Relevancy.md](./06_AOI_Relevancy.md) - AOI与网络相关性
8. [07_HighLoadOptimization.md](./07_HighLoadOptimization.md) - 高负载优化策略
9. [08_DistributedArchitecture.md](./08_DistributedArchitecture.md) - 分布式服务器架构
10. [09_PracticalExercises.md](./09_PracticalExercises.md) - 实战练习（本文档）