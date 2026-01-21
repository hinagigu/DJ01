// ============================================================
// DJ01HealEffect.h
// 治疗效果
// ============================================================

#pragma once

#include "CoreMinimal.h"
#include "DJ01AbilityEffect.h"
#include "DJ01DamageEffect.h"

#include "DJ01HealEffect.generated.h"

class UGameplayEffect;

/**
 * UDJ01HealEffect
 * 
 * 治疗效果 - 计算并应用治疗
 * 支持基础治疗 + 属性缩放
 */
UCLASS(meta = (DisplayName = "Heal Effect"))
class DJ01_API UDJ01HealEffect : public UDJ01AbilityEffect
{
    GENERATED_BODY()

public:
    UDJ01HealEffect();

    //~ Begin UDJ01AbilityEffect Interface
    virtual bool Execute_Implementation(FDJ01EffectContext& Context) override;
    virtual FString GetEffectDescription_Implementation() const override;
    virtual FText GetEffectTypeName() const override;
    //~ End UDJ01AbilityEffect Interface

protected:
    /** 基础治疗量 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Heal", meta = (ClampMin = "0.0"))
    float BaseHeal = 0.0f;

    /** 属性缩放列表 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Heal")
    TArray<FDJ01AttributeScaling> AttributeScalings;

    /** 是否治疗自己（否则治疗目标） */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Heal")
    bool bHealSelf = false;

    /** 用于应用治疗的 GameplayEffect */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Heal")
    TSubclassOf<UGameplayEffect> HealGameplayEffect;

public:
    /** 计算最终的原始治疗量 */
    UFUNCTION(BlueprintCallable, Category = "Heal")
    float CalculateRawHeal(const FDJ01EffectContext& Context) const;
};