// ============================================================
// DJ01DamageEffect.h
// 伤害效果
// ============================================================

#pragma once

#include "CoreMinimal.h"
#include "DJ01AbilityEffect.h"
#include "DJ01DamageTypes.h"

#include "DJ01DamageEffect.generated.h"

class UGameplayEffect;
class UAbilitySystemComponent;

/**
 * 属性缩放配置
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AttributeScaling
{
    GENERATED_BODY()

    /** 属性名称 (AttackPower, AbilityPower, MaxHealth 等) */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly)
    FName AttributeName;

    /** 缩放比例 (0.75 = 75%) */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, meta = (ClampMin = "0.0"))
    float Ratio = 0.0f;
};

/**
 * UDJ01DamageEffect
 * 
 * 伤害效果 - 计算并应用伤害
 * 支持基础伤害 + 属性缩放
 */
UCLASS(meta = (DisplayName = "Damage Effect"))
class DJ01_API UDJ01DamageEffect : public UDJ01AbilityEffect
{
    GENERATED_BODY()

public:
    UDJ01DamageEffect();

    //~ Begin UDJ01AbilityEffect Interface
    virtual bool Execute_Implementation(FDJ01EffectContext& Context) override;
    virtual FString GetEffectDescription_Implementation() const override;
    virtual FText GetEffectTypeName() const override;
    //~ End UDJ01AbilityEffect Interface

protected:
    /** 基础伤害值 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Damage", meta = (ClampMin = "0.0"))
    float BaseDamage = 0.0f;

    /** 伤害类型 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Damage")
    EDJ01DamageType DamageType = EDJ01DamageType::Physical;

    /** 属性缩放列表 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Damage")
    TArray<FDJ01AttributeScaling> AttributeScalings;

    /** 用于应用伤害的 GameplayEffect */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Damage")
    TSubclassOf<UGameplayEffect> DamageGameplayEffect;

public:
    /** 计算最终的原始伤害 */
    UFUNCTION(BlueprintCallable, Category = "Damage")
    float CalculateRawDamage(const FDJ01EffectContext& Context) const;

    /** 从 ASC 获取指定属性值 */
    UFUNCTION(BlueprintCallable, Category = "Damage")
    static float GetAttributeValue(UAbilitySystemComponent* ASC, FName AttributeName);
};