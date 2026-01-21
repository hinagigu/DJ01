// ============================================================
// UDJ01HealExecution
// 自动生成，可根据需要修改计算逻辑
// 生成时间: 2026-01-05 10:24:53
// ============================================================

#pragma once

#include "CoreMinimal.h"
#include "GameplayEffectExecutionCalculation.h"
#include "UDJ01HealExecution.generated.h"

/** 通用治疗计算 - 接收技能层计算的原始治疗量，可应用治疗增益/减益效果 */
UCLASS()
class DJ01_API UDJ01HealExecution : public UGameplayEffectExecutionCalculation
{
    GENERATED_BODY()

public:
    UDJ01HealExecution();

    virtual void Execute_Implementation(
        const FGameplayEffectCustomExecutionParameters& ExecutionParams,
        FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const override;
};
