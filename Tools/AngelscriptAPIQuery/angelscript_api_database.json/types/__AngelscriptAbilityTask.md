# __AngelscriptAbilityTask

## 方法

### ApplyRootMotionConstantForce
```angelscript
UAbilityTask_ApplyRootMotionConstantForce ApplyRootMotionConstantForce(UGameplayAbility OwningAbility, FName TaskInstanceName, FVector WorldDirection, float32 Strength, float32 Duration, bool bIsAdditive, UCurveFloat StrengthOverTime, ERootMotionFinishVelocityMode VelocityOnFinishMode, FVector SetVelocityOnFinish, float32 ClampVelocityOnFinish, bool bEnableGravity)
```

### ApplyRootMotionJumpForce
```angelscript
UAbilityTask_ApplyRootMotionJumpForce ApplyRootMotionJumpForce(UGameplayAbility OwningAbility, FName TaskInstanceName, FRotator Rotation, float32 Distance, float32 Height, float32 Duration, float32 MinimumLandedTriggerTime, bool bFinishOnLanded, ERootMotionFinishVelocityMode VelocityOnFinishMode, FVector SetVelocityOnFinish, float32 ClampVelocityOnFinish, UCurveVector PathOffsetCurve, UCurveFloat TimeMappingCurve)
```

### ApplyRootMotionMoveToActorForce
```angelscript
UAbilityTask_ApplyRootMotionMoveToActorForce ApplyRootMotionMoveToActorForce(UGameplayAbility OwningAbility, FName TaskInstanceName, AActor TargetActor, FVector TargetLocationOffset, ERootMotionMoveToActorTargetOffsetType OffsetAlignment, float32 Duration, UCurveFloat TargetLerpSpeedHorizontal, UCurveFloat TargetLerpSpeedVertical, bool bSetNewMovementMode, EMovementMode MovementMode, bool bRestrictSpeedToExpected, UCurveVector PathOffsetCurve, UCurveFloat TimeMappingCurve, ERootMotionFinishVelocityMode VelocityOnFinishMode, FVector SetVelocityOnFinish, float32 ClampVelocityOnFinish, bool bDisableDestinationReachedInterrupt)
```

### ApplyRootMotionMoveToForce
```angelscript
UAbilityTask_ApplyRootMotionMoveToForce ApplyRootMotionMoveToForce(UGameplayAbility OwningAbility, FName TaskInstanceName, FVector TargetLocation, float32 Duration, bool bSetNewMovementMode, EMovementMode MovementMode, bool bRestrictSpeedToExpected, UCurveVector PathOffsetCurve, ERootMotionFinishVelocityMode VelocityOnFinishMode, FVector SetVelocityOnFinish, float32 ClampVelocityOnFinish)
```

### ApplyRootMotionMoveToTargetDataActorForce
```angelscript
UAbilityTask_ApplyRootMotionMoveToActorForce ApplyRootMotionMoveToTargetDataActorForce(UGameplayAbility OwningAbility, FName TaskInstanceName, FGameplayAbilityTargetDataHandle TargetDataHandle, int TargetDataIndex, int TargetActorIndex, FVector TargetLocationOffset, ERootMotionMoveToActorTargetOffsetType OffsetAlignment, float32 Duration, UCurveFloat TargetLerpSpeedHorizontal, UCurveFloat TargetLerpSpeedVertical, bool bSetNewMovementMode, EMovementMode MovementMode, bool bRestrictSpeedToExpected, UCurveVector PathOffsetCurve, UCurveFloat TimeMappingCurve, ERootMotionFinishVelocityMode VelocityOnFinishMode, FVector SetVelocityOnFinish, float32 ClampVelocityOnFinish, bool bDisableDestinationReachedInterrupt)
```

### ApplyRootMotionRadialForce
```angelscript
UAbilityTask_ApplyRootMotionRadialForce ApplyRootMotionRadialForce(UGameplayAbility OwningAbility, FName TaskInstanceName, FVector Location, AActor LocationActor, float32 Strength, float32 Duration, float32 Radius, bool bIsPush, bool bIsAdditive, bool bNoZForce, UCurveFloat StrengthDistanceFalloff, UCurveFloat StrengthOverTime, bool bUseFixedWorldDirection, FRotator FixedWorldDirection, ERootMotionFinishVelocityMode VelocityOnFinishMode, FVector SetVelocityOnFinish, float32 ClampVelocityOnFinish)
```

### MoveToLocation
```angelscript
UAbilityTask_MoveToLocation MoveToLocation(UGameplayAbility OwningAbility, FName TaskInstanceName, FVector Location, float32 Duration, UCurveFloat InterpolationCurve, UCurveVector VectorInterpolationCurve)
```

### PlayMontageAndWait
```angelscript
UAbilityTask_PlayMontageAndWait PlayMontageAndWait(UGameplayAbility OwningAbility, FName TaskInstanceName, UAnimMontage MontageToPlay, float32 Rate, FName StartSection, bool bStopWhenAbilityEnds, float32 AnimRootMotionTranslationScale, float32 StartTimeSeconds)
```

### RepeatAction
```angelscript
UAbilityTask_Repeat RepeatAction(UGameplayAbility OwningAbility, float32 TimeBetweenActions, int TotalActionCount)
```

### SpawnActor
```angelscript
UAbilityTask_SpawnActor SpawnActor(UGameplayAbility OwningAbility, FGameplayAbilityTargetDataHandle TargetData, TSubclassOf<AActor> Class)
```

### StartAbilityState
```angelscript
UAbilityTask_StartAbilityState StartAbilityState(UGameplayAbility OwningAbility, FName StateName, bool bEndCurrentState)
```

### VisualizeTargeting
```angelscript
UAbilityTask_VisualizeTargeting VisualizeTargeting(UGameplayAbility OwningAbility, TSubclassOf<AGameplayAbilityTargetActor> TargetClass, FName TaskInstanceName, float32 Duration)
```

### VisualizeTargetingUsingActor
```angelscript
UAbilityTask_VisualizeTargeting VisualizeTargetingUsingActor(UGameplayAbility OwningAbility, AGameplayAbilityTargetActor TargetActor, FName TaskInstanceName, float32 Duration)
```

### WaitConfirmCancel
```angelscript
UAbilityTask_WaitConfirmCancel WaitConfirmCancel(UGameplayAbility OwningAbility)
```

### WaitDelay
```angelscript
UAbilityTask_WaitDelay WaitDelay(UGameplayAbility OwningAbility, float32 Time)
```

### WaitForAbilityActivate
```angelscript
UAbilityTask_WaitAbilityActivate WaitForAbilityActivate(UGameplayAbility OwningAbility, FGameplayTag WithTag, FGameplayTag WithoutTag, bool bIncludeTriggeredAbilities, bool bTriggerOnce)
```

### WaitForAbilityActivateQuery
```angelscript
UAbilityTask_WaitAbilityActivate WaitForAbilityActivateQuery(UGameplayAbility OwningAbility, FGameplayTagQuery Query, bool bIncludeTriggeredAbilities, bool bTriggerOnce)
```

### WaitForAbilityActivateWithTagRequirements
```angelscript
UAbilityTask_WaitAbilityActivate WaitForAbilityActivateWithTagRequirements(UGameplayAbility OwningAbility, FGameplayTagRequirements TagRequirements, bool bIncludeTriggeredAbilities, bool bTriggerOnce)
```

### WaitForAttributeChange
```angelscript
UAbilityTask_WaitAttributeChange WaitForAttributeChange(UGameplayAbility OwningAbility, FGameplayAttribute Attribute, FGameplayTag WithTag, FGameplayTag WithoutTag, bool bTriggerOnce, AActor ExternalOwner)
```

### WaitForAttributeChangeRatioThreshold
```angelscript
UAbilityTask_WaitAttributeChangeRatioThreshold WaitForAttributeChangeRatioThreshold(UGameplayAbility OwningAbility, FGameplayAttribute AttributeNumerator, FGameplayAttribute AttributeDenominator, EWaitAttributeChangeComparison ComparisonType, float32 ComparisonValue, bool bTriggerOnce, AActor ExternalOwner)
```

### WaitForAttributeChangeThreshold
```angelscript
UAbilityTask_WaitAttributeChangeThreshold WaitForAttributeChangeThreshold(UGameplayAbility OwningAbility, FGameplayAttribute Attribute, EWaitAttributeChangeComparison ComparisonType, float32 ComparisonValue, bool bTriggerOnce, AActor ExternalOwner)
```

### WaitForAttributeChangeWithComparison
```angelscript
UAbilityTask_WaitAttributeChange WaitForAttributeChangeWithComparison(UGameplayAbility OwningAbility, FGameplayAttribute Attribute, FGameplayTag WithTag, FGameplayTag WithoutTag, EWaitAttributeChangeComparison ComparisonType, float32 ComparisonValue, bool bTriggerOnce, AActor ExternalOwner)
```

### WaitForCancelInput
```angelscript
UAbilityTask_WaitCancel WaitForCancelInput(UGameplayAbility OwningAbility)
```

### WaitForConfirmInput
```angelscript
UAbilityTask_WaitConfirm WaitForConfirmInput(UGameplayAbility OwningAbility)
```

### WaitForGameplayEffectRemoved
```angelscript
UAbilityTask_WaitGameplayEffectRemoved WaitForGameplayEffectRemoved(UGameplayAbility OwningAbility, FActiveGameplayEffectHandle Handle)
```

### WaitForGameplayEffectStackChange
```angelscript
UAbilityTask_WaitGameplayEffectStackChange WaitForGameplayEffectStackChange(UGameplayAbility OwningAbility, FActiveGameplayEffectHandle Handle)
```

### WaitForNewAbilityCommit
```angelscript
UAbilityTask_WaitAbilityCommit WaitForNewAbilityCommit(UGameplayAbility OwningAbility, FGameplayTag WithTag, FGameplayTag WithoutTag, bool bTriggerOnce)
```

### WaitForNewAbilityCommitQuery
```angelscript
UAbilityTask_WaitAbilityCommit WaitForNewAbilityCommitQuery(UGameplayAbility OwningAbility, FGameplayTagQuery Query, bool bTriggerOnce)
```

### WaitForOverlap
```angelscript
UAbilityTask_WaitOverlap WaitForOverlap(UGameplayAbility OwningAbility)
```

### WaitGameplayEffectAppliedToSelf
```angelscript
UAbilityTask_WaitGameplayEffectApplied_Self WaitGameplayEffectAppliedToSelf(UGameplayAbility OwningAbility, FGameplayTargetDataFilterHandle Filter, FGameplayTagRequirements SourceTagRequirements, FGameplayTagRequirements TargetTagRequirements, bool bTriggerOnce, AActor ExternalOwner, bool bListenForPeriodicEffect)
```

### WaitGameplayEffectAppliedToSelfQuery
```angelscript
UAbilityTask_WaitGameplayEffectApplied_Self WaitGameplayEffectAppliedToSelfQuery(UGameplayAbility OwningAbility, FGameplayTargetDataFilterHandle Filter, FGameplayTagQuery SourceTagQuery, FGameplayTagQuery TargetTagQuery, bool bTriggerOnce, AActor ExternalOwner, bool bListenForPeriodicEffect)
```

### WaitGameplayEffectAppliedToTarget
```angelscript
UAbilityTask_WaitGameplayEffectApplied_Target WaitGameplayEffectAppliedToTarget(UGameplayAbility OwningAbility, FGameplayTargetDataFilterHandle Filter, FGameplayTagRequirements SourceTagRequirements, FGameplayTagRequirements TargetTagRequirements, bool bTriggerOnce, AActor ExternalOwner, bool bListenForPeriodicEffect)
```

### WaitGameplayEffectAppliedToTargetQuery
```angelscript
UAbilityTask_WaitGameplayEffectApplied_Target WaitGameplayEffectAppliedToTargetQuery(UGameplayAbility OwningAbility, FGameplayTargetDataFilterHandle Filter, FGameplayTagQuery SourceTagQuery, FGameplayTagQuery TargetTagQuery, bool bTriggerOnce, AActor ExternalOwner, bool bListenForPeriodicEffect)
```

### WaitGameplayEffectBlockedByImmunity
```angelscript
UAbilityTask_WaitGameplayEffectBlockedImmunity WaitGameplayEffectBlockedByImmunity(UGameplayAbility OwningAbility, FGameplayTagRequirements SourceTagRequirements, FGameplayTagRequirements TargetTagRequirements, AActor ExternalTarget, bool bTriggerOnce)
```

### WaitGameplayEvent
```angelscript
UAbilityTask_WaitGameplayEvent WaitGameplayEvent(UGameplayAbility OwningAbility, FGameplayTag Tag, AActor ExternalTarget, bool bTriggerOnce, bool bMatchExact)
```

### WaitGameplayTagAdd
```angelscript
UAbilityTask_WaitGameplayTagAdded WaitGameplayTagAdd(UGameplayAbility OwningAbility, FGameplayTag Tag, AActor ExternalTarget, bool bTriggerOnce)
```

### WaitGameplayTagQuery
```angelscript
UAbilityTask_WaitGameplayTagQuery WaitGameplayTagQuery(UGameplayAbility OwningAbility, FGameplayTagQuery Query, const AActor ExternalTarget, EWaitGameplayTagQueryTriggerCondition TriggerCondition, bool bTriggerOnce)
```

### WaitGameplayTagRemove
```angelscript
UAbilityTask_WaitGameplayTagRemoved WaitGameplayTagRemove(UGameplayAbility OwningAbility, FGameplayTag Tag, AActor ExternalTarget, bool bTriggerOnce)
```

### WaitInputPress
```angelscript
UAbilityTask_WaitInputPress WaitInputPress(UGameplayAbility OwningAbility, bool bTestAlreadyPressed)
```

### WaitInputRelease
```angelscript
UAbilityTask_WaitInputRelease WaitInputRelease(UGameplayAbility OwningAbility, bool bTestAlreadyReleased)
```

### WaitMovementModeChange
```angelscript
UAbilityTask_WaitMovementModeChange WaitMovementModeChange(UGameplayAbility OwningAbility, EMovementMode NewMode)
```

### WaitNetSync
```angelscript
UAbilityTask_NetworkSyncPoint WaitNetSync(UGameplayAbility OwningAbility, EAbilityTaskNetSyncType SyncType)
```

### WaitTargetData
```angelscript
UAbilityTask_WaitTargetData WaitTargetData(UGameplayAbility OwningAbility, FName TaskInstanceName, EGameplayTargetingConfirmation ConfirmationType, TSubclassOf<AGameplayAbilityTargetActor> TargetClass)
```

### WaitTargetDataUsingActor
```angelscript
UAbilityTask_WaitTargetData WaitTargetDataUsingActor(UGameplayAbility OwningAbility, FName TaskInstanceName, EGameplayTargetingConfirmation ConfirmationType, AGameplayAbilityTargetActor TargetActor)
```

### WaitVelocityChange
```angelscript
UAbilityTask_WaitVelocityChange WaitVelocityChange(UGameplayAbility OwningAbility, FVector Direction, float32 MinimumMagnitude)
```

