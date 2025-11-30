// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "GameplayEffectExecutionCalculation.h"

#include "DJ01HealExecution.generated.h"

class UObject;


/**
 * UDJ01HealExecution
 *
 * 治疗执行计算 - 用于通过 GameplayEffect 对目标进行治疗
 * 
 * 主要功能:
 * - 从源对象的 CombatSet 获取 BaseHeal
 * - 将最终治疗量输出到目标的 HealthSet.Healing 元属性
 */
UCLASS()
class DJ01_API UDJ01HealExecution : public UGameplayEffectExecutionCalculation
{
	GENERATED_BODY()

public:

	UDJ01HealExecution();

protected:

	virtual void Execute_Implementation(const FGameplayEffectCustomExecutionParameters& ExecutionParams, FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const override;
};