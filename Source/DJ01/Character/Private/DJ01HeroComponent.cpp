// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Character/Public/DJ01HeroComponent.h"
#include "Components/GameFrameworkComponentDelegates.h"
#include "Logging/MessageLog.h"
#include "EnhancedInputSubsystems.h"
#include "DJ01/Character/Public/DJ01PawnExtensionComponent.h"
#include "DJ01/Character/Public/DJ01PawnData.h"
#include "DJ01/Input/Public/DJ01InputConfig.h"
#include "DJ01/Input/Public/DJ01InputComponent.h"
#include "DJ01/Camera/Public/DJ01CameraComponent.h"
#include "DJ01/System/Public/DJ01GameplayTags.h"
#include "Components/GameFrameworkComponentManager.h"
#include "DJ01/Camera/Public/DJ01CameraMode.h"
#include "UserSettings/EnhancedInputUserSettings.h"
#include "InputMappingContext.h"
#include "GameFramework/PlayerController.h"
#include "GameFramework/PlayerState.h"
#include "DJ01/Player/Public/DJ01PlayerState.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01HeroComponent)

#if WITH_EDITOR
#include "Misc/UObjectToken.h"
#endif	// WITH_EDITOR

namespace DJ01Hero
{
	static const float LookYawRate = 300.0f;
	static const float LookPitchRate = 165.0f;
};

const FName UDJ01HeroComponent::NAME_BindInputsNow("BindInputsNow");
const FName UDJ01HeroComponent::NAME_ActorFeatureName("Hero");

UDJ01HeroComponent::UDJ01HeroComponent(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
	AbilityCameraMode = nullptr;
	bReadyToBindInputs = false;
}

void UDJ01HeroComponent::OnRegister()
{
	Super::OnRegister();

	if (!GetPawn<APawn>())
	{
		UE_LOG(LogTemp, Error, TEXT("[UDJ01HeroComponent::OnRegister] This component has been added to a blueprint whose base class is not a Pawn. To use this component, it MUST be placed on a Pawn Blueprint."));

#if WITH_EDITOR
		if (GIsEditor)
		{
			static const FText Message = NSLOCTEXT("DJ01HeroComponent", "NotOnPawnError", "has been added to a blueprint whose base class is not a Pawn. To use this component, it MUST be placed on a Pawn Blueprint. This will cause a crash if you PIE!");
			static const FName HeroMessageLogName = TEXT("DJ01HeroComponent");
			
			FMessageLog(HeroMessageLogName).Error() 
				->AddToken(FUObjectToken::Create(this, FText::FromString(GetNameSafe(this))))
				->AddToken(FTextToken::Create(Message));
				
			FMessageLog(HeroMessageLogName).Open();
		}
#endif
	}
	else
	{
		// 尽早注册到初始化状态系统，仅在游戏世界中有效
		RegisterInitStateFeature();
	}
}

void UDJ01HeroComponent::BeginPlay()
{
	Super::BeginPlay();

	// 监听 PawnExtensionComponent 的初始化状态变化
	BindOnActorInitStateChanged(UDJ01PawnExtensionComponent::NAME_ActorFeatureName, FGameplayTag(), false);

	// 通知我们已完成生成，然后尝试其余的初始化
	ensure(TryToChangeInitState(DJ01GameplayTags::InitState_Spawned));
	CheckDefaultInitialization();
}

void UDJ01HeroComponent::EndPlay(const EEndPlayReason::Type EndPlayReason)
{
	UnregisterInitStateFeature();

	Super::EndPlay(EndPlayReason);
}

bool UDJ01HeroComponent::CanChangeInitState(UGameFrameworkComponentManager* Manager, FGameplayTag CurrentState, FGameplayTag DesiredState) const
{
	return CanChangeInitStateWithLog(Manager, CurrentState, DesiredState);
	// check(Manager);
	//
	// APawn* Pawn = GetPawn<APawn>();
	//
	// if (!CurrentState.IsValid() && DesiredState == DJ01GameplayTags::InitState_Spawned)
	// {
	// 	// 只要有真实的 Pawn，就允许我们转换
	// 	if (Pawn)
	// 	{
	// 		return true;
	// 	}
	// }
	// else if (CurrentState == DJ01GameplayTags::InitState_Spawned && DesiredState == DJ01GameplayTags::InitState_DataAvailable)
	// {
	// 	// PlayerState 是必需的
	// 	if (!GetPlayerState<APlayerState>())
	// 	{
	// 		return false;
	// 	}
	//
	// 	// 如果是权威端或自主代理，需要等待拥有 PlayerState 注册所有权的 Controller
	// 	if (Pawn->GetLocalRole() != ROLE_SimulatedProxy)
	// 	{
	// 		AController* Controller = GetController<AController>();
	//
	// 		const bool bHasControllerPairedWithPS = (Controller != nullptr) && \
	// 			(Controller->PlayerState != nullptr) && \
	// 			(Controller->PlayerState->GetOwner() == Controller);
	//
	// 		if (!bHasControllerPairedWithPS)
	// 		{
	// 			return false;
	// 		}
	// 	}
	//
	// 	const bool bIsLocallyControlled = Pawn->IsLocallyControlled();
	// 	const bool bIsBot = Pawn->IsBotControlled();
	//
	// 	if (bIsLocallyControlled && !bIsBot)
	// 	{
	// 		APlayerController* PC = GetController<APlayerController>();
	//
	// 		// 本地控制时需要输入组件和本地玩家
	// 		if (!Pawn->InputComponent || !PC || !PC->GetLocalPlayer())
	// 		{
	// 			return false;
	// 		}
	// 	}
	//
	// 	return true;
	// }
	// else if (CurrentState == DJ01GameplayTags::InitState_DataAvailable && DesiredState == DJ01GameplayTags::InitState_DataInitialized)
	// {
	// 	// 等待 PlayerState 和 PawnExtension 组件
	// 	APlayerState* PS = GetPlayerState<APlayerState>();
	//
	// 	return PS && Manager->HasFeatureReachedInitState(Pawn, UDJ01PawnExtensionComponent::NAME_ActorFeatureName, DJ01GameplayTags::InitState_DataInitialized);
	// }
	// else if (CurrentState == DJ01GameplayTags::InitState_DataInitialized && DesiredState == DJ01GameplayTags::InitState_GameplayReady)
	// {
	// 	// TODO_ABILITY_SYSTEM: 添加能力初始化检查
	// 	return true;
	// }
	//
	// return false;
}

void UDJ01HeroComponent::HandleChangeInitState(UGameFrameworkComponentManager* Manager, FGameplayTag CurrentState, FGameplayTag DesiredState)
{
	if (CurrentState == DJ01GameplayTags::InitState_DataAvailable && DesiredState == DJ01GameplayTags::InitState_DataInitialized)
	{
		APawn* Pawn = GetPawn<APawn>();
		APlayerState* PS = GetPlayerState<APlayerState>();
		if (!ensure(Pawn && PS))
		{
			return;
		}

		const UDJ01PawnData* PawnData = nullptr;

		if (UDJ01PawnExtensionComponent* PawnExtComp = UDJ01PawnExtensionComponent::FindPawnExtensionComponent(Pawn))
		{
			PawnData = PawnExtComp->GetPawnData<UDJ01PawnData>();

			// 初始化能力系统
			// PlayerState 持有此玩家的持久数据（跨死亡和多个 Pawn 持续的状态）
			// 能力系统组件和属性集存在于 PlayerState 上
			if (ADJ01PlayerState* DJ01PS = Cast<ADJ01PlayerState>(PS))
			{
				PawnExtComp->InitializeAbilitySystem(DJ01PS->GetDJ01AbilitySystemComponent(), DJ01PS);
			}
		}

		if (APlayerController* PC = GetController<APlayerController>())
		{
			if (Pawn->InputComponent != nullptr)
			{
				InitializePlayerInput(Pawn->InputComponent);
			}
		}

		// 为所有 Pawn 连接委托，以防稍后观战
		if (PawnData)
		{
			if (UDJ01CameraComponent* CameraComponent = UDJ01CameraComponent::FindCameraComponent(Pawn))
			{
				CameraComponent->DetermineCameraModeDelegate.BindUObject(this, &ThisClass::DetermineCameraMode);
			}
		}
	}
}

void UDJ01HeroComponent::OnActorInitStateChanged(const FActorInitStateChangedParams& Params)
{
	if (Params.FeatureName == UDJ01PawnExtensionComponent::NAME_ActorFeatureName)
	{
		if (Params.FeatureState == DJ01GameplayTags::InitState_DataInitialized || Params.FeatureState == DJ01GameplayTags::InitState_GameplayReady)
		{
			// 如果扩展组件表示所有其他组件都已初始化，尝试进入下一个状态
			CheckDefaultInitialization();
		}
	}
}

bool UDJ01HeroComponent::CanChangeInitStateWithLog(UGameFrameworkComponentManager* Manager, FGameplayTag CurrentState, FGameplayTag DesiredState) const
{
	check(Manager);

	APawn* Pawn = GetPawn<APawn>();
	const bool bIsServer = GetWorld()->GetNetMode() != NM_Client;
	const FString NetPrefix = bIsServer ? TEXT("[服务端]") : TEXT("[客户端]");
	FString StateChangeInfo = FString::Printf(TEXT("%s 状态转换: %s -> %s"), *NetPrefix, 
		*CurrentState.ToString(), *DesiredState.ToString());
	
	bool bCanChange = false;
	FString FailReason;

	if (!CurrentState.IsValid() && DesiredState == DJ01GameplayTags::InitState_Spawned)
	{
		// 只要有真实的 Pawn，就允许我们转换
		if (Pawn)
		{
			bCanChange = true;
		}
		else
		{
			FailReason = TEXT("缺少有效的Pawn");
		}
	}
	else if (CurrentState == DJ01GameplayTags::InitState_Spawned && DesiredState == DJ01GameplayTags::InitState_DataAvailable)
	{
		// PlayerState 是必需的
		if (!GetPlayerState<APlayerState>())
		{
			FailReason = TEXT("缺少PlayerState");
			bCanChange = false;
		}
		// 如果是权威端或自主代理，需要等待拥有 PlayerState 注册所有权的 Controller
		else if (Pawn->GetLocalRole() != ROLE_SimulatedProxy)
		{
			AController* Controller = GetController<AController>();

			const bool bHasControllerPairedWithPS = (Controller != nullptr) && \
				(Controller->PlayerState != nullptr) && \
				(Controller->PlayerState->GetOwner() == Controller);

			if (!bHasControllerPairedWithPS)
			{
				FailReason = TEXT("Controller与PlayerState未正确配对");
				bCanChange = false;
			}
			else
			{
				const bool bIsLocallyControlled = Pawn->IsLocallyControlled();
				const bool bIsBot = Pawn->IsBotControlled();

				if (bIsLocallyControlled && !bIsBot)
				{
					APlayerController* PC = GetController<APlayerController>();

					// 本地控制时需要输入组件和本地玩家
					if (!Pawn->InputComponent || !PC || !PC->GetLocalPlayer())
					{
						FailReason = TEXT("本地控制但缺少InputComponent或LocalPlayer");
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
		else
		{
			bCanChange = true;
		}
	}
	else if (CurrentState == DJ01GameplayTags::InitState_DataAvailable && DesiredState == DJ01GameplayTags::InitState_DataInitialized)
	{
		// 等待 PlayerState 和 PawnExtension 组件
		APlayerState* PS = GetPlayerState<APlayerState>();

		if (!PS)
		{
			FailReason = TEXT("缺少PlayerState");
			bCanChange = false;
		}
		else if (!Manager->HasFeatureReachedInitState(Pawn, UDJ01PawnExtensionComponent::NAME_ActorFeatureName, DJ01GameplayTags::InitState_DataInitialized) &&
				 !Manager->HasFeatureReachedInitState(Pawn, UDJ01PawnExtensionComponent::NAME_ActorFeatureName, DJ01GameplayTags::InitState_GameplayReady))
		{
			FailReason = TEXT("PawnExtension组件未达到DataInitialized状态");
			bCanChange = false;
		}
		else
		{
			bCanChange = true;
		}
	}
	else if (CurrentState == DJ01GameplayTags::InitState_DataInitialized && DesiredState == DJ01GameplayTags::InitState_GameplayReady)
	{
		// TODO_ABILITY_SYSTEM: 添加能力初始化检查
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

void UDJ01HeroComponent::CheckDefaultInitialization()
{
	static const TArray<FGameplayTag> StateChain = { DJ01GameplayTags::InitState_Spawned, DJ01GameplayTags::InitState_DataAvailable, DJ01GameplayTags::InitState_DataInitialized, DJ01GameplayTags::InitState_GameplayReady };

	// 这将尝试从 Spawned（仅在 BeginPlay 中设置）通过数据初始化阶段进行，直到到达 GameplayReady
	ContinueInitStateChain(StateChain);
}

void UDJ01HeroComponent::InitializePlayerInput(UInputComponent* PlayerInputComponent)
{
	check(PlayerInputComponent);

	const APawn* Pawn = GetPawn<APawn>();
	if (!Pawn)
	{
		return;
	}

	const APlayerController* PC = GetController<APlayerController>();
	check(PC);

	const ULocalPlayer* LP = PC->GetLocalPlayer();
	check(LP);

	UEnhancedInputLocalPlayerSubsystem* Subsystem = LP->GetSubsystem<UEnhancedInputLocalPlayerSubsystem>();
	check(Subsystem);

	Subsystem->ClearAllMappings();

	if (const UDJ01PawnExtensionComponent* PawnExtComp = UDJ01PawnExtensionComponent::FindPawnExtensionComponent(Pawn))
	{
		if (const UDJ01PawnData* PawnData = PawnExtComp->GetPawnData<UDJ01PawnData>())
		{
			if (const UDJ01InputConfig* InputConfig = PawnData->InputConfig)
			{
				for (const FInputMappingContextAndPriority& Mapping : DefaultInputMappings)
				{
					if (UInputMappingContext* IMC = Mapping.InputMapping.Get())
					{
						if (Mapping.bRegisterWithSettings)
						{
							if (UEnhancedInputUserSettings* Settings = Subsystem->GetUserSettings())
							{
								Settings->RegisterInputMappingContext(IMC);
							}
							
							FModifyContextOptions Options = {};
							Options.bIgnoreAllPressedKeysUntilRelease = false;
							// 实际将配置添加到本地玩家							
							Subsystem->AddMappingContext(IMC, Mapping.Priority, Options);
						}
					}
				}

				// DJ01 InputComponent 有一些额外的函数来将 Gameplay Tags 映射到 Input Action
				// 如果希望此功能但仍想更改输入组件类，请将其作为
				// UDJ01InputComponent 的子类或相应地修改此组件
				UDJ01InputComponent* DJ01IC = Cast<UDJ01InputComponent>(PlayerInputComponent);
				if (ensureMsgf(DJ01IC, TEXT("Unexpected Input Component class! The Gameplay Abilities will not be bound to their inputs. Change the input component to UDJ01InputComponent or a subclass of it.")))
				{
					// 添加可能由玩家设置的键映射
					DJ01IC->AddInputMappings(InputConfig, Subsystem);

					// 绑定能力动作
					// 这是我们实际将输入动作绑定到 Gameplay Tag 的地方，这意味着 Gameplay Ability 蓝图将
					// 直接由这些输入动作的触发事件触发
					TArray<uint32> BindHandles;
					DJ01IC->BindAbilityActions(InputConfig, this, &ThisClass::Input_AbilityInputTagPressed, &ThisClass::Input_AbilityInputTagReleased, /*out*/ BindHandles);

					DJ01IC->BindNativeAction(InputConfig, DJ01GameplayTags::InputTag_Move, ETriggerEvent::Triggered, this, &ThisClass::Input_Move, /*bLogIfNotFound=*/ false);
					DJ01IC->BindNativeAction(InputConfig, DJ01GameplayTags::InputTag_Look_Mouse, ETriggerEvent::Triggered, this, &ThisClass::Input_LookMouse, /*bLogIfNotFound=*/ false);
					// DJ01IC->BindNativeAction(InputConfig, DJ01GameplayTags::InputTag_Look_Stick, ETriggerEvent::Triggered, this, &ThisClass::Input_LookStick, /*bLogIfNotFound=*/ false);
					// DJ01IC->BindNativeAction(InputConfig, DJ01GameplayTags::InputTag_Crouch, ETriggerEvent::Triggered, this, &ThisClass::Input_Crouch, /*bLogIfNotFound=*/ false);
					// DJ01IC->BindNativeAction(InputConfig, DJ01GameplayTags::InputTag_AutoRun, ETriggerEvent::Triggered, this, &ThisClass::Input_AutoRun, /*bLogIfNotFound=*/ false);
				}
			}
		}
	}

	if (ensure(!bReadyToBindInputs))
	{
		bReadyToBindInputs = true;
	}
 
	UGameFrameworkComponentManager::SendGameFrameworkComponentExtensionEvent(const_cast<APlayerController*>(PC), NAME_BindInputsNow);
	UGameFrameworkComponentManager::SendGameFrameworkComponentExtensionEvent(const_cast<APawn*>(Pawn), NAME_BindInputsNow);
}

void UDJ01HeroComponent::AddAdditionalInputConfig(const UDJ01InputConfig* InputConfig)
{
	TArray<uint32> BindHandles;

	const APawn* Pawn = GetPawn<APawn>();
	if (!Pawn)
	{
		return;
	}
	
	const APlayerController* PC = GetController<APlayerController>();
	check(PC);

	const ULocalPlayer* LP = PC->GetLocalPlayer();
	check(LP);

	UEnhancedInputLocalPlayerSubsystem* Subsystem = LP->GetSubsystem<UEnhancedInputLocalPlayerSubsystem>();
	check(Subsystem);

	if (const UDJ01PawnExtensionComponent* PawnExtComp = UDJ01PawnExtensionComponent::FindPawnExtensionComponent(Pawn))
	{
		UDJ01InputComponent* DJ01IC = Pawn->FindComponentByClass<UDJ01InputComponent>();
		if (ensureMsgf(DJ01IC, TEXT("Unexpected Input Component class! The Gameplay Abilities will not be bound to their inputs. Change the input component to UDJ01InputComponent or a subclass of it.")))
		{
			// 绑定能力动作
			DJ01IC->BindAbilityActions(InputConfig, this, &ThisClass::Input_AbilityInputTagPressed, &ThisClass::Input_AbilityInputTagReleased, /*out*/ BindHandles);
		}
	}
}

void UDJ01HeroComponent::RemoveAdditionalInputConfig(const UDJ01InputConfig* InputConfig)
{
	//@TODO: 实现！
}

bool UDJ01HeroComponent::IsReadyToBindInputs() const
{
	return bReadyToBindInputs;
}

void UDJ01HeroComponent::Input_AbilityInputTagPressed(FGameplayTag InputTag)
{
	if (const APawn* Pawn = GetPawn<APawn>())
	{
		if (const UDJ01PawnExtensionComponent* PawnExtComp = UDJ01PawnExtensionComponent::FindPawnExtensionComponent(Pawn))
		{
			if (UDJ01AbilitySystemComponent* DJ01ASC = PawnExtComp->GetDJ01AbilitySystemComponent())
			{
				DJ01ASC->AbilityInputTagPressed(InputTag);
			}
		}	
	}
}

void UDJ01HeroComponent::Input_AbilityInputTagReleased(FGameplayTag InputTag)
{
	const APawn* Pawn = GetPawn<APawn>();
	if (!Pawn)
	{
		return;
	}

	if (const UDJ01PawnExtensionComponent* PawnExtComp = UDJ01PawnExtensionComponent::FindPawnExtensionComponent(Pawn))
	{
		if (UDJ01AbilitySystemComponent* DJ01ASC = PawnExtComp->GetDJ01AbilitySystemComponent())
		{
			DJ01ASC->AbilityInputTagReleased(InputTag);
		}
	}
}

void UDJ01HeroComponent::Input_Move(const FInputActionValue& InputActionValue)
{
	APawn* Pawn = GetPawn<APawn>();
	AController* Controller = Pawn ? Pawn->GetController() : nullptr;

	// TODO_PLAYER_CONTROLLER: 如果实现了 DJ01PlayerController，添加自动运行取消逻辑
	// if (ADJ01PlayerController* DJ01Controller = Cast<ADJ01PlayerController>(Controller))
	// {
	// 	DJ01Controller->SetIsAutoRunning(false);
	// }
	
	if (Controller)
	{
		const FVector2D Value = InputActionValue.Get<FVector2D>();
		const FRotator MovementRotation(0.0f, Controller->GetControlRotation().Yaw, 0.0f);

		if (Value.X != 0.0f)
		{
			const FVector MovementDirection = MovementRotation.RotateVector(FVector::RightVector);
			Pawn->AddMovementInput(MovementDirection, Value.X);
		}

		if (Value.Y != 0.0f)
		{
			const FVector MovementDirection = MovementRotation.RotateVector(FVector::ForwardVector);
			Pawn->AddMovementInput(MovementDirection, Value.Y);
		}
	}
}

void UDJ01HeroComponent::Input_LookMouse(const FInputActionValue& InputActionValue)
{
	APawn* Pawn = GetPawn<APawn>();

	if (!Pawn)
	{
		return;
	}
	
	const FVector2D Value = InputActionValue.Get<FVector2D>();

	if (Value.X != 0.0f)
	{
		Pawn->AddControllerYawInput(Value.X);
	}

	if (Value.Y != 0.0f)
	{
		Pawn->AddControllerPitchInput(Value.Y);
	}
}

void UDJ01HeroComponent::Input_LookStick(const FInputActionValue& InputActionValue)
{
	APawn* Pawn = GetPawn<APawn>();

	if (!Pawn)
	{
		return;
	}
	
	const FVector2D Value = InputActionValue.Get<FVector2D>();

	const UWorld* World = GetWorld();
	check(World);

	if (Value.X != 0.0f)
	{
		Pawn->AddControllerYawInput(Value.X * DJ01Hero::LookYawRate * World->GetDeltaSeconds());
	}

	if (Value.Y != 0.0f)
	{
		Pawn->AddControllerPitchInput(Value.Y * DJ01Hero::LookPitchRate * World->GetDeltaSeconds());
	}
}

// void UDJ01HeroComponent::Input_Crouch(const FInputActionValue& InputActionValue)
// {
// 	if (ADJ01Character* Character = GetPawn<ADJ01Character>())
// 	{
// 		Character->ToggleCrouch();
// 	}
// }

void UDJ01HeroComponent::Input_AutoRun(const FInputActionValue& InputActionValue)
{
	// TODO_PLAYER_CONTROLLER: 实现自动运行功能
	// if (APawn* Pawn = GetPawn<APawn>())
	// {
	// 	if (ADJ01PlayerController* Controller = Cast<ADJ01PlayerController>(Pawn->GetController()))
	// 	{
	// 		// 切换自动运行
	// 		Controller->SetIsAutoRunning(!Controller->GetIsAutoRunning());
	// 	}	
	// }
}

TSubclassOf<UDJ01CameraMode> UDJ01HeroComponent::DetermineCameraMode() const
{
	if (AbilityCameraMode)
	{
		return AbilityCameraMode;
	}

	const APawn* Pawn = GetPawn<APawn>();
	if (!Pawn)
	{
		return nullptr;
	}

	if (UDJ01PawnExtensionComponent* PawnExtComp = UDJ01PawnExtensionComponent::FindPawnExtensionComponent(Pawn))
	{
		if (const UDJ01PawnData* PawnData = PawnExtComp->GetPawnData<UDJ01PawnData>())
		{
			return PawnData->DefaultCameraMode;
		}
	}

	return nullptr;
}

void UDJ01HeroComponent::SetAbilityCameraMode(TSubclassOf<UDJ01CameraMode> CameraMode, const FGameplayAbilitySpecHandle& OwningSpecHandle)
{
	if (CameraMode)
	{
		AbilityCameraMode = CameraMode;
		AbilityCameraModeOwningSpecHandle = OwningSpecHandle;
	}
}

void UDJ01HeroComponent::ClearAbilityCameraMode(const FGameplayAbilitySpecHandle& OwningSpecHandle)
{
	if (AbilityCameraModeOwningSpecHandle == OwningSpecHandle)
	{
		AbilityCameraMode = nullptr;
		AbilityCameraModeOwningSpecHandle = FGameplayAbilitySpecHandle();
	}
}

// 以下函数已弃用，UE 5.3+ 使用 FInputMappingContextAndPriority 系统
// 如果需要输入配置的激活/停用处理，请在 DefaultInputMappings 的 
// FInputMappingContextAndPriority 结构中配置相关选项