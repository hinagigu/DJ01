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
	// 仅从 Montage 提取 Root Motion
	// 普通移动动画使用 CharacterMovement，攻击/技能 Montage 使用 Root Motion
	RootMotionMode = ERootMotionMode::RootMotionFromMontagesOnly;
}

void UDJ01AnimInstance::TryInitializeGASBindings()
{
	if (bGASBindingsInitialized)
	{
		return;
	}

	AActor* OwningActor = GetOwningActor();
	if (!OwningActor)
	{
		return;
	}

	UAbilitySystemComponent* ASC = UAbilitySystemGlobals::GetAbilitySystemComponentFromActor(OwningActor);
	if (!ASC)
	{
		return; // ASC 还没准备好，下次再试
	}

	InitializeWithAbilitySystem(ASC);
	bGASBindingsInitialized = true;
}

void UDJ01AnimInstance::InitializeWithAbilitySystem(UAbilitySystemComponent* ASC)
{
	check(ASC);

	// 初始化 BindingSet - 自动注册 GAS 监听并同步初始值
	// 注意：宏内部已包含安全检查，AttributeSet 不存在时会使用默认值
	InitBindingSet_AnimState(ASC);

	// 解析属性引用（此时类信息已完整）
	GameplayTagPropertyMap.ResolveProperties(GetClass());
	
	// 初始化映射
	GameplayTagPropertyMap.Initialize(this, ASC);
	
	UE_LOG(LogTemp, Log, TEXT("DJ01AnimInstance: Initialized AnimState BindingSet + %d tag-to-property mappings"), 
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

	// 尝试初始化 GAS 绑定（可能会失败，因为 ASC 可能还没准备好）
	TryInitializeGASBindings();
}

void UDJ01AnimInstance::NativeUpdateAnimation(float DeltaSeconds)
{
	Super::NativeUpdateAnimation(DeltaSeconds);

	// 懒初始化：如果之前初始化失败，在这里重试
	if (!bGASBindingsInitialized)
	{
		TryInitializeGASBindings();
	}

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
	
	// 移动方向 (相对于角色朝向)
	if (GroundSpeed > 1.0f)
	{
		const FVector Velocity = CharMoveComp->Velocity;
		const FRotator ActorRotation = Character->GetActorRotation();
		MoveDirection = CalculateDirection(Velocity, ActorRotation);
	}
	// 速度太低时保持上一帧的方向，避免抖动
	
	//========================================
	// 空中物理状态
	//========================================
	
	const bool bWasFalling = bIsFalling;
	bIsFalling = CharMoveComp->IsFalling();
	
	// 空中计时
	if (bIsFalling)
	{
		TimeInAir += DeltaSeconds;
	}
	else if (bWasFalling)
	{
		// 刚落地时重置
		TimeInAir = 0.0f;
	}
	
	//========================================
	// 逻辑状态 - 由 BindingSet 自动处理
	// bHasJumped, bIsInAir 等由 GAS Tag 变化时自动同步
	//========================================
}
