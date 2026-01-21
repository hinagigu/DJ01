// ============================================================
// DJ01AbilityEffect.h
// 技能效果系统 - 基类和核心定义
// ============================================================

#pragma once

#include "CoreMinimal.h"
#include "UObject/NoExportTypes.h"
#include "GameplayTagContainer.h"
#include "DJ01AbilityEffect.generated.h"

class UAbilitySystemComponent;
class UGameplayAbility;

/**
 * 效果触发阶段
 * 定义效果在技能生命周期中的触发时机
 */
UENUM(BlueprintType)
enum class EDJ01EffectPhase : uint8
{
    /** 技能激活时立即触发 */
    OnActivate UMETA(DisplayName = "On Activate (激活时)"),
    
    /** 资源消耗后触发（前摇结束） */
    OnCommit UMETA(DisplayName = "On Commit (消耗后)"),
    
    /** 动画事件触发（如伤害帧） */
    OnAnimEvent UMETA(DisplayName = "On Anim Event (动画事件)"),
    
    /** 技能结束时触发 */
    OnEnd UMETA(DisplayName = "On End (结束时)"),
    
    /** 手动触发（代码调用） */
    Manual UMETA(DisplayName = "Manual (手动)")
};

/**
 * 效果执行上下文
 * 包含效果执行所需的所有信息
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01EffectContext
{
    GENERATED_BODY()

    FDJ01EffectContext()
        : InstigatorASC(nullptr)
        , AbilityLevel(1)
        , EventMagnitude(0.f)
        , SourceAbility(nullptr)
    {}

    /** 拥有此技能的 ASC（施法者） */
    UPROPERTY(BlueprintReadWrite, Category = "Context")
    TObjectPtr<UAbilitySystemComponent> InstigatorASC;

    /** 目标 ASC 列表 */
    UPROPERTY(BlueprintReadWrite, Category = "Context")
    TArray<TObjectPtr<UAbilitySystemComponent>> TargetASCs;

    /** 触发此效果的事件 Tag */
    UPROPERTY(BlueprintReadWrite, Category = "Context")
    FGameplayTag EventTag;

    /** 技能等级 */
    UPROPERTY(BlueprintReadWrite, Category = "Context")
    int32 AbilityLevel;

    /** 事件附加数值（可选） */
    UPROPERTY(BlueprintReadWrite, Category = "Context")
    float EventMagnitude;

    /** 技能实例（可选，用于访问技能数据） */
    UPROPERTY(BlueprintReadWrite, Category = "Context")
    TObjectPtr<UGameplayAbility> SourceAbility;

    /** 获取有效的施法者 ASC */
    UAbilitySystemComponent* GetInstigatorASC() const 
    { 
        return InstigatorASC.Get(); 
    }

    /** 获取有效的目标 ASC 列表 */
    TArray<UAbilitySystemComponent*> GetValidTargetASCs() const;

    /** 是否有有效目标 */
    bool HasValidTargets() const;
};

/**
 * UDJ01AbilityEffect
 * 
 * 技能效果基类，类似 ActorComponent 的设计理念。
 * 每个效果负责一种具体行为（伤害、治疗、Buff等）。
 * 
 * 使用方式：
 * 1. 继承此类创建具体效果（UDJ01DamageEffect, UDJ01HealEffect 等）
 * 2. 在 UDJ01GameplayAbility 的 Effects 数组中添加效果
 * 3. 设置触发阶段，技能会在对应时机自动执行效果
 */
UCLASS(Abstract, Blueprintable, BlueprintType, EditInlineNew, DefaultToInstanced, 
       meta = (ShowWorldContextPin))
class DJ01_API UDJ01AbilityEffect : public UObject
{
    GENERATED_BODY()

public:
    UDJ01AbilityEffect();

    /** 效果显示名称（编辑器/UI显示用） */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Effect")
    FText DisplayName;

    /** 效果描述 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Effect", meta = (MultiLine = true))
    FText Description;

    /** 是否启用此效果 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Effect")
    bool bEnabled = true;

    /**
     * 执行效果
     * @param Context - 执行上下文，包含施法者和目标信息
     * @return 是否成功执行
     */
    UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category = "Effect")
    bool Execute(UPARAM(ref) FDJ01EffectContext& Context);
    virtual bool Execute_Implementation(FDJ01EffectContext& Context);

    /**
     * 获取效果描述文本
     * 用于技能提示 UI 显示
     */
    UFUNCTION(BlueprintNativeEvent, BlueprintPure, Category = "Effect")
    FString GetEffectDescription() const;
    virtual FString GetEffectDescription_Implementation() const;

    /**
     * 获取效果类型名称（用于编辑器显示）
     */
    virtual FText GetEffectTypeName() const;

#if WITH_EDITOR
    /** 编辑器中获取节点标题 */
    virtual FText GetNodeTitle() const;
#endif
};

/**
 * 效果条目
 * 将效果绑定到特定的触发阶段
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AbilityEffectEntry
{
    GENERATED_BODY()

    FDJ01AbilityEffectEntry()
        : Phase(EDJ01EffectPhase::OnAnimEvent)
    {}

    /** 触发阶段 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Trigger")
    EDJ01EffectPhase Phase;

    /** 
     * 事件 Tag（当 Phase = OnAnimEvent 时使用）
     * 如：Event.Animation.DamageFrame
     */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Trigger",
        meta = (EditCondition = "Phase == EDJ01EffectPhase::OnAnimEvent", EditConditionHides))
    FGameplayTag EventTag;

    /** 
     * 效果实例
     * Instanced 允许在技能资产中内联编辑
     */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Instanced, Category = "Effect")
    TObjectPtr<UDJ01AbilityEffect> Effect;

    /** 检查是否应该在当前阶段触发 */
    bool ShouldTrigger(EDJ01EffectPhase CurrentPhase, const FGameplayTag& CurrentEventTag) const;
};