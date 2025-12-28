// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01AnimInstance.h"
#include "AbilitySystemGlobals.h"
#include "DJ01/Character/Public/DJ01Character.h"
#include "DJ01/Character/Public/DJ01CharacterMovementComponent.h"

#if WITH_EDITOR
#include "Misc/DataValidation.h"
#endif

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01AnimInstance)


UDJ01AnimInstance::UDJ01AnimInstance(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
	// 自动初始化 GameplayTag 到变量的映射
	// 由 Tag Manager 自动生成，无需手动配置
	DJ01_ANIM_INSTANCE_INIT_TAG_MAPPINGS()
}

void UDJ01AnimInstance::InitializeWithAbilitySystem(UAbilitySystemComponent* ASC)
{
	check(ASC);

	// 解析属性引用（此时类信息已完整）
	GameplayTagPropertyMap.ResolveProperties(GetClass());
	
	// 初始化映射
	GameplayTagPropertyMap.Initialize(this, ASC);
	
	UE_LOG(LogTemp, Log, TEXT("DJ01AnimInstance: Initialized %d tag-to-property mappings"), 
		GameplayTagPropertyMap.GetMappingCount());
}

#if WITH_EDITOR
EDataValidationResult UDJ01AnimInstance::IsDataValid(FDataValidationContext& Context) const
{
	Super::IsDataValid(Context);

	GameplayTagPropertyMap.IsDataValid(this, Context);

	return ((Context.GetNumErrors() > 0) ? EDataValidationResult::Invalid : EDataValidationResult::Valid);
}
#endif // WITH_EDITOR

void UDJ01AnimInstance::NativeInitializeAnimation()
{
	Super::NativeInitializeAnimation();

	if (AActor* OwningActor = GetOwningActor())
	{
		if (UAbilitySystemComponent* ASC = UAbilitySystemGlobals::GetAbilitySystemComponentFromActor(OwningActor))
		{
			InitializeWithAbilitySystem(ASC);
		}
	}
}

void UDJ01AnimInstance::NativeUpdateAnimation(float DeltaSeconds)
{
	Super::NativeUpdateAnimation(DeltaSeconds);

	const ADJ01Character* Character = Cast<ADJ01Character>(GetOwningActor());
	if (!Character)
	{
		return;
	}

	UDJ01CharacterMovementComponent* CharMoveComp = CastChecked<UDJ01CharacterMovementComponent>(Character->GetCharacterMovement());
	
	//========================================
	// 物理状态 - 从 CharacterMovement 读取
	//========================================
	
	// 地面距离
	const FDJ01CharacterGroundInfo& GroundInfo = CharMoveComp->GetGroundInfo();
	GroundDistance = GroundInfo.GroundDistance;
	
	// 移动速度 (XY平面)
	GroundSpeed = CharMoveComp->Velocity.Size2D();
	
	//========================================
	// 逻辑状态 - 由 GameplayTagPropertyMap 自动处理
	// 无需在此手动更新，Tag 变化时会自动同步到对应变量
	//========================================
}
