// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "GameplayEffectExecutionCalculation.h"

#include "DJ01DamageExecution.generated.h"

class UObject;


/**
 * UDJ01DamageExecution
 *
 * 伤害执行计算 - 用于通过 GameplayEffect 对目标造成伤害
 * 
 * 主要功能:
 * - 从源对象的 CombatSet 获取 BaseDamage
 * - 应用距离衰减和物理材质衰减
 * - 检查团队关系，决定是否允许伤害
 * - 将最终伤害输出到目标的 HealthSet.Damage 元属性
 */
UCLASS()
class DJ01_API UDJ01DamageExecution : public UGameplayEffectExecutionCalculation
{
	GENERATED_BODY()

public:

	UDJ01DamageExecution();

protected:

	virtual void Execute_Implementation(const FGameplayEffectCustomExecutionParameters& ExecutionParams, FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const override;
};