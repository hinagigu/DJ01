// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01/Player/Public/DJ01CheatManager.h"
#include "GameFramework/Pawn.h"
#include "DJ01/Player/Public/DJ01PlayerController.h"
#include "DJ01/Player/Public/DJ01DebugCameraController.h"
#include "Engine/Engine.h"
#include "Engine/GameViewportClient.h"
#include "Engine/Console.h"
#include "GameFramework/HUD.h"
#include "DJ01/System/Public/DJ01AssetManager.h"
// #include "System/LyraGameData.h" // TODO: System
#include "DJ01/System/Public/DJ01GameplayTags.h"
// #include "AbilitySystem/DJ01AbilitySystemComponent.h" // TODO: AbilitySystem
// #include "AbilitySystemGlobals.h" // TODO: AbilitySystem
// #include "Character/LyraHealthComponent.h" // TODO: Character
#include "DJ01/Character/Public/DJ01PawnExtensionComponent.h"
// #include "System/LyraSystemStatics.h" // TODO: System
// #include "DJ01/System/Public/DJ01DeveloperSettings.h" // TODO: DeveloperSettings

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01CheatManager)

DEFINE_LOG_CATEGORY(LogDJ01Cheat);

namespace DJ01Cheat
{
	static const FName NAME_Fixed = FName(TEXT("Fixed"));
	
	static bool bEnableDebugCameraCycling = false;
	static FAutoConsoleVariableRef CVarEnableDebugCameraCycling(
		TEXT("DJ01Cheat.EnableDebugCameraCycling"),
		bEnableDebugCameraCycling,
		TEXT("If true then you can cycle the debug camera while running the game."),
		ECVF_Cheat);

	static bool bStartInGodMode = false;
	static FAutoConsoleVariableRef CVarStartInGodMode(
		TEXT("DJ01Cheat.StartInGodMode"),
		bStartInGodMode,
		TEXT("If true then the God cheat will be applied on begin play"),
		ECVF_Cheat);
};


UDJ01CheatManager::UDJ01CheatManager()
{
	DebugCameraControllerClass = ADJ01DebugCameraController::StaticClass();
}

void UDJ01CheatManager::InitCheatManager()
{
	Super::InitCheatManager();

#if WITH_EDITOR
	if (GIsEditor)
	{
		// APlayerController* PC = GetOuterAPlayerController(); // TODO: DeveloperSettings
		// for (const FDJ01CheatToRun& CheatRow : GetDefault<UDJ01DeveloperSettings>()->CheatsToRun)
		// {
		// 	if (CheatRow.Phase == ECheatExecutionTime::OnCheatManagerCreated)
		// 	{
		// 		PC->ConsoleCommand(CheatRow.Cheat, /*bWriteToLog=*/ true);
		// 	}
		// }
	}
#endif

	if (DJ01Cheat::bStartInGodMode)
	{
		// God(); // TODO: AbilitySystem
	}
}

void UDJ01CheatManager::CheatOutputText(const FString& TextToOutput)
{
#if USING_CHEAT_MANAGER
	// Output to the console.
	if (GEngine && GEngine->GameViewport && GEngine->GameViewport->ViewportConsole)
	{
		GEngine->GameViewport->ViewportConsole->OutputText(TextToOutput);
	}

	// Output to log.
	UE_LOG(LogDJ01Cheat, Display, TEXT("%s"), *TextToOutput);
#endif // USING_CHEAT_MANAGER
}

void UDJ01CheatManager::Cheat(const FString& Msg)
{
	if (ADJ01PlayerController* DJ01PC = Cast<ADJ01PlayerController>(GetOuterAPlayerController()))
	{
		DJ01PC->ServerCheat(Msg.Left(128));
	}
}

void UDJ01CheatManager::CheatAll(const FString& Msg)
{
	if (ADJ01PlayerController* DJ01PC = Cast<ADJ01PlayerController>(GetOuterAPlayerController()))
	{
		DJ01PC->ServerCheatAll(Msg.Left(128));
	}
}

void UDJ01CheatManager::PlayNextGame()
{
	// ULyraSystemStatics::PlayNextGame(this); // TODO: System
}

void UDJ01CheatManager::EnableDebugCamera()
{
	Super::EnableDebugCamera();
}

void UDJ01CheatManager::DisableDebugCamera()
{
	FVector DebugCameraLocation;
	FRotator DebugCameraRotation;

	ADebugCameraController* DebugCC = Cast<ADebugCameraController>(GetOuter());
	APlayerController* OriginalPC = nullptr;

	if (DebugCC)
	{
		OriginalPC = DebugCC->OriginalControllerRef;
		DebugCC->GetPlayerViewPoint(DebugCameraLocation, DebugCameraRotation);
	}

	Super::DisableDebugCamera();

	if (OriginalPC && OriginalPC->PlayerCameraManager && (OriginalPC->PlayerCameraManager->CameraStyle == DJ01Cheat::NAME_Fixed))
	{
		OriginalPC->SetInitialLocationAndRotation(DebugCameraLocation, DebugCameraRotation);

		OriginalPC->PlayerCameraManager->ViewTarget.POV.Location = DebugCameraLocation;
		OriginalPC->PlayerCameraManager->ViewTarget.POV.Rotation = DebugCameraRotation;
		OriginalPC->PlayerCameraManager->PendingViewTarget.POV.Location = DebugCameraLocation;
		OriginalPC->PlayerCameraManager->PendingViewTarget.POV.Rotation = DebugCameraRotation;
	}
}

bool UDJ01CheatManager::InDebugCamera() const
{
	return (Cast<ADebugCameraController>(GetOuter()) ? true : false);
}

void UDJ01CheatManager::EnableFixedCamera()
{
	const ADebugCameraController* DebugCC = Cast<ADebugCameraController>(GetOuter());
	APlayerController* PC = (DebugCC ? ToRawPtr(DebugCC->OriginalControllerRef) : GetOuterAPlayerController());

	if (PC && PC->PlayerCameraManager)
	{
		PC->SetCameraMode(DJ01Cheat::NAME_Fixed);
	}
}

void UDJ01CheatManager::DisableFixedCamera()
{
	const ADebugCameraController* DebugCC = Cast<ADebugCameraController>(GetOuter());
	APlayerController* PC = (DebugCC ? ToRawPtr(DebugCC->OriginalControllerRef) : GetOuterAPlayerController());

	if (PC && PC->PlayerCameraManager)
	{
		PC->SetCameraMode(NAME_Default);
	}
}

bool UDJ01CheatManager::InFixedCamera() const
{
	const ADebugCameraController* DebugCC = Cast<ADebugCameraController>(GetOuter());
	const APlayerController* PC = (DebugCC ? ToRawPtr(DebugCC->OriginalControllerRef) : GetOuterAPlayerController());

	if (PC && PC->PlayerCameraManager)
	{
		return (PC->PlayerCameraManager->CameraStyle == DJ01Cheat::NAME_Fixed);
	}

	return false;
}

void UDJ01CheatManager::ToggleFixedCamera()
{
	if (InFixedCamera())
	{
		DisableFixedCamera();
	}
	else
	{
		EnableFixedCamera();
	}
}

void UDJ01CheatManager::CycleDebugCameras()
{
	if (!DJ01Cheat::bEnableDebugCameraCycling)
	{
		return;
	}
	
	if (InDebugCamera())
	{
		EnableFixedCamera();
		DisableDebugCamera();
	}
	else if (InFixedCamera())
	{
		DisableFixedCamera();
		DisableDebugCamera();
	}
	else
	{
		EnableDebugCamera();
		DisableFixedCamera();
	}
}

// void UDJ01CheatManager::CycleAbilitySystemDebug()
// {
// 	APlayerController* PC = Cast<APlayerController>(GetOuterAPlayerController());

// 	if (PC && PC->MyHUD)
// 	{
// 		if (!PC->MyHUD->bShowDebugInfo || !PC->MyHUD->DebugDisplay.Contains(TEXT("AbilitySystem")))
// 		{
// 			PC->MyHUD->ShowDebug(TEXT("AbilitySystem"));
// 		}

// 		PC->ConsoleCommand(TEXT("AbilitySystem.Debug.NextCategory"));
// 	}
// }

// void UDJ01CheatManager::CancelActivatedAbilities()
// {
// 	if (ULyraAbilitySystemComponent* LyraASC = GetPlayerAbilitySystemComponent())
// 	{
// 		const bool bReplicateCancelAbility = true;
// 		LyraASC->CancelInputActivatedAbilities(bReplicateCancelAbility);
// 	}
// }

// void UDJ01CheatManager::AddTagToSelf(FString TagName)
// {
// 	FGameplayTag Tag = LyraGameplayTags::FindTagByString(TagName, true);
// 	if (Tag.IsValid())
// 	{
// 		if (ULyraAbilitySystemComponent* LyraASC = GetPlayerAbilitySystemComponent())
// 		{
// 			LyraASC->AddDynamicTagGameplayEffect(Tag);
// 		}
// 	}
// 	else
// 	{
// 		UE_LOG(LogDJ01Cheat, Display, TEXT("AddTagToSelf: Could not find any tag matching [%s]."), *TagName);
// 	}
// }

// void UDJ01CheatManager::RemoveTagFromSelf(FString TagName)
// {
// 	FGameplayTag Tag = LyraGameplayTags::FindTagByString(TagName, true);
// 	if (Tag.IsValid())
// 	{
// 		if (ULyraAbilitySystemComponent* LyraASC = GetPlayerAbilitySystemComponent())
// 		{
// 			LyraASC->RemoveDynamicTagGameplayEffect(Tag);
// 		}
// 	}
// 	else
// 	{
// 		UE_LOG(LogDJ01Cheat, Display, TEXT("RemoveTagFromSelf: Could not find any tag matching [%s]."), *TagName);
// 	}
// }

// void UDJ01CheatManager::DamageSelf(float DamageAmount)
// {
// 	if (ULyraAbilitySystemComponent* LyraASC = GetPlayerAbilitySystemComponent())
// 	{
// 		ApplySetByCallerDamage(LyraASC, DamageAmount);
// 	}
// }

// void UDJ01CheatManager::DamageTarget(float DamageAmount)
// {
// 	if (ALyraPlayerController* LyraPC = Cast<ALyraPlayerController>(GetOuterAPlayerController()))
// 	{
// 		if (LyraPC->GetNetMode() == NM_Client)
// 		{
// 			// Automatically send cheat to server for convenience.
// 			LyraPC->ServerCheat(FString::Printf(TEXT("DamageTarget %.2f"), DamageAmount));
// 			return;
// 		}

// 		FHitResult TargetHitResult;
// 		AActor* TargetActor = GetTarget(LyraPC, TargetHitResult);

// 		if (ULyraAbilitySystemComponent* LyraTargetASC = Cast<ULyraAbilitySystemComponent>(UAbilitySystemGlobals::GetAbilitySystemComponentFromActor(TargetActor)))
// 		{
// 			ApplySetByCallerDamage(LyraTargetASC, DamageAmount);
// 		}
// 	}
// }

// void UDJ01CheatManager::ApplySetByCallerDamage(ULyraAbilitySystemComponent* LyraASC, float DamageAmount)
// {
// 	check(LyraASC);

// 	TSubclassOf<UGameplayEffect> DamageGE = ULyraAssetManager::GetSubclass(ULyraGameData::Get().DamageGameplayEffect_SetByCaller);
// 	FGameplayEffectSpecHandle SpecHandle = LyraASC->MakeOutgoingSpec(DamageGE, 1.0f, LyraASC->MakeEffectContext());

// 	if (SpecHandle.IsValid())
// 	{
// 		SpecHandle.Data->SetSetByCallerMagnitude(LyraGameplayTags::SetByCaller_Damage, DamageAmount);
// 		LyraASC->ApplyGameplayEffectSpecToSelf(*SpecHandle.Data.Get());
// 	}
// }

// void UDJ01CheatManager::HealSelf(float HealAmount)
// {
// 	if (ULyraAbilitySystemComponent* LyraASC = GetPlayerAbilitySystemComponent())
// 	{
// 		ApplySetByCallerHeal(LyraASC, HealAmount);
// 	}
// }

// void UDJ01CheatManager::HealTarget(float HealAmount)
// {
// 	if (ALyraPlayerController* LyraPC = Cast<ALyraPlayerController>(GetOuterAPlayerController()))
// 	{
// 		FHitResult TargetHitResult;
// 		AActor* TargetActor = GetTarget(LyraPC, TargetHitResult);

// 		if (ULyraAbilitySystemComponent* LyraTargetASC = Cast<ULyraAbilitySystemComponent>(UAbilitySystemGlobals::GetAbilitySystemComponentFromActor(TargetActor)))
// 		{
// 			ApplySetByCallerHeal(LyraTargetASC, HealAmount);
// 		}
// 	}
// }

// void UDJ01CheatManager::ApplySetByCallerHeal(ULyraAbilitySystemComponent* LyraASC, float HealAmount)
// {
// 	check(LyraASC);

// 	TSubclassOf<UGameplayEffect> HealGE = ULyraAssetManager::GetSubclass(ULyraGameData::Get().HealGameplayEffect_SetByCaller);
// 	FGameplayEffectSpecHandle SpecHandle = LyraASC->MakeOutgoingSpec(HealGE, 1.0f, LyraASC->MakeEffectContext());

// 	if (SpecHandle.IsValid())
// 	{
// 		SpecHandle.Data->SetSetByCallerMagnitude(LyraGameplayTags::SetByCaller_Heal, HealAmount);
// 		LyraASC->ApplyGameplayEffectSpecToSelf(*SpecHandle.Data.Get());
// 	}
// }

// ULyraAbilitySystemComponent* UDJ01CheatManager::GetPlayerAbilitySystemComponent() const
// {
// 	if (ALyraPlayerController* LyraPC = Cast<ALyraPlayerController>(GetOuterAPlayerController()))
// 	{
// 		return LyraPC->GetDJ01AbilitySystemComponent();
// 	}
// 	return nullptr;
// }

// void UDJ01CheatManager::DamageSelfDestruct()
// {
// 	if (ALyraPlayerController* LyraPC = Cast<ALyraPlayerController>(GetOuterAPlayerController()))
// 	{
//  		if (const ULyraPawnExtensionComponent* PawnExtComp = ULyraPawnExtensionComponent::FindPawnExtensionComponent(LyraPC->GetPawn()))
// 		{
// 			if (PawnExtComp->HasReachedInitState(LyraGameplayTags::InitState_GameplayReady))
// 			{
// 				if (ULyraHealthComponent* HealthComponent = ULyraHealthComponent::FindHealthComponent(LyraPC->GetPawn()))
// 				{
// 					HealthComponent->DamageSelfDestruct();
// 				}
// 			}
// 		}
// 	}
// }

// void UDJ01CheatManager::God()
// {
// 	if (ALyraPlayerController* LyraPC = Cast<ALyraPlayerController>(GetOuterAPlayerController()))
// 	{
// 		if (LyraPC->GetNetMode() == NM_Client)
// 		{
// 			// Automatically send cheat to server for convenience.
// 			LyraPC->ServerCheat(FString::Printf(TEXT("God")));
// 			return;
// 		}

// 		if (ULyraAbilitySystemComponent* LyraASC = LyraPC->GetDJ01AbilitySystemComponent())
// 		{
// 			const FGameplayTag Tag = LyraGameplayTags::Cheat_GodMode;
// 			const bool bHasTag = LyraASC->HasMatchingGameplayTag(Tag);

// 			if (bHasTag)
// 			{
// 				LyraASC->RemoveDynamicTagGameplayEffect(Tag);
// 			}
// 			else
// 			{
// 				LyraASC->AddDynamicTagGameplayEffect(Tag);
// 			}
// 		}
// 	}
// }

// void UDJ01CheatManager::UnlimitedHealth(int32 Enabled)
// {
// 	if (ULyraAbilitySystemComponent* LyraASC = GetPlayerAbilitySystemComponent())
// 	{
// 		const FGameplayTag Tag = LyraGameplayTags::Cheat_UnlimitedHealth;
// 		const bool bHasTag = LyraASC->HasMatchingGameplayTag(Tag);

// 		if ((Enabled == -1) || ((Enabled > 0) && !bHasTag) || ((Enabled == 0) && bHasTag))
// 		{
// 			if (bHasTag)
// 			{
// 				LyraASC->RemoveDynamicTagGameplayEffect(Tag);
// 			}
// 			else
// 			{
// 				LyraASC->AddDynamicTagGameplayEffect(Tag);
// 			}
// 		}
// 	}
// }

