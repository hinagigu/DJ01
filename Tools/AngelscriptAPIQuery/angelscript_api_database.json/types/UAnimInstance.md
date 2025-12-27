# UAnimInstance

**继承自**: `UObject`

## 属性

### OnMontageBlendingOut
- **类型**: `FOnMontageBlendingOutStartedMCDelegate`

### OnMontageBlendedIn
- **类型**: `FOnMontageBlendedInEndedMCDelegate`

### OnMontageStarted
- **类型**: `FOnMontageStartedMCDelegate`

### OnMontageEnded
- **类型**: `FOnMontageEndedMCDelegate`

### OnAllMontageInstancesEnded
- **类型**: `FOnAllMontageInstancesEndedMCDelegate`

### bReceiveNotifiesFromLinkedInstances
- **类型**: `bool`

### bPropagateNotifiesToLinkedInstances
- **类型**: `bool`

### bUseMainInstanceMontageEvaluationData
- **类型**: `bool`

## 方法

### Blueprint_GetMainAnimInstance
```angelscript
UAnimInstance Blueprint_GetMainAnimInstance()
```
Get the 'main' anim instance, i.e. the one that is hosted on the skeletal mesh component

### Blueprint_GetSlotMontageLocalWeight
```angelscript
float32 Blueprint_GetSlotMontageLocalWeight(FName SlotNodeName)
```
Get local weight of any montages this slot node is playing. If this slot is not currently playing a montage, it will return 0.

### BlueprintBeginPlay
```angelscript
void BlueprintBeginPlay()
```
Executed when begin play is called on the owning component

### BlueprintInitializeAnimation
```angelscript
void BlueprintInitializeAnimation()
```
Executed when the Animation is initialized

### BlueprintLinkedAnimationLayersInitialized
```angelscript
void BlueprintLinkedAnimationLayersInitialized()
```
Executed when the all Linked Animation Layers are initialized

### BlueprintPostEvaluateAnimation
```angelscript
void BlueprintPostEvaluateAnimation()
```
Executed after the Animation is evaluated

### BlueprintThreadSafeUpdateAnimation
```angelscript
void BlueprintThreadSafeUpdateAnimation(float DeltaTime)
```
Executed when the Animation Blueprint is updated on a worker thread, just prior to graph update

### BlueprintUpdateAnimation
```angelscript
void BlueprintUpdateAnimation(float DeltaTimeX)
```
Executed when the Animation is updated

### CalculateDirection
```angelscript
float32 CalculateDirection(FVector Velocity, FRotator BaseRotation)
```

### ClearAllTransitionEvents
```angelscript
void ClearAllTransitionEvents()
```
Removes all queued transition requests

### ClearMorphTargets
```angelscript
void ClearMorphTargets()
```
Clears the current morph targets.

### ClearTransitionEvents
```angelscript
void ClearTransitionEvents(FName EventName)
```
Removes all queued transition requests with the given event name

### DynamicMontage_IsPlayingFrom
```angelscript
bool DynamicMontage_IsPlayingFrom(const UAnimSequenceBase Animation)
```
Returns true if there is an animation montage is currently active and playing that was created from the provided animation.

### GetActiveCurveNames
```angelscript
void GetActiveCurveNames(EAnimCurveType CurveType, TArray<FName>& OutNames)
```
This returns last up-to-date list of active curve names

### GetAllCurveNames
```angelscript
void GetAllCurveNames(TArray<FName>& OutNames)
```
This returns all curve names. This is the same as calling GetActiveCurveNames with CurveType == AttributeCurve

### GetCurrentActiveMontage
```angelscript
UAnimMontage GetCurrentActiveMontage()
```
Get a current Active Montage in this AnimInstance.
              Note that there might be multiple Active at the same time. This will only return the first active one it finds. *

### GetCurveValue
```angelscript
float32 GetCurveValue(FName CurveName)
```
Returns the value of a named curve.

### GetCurveValueWithDefault
```angelscript
bool GetCurveValueWithDefault(FName CurveName, float32 DefaultValue, float32& OutValue)
```
Returns whether a named curve was found, its value, and a default value when it's not found.
@param        AnimInstance    The anim instance to find this curve value for.
@param        CurveName               The name of the curve.
@param        DefaultValue    Value to use when the curve is not found.
@param        OutValue                The curve's value.

### GetDeltaSeconds
```angelscript
float32 GetDeltaSeconds()
```
Get the current delta time

### GetLinkedAnimGraphInstanceByTag
```angelscript
UAnimInstance GetLinkedAnimGraphInstanceByTag(FName InTag)
```
Runs through all nodes, attempting to find the first linked instance by name/tag

### GetLinkedAnimLayerInstanceByClass
```angelscript
UAnimInstance GetLinkedAnimLayerInstanceByClass(TSubclassOf<UAnimInstance> InClass, bool bCheckForChildClass)
```
Gets the first layer linked instance corresponding to the specified class, optionally if bCheckForChildClass is true, it will check IsChildOf on InClass.

### GetLinkedAnimLayerInstanceByGroup
```angelscript
UAnimInstance GetLinkedAnimLayerInstanceByGroup(FName InGroup)
```
Gets the layer linked instance corresponding to the specified group

### GetLinkedAnimLayerInstanceByGroupAndClass
```angelscript
UAnimInstance GetLinkedAnimLayerInstanceByGroupAndClass(FName InGroup, TSubclassOf<UAnimInstance> InClass)
```
Gets layer linked instance that matches group and class

### GetLinkedAnimLayerInstancesByGroup
```angelscript
void GetLinkedAnimLayerInstancesByGroup(FName InGroup, TArray<UAnimInstance>& OutLinkedInstances)
```
Runs through all nodes, attempting to find all distinct layer linked instances in the group

### GetOwningActor
```angelscript
AActor GetOwningActor()
```
Returns the owning actor of this AnimInstance

### GetOwningComponent
```angelscript
USkeletalMeshComponent GetOwningComponent()
```
Returns the skeletal mesh component that has created this AnimInstance

### GetPropagateNotifiesToLinkedInstances
```angelscript
bool GetPropagateNotifiesToLinkedInstances()
```
Get whether to propagate notifies to any linked anim instances

### GetReceiveNotifiesFromLinkedInstances
```angelscript
bool GetReceiveNotifiesFromLinkedInstances()
```
Get whether to process notifies from any linked anim instances

### GetSyncGroupPosition
```angelscript
FMarkerSyncAnimPosition GetSyncGroupPosition(FName InSyncGroupName)
```

### GetTimeToClosestMarker
```angelscript
bool GetTimeToClosestMarker(FName SyncGroup, FName MarkerName, float32& OutMarkerTime)
```
--- AI communication end ---

### HasMarkerBeenHitThisFrame
```angelscript
bool HasMarkerBeenHitThisFrame(FName SyncGroup, FName MarkerName)
```

### IsAnyMontagePlaying
```angelscript
bool IsAnyMontagePlaying()
```
Returns true if any montage is playing currently. Doesn't mean it's active though, it could be blending out.

### IsPlayingSlotAnimation
```angelscript
bool IsPlayingSlotAnimation(const UAnimSequenceBase Asset, FName SlotNodeName)
```
Return true if it's playing the slot animation

### IsSlotActive
```angelscript
bool IsSlotActive(FName SlotNodeName)
```
Return true if this instance has an active montage in the given slot. A UAnimMontage that is playing in the slot and blending out is not determined to be "active".

### IsSyncGroupBetweenMarkers
```angelscript
bool IsSyncGroupBetweenMarkers(FName InSyncGroupName, FName PreviousMarker, FName NextMarker, bool bRespectMarkerOrder)
```

### IsUsingMainInstanceMontageEvaluationData
```angelscript
bool IsUsingMainInstanceMontageEvaluationData()
```

### LinkAnimClassLayers
```angelscript
void LinkAnimClassLayers(TSubclassOf<UAnimInstance> InClass)
```
Runs through all layer nodes, attempting to find layer nodes that are implemented by the specified class, then sets up a linked instance of the class for each.
Allocates one linked instance to run each of the groups specified in the class, so state is shared. If a layer is not grouped (ie. NAME_None), then state is not shared
and a separate linked instance is allocated for each layer node.
If InClass is null, then all layers are reset to their defaults.

### LinkAnimGraphByTag
```angelscript
void LinkAnimGraphByTag(FName InTag, TSubclassOf<UAnimInstance> InClass)
```
Runs through all nodes, attempting to find a linked instance by name/tag, then sets the class of each node if the tag matches

### Montage_GetBlendTime
```angelscript
float32 Montage_GetBlendTime(const UAnimMontage Montage)
```
Get the current blend time of the Montage.
      If Montage reference is NULL, it will return the current blend time on the first active Montage found.

### Montage_GetCurrentSection
```angelscript
FName Montage_GetCurrentSection(const UAnimMontage Montage)
```
Returns the name of the current animation montage section.

### Montage_GetEffectivePlayRate
```angelscript
float32 Montage_GetEffectivePlayRate(const UAnimMontage Montage)
```
Get scaled PlayRate for Montage. This accounts for RateScale, so it will reflect the actual play rate seen in game.
      If Montage reference is NULL, scaled PlayRate for any Active Montage will be returned.
      If Montage is not playing, 0 is returned.

### Montage_GetIsStopped
```angelscript
bool Montage_GetIsStopped(const UAnimMontage Montage)
```
return true if Montage is not currently active. (not valid or blending out)

### Montage_GetPlayRate
```angelscript
float32 Montage_GetPlayRate(const UAnimMontage Montage)
```
Get PlayRate for Montage. This does not account for RateScale, so it may not reflect the actual play rate seen in game (see Montage_GetEffectivePlayRate).
      If Montage reference is NULL, PlayRate for any Active Montage will be returned.
      If Montage is not playing, 0 is returned.

### Montage_GetPosition
```angelscript
float32 Montage_GetPosition(const UAnimMontage Montage)
```
Get Current Montage Position

### Montage_IsActive
```angelscript
bool Montage_IsActive(const UAnimMontage Montage)
```
Returns true if the animation montage is active. If the Montage reference is NULL, it will return true if any Montage is active.

### Montage_IsPlaying
```angelscript
bool Montage_IsPlaying(const UAnimMontage Montage)
```
Returns true if the animation montage is currently active and playing.
      If reference is NULL, it will return true is ANY montage is currently active and playing.

### Montage_JumpToSection
```angelscript
void Montage_JumpToSection(FName SectionName, const UAnimMontage Montage)
```
Makes a montage jump to a named section. If Montage reference is NULL, it will do that to all active montages.

### Montage_JumpToSectionsEnd
```angelscript
void Montage_JumpToSectionsEnd(FName SectionName, const UAnimMontage Montage)
```
Makes a montage jump to the end of a named section. If Montage reference is NULL, it will do that to all active montages.

### Montage_Pause
```angelscript
void Montage_Pause(const UAnimMontage Montage)
```
Pauses the animation montage. If reference is NULL, it will pause ALL active montages.

### Montage_Play
```angelscript
float32 Montage_Play(UAnimMontage MontageToPlay, float32 InPlayRate, EMontagePlayReturnType ReturnValueType, float32 InTimeToStartMontageAt, bool bStopAllMontages)
```
Plays an animation montage. Returns the length of the animation montage in seconds. Returns 0.f if failed to play.

### Montage_PlayWithBlendIn
```angelscript
float32 Montage_PlayWithBlendIn(UAnimMontage MontageToPlay, FAlphaBlendArgs BlendIn, float32 InPlayRate, EMontagePlayReturnType ReturnValueType, float32 InTimeToStartMontageAt, bool bStopAllMontages)
```
Plays an animation montage. Same as Montage_Play, but you can specify an AlphaBlend for Blend In settings.

### Montage_PlayWithBlendSettings
```angelscript
float32 Montage_PlayWithBlendSettings(UAnimMontage MontageToPlay, FMontageBlendSettings BlendInSettings, float32 InPlayRate, EMontagePlayReturnType ReturnValueType, float32 InTimeToStartMontageAt, bool bStopAllMontages)
```
Plays an animation montage. Same as Montage_Play, but you can overwrite all of the montage's default blend in settings.

### Montage_Resume
```angelscript
void Montage_Resume(const UAnimMontage Montage)
```
Resumes a paused animation montage. If reference is NULL, it will resume ALL active montages.

### Montage_SetNextSection
```angelscript
void Montage_SetNextSection(FName SectionNameToChange, FName NextSection, const UAnimMontage Montage)
```
Relink new next section AFTER SectionNameToChange in run-time
    You can link section order the way you like in editor, but in run-time if you'd like to change it dynamically,
    use this function to relink the next section
    For example, you can have Start->Loop->Loop->Loop.... but when you want it to end, you can relink
    next section of Loop to be End to finish the montage, in which case, it stops looping by Loop->End.

@param SectionNameToChange : This should be the name of the Montage Section after which you want to insert a new next section
@param NextSection   : new next section

### Montage_SetPlayRate
```angelscript
void Montage_SetPlayRate(const UAnimMontage Montage, float32 NewPlayRate)
```
Change AnimMontage play rate. NewPlayRate = 1.0 is the default playback rate.

### Montage_SetPosition
```angelscript
void Montage_SetPosition(const UAnimMontage Montage, float32 NewPosition)
```
Set position.

### Montage_Stop
```angelscript
void Montage_Stop(float32 InBlendOutTime, const UAnimMontage Montage)
```
Stopped montages will blend out using their montage asset's BlendOut, with InBlendOutTime as the BlendTime

### Montage_StopGroupByName
```angelscript
void Montage_StopGroupByName(float32 InBlendOutTime, FName GroupName)
```
Stops all active montages belonging to a group.

### Montage_StopWithBlendOut
```angelscript
void Montage_StopWithBlendOut(FAlphaBlendArgs BlendOut, const UAnimMontage Montage)
```
Same as Montage_Stop. Uses values from the AlphaBlendArgs. Other settings come from the montage asset

### Montage_StopWithBlendSettings
```angelscript
void Montage_StopWithBlendSettings(FMontageBlendSettings BlendOutSettings, const UAnimMontage Montage)
```
Same as Montage_Stop, but all blend settings are provided instead of using the ones on the montage asset

### MontageSync_Follow
```angelscript
void MontageSync_Follow(const UAnimMontage MontageFollower, const UAnimInstance OtherAnimInstance, const UAnimMontage MontageLeader)
```
Synchronize a montage to another anim instance's montage. Both montages must be playing already
@param MontageFollower : The montage that will follow the leader in OtherAnimInstance
@param OtherAnimInstance      : The other anim instance we want to synchronize to. Can be set to self
@param MontageLeader  : The montage we want to follow in the other anim instance

### MontageSync_StopFollowing
```angelscript
void MontageSync_StopFollowing(const UAnimMontage MontageFollower)
```
Stop following the montage's leader in this anim instance
@param MontageFollower : The montage we want to stop synchronizing

### PlaySlotAnimationAsDynamicMontage
```angelscript
UAnimMontage PlaySlotAnimationAsDynamicMontage(UAnimSequenceBase Asset, FName SlotNodeName, float32 BlendInTime, float32 BlendOutTime, float32 InPlayRate, int LoopCount, float32 BlendOutTriggerTime, float32 InTimeToStartMontageAt)
```
Play normal animation asset on the slot node by creating a dynamic UAnimMontage. You can only play one asset (whether montage or animsequence) at a time per SlotGroup.

### PlaySlotAnimationAsDynamicMontage_WithBlendArgs
```angelscript
UAnimMontage PlaySlotAnimationAsDynamicMontage_WithBlendArgs(UAnimSequenceBase Asset, FName SlotNodeName, FAlphaBlendArgs BlendIn, FAlphaBlendArgs BlendOut, float32 InPlayRate, int LoopCount, float32 BlendOutTriggerTime, float32 InTimeToStartMontageAt)
```
Play normal animation asset on the slot node by creating a dynamic UAnimMontage with blend in arguments. You can only play one asset (whether montage or animsequence) at a time per SlotGroup.

### PlaySlotAnimationAsDynamicMontage_WithBlendSettings
```angelscript
UAnimMontage PlaySlotAnimationAsDynamicMontage_WithBlendSettings(UAnimSequenceBase Asset, FName SlotNodeName, FMontageBlendSettings BlendInSettings, FMontageBlendSettings BlendOutSettings, float32 InPlayRate, int LoopCount, float32 BlendOutTriggerTime, float32 InTimeToStartMontageAt)
```
Play normal animation asset on the slot node by creating a dynamic UAnimMontage with blend in settings. You can only play one asset (whether montage or animsequence) at a time per SlotGroup.

### RemovePoseSnapshot
```angelscript
void RemovePoseSnapshot(FName SnapshotName)
```
Remove a previously saved pose snapshot from the internal snapshot cache

### RequestSlotGroupInertialization
```angelscript
void RequestSlotGroupInertialization(FName InSlotGroupName, float32 Duration, const UBlendProfile BlendProfile)
```
Requests an inertial blend during the next anim graph update. Requires your anim graph to have a slot node belonging to the specified group name

### RequestTransitionEvent
```angelscript
bool RequestTransitionEvent(FName EventName, float RequestTimeout, ETransitionRequestQueueMode QueueMode, ETransitionRequestOverwriteMode OverwriteMode)
```
Attempts to queue a transition request, returns true if the request was successful

### ResetDynamics
```angelscript
void ResetDynamics(ETeleportType InTeleportType)
```
Reset any dynamics running simulation-style updates (e.g. on teleport, time skip etc.)

### SavePoseSnapshot
```angelscript
void SavePoseSnapshot(FName SnapshotName)
```
Takes a snapshot of the current skeletal mesh component pose & saves it internally.
This snapshot can then be retrieved by name in the animation blueprint for blending.
The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1 and then used it at LOD0 any bones not in LOD1 will use the reference pose

### SetMorphTarget
```angelscript
void SetMorphTarget(FName MorphTargetName, float32 Value)
```
Sets a morph target to a certain weight.

### SetPropagateNotifiesToLinkedInstances
```angelscript
void SetPropagateNotifiesToLinkedInstances(bool bSet)
```
Set whether to propagate notifies to any linked anim instances

### SetReceiveNotifiesFromLinkedInstances
```angelscript
void SetReceiveNotifiesFromLinkedInstances(bool bSet)
```
Set whether to process notifies from any linked anim instances

### SetRootMotionMode
```angelscript
void SetRootMotionMode(ERootMotionMode Value)
```
Set RootMotionMode

### SetUseMainInstanceMontageEvaluationData
```angelscript
void SetUseMainInstanceMontageEvaluationData(bool bSet)
```

### SnapshotPose
```angelscript
void SnapshotPose(FPoseSnapshot& Snapshot)
```
Takes a snapshot of the current skeletal mesh component pose and saves it to the specified snapshot.
The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1
and then used it at LOD0 any bones not in LOD1 will use the reference pose

### StopSlotAnimation
```angelscript
void StopSlotAnimation(float32 InBlendOutTime, FName SlotNodeName)
```
Stops currently playing slot animation slot or all

### TryGetPawnOwner
```angelscript
APawn TryGetPawnOwner()
```
kismet event functions

### UnlinkAnimClassLayers
```angelscript
void UnlinkAnimClassLayers(TSubclassOf<UAnimInstance> InClass)
```
Runs through all layer nodes, attempting to find layer nodes that are currently running the specified class, then resets each to its default value.
State sharing rules are as with SetLayerOverlay.
If InClass is null, does nothing.

### WasAnimNotifyStateActiveInAnyState
```angelscript
bool WasAnimNotifyStateActiveInAnyState(TSubclassOf<UAnimNotifyState> AnimNotifyStateType)
```
Get whether a particular notify state was active in any state machine last tick.

