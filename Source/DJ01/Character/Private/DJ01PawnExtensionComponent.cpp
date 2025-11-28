// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01/Character/Public/DJ01PawnExtensionComponent.h"
#include "DJ01/Character/Public/DJ01PawnData.h"
#include "DJ01/System/Public/DJ01GameplayTags.h"
#include "Components/GameFrameworkComponentManager.h"
#include "GameFramework/Controller.h"
#include "GameFramework/Pawn.h"
#include "Net/UnrealNetwork.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"

#include "WorldPartition/ContentBundle/ContentBundleLog.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01PawnExtensionComponent)

class FLifetimeProperty;
class UActorComponent;

const FName UDJ01PawnExtensionComponent::NAME_ActorFeatureName("PawnExtension");

UDJ01PawnExtensionComponent::UDJ01PawnExtensionComponent(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
	PrimaryComponentTick.bStartWithTickEnabled = false;
	PrimaryComponentTick.bCanEverTick = false;

	SetIsReplicatedByDefault(true);

	PawnData = nullptr;
	AbilitySystemComponent = nullptr;
}

void UDJ01PawnExtensionComponent::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
	Super::GetLifetimeReplicatedProps(OutLifetimeProps);

	DOREPLIFETIME(UDJ01PawnExtensionComponent, PawnData);
}

void UDJ01PawnExtensionComponent::OnRegister()
{
	Super::OnRegister();

	const APawn* Pawn = GetPawn<APawn>();
	ensureAlwaysMsgf((Pawn != nullptr), TEXT("DJ01PawnExtensionComponent on [%s] can only be added to Pawn actors."), *GetNameSafe(GetOwner()));

	TArray<UActorComponent*> PawnExtensionComponents;
	GetOwner()->GetComponents(UDJ01PawnExtensionComponent::StaticClass(), PawnExtensionComponents);
	ensureAlwaysMsgf((PawnExtensionComponents.Num() == 1), TEXT("Only one DJ01PawnExtensionComponent should exist on [%s]."), *GetNameSafe(GetOwner()));

	// 尽早向初始化状态系统注册，这仅在游戏世界中有效
	RegisterInitStateFeature();
}

void UDJ01PawnExtensionComponent::BeginPlay()
{
	Super::BeginPlay();

	// 监听所有功能的变化
	BindOnActorInitStateChanged(NAME_None, FGameplayTag(), false);
	
	// 通知状态管理器我们已生成，然后尝试其余的默认初始化
	ensure(TryToChangeInitState(DJ01GameplayTags::InitState_Spawned));
	CheckDefaultInitialization();
}

void UDJ01PawnExtensionComponent::EndPlay(const EEndPlayReason::Type EndPlayReason)
{
	UninitializeAbilitySystem();
	UnregisterInitStateFeature();

	Super::EndPlay(EndPlayReason);
}

void UDJ01PawnExtensionComponent::SetPawnData(const UDJ01PawnData* InPawnData)
{
	check(InPawnData);

	APawn* Pawn = GetPawnChecked<APawn>();

	if (Pawn->GetLocalRole() != ROLE_Authority)
	{
		return;
	}

	if (PawnData)
	{
		UE_LOG(LogTemp, Error, TEXT("Trying to set PawnData [%s] on pawn [%s] that already has valid PawnData [%s]."), 
			*GetNameSafe(InPawnData), *GetNameSafe(Pawn), *GetNameSafe(PawnData));
		return;
	}

	PawnData = InPawnData;

	Pawn->ForceNetUpdate();

	CheckDefaultInitialization();
}

void UDJ01PawnExtensionComponent::OnRep_PawnData()
{
	CheckDefaultInitialization();
}

void UDJ01PawnExtensionComponent::InitializeAbilitySystem(UDJ01AbilitySystemComponent* InASC, AActor* InOwnerActor)
{
	check(InASC);
	check(InOwnerActor);

	if (AbilitySystemComponent == InASC)
	{
		// AbilitySystem 组件未改变
		return;
	}

	if (AbilitySystemComponent)
	{
		// 清理旧的 AbilitySystem 组件
		UninitializeAbilitySystem();
	}

	APawn* Pawn = GetPawnChecked<APawn>();
	AActor* ExistingAvatar = InASC->GetAvatarActor();

	UE_LOG(LogTemp, Verbose, TEXT("Setting up ASC [%s] on pawn [%s] owner [%s], existing [%s]"), 
		*GetNameSafe(InASC), *GetNameSafe(Pawn), *GetNameSafe(InOwnerActor), *GetNameSafe(ExistingAvatar));

	if ((ExistingAvatar != nullptr) && (ExistingAvatar != Pawn))
	{
		UE_LOG(LogTemp, Log, TEXT("Existing avatar (authority=%d)"), ExistingAvatar->HasAuthority() ? 1 : 0);

		// 已经有一个 Pawn 充当 ASC 的 Avatar，所以我们需要将其踢出
		// 这可能发生在客户端延迟时：他们的新 Pawn 在旧 Pawn 被移除之前生成并被控制
		ensure(!ExistingAvatar->HasAuthority());

		if (UDJ01PawnExtensionComponent* OtherExtensionComponent = FindPawnExtensionComponent(ExistingAvatar))
		{
			OtherExtensionComponent->UninitializeAbilitySystem();
		}
	}

	AbilitySystemComponent = InASC;
	AbilitySystemComponent->InitAbilityActorInfo(InOwnerActor, Pawn);

	// 如果 PawnData 中配置了 TagRelationshipMapping，则设置到 ASC
	// if (ensure(PawnData))
	// {
	// 	InASC->SetTagRelationshipMapping(PawnData->TagRelationshipMapping);
	// }

	OnAbilitySystemInitialized.Broadcast();
}

void UDJ01PawnExtensionComponent::UninitializeAbilitySystem()
{
	if (!AbilitySystemComponent)
	{
		return;
	}

	// 如果我们仍然是 Avatar Actor，则取消初始化 ASC（否则另一个 Pawn 在成为 Avatar Actor 时已经这样做了）
	if (AbilitySystemComponent->GetAvatarActor() == GetOwner())
	{
		FGameplayTagContainer AbilityTypesToIgnore;
		// AbilityTypesToIgnore.AddTag(DJ01GameplayTags::Ability_Behavior_SurvivesDeath);

		AbilitySystemComponent->CancelAbilities(nullptr, &AbilityTypesToIgnore);
		AbilitySystemComponent->ClearAbilityInput();
		AbilitySystemComponent->RemoveAllGameplayCues();

		if (AbilitySystemComponent->GetOwnerActor() != nullptr)
		{
			AbilitySystemComponent->SetAvatarActor(nullptr);
		}
		else
		{
			// 如果 ASC 没有有效的 Owner，我们需要清除所有 Actor 信息，而不仅仅是 Avatar 配对
			AbilitySystemComponent->ClearActorInfo();
		}

		OnAbilitySystemUninitialized.Broadcast();
	}

	AbilitySystemComponent = nullptr;
}

void UDJ01PawnExtensionComponent::HandleControllerChanged()
{
	if (AbilitySystemComponent && (AbilitySystemComponent->GetAvatarActor() == GetPawnChecked<APawn>()))
	{
		ensure(AbilitySystemComponent->AbilityActorInfo->OwnerActor == AbilitySystemComponent->GetOwnerActor());
		if (AbilitySystemComponent->GetOwnerActor() == nullptr)
		{
			UninitializeAbilitySystem();
		}
		else
		{
			AbilitySystemComponent->RefreshAbilityActorInfo();
		}
	}

	CheckDefaultInitialization();
}

void UDJ01PawnExtensionComponent::HandlePlayerStateReplicated()
{
	CheckDefaultInitialization();
}

void UDJ01PawnExtensionComponent::SetupPlayerInputComponent()
{
	CheckDefaultInitialization();
}

void UDJ01PawnExtensionComponent::CheckDefaultInitialization()
{
	// 在检查我们的进度之前，尝试推进我们可能依赖的任何其他功能
	CheckDefaultInitializationForImplementers();

	// 初始化状态链：Spawned -> DataAvailable -> DataInitialized -> GameplayReady
	static const TArray<FGameplayTag> StateChain = { 
		DJ01GameplayTags::InitState_Spawned, 
		DJ01GameplayTags::InitState_DataAvailable, 
		DJ01GameplayTags::InitState_DataInitialized, 
		DJ01GameplayTags::InitState_GameplayReady 
	};

	// 这将尝试从 Spawned（仅在 BeginPlay 中设置）通过数据初始化阶段进行，直到达到 GameplayReady
	ContinueInitStateChain(StateChain);
}

bool UDJ01PawnExtensionComponent::CanChangeInitState(UGameFrameworkComponentManager* Manager, FGameplayTag CurrentState, FGameplayTag DesiredState) const
{
	check(Manager);

	APawn* Pawn = GetPawn<APawn>();
	const bool bIsServer = GetWorld()->GetNetMode() != NM_Client;
	const FString NetPrefix = bIsServer ? TEXT("[服务端]") : TEXT("[客户端]");
	FString StateChangeInfo = FString::Printf(TEXT("%s PawnExtension 状态转换: %s -> %s"), *NetPrefix, 
		*CurrentState.ToString(), *DesiredState.ToString());

	bool bCanChange = false;
	FString FailReason;

	// 无状态 -> Spawned
	if (!CurrentState.IsValid() && DesiredState == DJ01GameplayTags::InitState_Spawned)
	{
		// 只要我们在有效的 Pawn 上，我们就算作已生成
		if (Pawn)
		{
			bCanChange = true;
		}
		else
		{
			FailReason = TEXT("缺少有效的Pawn");
		}
	}
	// Spawned -> DataAvailable
	else if (CurrentState == DJ01GameplayTags::InitState_Spawned && DesiredState == DJ01GameplayTags::InitState_DataAvailable)
	{
		// 需要 PawnData
		if (!PawnData)
		{
			FailReason = TEXT("缺少PawnData");
			// UE_LOG(LogTemp, Error, TEXT("[UDJ01PawnExtensionComponent::CanChangeInitState] Pawn [%s] is missing PawnData."), *GetNameSafe(Pawn));
			bCanChange = false;
		}
		else
		{
			const bool bHasAuthority = Pawn->HasAuthority();
			const bool bIsLocallyControlled = Pawn->IsLocallyControlled();

			if (bHasAuthority || bIsLocallyControlled)
			{
				// 检查是否被 Controller 控制
				if (!GetController<AController>())
				{
					FailReason = TEXT("缺少Controller");
					bCanChange = false;
				}
				else
				{
					bCanChange = true;
				}
			}
			else
			{
				bCanChange = true;
			}
		}
	}
	// DataAvailable -> DataInitialized
	else if (CurrentState == DJ01GameplayTags::InitState_DataAvailable && DesiredState == DJ01GameplayTags::InitState_DataInitialized)
	{
		// 如果所有功能都达到了 DataAvailable，则转换到 DataInitialized
		if (!Manager->HaveAllFeaturesReachedInitState(Pawn, DJ01GameplayTags::InitState_DataAvailable))
		{
			FailReason = TEXT("并非所有功能都达到了DataAvailable状态");
			bCanChange = false;
		}
		else
		{
			bCanChange = true;
		}
	}
	// DataInitialized -> GameplayReady
	else if (CurrentState == DJ01GameplayTags::InitState_DataInitialized && DesiredState == DJ01GameplayTags::InitState_GameplayReady)
	{
		bCanChange = true;
	}
	else
	{
		FailReason = TEXT("未知的状态转换");
		bCanChange = false;
	}

	if (bCanChange)
	{
		UE_LOG(LogTemp, Log, TEXT("%s: 转换成功"), *StateChangeInfo);
	}
	else
	{
		UE_LOG(LogTemp, Warning, TEXT("%s: 转换失败, 原因: %s"), *StateChangeInfo, *FailReason);
	}

	return bCanChange;
}

void UDJ01PawnExtensionComponent::HandleChangeInitState(UGameFrameworkComponentManager* Manager, FGameplayTag CurrentState, FGameplayTag DesiredState)
{
	if (DesiredState == DJ01GameplayTags::InitState_DataInitialized)
	{
		// 这目前全部由监听此状态变化的其他组件处理
	}
}

void UDJ01PawnExtensionComponent::OnActorInitStateChanged(const FActorInitStateChangedParams& Params)
{
	// 如果另一个功能现在处于 DataAvailable，查看我们是否应该转换到 DataInitialized
	if (Params.FeatureName != NAME_ActorFeatureName)
	{
		if (Params.FeatureState == DJ01GameplayTags::InitState_DataAvailable)
		{
			CheckDefaultInitialization();
		}
	}
}

void UDJ01PawnExtensionComponent::OnAbilitySystemInitialized_RegisterAndCall(FSimpleMulticastDelegate::FDelegate Delegate)
{
	if (!OnAbilitySystemInitialized.IsBoundToObject(Delegate.GetUObject()))
	{
		OnAbilitySystemInitialized.Add(Delegate);
	}

	if (AbilitySystemComponent)
	{
		Delegate.Execute();
	}
}

void UDJ01PawnExtensionComponent::OnAbilitySystemUninitialized_Register(FSimpleMulticastDelegate::FDelegate Delegate)
{
	if (!OnAbilitySystemUninitialized.IsBoundToObject(Delegate.GetUObject()))
	{
		OnAbilitySystemUninitialized.Add(Delegate);
	}
}