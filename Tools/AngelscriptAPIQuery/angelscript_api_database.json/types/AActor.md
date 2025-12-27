# AActor

**继承自**: `UObject`

Actor is the base class for an Object that can be placed or spawned in a level.
Actors may contain a collection of ActorComponents, which can be used to control how actors move, how they are rendered, etc.
The other main function of an Actor is the replication of properties and function calls across the network during play.


Actor initialization has multiple steps, here's the order of important virtual functions that get called:
- UObject::PostLoad: For actors statically placed in a level, the normal UObject PostLoad gets called both in the editor and during gameplay.
                     This is not called for newly spawned actors.
- UActorComponent::OnComponentCreated: When an actor is spawned in the editor or during gameplay, this gets called for any native components.
                                       For blueprint-created components, this gets called during construction for that component.
                                       This is not called for components loaded from a level.
- AActor::PreRegisterAllComponents: For statically placed actors and spawned actors that have native root components, this gets called now.
                                    For blueprint actors without a native root component, these registration functions get called later during construction.
- UActorComponent::RegisterComponent: All components are registered in editor and at runtime, this creates their physical/visual representation.
                                      These calls may be distributed over multiple frames, but are always after PreRegisterAllComponents.
                                      This may also get called later on after an UnregisterComponent call removes it from the world.
- AActor::PostRegisterAllComponents: Called for all actors both in the editor and in gameplay, this is the last function that is called in all cases.
- AActor::PostActorCreated: When an actor is created in the editor or during gameplay, this gets called right before construction.
                            This is not called for components loaded from a level.
- AActor::UserConstructionScript: Called for blueprints that implement a construction script.
- AActor::OnConstruction: Called at the end of ExecuteConstruction, which calls the blueprint construction script.
                          This is called after all blueprint-created components are fully created and registered.
                          This is only called during gameplay for spawned actors, and may get rerun in the editor when changing blueprints.
- AActor::PreInitializeComponents: Called before InitializeComponent is called on the actor's components.
                                   This is only called during gameplay and in certain editor preview windows.
- UActorComponent::Activate: This will be called only if the component has bAutoActivate set.
                             It will also got called later on if a component is manually activated.
- UActorComponent::InitializeComponent: This will be called only if the component has bWantsInitializeComponentSet.
                                        This only happens once per gameplay session.
- AActor::PostInitializeComponents: Called after the actor's components have been initialized, only during gameplay and some editor previews.
- AActor::BeginPlay: Called when the level starts ticking, only during actual gameplay.
                     This normally happens right after PostInitializeComponents but can be delayed for networked or child actors.

@see https://docs.unrealengine.com/Programming/UnrealArchitecture/Actors
@see https://docs.unrealengine.com/Programming/UnrealArchitecture/Actors/ActorLifecycle
@see UActorComponent

## 属性

### PrimaryActorTick
- **类型**: `FActorTickFunction`
- **描述**: Primary Actor tick function, which calls TickActor().
Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
@see https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
@see AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()

### UpdateOverlapsMethodDuringLevelStreaming
- **类型**: `EActorUpdateOverlapsMethod`
- **描述**: Condition for calling UpdateOverlaps() to initialize overlap state when loaded in during level streaming.
If set to 'UseConfigDefault', the default specified in ini (displayed in 'DefaultUpdateOverlapsMethodDuringLevelStreaming') will be used.
If overlaps are not initialized, this actor and attached components will not have an initial state of what objects are touching it,
and overlap events may only come in once one of those objects update overlaps themselves (for example when moving).
However if an object touching it *does* initialize state, both objects will know about their touching state with each other.
This can be a potentially large performance savings during level loading and streaming, and is safe if the object and others initially
overlapping it do not need the overlap state because they will not trigger overlap notifications.

Note that if 'bGenerateOverlapEventsDuringLevelStreaming' is true, overlaps are always updated in this case, but that flag
determines whether the Begin/End overlap events are triggered.

@see bGenerateOverlapEventsDuringLevelStreaming, DefaultUpdateOverlapsMethodDuringLevelStreaming, GetUpdateOverlapsMethodDuringLevelStreaming()

### InitialLifeSpan
- **类型**: `float32`

### CustomTimeDilation
- **类型**: `float32`
- **描述**: Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.

### RuntimeGrid
- **类型**: `FName`
- **描述**: Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
If None, the decision will be left to the partition.

### ReplicatedMovement
- **类型**: `FRepMovement`
- **描述**: Used for replication of our RootComponent's position and velocity

### SpawnCollisionHandlingMethod
- **类型**: `ESpawnActorCollisionHandlingMethod`

### AutoReceiveInput
- **类型**: `EAutoReceiveInput`
- **描述**: Automatically registers this actor to receive input from a player.

### InputPriority
- **类型**: `int`
- **描述**: The priority of this input component when pushed in to the stack.

### NetCullDistanceSquared
- **类型**: `float32`

### NetUpdateFrequency
- **类型**: `float32`

### MinNetUpdateFrequency
- **类型**: `float32`

### NetPriority
- **类型**: `float32`

### PivotOffset
- **类型**: `FVector`

### HLODLayer
- **类型**: `UHLODLayer`
- **描述**: The UHLODLayer in which this actor should be included.

### Layers
- **类型**: `TArray<FName>`
- **描述**: Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.

### ActorGuid
- **类型**: `FGuid`
- **描述**: The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
@see         ActorInstanceGuid, FActorInstanceGuidMapper
@note        Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults.
                     See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.

### ActorInstanceGuid
- **类型**: `FGuid`
- **描述**: The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
@see         ActorGuid
@note        This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.

### ContentBundleGuid
- **类型**: `FGuid`
- **描述**: The GUID for this actor's content bundle.

### DataLayerAssets
- **类型**: `TArray<TSoftObjectPtr<UDataLayerAsset>>`

### SpriteScale
- **类型**: `float32`

### Tags
- **类型**: `TArray<FName>`

### OnTakeAnyDamage
- **类型**: `FTakeAnyDamageSignature`

### OnTakePointDamage
- **类型**: `FTakePointDamageSignature`

### OnTakeRadialDamage
- **类型**: `FTakeRadialDamageSignature`

### OnActorBeginOverlap
- **类型**: `FActorBeginOverlapSignature`

### OnActorEndOverlap
- **类型**: `FActorEndOverlapSignature`

### OnBeginCursorOver
- **类型**: `FActorBeginCursorOverSignature`

### OnEndCursorOver
- **类型**: `FActorEndCursorOverSignature`

### OnClicked
- **类型**: `FActorOnClickedSignature`

### OnReleased
- **类型**: `FActorOnReleasedSignature`

### OnInputTouchBegin
- **类型**: `FActorOnInputTouchBeginSignature`

### OnInputTouchEnd
- **类型**: `FActorOnInputTouchEndSignature`

### OnInputTouchEnter
- **类型**: `FActorBeginTouchOverSignature`

### OnInputTouchLeave
- **类型**: `FActorEndTouchOverSignature`

### OnActorHit
- **类型**: `FActorHitSignature`

### OnDestroyed
- **类型**: `FActorDestroyedSignature`

### OnEndPlay
- **类型**: `FActorEndPlaySignature`

### bAutoDestroyWhenFinished
- **类型**: `bool`

### bOnlyRelevantToOwner
- **类型**: `bool`

### bAlwaysRelevant
- **类型**: `bool`

### bReplicateMovement
- **类型**: `bool`

### bCallPreReplication
- **类型**: `bool`

### bCallPreReplicationForReplay
- **类型**: `bool`

### bHidden
- **类型**: `bool`

### bIsMainWorldOnly
- **类型**: `bool`

### bNetLoadOnClient
- **类型**: `bool`

### bNetUseOwnerRelevancy
- **类型**: `bool`

### bRelevantForLevelBounds
- **类型**: `bool`

### bReplayRewindable
- **类型**: `bool`

### bAllowTickBeforeBeginPlay
- **类型**: `bool`

### bCanBeDamaged
- **类型**: `bool`

### bBlockInput
- **类型**: `bool`

### bFindCameraComponentWhenViewTarget
- **类型**: `bool`

### bGenerateOverlapEventsDuringLevelStreaming
- **类型**: `bool`

### bIgnoresOriginShifting
- **类型**: `bool`

### bEnableAutoLODGeneration
- **类型**: `bool`

### bIsEditorOnlyActor
- **类型**: `bool`

### bReplicates
- **类型**: `bool`

### bCanBeInCluster
- **类型**: `bool`

### bReplicateUsingRegisteredSubObjectList
- **类型**: `bool`

### bAsyncPhysicsTickEnabled
- **类型**: `bool`

### NetDormancy
- **类型**: `ENetDormancy`

### Instigator
- **类型**: `APawn`

### RootComponent
- **类型**: `USceneComponent`

### bOptimizeBPComponentData
- **类型**: `bool`

### bIsSpatiallyLoaded
- **类型**: `bool`

## 方法

### IsActorInitialized
```angelscript
bool IsActorInitialized()
```

### HasActorBegunPlay
```angelscript
bool HasActorBegunPlay()
```

### IsHidden
```angelscript
bool IsHidden()
```

### GetActorNameOrLabel
```angelscript
FString GetActorNameOrLabel()
```

### GetGameInstance
```angelscript
UGameInstance GetGameInstance()
```

### GetComponentsByClass
```angelscript
void GetComponentsByClass(? OutComponents)
```

### GetComponentsByClass
```angelscript
void GetComponentsByClass(UClass ComponentClass, ? OutComponents)
```

### GetActorInstigator
```angelscript
APawn GetActorInstigator()
```

### GetActorInstigatorController
```angelscript
AController GetActorInstigatorController()
```

### ActorHasTag
```angelscript
bool ActorHasTag(FName Tag)
```
See if this actor's Tags array contains the supplied name tag

### AddTickPrerequisiteActor
```angelscript
void AddTickPrerequisiteActor(AActor PrerequisiteActor)
```
Make this actor tick after PrerequisiteActor. This only applies to this actor's tick function; dependencies for owned components must be set up separately if desired.

### AddTickPrerequisiteComponent
```angelscript
void AddTickPrerequisiteComponent(UActorComponent PrerequisiteComponent)
```
Make this actor tick after PrerequisiteComponent. This only applies to this actor's tick function; dependencies for owned components must be set up separately if desired.

### CanTriggerResimulation
```angelscript
bool CanTriggerResimulation()
```
Can this body trigger a resimulation when Physics Prediction is enabled

### CreateInputComponent
```angelscript
void CreateInputComponent(TSubclassOf<UInputComponent> InputComponentToCreate)
```
Creates an input component from the input component passed in
@param InputComponentToCreate The UInputComponent to create.

### DetachRootComponentFromParent
```angelscript
void DetachRootComponentFromParent(bool bMaintainWorldPosition)
```

### DisableInput
```angelscript
void DisableInput(APlayerController PlayerController)
```
Removes this actor from the stack of input being handled by a PlayerController.
@param PlayerController The PlayerController whose input events we no longer want to receive. If null, this actor will stop receiving input from all PlayerControllers.

### EnableInput
```angelscript
void EnableInput(APlayerController PlayerController)
```
Pushes this actor on to the stack of input being handled by a PlayerController.
@param PlayerController The PlayerController whose input events we want to receive.

### FindComponentByTag
```angelscript
UActorComponent FindComponentByTag(TSubclassOf<UActorComponent> ComponentClass, FName Tag)
```
Searches components array and returns first encountered component with a given tag.

### FlushNetDormancy
```angelscript
void FlushNetDormancy()
```
Forces dormant actor to replicate but doesn't change NetDormancy state (i.e., they will go dormant again if left dormant)

### ForceNetUpdate
```angelscript
void ForceNetUpdate()
```
Force actor to be updated to clients/demo net drivers

### GetActorBounds
```angelscript
void GetActorBounds(bool bOnlyCollidingComponents, FVector& Origin, FVector& BoxExtent, bool bIncludeFromChildActors)
```
Returns the bounding box of all components that make up this Actor (excluding ChildActorComponents).
@param       bOnlyCollidingComponents        If true, will only return the bounding box for components with collision enabled.
@param       Origin                                          Set to the center of the actor in world space
@param       BoxExtent                                       Set to half the actor's size in 3d space
@param       bIncludeFromChildActors         If true then recurse in to ChildActor components

### GetActorEnableCollision
```angelscript
bool GetActorEnableCollision()
```
Get current state of collision for the whole actor

### GetActorEyesViewPoint
```angelscript
void GetActorEyesViewPoint(FVector& OutLocation, FRotator& OutRotation)
```
Returns the point of view of the actor.
Note that this doesn't mean the camera, but the 'eyes' of the actor.
For example, for a Pawn, this would define the eye height location,
and view rotation (which is different from the pawn rotation which has a zeroed pitch component).
A camera first person view will typically use this view point. Most traces (weapon, AI) will be done from this view point.

@param       OutLocation - location of view point
@param       OutRotation - view rotation of actor.

### GetActorForwardVector
```angelscript
FVector GetActorForwardVector()
```
Get the forward (X) vector (length 1.0) from this Actor, in world space.

### GetActorLabel
```angelscript
FString GetActorLabel(bool bCreateIfNone)
```
Returns this actor's current label.  Actor labels are only available in development builds.

### GetActorRelativeScale3D
```angelscript
FVector GetActorRelativeScale3D()
```
Return the actor's relative scale 3d

### GetActorRightVector
```angelscript
FVector GetActorRightVector()
```
Get the right (Y) vector (length 1.0) from this Actor, in world space.

### GetActorScale3D
```angelscript
FVector GetActorScale3D()
```
Returns the Actor's world-space scale.

### GetActorTickInterval
```angelscript
float32 GetActorTickInterval()
```
Returns the tick interval of this actor's primary tick function

### GetActorTimeDilation
```angelscript
float32 GetActorTimeDilation()
```
Get ActorTimeDilation - this can be used for input control or speed control for slomo.
We don't want to scale input globally because input can be used for UI, which do not care for TimeDilation.

### GetActorUpVector
```angelscript
FVector GetActorUpVector()
```
Get the up (Z) vector (length 1.0) from this Actor, in world space.

### GetAllChildActors
```angelscript
void GetAllChildActors(TArray<AActor>& ChildActors, bool bIncludeDescendants)
```
Returns a list of all actors spawned by our Child Actor Components, including children of children.
This does not return the contents of the Children array

### GetAttachedActors
```angelscript
void GetAttachedActors(TArray<AActor>& OutActors, bool bResetArray, bool bRecursivelyIncludeAttachedActors)
```
Find all Actors which are attached directly to a component in this actor

### GetAttachParentActor
```angelscript
AActor GetAttachParentActor()
```
Walk up the attachment chain from RootComponent until we encounter a different actor, and return it. If we are not attached to a component in a different actor, returns nullptr

### GetAttachParentSocketName
```angelscript
FName GetAttachParentSocketName()
```
Walk up the attachment chain from RootComponent until we encounter a different actor, and return the socket name in the component. If we are not attached to a component in a different actor, returns NAME_None

### GetComponentByClass
```angelscript
UActorComponent GetComponentByClass(TSubclassOf<UActorComponent> ComponentClass)
```
Searches components array and returns first encountered component of the specified class

### GetComponentsByInterface
```angelscript
TArray<UActorComponent> GetComponentsByInterface(TSubclassOf<UInterface> Interface)
```
Gets all the components that implements the given interface.

### GetComponentsByTag
```angelscript
TArray<UActorComponent> GetComponentsByTag(TSubclassOf<UActorComponent> ComponentClass, FName Tag)
```
Gets all the components that inherit from the given class with a given tag.

### GetDefaultActorLabel
```angelscript
FString GetDefaultActorLabel()
```
Returns this actor's default label (does not include any numeric suffix).  Actor labels are only available in development builds.

### GetDistanceTo
```angelscript
float32 GetDistanceTo(const AActor OtherActor)
```
Returns the distance from this Actor to OtherActor.

### GetDotProductTo
```angelscript
float32 GetDotProductTo(const AActor OtherActor)
```
Returns the dot product from this Actor to OtherActor. Returns -2.0 on failure. Returns 0.0 for coincidental actors.

### GetFolderPath
```angelscript
FName GetFolderPath()
```
Returns this actor's folder path. Actor folder paths are only available in development builds.

### GetGameTimeSinceCreation
```angelscript
float32 GetGameTimeSinceCreation()
```
The number of seconds (in game time) since this Actor was created, relative to Get Game Time In Seconds.

### GetHorizontalDistanceTo
```angelscript
float32 GetHorizontalDistanceTo(const AActor OtherActor)
```
Returns the distance from this Actor to OtherActor, ignoring Z.

### GetHorizontalDotProductTo
```angelscript
float32 GetHorizontalDotProductTo(const AActor OtherActor)
```
Returns the dot product from this Actor to OtherActor, ignoring Z. Returns -2.0 on failure. Returns 0.0 for coincidental actors.

### GetInstigator
```angelscript
APawn GetInstigator()
```
Returns the instigator for this actor, or nullptr if there is none.

### GetInstigatorController
```angelscript
AController GetInstigatorController()
```
Returns the instigator's controller for this actor, or nullptr if there is none.

### GetLevel
```angelscript
ULevel GetLevel()
```
Return the ULevel that this Actor is part of.

### GetLevelTransform
```angelscript
FTransform GetLevelTransform()
```
Return the FTransform of the level this actor is a part of.

### GetLifeSpan
```angelscript
float32 GetLifeSpan()
```
Get the remaining lifespan of this actor. If zero is returned the actor lives forever.

### GetLocalRole
```angelscript
ENetRole GetLocalRole()
```
Returns how much control the local machine has over this actor.

### GetOverlappingActors
```angelscript
void GetOverlappingActors(TArray<AActor>& OverlappingActors, TSubclassOf<AActor> ClassFilter)
```
Returns list of actors this actor is overlapping (any component overlapping any component). Does not return itself.
@param OverlappingActors             [out] Returned list of overlapping actors
@param ClassFilter                   [optional] If set, only returns actors of this class or subclasses

### GetOverlappingComponents
```angelscript
void GetOverlappingComponents(TArray<UPrimitiveComponent>& OverlappingComponents)
```
Returns list of components this actor is overlapping.

### GetOwner
```angelscript
AActor GetOwner()
```
Get the owner of this Actor, used primarily for network replication.

### GetParentActor
```angelscript
AActor GetParentActor()
```
If this Actor was created by a Child Actor Component returns the Actor that owns that Child Actor Component

### GetParentComponent
```angelscript
UChildActorComponent GetParentComponent()
```
If this Actor was created by a Child Actor Component returns that Child Actor Component

### GetPhysicsReplicationMode
```angelscript
EPhysicsReplicationMode GetPhysicsReplicationMode()
```
Get the physics replication mode of this body, via EPhysicsReplicationMode

### GetRayTracingGroupId
```angelscript
int GetRayTracingGroupId()
```
Return the RayTracingGroupId for this actor.

### GetRemoteRole
```angelscript
ENetRole GetRemoteRole()
```
Returns how much control the remote machine has over this actor.

### GetResimulationThreshold
```angelscript
float32 GetResimulationThreshold()
```
Get the error threshold in centimeters before this object should enforce a resimulation to trigger.

### GetSquaredDistanceTo
```angelscript
float32 GetSquaredDistanceTo(const AActor OtherActor)
```
Returns the squared distance from this Actor to OtherActor.

### GetSquaredHorizontalDistanceTo
```angelscript
float32 GetSquaredHorizontalDistanceTo(const AActor OtherActor)
```
Returns the squared distance from this Actor to OtherActor, ignoring Z.

### GetTickableWhenPaused
```angelscript
bool GetTickableWhenPaused()
```
Gets whether this actor can tick when paused.

### GetActorTransform
```angelscript
FTransform GetActorTransform()
```
Get the actor-to-world transform.
@return The transform that transforms from actor space to world space.

### GetVelocity
```angelscript
FVector GetVelocity()
```
Returns velocity (in cm/s (Unreal Units/second) of the rootcomponent if it is either using physics or has an associated MovementComponent

### GetVerticalDistanceTo
```angelscript
float32 GetVerticalDistanceTo(const AActor OtherActor)
```
Returns the distance from this Actor to OtherActor, ignoring XY.

### HasAuthority
```angelscript
bool HasAuthority()
```
Returns whether this actor has network authority

### IsActorBeingDestroyed
```angelscript
bool IsActorBeingDestroyed()
```
Returns true if this actor is currently being destroyed, some gameplay events may be unsafe

### IsActorTickEnabled
```angelscript
bool IsActorTickEnabled()
```
Returns whether this actor has tick enabled or not

### IsChildActor
```angelscript
bool IsChildActor()
```
Returns whether this Actor was spawned by a child actor component

### IsEditable
```angelscript
bool IsEditable()
```
Returns true if this actor is allowed to be displayed, selected and manipulated by the editor.

### IsHiddenEd
```angelscript
bool IsHiddenEd()
```
Returns true if this actor is hidden in the editor viewports, also checking temporary flags.

### IsHiddenEdAtStartup
```angelscript
bool IsHiddenEdAtStartup()
```
Returns true if the actor is hidden upon editor startup/by default, false if it is not

### IsOverlappingActor
```angelscript
bool IsOverlappingActor(const AActor Other)
```
Check whether any component of this Actor is overlapping any component of another Actor.
@param Other The other Actor to test against
@return Whether any component of this Actor is overlapping any component of another Actor.

### IsSelectable
```angelscript
bool IsSelectable()
```
Returns true if this actor can EVER be selected in a level in the editor.  Can be overridden by specific actors to make them unselectable.

### IsTemporarilyHiddenInEditor
```angelscript
bool IsTemporarilyHiddenInEditor(bool bIncludeParent)
```
Returns whether or not this actor was explicitly hidden in the editor for the duration of the current editor session
@param bIncludeParent - Whether to recurse up child actor hierarchy or not

### AddActorLocalOffset
```angelscript
void AddActorLocalOffset(FVector DeltaLocation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the location of this component in its local reference frame.
@param DelatLocation         The change in location in local space.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire swept volume.
                         Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated.
                         Setting the location without teleporting will not update the location of simulated child/attached components.

### AddActorLocalRotation
```angelscript
void AddActorLocalRotation(FRotator DeltaRotation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the rotation of this component in its local reference frame
@param DeltaRotation         The change in rotation in local space.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire swept volume.
                         Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated.
                         Setting the rotation without teleporting will not update the rotation of simulated child/attached components.

### AddActorLocalTransform
```angelscript
void AddActorLocalTransform(FTransform NewTransform, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the transform of this component in its local reference frame
@param NewTransform          The change in transform in local space.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire swept volume.
                         Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated.
                         Setting the transform without teleporting will not update the transform of simulated child/attached components.

### AddActorWorldOffset
```angelscript
void AddActorWorldOffset(FVector DeltaLocation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the location of this actor in world space.

@param DeltaLocation         The change in location.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire swept volume.
                         Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated.
                         Setting the location without teleporting will not update the location of simulated child/attached components.
@param SweepHitResult        The hit result from the move if swept.

### AddActorWorldRotation
```angelscript
void AddActorWorldRotation(FRotator DeltaRotation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the rotation of this actor in world space.

@param DeltaRotation         The change in rotation.
@param bSweep                        Whether to sweep to the target rotation (not currently supported for rotation).
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire swept volume.
                         Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated.
                         Setting the rotation without teleporting will not update the rotation of simulated child/attached components.
@param SweepHitResult        The hit result from the move if swept.

### AddActorWorldTransform
```angelscript
void AddActorWorldTransform(FTransform DeltaTransform, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the transform of this actor in world space. Ignores scale and sets it to (1,1,1).

### AddActorWorldTransformKeepScale
```angelscript
void AddActorWorldTransformKeepScale(FTransform DeltaTransform, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the transform of this actor in world space. Scale is unchanged.

### AttachRootComponentTo
```angelscript
void AttachRootComponentTo(USceneComponent InParent, FName InSocketName, EAttachLocation AttachLocationType, bool bWeldSimulatedBodies)
```

### AttachRootComponentToActor
```angelscript
void AttachRootComponentToActor(AActor InParentActor, FName InSocketName, EAttachLocation AttachLocationType, bool bWeldSimulatedBodies)
```

### AttachToActor
```angelscript
bool AttachToActor(AActor ParentActor, FName SocketName, EAttachmentRule LocationRule, EAttachmentRule RotationRule, EAttachmentRule ScaleRule, bool bWeldSimulatedBodies)
```
Attaches the RootComponent of this Actor to the supplied actor, optionally at a named socket.
@param ParentActor                           Actor to attach this actor's RootComponent to
@param SocketName                            Socket name to attach to, if any
@param LocationRule                          How to handle translation when attaching.
@param RotationRule                          How to handle rotation when attaching.
@param ScaleRule                                     How to handle scale when attaching.
@param bWeldSimulatedBodies          Whether to weld together simulated physics bodies.This transfers the shapes in the welded object into the parent (if simulated), which can result in permanent changes that persist even after subsequently detaching.
@return                                                      Whether the attachment was successful or not

### AttachToComponent
```angelscript
bool AttachToComponent(USceneComponent Parent, FName SocketName, EAttachmentRule LocationRule, EAttachmentRule RotationRule, EAttachmentRule ScaleRule, bool bWeldSimulatedBodies)
```
Attaches the RootComponent of this Actor to the supplied component, optionally at a named socket. It is not valid to call this on components that are not Registered.
@param Parent                                        Parent to attach to.
@param SocketName                            Optional socket to attach to on the parent.
@param LocationRule                          How to handle translation when attaching.
@param RotationRule                          How to handle rotation when attaching.
@param ScaleRule                                     How to handle scale when attaching.
@param bWeldSimulatedBodies          Whether to weld together simulated physics bodies. This transfers the shapes in the welded object into the parent (if simulated), which can result in permanent changes that persist even after subsequently detaching.
@return                                                      Whether the attachment was successful or not

### DestroyActor
```angelscript
void DestroyActor()
```
Destroy the actor

### DetachFromActor
```angelscript
void DetachFromActor(EDetachmentRule LocationRule, EDetachmentRule RotationRule, EDetachmentRule ScaleRule)
```
Detaches the RootComponent of this Actor from any SceneComponent it is currently attached to.
@param  LocationRule                         How to handle translation when detaching.
@param  RotationRule                         How to handle rotation when detaching.
@param  ScaleRule                            How to handle scale when detaching.

### GetActorLocation
```angelscript
FVector GetActorLocation()
```
Returns the location of the RootComponent of this Actor

### GetActorRotation
```angelscript
FRotator GetActorRotation()
```
Returns rotation of the RootComponent of this Actor.

### GetComponentsByClass
```angelscript
TArray<UActorComponent> GetComponentsByClass(TSubclassOf<UActorComponent> ComponentClass)
```
Gets all the components that inherit from the given class.
Currently returns an array of UActorComponent which must be cast to the correct type.
This intended to only be used by blueprints. Use GetComponents() in C++.

### GetRootComponent
```angelscript
USceneComponent GetRootComponent()
```
Returns the RootComponent of this Actor

### OnBecomeViewTarget
```angelscript
void OnBecomeViewTarget(APlayerController PC)
```
Event called when this Actor becomes the view target for the given PlayerController.

### OnEndViewTarget
```angelscript
void OnEndViewTarget(APlayerController PC)
```
Event called when this Actor is no longer the view target for the given PlayerController.

### OnReset
```angelscript
void OnReset()
```
Event called when this Actor is reset to its initial state - used when restarting level without reloading.

### SetActorLocation
```angelscript
bool SetActorLocation(FVector NewLocation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Move the Actor to the specified location.
@param NewLocation   The new location to move the Actor to.
@param bSweep                Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                             Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport             Whether we teleport the physics state (if physics collision is enabled for this object).
                                             If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                             If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                             If CCD is on and not teleporting, this will affect objects along the entire swept volume.
                     Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated.
                     Setting the location without teleporting will not update the location of simulated child/attached components.
@param SweepHitResult        The hit result from the move if swept.
@return      Whether the location was successfully set (if not swept), or whether movement occurred at all (if swept).

### SetActorLocationAndRotation
```angelscript
bool SetActorLocationAndRotation(FVector NewLocation, FRotator NewRotation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Move the actor instantly to the specified location and rotation.

@param NewLocation           The new location to teleport the Actor to.
@param NewRotation           The new rotation for the Actor.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire swept volume.
                         Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated.
                         Setting the location without teleporting will not update the location of simulated child/attached components.
@param SweepHitResult        The hit result from the move if swept.
@return      Whether the rotation was successfully set.

### SetActorRelativeLocation
```angelscript
void SetActorRelativeLocation(FVector NewRelativeLocation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Set the actor's RootComponent to the specified relative location.
@param NewRelativeLocation   New relative location of the actor's root component
@param bSweep                                Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                             Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                             Whether we teleport the physics state (if physics collision is enabled for this object).
                                                             If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                             If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                             If CCD is on and not teleporting, this will affect objects along the entire swept volume.
                             Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated.
                             Setting the location without teleporting will not update the location of simulated child/attached components.

### SetActorRelativeRotation
```angelscript
void SetActorRelativeRotation(FRotator NewRelativeRotation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Set the actor's RootComponent to the specified relative rotation
@param NewRelativeRotation   New relative rotation of the actor's root component
@param bSweep                                Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                             Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                             Whether we teleport the physics state (if physics collision is enabled for this object).
                                                             If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                             If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                             If CCD is on and not teleporting, this will affect objects along the entire swept volume.
                             Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated.
                             Setting the rotation without teleporting will not update the rotation of simulated child/attached components.

### SetActorRelativeTransform
```angelscript
void SetActorRelativeTransform(FTransform NewRelativeTransform, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Set the actor's RootComponent to the specified relative transform
@param NewRelativeTransform          New relative transform of the actor's root component
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire swept volume.
                         Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated.
                         Setting the transform without teleporting will not update the transform of simulated child/attached components.

### SetActorRotation
```angelscript
bool SetActorRotation(FRotator NewRotation, bool bTeleportPhysics)
```
Set the Actor's rotation instantly to the specified rotation.

@param       NewRotation     The new rotation for the Actor.
@param       bTeleportPhysics Whether we teleport the physics state (if physics collision is enabled for this object).
                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
         Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated.
         Setting the rotation without teleporting will not update the rotation of simulated child/attached components.
@return      Whether the rotation was successfully set.

### SetActorTransform
```angelscript
bool SetActorTransform(FTransform NewTransform, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Set the Actors transform to the specified one.
@param NewTransform          The new transform.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire swept volume.
                         Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated.
                         Setting the transform without teleporting will not update the transform of simulated child/attached components.

### Teleport
```angelscript
bool Teleport(FVector DestLocation, FRotator DestRotation)
```
Teleport this actor to a new location. If the actor doesn't fit exactly at the location specified, tries to slightly move it out of walls and such.

@param DestLocation The target destination point
@param DestRotation The target rotation at the destination
@return true if the actor has been successfully moved, or false if it couldn't fit.

### MakeNoise
```angelscript
void MakeNoise(float32 Loudness, APawn NoiseInstigator, FVector NoiseLocation, float32 MaxRange, FName Tag)
```
Trigger a noise caused by a given Pawn, at a given location.
Note that the NoiseInstigator Pawn MUST have a PawnNoiseEmitterComponent for the noise to be detected by a PawnSensingComponent.
Senders of MakeNoise should have an Instigator if they are not pawns, or pass a NoiseInstigator.

@param Loudness The relative loudness of this noise. Usual range is 0 (no noise) to 1 (full volume). If MaxRange is used, this scales the max range, otherwise it affects the hearing range specified by the sensor.
@param NoiseInstigator Pawn responsible for this noise.  Uses the actor's Instigator if NoiseInstigator is null
@param NoiseLocation Position of noise source.  If zero vector, use the actor's location.
@param MaxRange Max range at which the sound may be heard. A value of 0 indicates no max range (though perception may have its own range). Loudness scales the range. (Note: not supported for legacy PawnSensingComponent, only for AIPerception)
@param Tag Identifier for the noise.

### PrestreamTextures
```angelscript
void PrestreamTextures(float32 Seconds, bool bEnableStreaming, int CinematicTextureGroups)
```
Calls PrestreamTextures() for all the actor's meshcomponents.
@param Seconds - Number of seconds to force all mip-levels to be resident
@param bEnableStreaming      - Whether to start (true) or stop (false) streaming
@param CinematicTextureGroups - Bitfield indicating which texture groups that use extra high-resolution mips

### ActorBeginCursorOver
```angelscript
void ActorBeginCursorOver()
```
Event when this actor has the mouse moved over it with the clickable interface.

### ActorBeginOverlap
```angelscript
void ActorBeginOverlap(AActor OtherActor)
```
Event when this actor overlaps another actor, for example a player walking into a trigger.
For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events.
@note Components on both this and the other Actor must have bGenerateOverlapEvents set to true to generate overlap events.

### ActorEndCursorOver
```angelscript
void ActorEndCursorOver()
```
Event when this actor has the mouse moved off of it with the clickable interface.

### ActorEndOverlap
```angelscript
void ActorEndOverlap(AActor OtherActor)
```
Event when an actor no longer overlaps another actor, and they have separated.
@note Components on both this and the other Actor must have bGenerateOverlapEvents set to true to generate overlap events.

### ActorOnClicked
```angelscript
void ActorOnClicked(FKey ButtonPressed)
```
Event when this actor is clicked by the mouse when using the clickable interface.

### ActorOnInputTouchBegin
```angelscript
void ActorOnInputTouchBegin(ETouchIndex FingerIndex)
```
Event when this actor is touched when click events are enabled.

### ActorOnInputTouchEnd
```angelscript
void ActorOnInputTouchEnd(ETouchIndex FingerIndex)
```
Event when this actor is under the finger when untouched when click events are enabled.

### ActorOnInputTouchEnter
```angelscript
void ActorOnInputTouchEnter(ETouchIndex FingerIndex)
```
Event when this actor has a finger moved over it with the clickable interface.

### ActorOnInputTouchLeave
```angelscript
void ActorOnInputTouchLeave(ETouchIndex FingerIndex)
```
Event when this actor has a finger moved off of it with the clickable interface.

### ActorOnReleased
```angelscript
void ActorOnReleased(FKey ButtonReleased)
```
Event when this actor is under the mouse when left mouse button is released while using the clickable interface.

### AnyDamage
```angelscript
void AnyDamage(float Damage, const UDamageType DamageType, AController InstigatedBy, AActor DamageCauser)
```
Event when this actor takes ANY damage

### AsyncPhysicsTick
```angelscript
void AsyncPhysicsTick(float DeltaSeconds, float SimSeconds)
```
Event called every physics tick if bAsyncPhysicsTickEnabled is true

### BeginPlay
```angelscript
void BeginPlay()
```
Event when play begins for this actor.

### Destroyed
```angelscript
void Destroyed()
```
Called when the actor has been explicitly destroyed.

### EndPlay
```angelscript
void EndPlay(EEndPlayReason EndPlayReason)
```
Event to notify blueprints this actor is being deleted or removed from a level.

### Hit
```angelscript
void Hit(UPrimitiveComponent MyComp, AActor Other, UPrimitiveComponent OtherComp, bool bSelfMoved, FVector HitLocation, FVector HitNormal, FVector NormalImpulse, FHitResult Hit)
```
Event when this actor bumps into a blocking object, or blocks another actor that bumps into it.
This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.
For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event.

@note For collisions during physics simulation to generate hit events, 'Simulation Generates Hit Events' must be enabled.
@note When receiving a hit from another object's movement (bSelfMoved is false), the directions of 'Hit.Normal' and 'Hit.ImpactNormal'
will be adjusted to indicate force from the other object against this object.
@note NormalImpulse will be filled in for physics-simulating bodies, but will be zero for swept-component blocking collisions.

### PointDamage
```angelscript
void PointDamage(float Damage, const UDamageType DamageType, FVector HitLocation, FVector HitNormal, UPrimitiveComponent HitComponent, FName BoneName, FVector ShotFromDirection, AController InstigatedBy, AActor DamageCauser, FHitResult HitInfo)
```
Event when this actor takes POINT damage

### RadialDamage
```angelscript
void RadialDamage(float DamageReceived, const UDamageType DamageType, FVector Origin, FHitResult HitInfo, AController InstigatedBy, AActor DamageCauser)
```
Event when this actor takes RADIAL damage

### Tick
```angelscript
void Tick(float DeltaSeconds)
```
Event called every frame, if ticking is enabled

### RemoveTickPrerequisiteActor
```angelscript
void RemoveTickPrerequisiteActor(AActor PrerequisiteActor)
```
Remove tick dependency on PrerequisiteActor.

### RemoveTickPrerequisiteComponent
```angelscript
void RemoveTickPrerequisiteComponent(UActorComponent PrerequisiteComponent)
```
Remove tick dependency on PrerequisiteComponent.

### SetActorEnableCollision
```angelscript
void SetActorEnableCollision(bool bNewActorEnableCollision)
```
Allows enabling/disabling collision for the whole actor

### SetActorHiddenInGame
```angelscript
void SetActorHiddenInGame(bool bNewHidden)
```
Sets the actor to be hidden in the game
@param  bNewHidden      Whether or not to hide the actor and all its components

### SetActorLabel
```angelscript
void SetActorLabel(FString NewActorLabel, bool bMarkDirty)
```
Assigns a new label to this actor.  Actor labels are only available in development builds.
@param       NewActorLabel   The new label string to assign to the actor.  If empty, the actor will have a default label.
@param       bMarkDirty              If true the actor's package will be marked dirty for saving.  Otherwise it will not be.  You should pass false for this parameter if dirtying is not allowed (like during loads)

### SetActorRelativeScale3D
```angelscript
void SetActorRelativeScale3D(FVector NewRelativeScale)
```
Set the actor's RootComponent to the specified relative scale 3d
@param NewRelativeScale      New scale to set the actor's RootComponent to

### SetActorScale3D
```angelscript
void SetActorScale3D(FVector NewScale3D)
```
Set the Actor's world-space scale.

### SetActorTickEnabled
```angelscript
void SetActorTickEnabled(bool bEnabled)
```
Set this actor's tick functions to be enabled or disabled. Only has an effect if the function is registered
This only modifies the tick function on actor itself
@param       bEnabled        Whether it should be enabled or not

### SetActorTickInterval
```angelscript
void SetActorTickInterval(float32 TickInterval)
```
Sets the tick interval of this actor's primary tick function. Will not enable a disabled tick function. Takes effect on next tick.
@param TickInterval  The rate at which this actor should be ticking

### SetAutoDestroyWhenFinished
```angelscript
void SetAutoDestroyWhenFinished(bool bVal)
```

### SetFolderPath
```angelscript
void SetFolderPath(FName NewFolderPath)
```
Assigns a new folder to this actor. Actor folder paths are only available in development builds.
@param       NewFolderPath           The new folder to assign to the actor.

### SetIsTemporarilyHiddenInEditor
```angelscript
void SetIsTemporarilyHiddenInEditor(bool bIsHidden)
```
Explicitly sets whether or not this actor is hidden in the editor for the duration of the current editor session
@param bIsHidden     True if the actor is hidden

### SetLifeSpan
```angelscript
void SetLifeSpan(float32 InLifespan)
```
Set the lifespan of this actor. When it expires the object will be destroyed. If requested lifespan is 0, the timer is cleared and the actor will not be destroyed.

### SetNetDormancy
```angelscript
void SetNetDormancy(ENetDormancy NewDormancy)
```
Puts actor in dormant networking state

### SetOwner
```angelscript
void SetOwner(AActor NewOwner)
```
Set the owner of this Actor, used primarily for network replication.
@param NewOwner      The Actor who takes over ownership of this Actor

### SetPhysicsReplicationMode
```angelscript
void SetPhysicsReplicationMode(EPhysicsReplicationMode ReplicationMode)
```
Set the physics replication mode of this body, via EPhysicsReplicationMode

### SetRayTracingGroupId
```angelscript
void SetRayTracingGroupId(int InRaytracingGroupId)
```
Specify a RayTracingGroupId for this actors. Components with invalid RayTracingGroupId will inherit the actors.

### SetReplicateMovement
```angelscript
void SetReplicateMovement(bool bInReplicateMovement)
```
Set whether this actor's movement replicates to network clients.
@param bInReplicateMovement Whether this Actor's movement replicates to clients.

### SetReplicates
```angelscript
void SetReplicates(bool bInReplicates)
```
Set whether this actor replicates to network clients. When this actor is spawned on the server it will be sent to clients as well.
Properties flagged for replication will update on clients if they change on the server.
Internally changes the RemoteRole property and handles the cases where the actor needs to be added to the network actor list.
@param bInReplicates Whether this Actor replicates to network clients.
@see https://docs.unrealengine.com/InteractiveExperiences/Networking/Actors

### SetTickableWhenPaused
```angelscript
void SetTickableWhenPaused(bool bTickableWhenPaused)
```
Sets whether this actor can tick when paused.

### SetTickGroup
```angelscript
void SetTickGroup(ETickingGroup NewTickGroup)
```
Sets the ticking group for this actor.
@param NewTickGroup the new value to assign

### TearOff
```angelscript
void TearOff()
```
Networking - Server - TearOff this actor to stop replication to clients. Will set bTearOff to true.

### ConstructionScript
```angelscript
void ConstructionScript()
```
Construction script, the place to spawn components and do other setup.
@note Name used in CreateBlueprint function

### WasRecentlyRendered
```angelscript
bool WasRecentlyRendered(float32 Tolerance)
```
Returns true if this actor has been rendered "recently", with a tolerance in seconds to define what "recent" means.
e.g.: If a tolerance of 0.1 is used, this function will return true only if the actor was rendered in the last 0.1 seconds of game time.

@param Tolerance  How many seconds ago the actor last render time can be and still count as having been "recently" rendered.
@return Whether this actor was recently rendered.

### AddActorLocalOffset
```angelscript
void AddActorLocalOffset(FVector DeltaLocation)
```

### AddActorLocalRotation
```angelscript
void AddActorLocalRotation(FRotator DeltaRotation)
```

### AddActorLocalRotation
```angelscript
void AddActorLocalRotation(FQuat DeltaRotation)
```

### AddActorLocalTransform
```angelscript
void AddActorLocalTransform(FTransform DeltaTransform)
```

### AddActorWorldOffset
```angelscript
void AddActorWorldOffset(FVector DeltaLocation)
```

### AddActorWorldRotation
```angelscript
void AddActorWorldRotation(FRotator DeltaRotation)
```

### AddActorWorldRotation
```angelscript
void AddActorWorldRotation(FQuat DeltaRotation)
```

### AddActorWorldTransform
```angelscript
void AddActorWorldTransform(FTransform DeltaTransform)
```

### AttachToActor
```angelscript
void AttachToActor(AActor ParentActor, FName SocketName, EAttachmentRule AttachmentRule)
```

### AttachToComponent
```angelscript
void AttachToComponent(USceneComponent Parent, FName SocketName, EAttachmentRule AttachmentRule)
```

### GetActorQuat
```angelscript
FQuat GetActorQuat()
```

### GetActorRelativeLocation
```angelscript
FVector GetActorRelativeLocation()
```

### GetActorRelativeRotation
```angelscript
FRotator GetActorRelativeRotation()
```

### GetActorRelativeTransform
```angelscript
FTransform GetActorRelativeTransform()
```

### RerunConstructionScripts
```angelscript
void RerunConstructionScripts()
```

### SetActorLocation
```angelscript
void SetActorLocation(FVector NewLocation)
```

### SetActorLocationAndRotation
```angelscript
void SetActorLocationAndRotation(FVector NewLocation, FRotator NewRotation, bool bTeleport)
```

### SetActorLocationAndRotation
```angelscript
void SetActorLocationAndRotation(FVector NewLocation, FQuat NewRotation, bool bTeleport)
```

### SetActorQuat
```angelscript
void SetActorQuat(FQuat NewRotation)
```

### SetActorRelativeLocation
```angelscript
void SetActorRelativeLocation(FVector NewRelativeLocation)
```

### SetActorRelativeRotation
```angelscript
void SetActorRelativeRotation(FRotator NewRelativeRotation)
```

### SetActorRelativeRotation
```angelscript
void SetActorRelativeRotation(FQuat NewRelativeRotation)
```

### SetActorRelativeTransform
```angelscript
void SetActorRelativeTransform(FTransform NewRelativeTransform)
```

### SetActorRotation
```angelscript
void SetActorRotation(FRotator NewRotation)
```

### SetActorRotation
```angelscript
void SetActorRotation(FQuat NewRotation)
```

### SetActorTransform
```angelscript
void SetActorTransform(FTransform NewTransform)
```

### SetbRunConstructionScriptOnDrag
```angelscript
void SetbRunConstructionScriptOnDrag(bool Value)
```

### CreateComponent
```angelscript
UActorComponent CreateComponent(TSubclassOf<UActorComponent> ComponentClass, FName WithName)
```

### GetComponent
```angelscript
UActorComponent GetComponent(TSubclassOf<UActorComponent> ComponentClass, FName WithName)
```

### GetOrCreateComponent
```angelscript
UActorComponent GetOrCreateComponent(TSubclassOf<UActorComponent> ComponentClass, FName WithName)
```

### GetAllComponents
```angelscript
void GetAllComponents(UClass ComponentClass, TArray<UActorComponent>& OutComponents)
```

