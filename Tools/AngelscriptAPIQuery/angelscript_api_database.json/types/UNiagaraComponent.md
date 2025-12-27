# UNiagaraComponent

**继承自**: `UFXSystemComponent`

UNiagaraComponent is the primitive component for a Niagara System.
@see ANiagaraActor
@see UNiagaraSystem

## 属性

### TemplateParameterOverrides
- **类型**: `TMap<FNiagaraVariableBase,FNiagaraVariant>`

### InstanceParameterOverrides
- **类型**: `TMap<FNiagaraVariableBase,FNiagaraVariant>`

### WarmupTickCount
- **类型**: `int`
- **描述**: Number of ticks to process for warmup of the system. Total warmup time is WarmupTickCount * WarmupTickDelta.

### WarmupTickDelta
- **类型**: `float32`
- **描述**: Delta time used when ticking the system in warmup mode.

### OnSystemFinished
- **类型**: `FOnNiagaraSystemFinished`

### AutoAttachParent
- **类型**: `TWeakObjectPtr<USceneComponent>`

### AutoAttachSocketName
- **类型**: `FName`

### AutoAttachLocationRule
- **类型**: `EAttachmentRule`

### AutoAttachRotationRule
- **类型**: `EAttachmentRule`

### AutoAttachScaleRule
- **类型**: `EAttachmentRule`

### bAllowScalability
- **类型**: `bool`

### bForceSolo
- **类型**: `bool`

### bEnableGpuComputeDebug
- **类型**: `bool`

### bOverrideWarmupSettings
- **类型**: `bool`

### bAutoManageAttachment
- **类型**: `bool`

### bAutoAttachWeldSimulatedBodies
- **类型**: `bool`

### bWaitForCompilationOnActivate
- **类型**: `bool`

## 方法

### AdvanceSimulation
```angelscript
void AdvanceSimulation(int TickCount, float32 TickDeltaSeconds)
```
Advances this system's simulation by the specified number of ticks and delta time.

### AdvanceSimulationByTime
```angelscript
void AdvanceSimulationByTime(float32 SimulateTime, float32 TickDeltaSeconds)
```
Advances this system's simulation by the specified time in seconds and delta time. Advancement is done in whole ticks of TickDeltaSeconds so actual simulated time will be the nearest lower multiple of TickDeltaSeconds.

### ClearEmitterFixedBounds
```angelscript
void ClearEmitterFixedBounds(FName EmitterName)
```
Clear any previously set fixed bounds for the emitter instance.

### ClearSimCache
```angelscript
void ClearSimCache(bool bResetSystem)
```
Clear any active simulation cache.
When clearing a simulation cache that has been running you may wish to reset or continue, this option is only
valid when using a full simulation cache.  A renderer only cache will always reset as we can not continue the
simulation due to missing simulation data.

### ClearSystemFixedBounds
```angelscript
void ClearSystemFixedBounds()
```
Clear any previously set fixed bounds for the system instance.

### GetAgeUpdateMode
```angelscript
ENiagaraAgeUpdateMode GetAgeUpdateMode()
```

### GetAllowScalability
```angelscript
bool GetAllowScalability()
```

### GetAsset
```angelscript
UNiagaraSystem GetAsset()
```

### GetCustomTimeDilation
```angelscript
float32 GetCustomTimeDilation()
```

### GetDataInterface
```angelscript
UNiagaraDataInterface GetDataInterface(FString Name)
```

### GetDesiredAge
```angelscript
float32 GetDesiredAge()
```
Gets the desired age of the System instance.  This is only relevant when using the DesiredAge age update mode.

### GetEmitterFixedBounds
```angelscript
FBox GetEmitterFixedBounds(FName EmitterName)
```
Gets the fixed bounds for an emitter instance.
This will return the user set fixed bounds if set, or the emitters fixed bounds if set.
Note: The returned box may be invalid if no fixed bounds exist

### GetForceLocalPlayerEffect
```angelscript
bool GetForceLocalPlayerEffect()
```

### GetForceSolo
```angelscript
bool GetForceSolo()
```

### GetLockDesiredAgeDeltaTimeToSeekDelta
```angelscript
bool GetLockDesiredAgeDeltaTimeToSeekDelta()
```
Gets whether or not the delta time used to tick the system instance when using desired age is locked to the seek delta.  When true, the system instance
      will only be ticked when the desired age has changed by more than the seek delta.  When false the system instance will be ticked by the change in desired
      age when not seeking.

### GetMaxSimTime
```angelscript
float32 GetMaxSimTime()
```
Get the maximum CPU time in seconds we will simulate to the desired age, when we go beyond this limit ticks will be processed in the next frame.
This is only relevant when using the DesiredAge age update mode.
Note: The componet will not be visibile if we have ticks to process and SetCanRenderWhileSeeking is set to true

### GetOcclusionQueryMode
```angelscript
ENiagaraOcclusionQueryMode GetOcclusionQueryMode()
```

### GetPreviewLODDistance
```angelscript
float32 GetPreviewLODDistance()
```

### GetPreviewLODDistanceEnabled
```angelscript
bool GetPreviewLODDistanceEnabled()
```

### GetRandomSeedOffset
```angelscript
int GetRandomSeedOffset()
```

### GetSeekDelta
```angelscript
float32 GetSeekDelta()
```
Gets the delta value which is used when seeking from the current age, to the desired age.  This is only relevant
      when using the DesiredAge age update mode.

### GetSimCache
```angelscript
UNiagaraSimCache GetSimCache()
```
Get the active simulation cache, will return null if we do not have an active one.

### GetSystemFixedBounds
```angelscript
FBox GetSystemFixedBounds()
```
Gets the fixed bounds for the system instance.
This will return the user set fixed bounds if set, or the systems fixed bounds if set.
Note: The returned box may be invalid if no fixed bounds exist

### GetTickBehavior
```angelscript
ENiagaraTickBehavior GetTickBehavior()
```

### InitForPerformanceBaseline
```angelscript
void InitForPerformanceBaseline()
```
Initializes this component for capturing a performance baseline.
This will do things such as disabling distance culling and setting a LODDistance of 0 to ensure the effect is at it's maximum cost.

### IsPaused
```angelscript
bool IsPaused()
```

### ReinitializeSystem
```angelscript
void ReinitializeSystem()
```
Called on when an external object wishes to force this System to reinitialize itself from the System data.

### ResetSystem
```angelscript
void ResetSystem()
```
Resets the System to it's initial pre-simulated state.

### SeekToDesiredAge
```angelscript
void SeekToDesiredAge(float32 InDesiredAge)
```
Sets the desired age of the System instance and designates that this change is a seek.  When seeking to a desired age the
          The component can optionally prevent rendering.

### SetAgeUpdateMode
```angelscript
void SetAgeUpdateMode(ENiagaraAgeUpdateMode InAgeUpdateMode)
```
Sets the age update mode for the System instance.

### SetAllowScalability
```angelscript
void SetAllowScalability(bool bAllow)
```
Set whether this component is allowed to perform scalability checks and potentially be culled etc. Occasionally it is useful to disable this for specific components. E.g. Effects on the local player.

### SetAsset
```angelscript
void SetAsset(UNiagaraSystem InAsset, bool bResetExistingOverrideParameters)
```
Switch which asset the component is using.
This requires Niagara to wait for concurrent execution and the override parameter store to be synchronized with the new asset.
By default existing parameters are reset when we call SetAsset, modify bResetExistingOverrideParameters to leave existing parameter data as is.

### SetAutoDestroy
```angelscript
void SetAutoDestroy(bool bInAutoDestroy)
```

### SetCanRenderWhileSeeking
```angelscript
void SetCanRenderWhileSeeking(bool bInCanRenderWhileSeeking)
```
Sets whether or not the system can render while seeking.

### SetCustomTimeDilation
```angelscript
void SetCustomTimeDilation(float32 Dilation)
```
Sets the custom time dilation value for the component.
Note: This is only available on components that are in solo mode currently.

### SetDesiredAge
```angelscript
void SetDesiredAge(float32 InDesiredAge)
```
Sets the desired age of the System instance.  This is only relevant when using the DesiredAge age update mode.

### SetEmitterFixedBounds
```angelscript
void SetEmitterFixedBounds(FName EmitterName, FBox LocalBounds)
```
Sets the fixed bounds for an emitter instance, this overrides all other bounds.
The box is expected to be in local space not world space.
A default uninitialized box will clear the fixed bounds and revert back to emitter fixed / dynamic bounds.

### SetForceLocalPlayerEffect
```angelscript
void SetForceLocalPlayerEffect(bool bIsPlayerEffect)
```

### SetForceSolo
```angelscript
void SetForceSolo(bool bInForceSolo)
```

### SetGpuComputeDebug
```angelscript
void SetGpuComputeDebug(bool bEnableDebug)
```

### SetLockDesiredAgeDeltaTimeToSeekDelta
```angelscript
void SetLockDesiredAgeDeltaTimeToSeekDelta(bool bLock)
```
Sets whether or not the delta time used to tick the system instance when using desired age is locked to the seek delta.  When true, the system instance
      will only be ticked when the desired age has changed by more than the seek delta.  When false the system instance will be ticked by the change in desired
      age when not seeking.

### SetMaxSimTime
```angelscript
void SetMaxSimTime(float32 InMaxTime)
```
Sets the maximum CPU time in seconds we will simulate to the desired age, when we go beyond this limit ticks will be processed in the next frame.
This is only relevant when using the DesiredAge age update mode.
Note: The componet will not be visibile if we have ticks to process and SetCanRenderWhileSeeking is set to true

### SetNiagaraVariableActor
```angelscript
void SetNiagaraVariableActor(FString InVariableName, AActor Actor)
```

### SetNiagaraVariableBool
```angelscript
void SetNiagaraVariableBool(FString InVariableName, bool InValue)
```

### SetNiagaraVariableFloat
```angelscript
void SetNiagaraVariableFloat(FString InVariableName, float32 InValue)
```

### SetNiagaraVariableInt
```angelscript
void SetNiagaraVariableInt(FString InVariableName, int InValue)
```

### SetNiagaraVariableLinearColor
```angelscript
void SetNiagaraVariableLinearColor(FString InVariableName, FLinearColor InValue)
```

### SetNiagaraVariableMatrix
```angelscript
void SetNiagaraVariableMatrix(FString InVariableName, FMatrix InValue)
```

### SetNiagaraVariableObject
```angelscript
void SetNiagaraVariableObject(FString InVariableName, UObject Object)
```

### SetNiagaraVariablePosition
```angelscript
void SetNiagaraVariablePosition(FString InVariableName, FVector InValue)
```

### SetNiagaraVariableQuat
```angelscript
void SetNiagaraVariableQuat(FString InVariableName, FQuat InValue)
```

### SetNiagaraVariableVec2
```angelscript
void SetNiagaraVariableVec2(FString InVariableName, FVector2D InValue)
```

### SetNiagaraVariableVec3
```angelscript
void SetNiagaraVariableVec3(FString InVariableName, FVector InValue)
```

### SetNiagaraVariableVec4
```angelscript
void SetNiagaraVariableVec4(FString InVariableName, FVector4 InValue)
```

### SetOcclusionQueryMode
```angelscript
void SetOcclusionQueryMode(ENiagaraOcclusionQueryMode Mode)
```

### SetPaused
```angelscript
void SetPaused(bool bInPaused)
```

### SetPreviewLODDistance
```angelscript
void SetPreviewLODDistance(bool bEnablePreviewLODDistance, float32 PreviewLODDistance, float32 PreviewMaxDistance)
```

### SetRandomSeedOffset
```angelscript
void SetRandomSeedOffset(int NewRandomSeedOffset)
```

### SetRenderingEnabled
```angelscript
void SetRenderingEnabled(bool bInRenderingEnabled)
```
Sets whether or not rendering is enabled for this component.

### SetSeekDelta
```angelscript
void SetSeekDelta(float32 InSeekDelta)
```
Sets the delta value which is used when seeking from the current age, to the desired age.  This is only relevant
      when using the DesiredAge age update mode.

### SetSimCache
```angelscript
void SetSimCache(UNiagaraSimCache SimCache, bool bResetSystem)
```
Sets the simulation cache to use for the component.
A null SimCache parameter will clear the active simulation cache.
When clearing a simulation cache that has been running you may wish to reset or continue, this option is only
valid when using a full simulation cache.  A renderer only cache will always reset as we can not continue the
simulation due to missing simulation data.

### SetSystemFixedBounds
```angelscript
void SetSystemFixedBounds(FBox LocalBounds)
```
Sets the fixed bounds for the system instance, this overrides all other bounds.
The box is expected to be in local space not world space.
A default uninitialized box will clear the fixed bounds and revert back to system fixed / dynamic bounds.

### SetTickBehavior
```angelscript
void SetTickBehavior(ENiagaraTickBehavior NewTickBehavior)
```

### SetVariableActor
```angelscript
void SetVariableActor(FName InVariableName, AActor Actor)
```

### SetVariableBool
```angelscript
void SetVariableBool(FName InVariableName, bool InValue)
```
Sets a Niagara bool parameter by name, overriding locally if necessary.

### SetVariableFloat
```angelscript
void SetVariableFloat(FName InVariableName, float32 InValue)
```
Sets a Niagara float parameter by name, overriding locally if necessary.

### SetVariableInt
```angelscript
void SetVariableInt(FName InVariableName, int InValue)
```
Sets a Niagara int parameter by name, overriding locally if necessary.

### SetVariableLinearColor
```angelscript
void SetVariableLinearColor(FName InVariableName, FLinearColor InValue)
```
Sets a Niagara FLinearColor parameter by name, overriding locally if necessary.

### SetVariableMaterial
```angelscript
void SetVariableMaterial(FName InVariableName, UMaterialInterface Object)
```

### SetVariableMatrix
```angelscript
void SetVariableMatrix(FName InVariableName, FMatrix InValue)
```
Sets a Niagara matrix parameter by name, overriding locally if necessary.

### SetVariableObject
```angelscript
void SetVariableObject(FName InVariableName, UObject Object)
```

### SetVariablePosition
```angelscript
void SetVariablePosition(FName InVariableName, FVector InValue)
```
Sets a Niagara Position parameter by name, overriding locally if necessary.

### SetVariableQuat
```angelscript
void SetVariableQuat(FName InVariableName, FQuat InValue)
```
Sets a Niagara quaternion parameter by name, overriding locally if necessary.

### SetVariableStaticMesh
```angelscript
void SetVariableStaticMesh(FName InVariableName, UStaticMesh InValue)
```

### SetVariableTexture
```angelscript
void SetVariableTexture(FName InVariableName, UTexture Texture)
```

### SetVariableTextureRenderTarget
```angelscript
void SetVariableTextureRenderTarget(FName InVariableName, UTextureRenderTarget TextureRenderTarget)
```

### SetVariableVec2
```angelscript
void SetVariableVec2(FName InVariableName, FVector2D InValue)
```
Sets a Niagara Vector2 parameter by name, overriding locally if necessary.

### SetVariableVec3
```angelscript
void SetVariableVec3(FName InVariableName, FVector InValue)
```
Sets a Niagara Vector3 parameter by name, overriding locally if necessary.

### SetVariableVec4
```angelscript
void SetVariableVec4(FName InVariableName, FVector4 InValue)
```
Sets a Niagara Vector4 parameter by name, overriding locally if necessary.

