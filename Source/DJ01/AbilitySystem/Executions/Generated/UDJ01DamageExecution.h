// ============================================================
// UDJ01DamageExecution
// 自动生成，可根据需要修改计算逻辑
// 生成时间: 2026-01-05 10:24:53
// ============================================================

#pragma once

#include "CoreMinimal.h"
#include "GameplayEffectExecutionCalculation.h"
#include "UDJ01DamageExecution.generated.h"

/** 通用伤害计算 - 接收技能层计算的原始伤害，应用护甲/魔抗减伤 */
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
