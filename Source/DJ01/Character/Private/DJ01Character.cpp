// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01/Character/Public/DJ01Character.h"
#include "DJ01/Character/Public/DJ01PawnExtensionComponent.h"
#include "DJ01/Character/Public/DJ01CharacterMovementComponent.h"
#include "DJ01/Camera/Public/DJ01CameraComponent.h"
#include "Components/CapsuleComponent.h"
#include "Components/SkeletalMeshComponent.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01Character)

static FName NAME_DJ01CharacterCollisionProfile_Capsule(TEXT("DJ01PawnCapsule"));
static FName NAME_DJ01CharacterCollisionProfile_Mesh(TEXT("DJ01PawnMesh"));

ADJ01Character::ADJ01Character(const FObjectInitializer& ObjectInitializer)
    : Super(ObjectInitializer.SetDefaultSubobjectClass<UDJ01CharacterMovementComponent>(ACharacter::CharacterMovementComponentName))
{
    // 尽可能避免角色 Tick
    PrimaryActorTick.bCanEverTick = false;
    PrimaryActorTick.bStartWithTickEnabled = false;

    // 网络剔除距离
    NetCullDistanceSquared = 900000000.0f;

    // 配置碰撞胶囊体
    UCapsuleComponent* CapsuleComp = GetCapsuleComponent();
    check(CapsuleComp);
    CapsuleComp->InitCapsuleSize(40.0f, 90.0f);
    CapsuleComp->SetCollisionProfileName(NAME_DJ01CharacterCollisionProfile_Capsule);

    // 配置骨骼网格
    USkeletalMeshComponent* MeshComp = GetMesh();
    check(MeshComp);
    MeshComp->SetRelativeRotation(FRotator(0.0f, -90.0f, 0.0f));  // 旋转网格使其朝向 X 轴，因为它导出时朝向 Y 轴
    MeshComp->SetCollisionProfileName(NAME_DJ01CharacterCollisionProfile_Mesh);

    // 配置移动组件
    UDJ01CharacterMovementComponent* DJ01MoveComp = CastChecked<UDJ01CharacterMovementComponent>(GetCharacterMovement());
    // 移动组件的具体配置已在 UDJ01CharacterMovementComponent 的构造函数中完成

    // 配置旋转 - RPG 通常使用移动方向旋转
    bUseControllerRotationPitch = false;
    bUseControllerRotationYaw = false;  // 改为 false，让移动组件控制旋转
    bUseControllerRotationRoll = false;

    // 配置视角高度
    BaseEyeHeight = 80.0f;
    CrouchedEyeHeight = 50.0f;

    // 创建 PawnExtension 组件 - 管理整个 Pawn 的生命周期
    PawnExtComponent = CreateDefaultSubobject<UDJ01PawnExtensionComponent>(TEXT("PawnExtensionComponent"));
	
    // AbilitySystem 相关的委托注册
    PawnExtComponent->OnAbilitySystemInitialized_RegisterAndCall(FSimpleMulticastDelegate::FDelegate::CreateUObject(this, &ThisClass::OnAbilitySystemInitialized));
    PawnExtComponent->OnAbilitySystemUninitialized_Register(FSimpleMulticastDelegate::FDelegate::CreateUObject(this, &ThisClass::OnAbilitySystemUninitialized));

    // 创建 Camera 组件 - 处理相机
    CameraComponent = CreateDefaultSubobject<UDJ01CameraComponent>(TEXT("CameraComponent"));
    CameraComponent->SetRelativeLocation(FVector(-300.0f, 0.0f, 75.0f));
}

void ADJ01Character::PreInitializeComponents()
{
    Super::PreInitializeComponents();
}

void ADJ01Character::BeginPlay()
{
    Super::BeginPlay();
}

void ADJ01Character::EndPlay(const EEndPlayReason::Type EndPlayReason)
{
    Super::EndPlay(EndPlayReason);
}

void ADJ01Character::Reset()
{
    // 禁用移动和碰撞
    if (Controller)
    {
        Controller->SetIgnoreMoveInput(true);
    }

    UCapsuleComponent* CapsuleComp = GetCapsuleComponent();
    check(CapsuleComp);
    CapsuleComp->SetCollisionEnabled(ECollisionEnabled::NoCollision);
    CapsuleComp->SetCollisionResponseToAllChannels(ECR_Ignore);

    K2_OnReset();

    // TODO: 可能需要额外的清理逻辑
}

void ADJ01Character::PossessedBy(AController* NewController)
{
    Super::PossessedBy(NewController);

    // 通知 PawnExtComponent Controller 已改变
    PawnExtComponent->HandleControllerChanged();
}

void ADJ01Character::UnPossessed()
{
    Super::UnPossessed();

    // 通知 PawnExtComponent Controller 已改变
    PawnExtComponent->HandleControllerChanged();
}

void ADJ01Character::OnRep_Controller()
{
    Super::OnRep_Controller();

    // 通知 PawnExtComponent Controller 已改变
    PawnExtComponent->HandleControllerChanged();
}

void ADJ01Character::OnRep_PlayerState()
{
    Super::OnRep_PlayerState();

    // 通知 PawnExtComponent PlayerState 已复制
    PawnExtComponent->HandlePlayerStateReplicated();
}

void ADJ01Character::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
    Super::SetupPlayerInputComponent(PlayerInputComponent);

    // 委托给 PawnExtensionComponent，它会协调初始化
    // PawnExtensionComponent 会在适当的时机通知其他组件（如 HeroComponent）进行输入设置
    PawnExtComponent->SetupPlayerInputComponent();
}

//~ Begin IAbilitySystemInterface
UAbilitySystemComponent* ADJ01Character::GetAbilitySystemComponent() const
{
    if (PawnExtComponent == nullptr)
    {
        return nullptr;
    }

    return PawnExtComponent->GetDJ01AbilitySystemComponent();
}
//~ End IAbilitySystemInterface

//~ Begin IGameplayTagAssetInterface
void ADJ01Character::GetOwnedGameplayTags(FGameplayTagContainer& TagContainer) const
{
    if (const UDJ01AbilitySystemComponent* ASC = Cast<UDJ01AbilitySystemComponent>(GetAbilitySystemComponent()))
    {
        ASC->GetOwnedGameplayTags(TagContainer);
    }
}

bool ADJ01Character::HasMatchingGameplayTag(FGameplayTag TagToCheck) const
{
    if (const UDJ01AbilitySystemComponent* ASC = Cast<UDJ01AbilitySystemComponent>(GetAbilitySystemComponent()))
    {
        return ASC->HasMatchingGameplayTag(TagToCheck);
    }

    return false;
}

bool ADJ01Character::HasAllMatchingGameplayTags(const FGameplayTagContainer& TagContainer) const
{
    if (const UDJ01AbilitySystemComponent* ASC = Cast<UDJ01AbilitySystemComponent>(GetAbilitySystemComponent()))
    {
        return ASC->HasAllMatchingGameplayTags(TagContainer);
    }

    return false;
}

bool ADJ01Character::HasAnyMatchingGameplayTags(const FGameplayTagContainer& TagContainer) const
{
    if (const UDJ01AbilitySystemComponent* ASC = Cast<UDJ01AbilitySystemComponent>(GetAbilitySystemComponent()))
    {
        return ASC->HasAnyMatchingGameplayTags(TagContainer);
    }

    return false;
}
//~ End IGameplayTagAssetInterface

void ADJ01Character::OnAbilitySystemInitialized()
{
    UDJ01AbilitySystemComponent* ASC = Cast<UDJ01AbilitySystemComponent>(GetAbilitySystemComponent());
    check(ASC);

    // 可以在这里初始化其他依赖 AbilitySystem 的组件
    // 例如：HealthComponent->InitializeWithAbilitySystem(ASC);
}

void ADJ01Character::OnAbilitySystemUninitialized()
{
    // 清理 AbilitySystem 相关内容
    // 例如：HealthComponent->UninitializeFromAbilitySystem();
}
