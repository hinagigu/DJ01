#pragma once

#include "CoreMinimal.h"
#include "ModularCharacter.h"
#include "TestCharacter.generated.h"

/**
 * 测试用角色类，用于测试GameFeature功能
 */
UCLASS()
class TESTRUNTIME_API ATestCharacter : public AModularCharacter
{
    GENERATED_BODY()

public:
    ATestCharacter(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

    // 重写APawn接口
    virtual void PawnClientRestart() override;

protected:
    virtual void BeginPlay() override;
};