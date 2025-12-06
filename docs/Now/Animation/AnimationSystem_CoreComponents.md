# DJ01 动画系统 - 核心组件设计

> 返回 [动画系统总览](./AnimationSystem_Overview.md)

---

## 目录

1. [UDJ01AnimInstance](#1-udj01animinstance)
2. [UALI_DJ01AnimLayers](#2-uali_dj01animlayers)
3. [UDJ01AnimDataAsset](#3-udj01animdataasset)
4. [UDJ01AbilityTask_PlayMontageAndWait](#4-udj01abilitytask_playmontageandwait)

---

## 1. UDJ01AnimInstance

**文件**: `Source/DJ01/Animation/DJ01AnimInstance.h/cpp`

动画实例基类，所有角色动画蓝图的父类。

### 1.1 类定义

```cpp
UCLASS()
class DJ01_API UDJ01AnimInstance : public UAnimInstance
{
    GENERATED_BODY()

public:
    //========================================
    // 初始化与更新
    //========================================
    
    virtual void NativeInitializeAnimation() override;
    virtual void NativeThreadSafeUpdateAnimation(float DeltaSeconds) override;
    
    //========================================
    // 移动数据 (线程安全访问)
    //========================================
    
    UPROPERTY(BlueprintReadOnly, Category = "Locomotion")
    float GroundSpeed;
    
    UPROPERTY(BlueprintReadOnly, Category = "Locomotion")
    float MovementDirection;  // -180 to 180
    
    UPROPERTY(BlueprintReadOnly, Category = "Locomotion")
    bool bIsMoving;
    
    UPROPERTY(BlueprintReadOnly, Category = "Locomotion")
    bool bIsFalling;
    
    UPROPERTY(BlueprintReadOnly, Category = "Locomotion")
    bool bIsJumping;
    
    //========================================
    // 战斗状态 (由GameplayTag驱动)
    //========================================
    
    // 已有: FGameplayTagBlueprintPropertyMap GameplayTagPropertyMap;
    // 配置Tag到以下属性的映射:
    
    UPROPERTY(BlueprintReadOnly, Category = "Combat")
    bool bIsInCombat;         // State.Combat
    
    UPROPERTY(BlueprintReadOnly, Category = "Combat")
    bool bIsAttacking;        // State.Combat.Attacking
    
    UPROPERTY(BlueprintReadOnly, Category = "Combat")
    bool bIsCasting;          // State.Combat.Casting
    
    UPROPERTY(BlueprintReadOnly, Category = "Combat")
    bool bIsStunned;          // State.Debuff.Stunned
    
    //========================================
    // 链接动画层管理
    //========================================
    
    UFUNCTION(BlueprintCallable, Category = "Animation|Layers")
    void LinkAnimLayer(TSubclassOf<UAnimInstance> InAnimLayerClass);
    
    UFUNCTION(BlueprintCallable, Category = "Animation|Layers")
    void UnlinkAnimLayer(TSubclassOf<UAnimInstance> InAnimLayerClass);

protected:
    UPROPERTY(Transient)
    TObjectPtr<ACharacter> OwningCharacter;
    
    UPROPERTY(Transient)
    TObjectPtr<UCharacterMovementComponent> MovementComponent;
};
```

### 1.2 线程安全更新实现

```cpp
void UDJ01AnimInstance::NativeThreadSafeUpdateAnimation(float DeltaSeconds)
{
    Super::NativeThreadSafeUpdateAnimation(DeltaSeconds);
    
    if (!OwningCharacter || !MovementComponent)
    {
        return;
    }
    
    // 使用 Property Access 获取数据 (线程安全)
    FVector Velocity = MovementComponent->Velocity;
    
    GroundSpeed = Velocity.Size2D();
    bIsMoving = GroundSpeed > 3.0f;
    bIsFalling = MovementComponent->IsFalling();
    
    // 计算移动方向 (相对于角色朝向)
    if (bIsMoving)
    {
        FRotator CharacterRotation = OwningCharacter->GetActorRotation();
        FRotator VelocityRotation = Velocity.ToOrientationRotator();
        FRotator Delta = (VelocityRotation - CharacterRotation).GetNormalized();
        MovementDirection = Delta.Yaw;
    }
}
```

---

## 2. UALI_DJ01AnimLayers

**文件**: `Source/DJ01/Animation/ALI_DJ01AnimLayers.h`

动画层接口，定义可被链接层覆盖的动画槽位。

### 2.1 接口定义

```cpp
#pragma once

#include "CoreMinimal.h"
#include "Animation/AnimInstance.h"
#include "ALI_DJ01AnimLayers.generated.h"

/**
 * 动画层接口 - 定义可被链接层覆盖的动画层
 * 
 * 使用方式:
 * 1. 主动画蓝图实现此接口
 * 2. 链接层蓝图也实现此接口并覆盖对应函数
 * 3. 运行时通过LinkAnimClassLayers动态切换
 */
UINTERFACE(MinimalAPI, Blueprintable, BlueprintType)
class UALI_DJ01AnimLayers : public UInterface
{
    GENERATED_BODY()
};

class DJ01_API IALI_DJ01AnimLayers
{
    GENERATED_BODY()

public:
    //========================================
    // 全身动画层 (用于技能、特殊动作)
    //========================================
    
    UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, 
              Category = "Animation Layers|FullBody")
    FAnimPose GetFullBodyPose();
    
    //========================================
    // 上身动画层 (用于攻击、施法)
    //========================================
    
    UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, 
              Category = "Animation Layers|UpperBody")
    FAnimPose GetUpperBodyPose();
    
    //========================================
    // 移动动画层
    //========================================
    
    UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, 
              Category = "Animation Layers|Locomotion")
    FAnimPose GetLocomotionPose();
    
    //========================================
    // Idle动画层
    //========================================
    
    UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, 
              Category = "Animation Layers|Idle")
    FAnimPose GetIdlePose();
};
```

### 2.2 使用示意图

```
主动画蓝图 (ABP_DJ01Character_Base)
│
├── 实现 IALI_DJ01AnimLayers 接口
│   ├── GetFullBodyPose()  ──→ [Linked Layer插槽]
│   ├── GetUpperBodyPose() ──→ [Linked Layer插槽]
│   └── GetLocomotionPose()──→ [Linked Layer插槽]
│
└── 运行时调用 LinkAnimClassLayers(ABP_SwordAnimLayers)
    │
    └── ABP_SwordAnimLayers 覆盖接口函数
        ├── GetFullBodyPose()  → 剑术全身动画
        ├── GetUpperBodyPose() → 剑术上身动画
        └── GetLocomotionPose()→ 持剑跑步动画
```

---

## 3. UDJ01AnimDataAsset

**文件**: `Source/DJ01/Animation/DJ01AnimDataAsset.h/cpp`

动画数据资产，定义一套完整的动画配置。

### 3.1 辅助结构体

```cpp
/**
 * 动画蒙太奇条目 - 将GameplayTag映射到蒙太奇
 */
USTRUCT(BlueprintType)
struct FDJ01MontageEntry
{
    GENERATED_BODY()
    
    UPROPERTY(EditDefaultsOnly, Category = "Animation")
    FGameplayTag TriggerTag;
    
    UPROPERTY(EditDefaultsOnly, Category = "Animation")
    TObjectPtr<UAnimMontage> Montage;
    
    UPROPERTY(EditDefaultsOnly, Category = "Animation")
    float PlayRate = 1.0f;
    
    UPROPERTY(EditDefaultsOnly, Category = "Animation")
    FName StartSection = NAME_None;
};
```

### 3.2 数据资产类

```cpp
UCLASS(BlueprintType)
class DJ01_API UDJ01AnimDataAsset : public UPrimaryDataAsset
{
    GENERATED_BODY()

public:
    //========================================
    // 资产标识
    //========================================
    
    UPROPERTY(EditDefaultsOnly, Category = "Identity")
    FGameplayTag AnimSetTag;
    
    //========================================
    // 链接动画层配置
    //========================================
    
    UPROPERTY(EditDefaultsOnly, Category = "Animation Layers")
    TSubclassOf<UAnimInstance> LinkedAnimLayerClass;
    
    //========================================
    // 战斗蒙太奇
    //========================================
    
    UPROPERTY(EditDefaultsOnly, Category = "Combat|Montages")
    TArray<TObjectPtr<UAnimMontage>> LightAttackCombo;
    
    UPROPERTY(EditDefaultsOnly, Category = "Combat|Montages")
    TObjectPtr<UAnimMontage> HeavyAttackMontage;
    
    UPROPERTY(EditDefaultsOnly, Category = "Combat|Montages")
    TObjectPtr<UAnimMontage> DodgeMontage;
    
    UPROPERTY(EditDefaultsOnly, Category = "Combat|Montages")
    TArray<TObjectPtr<UAnimMontage>> HitReactMontages;
    
    UPROPERTY(EditDefaultsOnly, Category = "Combat|Montages")
    TObjectPtr<UAnimMontage> DeathMontage;
    
    //========================================
    // 技能蒙太奇映射
    //========================================
    
    UPROPERTY(EditDefaultsOnly, Category = "Abilities|Montages")
    TArray<FDJ01MontageEntry> AbilityMontages;
    
    //========================================
    // 辅助函数
    //========================================
    
    UFUNCTION(BlueprintCallable, Category = "Animation")
    UAnimMontage* GetMontageForTag(FGameplayTag Tag) const;
    
    UFUNCTION(BlueprintCallable, Category = "Animation")
    UAnimMontage* GetNextLightAttackMontage(int32 ComboIndex) const;
    
    UFUNCTION(BlueprintCallable, Category = "Animation")
    UAnimMontage* GetRandomHitReactMontage() const;

    virtual FPrimaryAssetId GetPrimaryAssetId() const override;
};
```

### 3.3 实现示例

```cpp
UAnimMontage* UDJ01AnimDataAsset::GetNextLightAttackMontage(int32 ComboIndex) const
{
    if (LightAttackCombo.IsValidIndex(ComboIndex))
    {
        return LightAttackCombo[ComboIndex];
    }
    return nullptr;
}

UAnimMontage* UDJ01AnimDataAsset::GetRandomHitReactMontage() const
{
    if (HitReactMontages.Num() > 0)
    {
        int32 Index = FMath::RandRange(0, HitReactMontages.Num() - 1);
        return HitReactMontages[Index];
    }
    return nullptr;
}

UAnimMontage* UDJ01AnimDataAsset::GetMontageForTag(FGameplayTag Tag) const
{
    for (const FDJ01MontageEntry& Entry : AbilityMontages)
    {
        if (Entry.TriggerTag.MatchesTagExact(Tag))
        {
            return Entry.Montage;
        }
    }
    return nullptr;
}
```

---

## 4. UDJ01AbilityTask_PlayMontageAndWait

**文件**: `Source/DJ01/AbilitySystem/Tasks/DJ01AbilityTask_PlayMontageAndWait.h/cpp`

播放蒙太奇并等待的技能任务。

### 4.1 委托定义

```cpp
DECLARE_DYNAMIC_MULTICAST_DELEGATE(FDJ01MontageNotifyDelegate);
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FDJ01MontageEventDelegate, FGameplayTag, EventTag);
```

### 4.2 类定义

```cpp
UCLASS()
class DJ01_API UDJ01AbilityTask_PlayMontageAndWait : public UAbilityTask
{
    GENERATED_BODY()

public:
    /**
     * 创建并开始播放蒙太奇任务
     */
    UFUNCTION(BlueprintCallable, Category = "Ability|Tasks", 
              meta = (DisplayName = "Play Montage and Wait (DJ01)",
                      HidePin = "OwningAbility",
                      DefaultToSelf = "OwningAbility",
                      BlueprintInternalUseOnly = "TRUE"))
    static UDJ01AbilityTask_PlayMontageAndWait* CreatePlayMontageAndWaitProxy(
        UGameplayAbility* OwningAbility,
        FName TaskInstanceName,
        UAnimMontage* MontageToPlay,
        float Rate = 1.0f,
        FName StartSection = NAME_None,
        bool bStopWhenAbilityEnds = true,
        float AnimRootMotionTranslationScale = 1.0f);

    //========================================
    // 委托
    //========================================
    
    /** 蒙太奇播放完成 */
    UPROPERTY(BlueprintAssignable)
    FDJ01MontageNotifyDelegate OnCompleted;
    
    /** 蒙太奇被混合打断 */
    UPROPERTY(BlueprintAssignable)
    FDJ01MontageNotifyDelegate OnBlendOut;
    
    /** 蒙太奇被中断 */
    UPROPERTY(BlueprintAssignable)
    FDJ01MontageNotifyDelegate OnInterrupted;
    
    /** 蒙太奇被取消 */
    UPROPERTY(BlueprintAssignable)
    FDJ01MontageNotifyDelegate OnCancelled;
    
    /** 收到动画事件通知 */
    UPROPERTY(BlueprintAssignable)
    FDJ01MontageEventDelegate OnGameplayEventReceived;

    //========================================
    // UAbilityTask 接口
    //========================================
    
    virtual void Activate() override;
    virtual void ExternalCancel() override;
    virtual void OnDestroy(bool bInOwnerFinished) override;

protected:
    UPROPERTY()
    TObjectPtr<UAnimMontage> MontageToPlay;
    
    float Rate;
    FName StartSection;
    float AnimRootMotionTranslationScale;
    bool bStopWhenAbilityEnds;
    
    void OnMontageEnded(UAnimMontage* Montage, bool bInterrupted);
    void OnMontageBlendingOut(UAnimMontage* Montage, bool bInterrupted);
    void OnGameplayEvent(FGameplayTag EventTag, const FGameplayEventData* Payload);
    
    FOnMontageEnded EndedDelegate;
    FOnMontageBlendingOut BlendingOutDelegate;
    FDelegateHandle EventHandle;
};
```

### 4.3 蓝图使用示例

```
[ActivateAbility]
       │
       ▼
┌──────────────────────────────────────┐
│ Play Montage and Wait (DJ01)         │
│ ┌──────────────────────────────────┐ │
│ │ Montage: AM_LightAttack_01       │ │
│ │ Rate: 1.0                        │ │
│ │ Stop When Ability Ends: ✓       │ │
│ └──────────────────────────────────┘ │
│                                      │
│ ○ On Completed ──────→ [EndAbility] │
│ ○ On Interrupted ────→ [EndAbility] │
│ ○ On Gameplay Event ─→ [处理事件]   │
│   └─ Event Tag: Event.Animation.*   │
└──────────────────────────────────────┘
```

---

## 更新日志

| 日期 | 变更内容 |
|-----|---------|
| 2024-12 | 从主文档拆分 |