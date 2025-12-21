// ============================================================
// UDJ01DamageExecution
// 自动生成，可根据需要修改计算逻辑
// 生成时间: 2025-12-21 20:07:26
// ============================================================

#pragma once

#include "CoreMinimal.h"
#include "GameplayEffectExecutionCalculation.h"
#include "UDJ01DamageExecution.generated.h"

/** Damage 计算 */
UCLASS()
class DJ01_API UDJ01DamageExecution : public UGameplayEffectExecutionCalculation
{
    GENERATED_BODY()

public:
    UDJ01DamageExecution();

    virtual void Execute_Implementation(
        const FGameplayEffectCustomExecutionParameters& ExecutionParams,
        FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const override;
};
