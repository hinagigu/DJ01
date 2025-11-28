// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Logging/LogMacros.h"

DJ01_API DECLARE_LOG_CATEGORY_EXTERN(LogDJ01, Log, All);
DJ01_API DECLARE_LOG_CATEGORY_EXTERN(LogDJ01Experience, Log, All);
DJ01_API DECLARE_LOG_CATEGORY_EXTERN(LogDJ01Teams, Log, All);
DJ01_API DECLARE_LOG_CATEGORY_EXTERN(LogDJ01AbilitySystem, Log, All);

DJ01_API FString GetClientServerContextString(UObject* ContextObject = nullptr);

