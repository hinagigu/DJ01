// Fill out your copyright notice in the Description page of Project Settings.

#include "DJ01/System/Public/DJ01LogChannels.h"

DEFINE_LOG_CATEGORY(LogDJ01);
DEFINE_LOG_CATEGORY(LogDJ01Experience);
DEFINE_LOG_CATEGORY(LogDJ01Teams);
DEFINE_LOG_CATEGORY(LogDJ01AbilitySystem);

FString GetClientServerContextString(UObject* ContextObject)
{
	ENetRole Role = ROLE_None;

	if (AActor* Actor = Cast<AActor>(ContextObject))
	{
		Role = Actor->GetLocalRole();
	}
	else if (UActorComponent* Component = Cast<UActorComponent>(ContextObject))
	{
		Role = Component->GetOwnerRole();
	}

	if (Role != ROLE_None)
	{
		return (Role == ROLE_Authority) ? TEXT("Server") : TEXT("Client");
	}
	else
	{
#if WITH_EDITOR
		if (GIsEditor)
		{
			extern ENGINE_API FString GPlayInEditorContextString;
			return GPlayInEditorContextString;
		}
#endif
	}

	return TEXT("[]");
}
