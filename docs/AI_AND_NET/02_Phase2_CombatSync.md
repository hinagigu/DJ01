# Phase 2: GAS 战斗同步系统

> **目标**：基于 GAS (Gameplay Ability System) 构建高精度战斗同步框架，实现客户端预测、服务端验证和回滚校正。

---

## 2.1 核心目标

| 功能模块 | 说明 |
|---------|------|
| **客户端预测** | 技能释放时本地立即播放动画/特效，无需等待服务端确认 |
| **服务端权威** | 伤害计算、命中判定均在服务端执行，防止作弊 |
| **预测回滚** | 服务端驳回预测时，客户端平滑回滚到正确状态 |
| **状态复制** | 属性变化通过 GAS 的 AttributeSet 自动同步 |

---

## 2.2 文件结构规划

```
Source/DJ01/
├── AbilitySystem/
│   ├── Public/
│   │   ├── DJ01AbilitySystemComponent.h     // 扩展 ASC，加入预测逻辑
│   │   ├── DJ01GameplayAbility_Melee.h      // 近战技能基类
│   │   ├── DJ01GameplayAbility_Ranged.h     // 远程技能基类
│   │   ├── DJ01DamageExecution.h            // 伤害执行计算
│   │   └── DJ01PredictionTypes.h            // 预测相关结构体
│   └── Private/
│       ├── DJ01AbilitySystemComponent.cpp
│       ├── DJ01GameplayAbility_Melee.cpp
│       ├── DJ01GameplayAbility_Ranged.cpp
│       └── DJ01DamageExecution.cpp
```

---

## 2.3 核心代码实现

### 2.3.1 预测结构体定义

```cpp
// DJ01PredictionTypes.h
#pragma once

#include "CoreMinimal.h"
#include "DJ01PredictionTypes.generated.h"

/**
 * 客户端预测的技能快照
 * 用于在服务端驳回时进行回滚比对
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AbilitySnapshot
{
    GENERATED_BODY()

    // 预测键，用于匹配服务端响应
    UPROPERTY()
    uint32 PredictionKey = 0;

    // 技能释放时的时间戳（客户端本地时间）
    UPROPERTY()
    float ClientTimestamp = 0.0f;

    // 技能释放时的角色位置
    UPROPERTY()
    FVector CharacterLocation = FVector::ZeroVector;

    // 技能释放时的角色朝向
    UPROPERTY()
    FRotator CharacterRotation = FRotator::ZeroRotator;

    // 目标Actor（如有）
    UPROPERTY()
    TWeakObjectPtr<AActor> TargetActor = nullptr;

    // 目标位置（用于AOE技能）
    UPROPERTY()
    FVector TargetLocation = FVector::ZeroVector;
};

/**
 * 服务端返回的技能执行结果
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AbilityResult
{
    GENERATED_BODY()

    // 对应的预测键
    UPROPERTY()
    uint32 PredictionKey = 0;

    // 是否成功执行
    UPROPERTY()
    bool bSuccess = false;

    // 失败原因（用于回滚和UI提示）
    UPROPERTY()
    FString FailureReason;

    // 服务端修正后的位置（如有位移技能）
    UPROPERTY()
    FVector CorrectedLocation = FVector::ZeroVector;

    // 实际造成的伤害值
    UPROPERTY()
    float ActualDamage = 0.0f;
};
```

---

### 2.3.2 扩展 AbilitySystemComponent

```cpp
// DJ01AbilitySystemComponent.h
#pragma once

#include "CoreMinimal.h"
#include "AbilitySystemComponent.h"
#include "DJ01PredictionTypes.h"
#include "DJ01AbilitySystemComponent.generated.h"

DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnAbilityPredictionRejected, const FDJ01AbilityResult&, Result);

/**
 * DJ01 项目的 ASC 扩展
 * 增加了客户端预测管理和回滚机制
 */
UCLASS(ClassGroup=(DJ01), meta=(BlueprintSpawnableComponent))
class DJ01_API UDJ01AbilitySystemComponent : public UAbilitySystemComponent
{
    GENERATED_BODY()

public:
    UDJ01AbilitySystemComponent();

    //~ Begin UAbilitySystemComponent Interface
    virtual void InitAbilityActorInfo(AActor* InOwnerActor, AActor* InAvatarActor) override;
    //~ End UAbilitySystemComponent Interface

    // ========== 客户端预测 API ==========

    /**
     * 客户端调用：创建预测快照并发送到服务端
     * @param AbilityHandle 技能句柄
     * @param Snapshot 预测快照
     * @return 分配的预测键
     */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Prediction")
    uint32 CreatePrediction(FGameplayAbilitySpecHandle AbilityHandle, FDJ01AbilitySnapshot& Snapshot);

    /**
     * 服务端调用：验证客户端的预测快照
     * @param Snapshot 客户端发来的快照
     * @param OutResult 验证结果
     * @return 是否验证通过
     */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Prediction", Server, Reliable)
    void ServerValidatePrediction(const FDJ01AbilitySnapshot& Snapshot);

    /**
     * 客户端回调：处理服务端返回的结果
     */
    UFUNCTION(Client, Reliable)
    void ClientReceivePredictionResult(const FDJ01AbilityResult& Result);

    // ========== 回滚机制 ==========

    /** 当预测被驳回时触发 */
    UPROPERTY(BlueprintAssignable, Category = "DJ01|Prediction")
    FOnAbilityPredictionRejected OnPredictionRejected;

protected:
    /** 执行回滚到服务端修正状态 */
    void ExecuteRollback(const FDJ01AbilityResult& Result);

    /** 清理已确认的预测 */
    void CleanupConfirmedPrediction(uint32 PredictionKey);

private:
    // 待确认的预测队列（客户端维护）
    UPROPERTY()
    TMap<uint32, FDJ01AbilitySnapshot> PendingPredictions;

    // 预测键生成器
    uint32 NextPredictionKey = 1;

    // 最大允许的预测延迟（毫秒）
    UPROPERTY(EditDefaultsOnly, Category = "DJ01|Prediction")
    float MaxPredictionLatency = 200.0f;
};
```

---

### 2.3.3 ASC 实现文件

```cpp
// DJ01AbilitySystemComponent.cpp
#include "DJ01AbilitySystemComponent.h"
#include "GameFramework/Character.h"
#include "Net/UnrealNetwork.h"

UDJ01AbilitySystemComponent::UDJ01AbilitySystemComponent()
{
    SetIsReplicatedByDefault(true);
}

void UDJ01AbilitySystemComponent::InitAbilityActorInfo(AActor* InOwnerActor, AActor* InAvatarActor)
{
    Super::InitAbilityActorInfo(InOwnerActor, InAvatarActor);

    // 确保 OwnerActor 有效
    if (InOwnerActor)
    {
        // 可在此初始化预测相关的状态
    }
}

uint32 UDJ01AbilitySystemComponent::CreatePrediction(FGameplayAbilitySpecHandle AbilityHandle, FDJ01AbilitySnapshot& Snapshot)
{
    // 分配预测键
    Snapshot.PredictionKey = NextPredictionKey++;

    // 记录当前时间戳
    Snapshot.ClientTimestamp = GetWorld()->GetTimeSeconds();

    // 记录当前位置和朝向
    if (ACharacter* Character = Cast<ACharacter>(GetAvatarActor()))
    {
        Snapshot.CharacterLocation = Character->GetActorLocation();
        Snapshot.CharacterRotation = Character->GetActorRotation();
    }

    // 缓存到待确认队列
    PendingPredictions.Add(Snapshot.PredictionKey, Snapshot);

    // 发送到服务端验证
    ServerValidatePrediction(Snapshot);

    return Snapshot.PredictionKey;
}

void UDJ01AbilitySystemComponent::ServerValidatePrediction_Implementation(const FDJ01AbilitySnapshot& Snapshot)
{
    FDJ01AbilityResult Result;
    Result.PredictionKey = Snapshot.PredictionKey;

    // ========== 服务端验证逻辑 ==========

    // 1. 检查时间戳合理性（防止重放攻击）
    float ServerTime = GetWorld()->GetTimeSeconds();
    float Latency = (ServerTime - Snapshot.ClientTimestamp) * 1000.0f; // 转换为毫秒
    
    if (Latency > MaxPredictionLatency || Latency < 0)
    {
        Result.bSuccess = false;
        Result.FailureReason = FString::Printf(TEXT("Invalid timestamp. Latency: %.2fms"), Latency);
        ClientReceivePredictionResult(Result);
        return;
    }

    // 2. 检查位置合理性（防止瞬移作弊）
    if (ACharacter* Character = Cast<ACharacter>(GetAvatarActor()))
    {
        float DistanceDelta = FVector::Dist(Character->GetActorLocation(), Snapshot.CharacterLocation);
        float MaxAllowedDistance = Character->GetCharacterMovement()->MaxWalkSpeed * (Latency / 1000.0f) * 1.5f;
        
        if (DistanceDelta > MaxAllowedDistance)
        {
            Result.bSuccess = false;
            Result.FailureReason = FString::Printf(TEXT("Position mismatch. Delta: %.2f"), DistanceDelta);
            Result.CorrectedLocation = Character->GetActorLocation();
            ClientReceivePredictionResult(Result);
            return;
        }
    }

    // 3. 验证通过，执行实际技能逻辑
    Result.bSuccess = true;
    Result.ActualDamage = 0.0f; // 实际伤害由 DamageExecution 计算

    // 返回结果给客户端
    ClientReceivePredictionResult(Result);
}

void UDJ01AbilitySystemComponent::ClientReceivePredictionResult_Implementation(const FDJ01AbilityResult& Result)
{
    if (!Result.bSuccess)
    {
        // 预测被驳回，执行回滚
        ExecuteRollback(Result);
        OnPredictionRejected.Broadcast(Result);
    }

    // 无论成功与否，清理该预测
    CleanupConfirmedPrediction(Result.PredictionKey);
}

void UDJ01AbilitySystemComponent::ExecuteRollback(const FDJ01AbilityResult& Result)
{
    // 检查是否需要位置回滚
    if (!Result.CorrectedLocation.IsZero())
    {
        if (ACharacter* Character = Cast<ACharacter>(GetAvatarActor()))
        {
            // 平滑插值到正确位置，而非直接设置
            // 实际项目中应使用更复杂的插值逻辑
            Character->SetActorLocation(Result.CorrectedLocation);
        }
    }

    // 记录日志用于调试
    UE_LOG(LogTemp, Warning, TEXT("[DJ01 ASC] Prediction %d rejected: %s"), 
           Result.PredictionKey, *Result.FailureReason);
}

void UDJ01AbilitySystemComponent::CleanupConfirmedPrediction(uint32 PredictionKey)
{
    PendingPredictions.Remove(PredictionKey);
}
```

---

### 2.3.4 服务端权威伤害执行

```cpp
// DJ01DamageExecution.h
#pragma once

#include "CoreMinimal.h"
#include "GameplayEffectExecutionCalculation.h"
#include "DJ01DamageExecution.generated.h"

/**
 * 伤害执行计算类
 * 服务端权威计算，客户端仅显示结果
 */
UCLASS()
class DJ01_API UDJ01DamageExecution : public UGameplayEffectExecutionCalculation
{
    GENERATED_BODY()

public:
    UDJ01DamageExecution();

    virtual void Execute_Implementation(
        const FGameplayEffectCustomExecutionParameters& ExecutionParams,
        FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const override;

private:
    // 捕获的属性
    FGameplayEffectAttributeCaptureDefinition AttackDef;
    FGameplayEffectAttributeCaptureDefinition DefenseDef;
    FGameplayEffectAttributeCaptureDefinition HealthDef;
};
```

```cpp
// DJ01DamageExecution.cpp
#include "DJ01DamageExecution.h"
#include "AbilitySystemComponent.h"
#include "DJ01AttributeSet.h" // 假设已有属性集定义

// 静态属性捕获宏
struct DJ01DamageStatics
{
    DECLARE_ATTRIBUTE_CAPTUREDEF(Attack);
    DECLARE_ATTRIBUTE_CAPTUREDEF(Defense);
    DECLARE_ATTRIBUTE_CAPTUREDEF(Health);

    DJ01DamageStatics()
    {
        DEFINE_ATTRIBUTE_CAPTUREDEF(UDJ01AttributeSet, Attack, Source, true);
        DEFINE_ATTRIBUTE_CAPTUREDEF(UDJ01AttributeSet, Defense, Target, true);
        DEFINE_ATTRIBUTE_CAPTUREDEF(UDJ01AttributeSet, Health, Target, false);
    }
};

static const DJ01DamageStatics& DamageStatics()
{
    static DJ01DamageStatics DmgStatics;
    return DmgStatics;
}

UDJ01DamageExecution::UDJ01DamageExecution()
{
    RelevantAttributesToCapture.Add(DamageStatics().AttackDef);
    RelevantAttributesToCapture.Add(DamageStatics().DefenseDef);
    RelevantAttributesToCapture.Add(DamageStatics().HealthDef);
}

void UDJ01DamageExecution::Execute_Implementation(
    const FGameplayEffectCustomExecutionParameters& ExecutionParams,
    FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const
{
    // 获取 ASC
    UAbilitySystemComponent* SourceASC = ExecutionParams.GetSourceAbilitySystemComponent();
    UAbilitySystemComponent* TargetASC = ExecutionParams.GetTargetAbilitySystemComponent();

    if (!SourceASC || !TargetASC) return;

    // 获取属性值
    float Attack = 0.0f;
    float Defense = 0.0f;

    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(
        DamageStatics().AttackDef, 
        FAggregatorEvaluateParameters(), 
        Attack);

    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(
        DamageStatics().DefenseDef, 
        FAggregatorEvaluateParameters(), 
        Defense);

    // ========== 伤害公式（服务端权威） ==========
    // FinalDamage = Attack * (100 / (100 + Defense))
    float DamageMultiplier = 100.0f / (100.0f + Defense);
    float FinalDamage = Attack * DamageMultiplier;

    // 最小伤害保底
    FinalDamage = FMath::Max(FinalDamage, 1.0f);

    // 应用伤害到生命值
    if (FinalDamage > 0.0f)
    {
        OutExecutionOutput.AddOutputModifier(
            FGameplayModifierEvaluatedData(
                DamageStatics().HealthProperty,
                EGameplayModOp::Additive,
                -FinalDamage));
    }

    // 记录日志
    UE_LOG(LogTemp, Log, TEXT("[DJ01 Damage] Attack: %.1f, Defense: %.1f, Final: %.1f"), 
           Attack, Defense, FinalDamage);
}
```

---

## 2.4 近战技能基类示例

```cpp
// DJ01GameplayAbility_Melee.h
#pragma once

#include "CoreMinimal.h"
#include "Abilities/GameplayAbility.h"
#include "DJ01PredictionTypes.h"
#include "DJ01GameplayAbility_Melee.generated.h"

/**
 * 近战技能基类
 * 支持客户端预测和服务端验证
 */
UCLASS()
class DJ01_API UDJ01GameplayAbility_Melee : public UGameplayAbility
{
    GENERATED_BODY()

public:
    UDJ01GameplayAbility_Melee();

    //~ Begin UGameplayAbility Interface
    virtual void ActivateAbility(
        const FGameplayAbilitySpecHandle Handle,
        const FGameplayAbilityActorInfo* ActorInfo,
        const FGameplayAbilityActivationInfo ActivationInfo,
        const FGameplayEventData* TriggerEventData) override;
    //~ End UGameplayAbility Interface

protected:
    /** 攻击范围 */
    UPROPERTY(EditDefaultsOnly, Category = "DJ01|Combat")
    float AttackRange = 200.0f;

    /** 攻击角度（度） */
    UPROPERTY(EditDefaultsOnly, Category = "DJ01|Combat")
    float AttackAngle = 90.0f;

    /** 伤害 GameplayEffect */
    UPROPERTY(EditDefaultsOnly, Category = "DJ01|Combat")
    TSubclassOf<UGameplayEffect> DamageEffectClass;

    /** 执行命中检测 */
    UFUNCTION()
    void PerformHitDetection();

    /** 应用伤害到目标 */
    void ApplyDamageToTarget(AActor* Target);
};
```

---

## 2.5 实现步骤清单

| 序号 | 任务 | 文件 | 依赖 |
|-----|------|------|------|
| 2.1 | 创建预测结构体 | `DJ01PredictionTypes.h` | 无 |
| 2.2 | 扩展 ASC 头文件 | `DJ01AbilitySystemComponent.h` | 2.1 |
| 2.3 | 实现 ASC 预测逻辑 | `DJ01AbilitySystemComponent.cpp` | 2.2 |
| 2.4 | 创建伤害执行类 | `DJ01DamageExecution.h/.cpp` | 属性集 |
| 2.5 | 创建近战技能基类 | `DJ01GameplayAbility_Melee.h/.cpp` | 2.2, 2.4 |
| 2.6 | 创建远程技能基类 | `DJ01GameplayAbility_Ranged.h/.cpp` | 2.2, 2.4 |
| 2.7 | 编写单元测试 | `DJ01CombatSyncTests.cpp` | 2.1-2.6 |

---

## 2.6 测试验证点

### 本地测试
1. **预测生成**：技能释放时 `PredingPredictions` 正确添加条目
2. **RPC 调用**：`ServerValidatePrediction` 在服务端正确接收
3. **结果回调**：`ClientReceivePredictionResult` 在客户端正确触发

### 网络测试（PIE 多客户端）
1. **正常流程**：技能动画立即播放，服务端确认后清理预测
2. **驳回流程**：模拟作弊输入，验证回滚正确执行
3. **延迟模拟**：使用 `Net PktLag=200` 测试高延迟场景

### 压力测试
1. **连续释放**：快速连续使用技能，验证预测队列不溢出
2. **并发目标**：多个玩家同时攻击同一目标，验证伤害计算正确

---

## 2.7 下一步

完成 Phase 2 后，继续阅读 [03_Phase3_AISystem.md](./03_Phase3_AISystem.md) 进行 AI 大模型集成。