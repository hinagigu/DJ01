// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "LoadingProcessInterface.h"
#include "UObject/Object.h"

#include "LoadingProcessTask.generated.h"

struct FFrame;

/**
 * ULoadingProcessTask
 * 
 * A simple UObject that implements ILoadingProcessInterface, useful for Blueprint-driven loading scenarios.
 * Create an instance of this, and it will keep the loading screen visible until you call Unregister().
 */
UCLASS(BlueprintType)
class LOADINGSCREEN_API ULoadingProcessTask : public UObject, public ILoadingProcessInterface
{
	GENERATED_BODY()
	
public:
	/**
	 * Creates a loading screen task that will keep the loading screen visible
	 * @param WorldContextObject The world context
	 * @param ShowLoadingScreenReason A debug string describing why the loading screen should be shown
	 */
	UFUNCTION(BlueprintCallable, meta=(WorldContext = "WorldContextObject"))
	static ULoadingProcessTask* CreateLoadingScreenProcessTask(UObject* WorldContextObject, const FString& ShowLoadingScreenReason);

public:
	ULoadingProcessTask() { }

	/** Call this when you're done with the loading task to allow the loading screen to be dismissed */
	UFUNCTION(BlueprintCallable)
	void Unregister();

	/** Updates the reason string (useful for debugging) */
	UFUNCTION(BlueprintCallable)
	void SetShowLoadingScreenReason(const FString& InReason);

	//~ILoadingProcessInterface interface
	virtual bool ShouldShowLoadingScreen(FString& OutReason) const override;
	//~End of ILoadingProcessInterface interface
	
private:
	FString Reason;
};