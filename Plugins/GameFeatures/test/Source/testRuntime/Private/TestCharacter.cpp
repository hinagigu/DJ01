#include "TestCharacter.h"

ATestCharacter::ATestCharacter(const FObjectInitializer& ObjectInitializer)
    : Super(ObjectInitializer)
{
    // 设置默认值
    bUseControllerRotationPitch = false;
    bUseControllerRotationYaw = true;
    bUseControllerRotationRoll = false;
}

void ATestCharacter::BeginPlay()
{
    Super::BeginPlay();
}

void ATestCharacter::PawnClientRestart()
{
    Super::PawnClientRestart();
    
}

