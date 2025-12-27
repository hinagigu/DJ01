# USceneComponent

**继承自**: `UActorComponent`

A SceneComponent has a transform and supports attachment, but has no rendering or collision capabilities.
Useful as a 'dummy' component in the hierarchy to offset others.
@see [Scene Components](https://docs.unrealengine.com/latest/INT/Programming/UnrealArchitecture/Actors/Components/index.html#scenecomponents)

## 属性

### DetailMode
- **类型**: `EDetailMode`

### PhysicsVolumeChangedDelegate
- **类型**: `FPhysicsVolumeChanged`

### bShouldUpdatePhysicsVolume
- **类型**: `bool`

### bAbsoluteLocation
- **类型**: `bool`

### bAbsoluteRotation
- **类型**: `bool`

### bAbsoluteScale
- **类型**: `bool`

### bVisible
- **类型**: `bool`

### bHiddenInGame
- **类型**: `bool`

### bUseAttachParentBound
- **类型**: `bool`

### Mobility
- **类型**: `EComponentMobility`

## 方法

### GetChildComponentByClass
```angelscript
USceneComponent GetChildComponentByClass(TSubclassOf<USceneComponent> ComponentClass)
```

### GetChildrenComponentsByClass
```angelscript
void GetChildrenComponentsByClass(UClass ComponentClass, bool bIncludeAllDescendants, ? OutChildren)
```

### DetachFromParent
```angelscript
void DetachFromParent(bool bMaintainWorldPosition, bool bCallModify)
```

### DoesSocketExist
```angelscript
bool DoesSocketExist(FName InSocketName)
```
Return true if socket with the given name exists
@param InSocketName Name of the socket or the bone to get the transform

### GetAllSocketNames
```angelscript
TArray<FName> GetAllSocketNames()
```
Gets the names of all the sockets on the component.
@return Get the names of all the sockets on the component.

### GetAttachParent
```angelscript
USceneComponent GetAttachParent()
```
Get the SceneComponent we are attached to.

### GetAttachSocketName
```angelscript
FName GetAttachSocketName()
```
Get the socket we are attached to.

### GetChildComponent
```angelscript
USceneComponent GetChildComponent(int ChildIndex)
```
Gets the attached child component at the specified location

### GetChildrenComponents
```angelscript
void GetChildrenComponents(bool bIncludeAllDescendants, TArray<USceneComponent>& Children)
```
Gets all components that are attached to this component, possibly recursively
@param bIncludeAllDescendants Whether to include all descendants in the list of children (i.e. grandchildren, great grandchildren, etc.)
@param Children The list of attached child components

### GetComponentVelocity
```angelscript
FVector GetComponentVelocity()
```
Get velocity of the component: either ComponentVelocity, or the velocity of the physics body if simulating physics.
@return Velocity of the component

### GetForwardVector
```angelscript
FVector GetForwardVector()
```
Get the forward (X) unit direction vector from this component, in world space.

### GetNumChildrenComponents
```angelscript
int GetNumChildrenComponents()
```
Gets the number of attached children components

### GetParentComponents
```angelscript
void GetParentComponents(TArray<USceneComponent>& Parents)
```
Gets all attachment parent components up to and including the root component

### GetPhysicsVolume
```angelscript
APhysicsVolume GetPhysicsVolume()
```
Get the PhysicsVolume overlapping this component.

### GetRelativeTransform
```angelscript
FTransform GetRelativeTransform()
```
Returns the transform of the component relative to its parent

### GetRightVector
```angelscript
FVector GetRightVector()
```
Get the right (Y) unit direction vector from this component, in world space.

### GetShouldUpdatePhysicsVolume
```angelscript
bool GetShouldUpdatePhysicsVolume()
```
Gets whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.

### GetSocketLocation
```angelscript
FVector GetSocketLocation(FName InSocketName)
```
Get world-space socket or bone location.
@param InSocketName Name of the socket or the bone to get the transform
@return Socket transform in world space if socket is found. Otherwise it will return component's transform in world space.

### GetSocketRotation
```angelscript
FRotator GetSocketRotation(FName InSocketName)
```
Get world-space socket or bone  FRotator rotation.
@param InSocketName Name of the socket or the bone to get the transform
@return Socket transform in world space if socket if found. Otherwise it will return component's transform in world space.

### GetSocketTransform
```angelscript
FTransform GetSocketTransform(FName InSocketName, ERelativeTransformSpace TransformSpace)
```
Get world-space socket transform.
@param InSocketName Name of the socket or the bone to get the transform
@return Socket transform in world space if socket if found. Otherwise it will return component's transform in world space.

### GetUpVector
```angelscript
FVector GetUpVector()
```
Get the up (Z) unit direction vector from this component, in world space.

### IsAnySimulatingPhysics
```angelscript
bool IsAnySimulatingPhysics()
```
Returns whether the specified body is currently using physics simulation

### IsSimulatingPhysics
```angelscript
bool IsSimulatingPhysics(FName BoneName)
```
Returns whether the specified body is currently using physics simulation

### IsVisible
```angelscript
bool IsVisible()
```
Returns true if this component is visible in the current context

### AddLocalOffset
```angelscript
void AddLocalOffset(FVector DeltaLocation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the location of the component in its local reference frame
@param DeltaLocation         Change in location of the component in its local reference frame.
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

### AddLocalRotation
```angelscript
void AddLocalRotation(FRotator DeltaRotation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the rotation of the component in its local reference frame
@param DeltaRotation         Change in rotation of the component in its local reference frame.
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination (currently not supported for rotation).
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).

### AddLocalTransform
```angelscript
void AddLocalTransform(FTransform DeltaTransform, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the transform of the component in its local reference frame. Scale is unchanged.
@param DeltaTransform        Change in transform of the component in its local reference frame. Scale is unchanged.
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

### AddRelativeLocation
```angelscript
void AddRelativeLocation(FVector DeltaLocation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the translation of the component relative to its parent
@param DeltaLocation         Change in location of the component relative to its parent
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

### AddRelativeRotation
```angelscript
void AddRelativeRotation(FRotator DeltaRotation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta the rotation of the component relative to its parent
@param DeltaRotation         Change in rotation of the component relative to is parent.
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination (currently not supported for rotation).
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).

### AddWorldOffset
```angelscript
void AddWorldOffset(FVector DeltaLocation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the location of the component in world space.
@param DeltaLocation         Change in location in world space for the component.
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

### AddWorldRotation
```angelscript
void AddWorldRotation(FRotator DeltaRotation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the rotation of the component in world space.
@param DeltaRotation         Change in rotation in world space for the component.
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination (currently not supported for rotation).
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

### AddWorldTransform
```angelscript
void AddWorldTransform(FTransform DeltaTransform, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the transform of the component in world space. Ignores scale and sets it to (1,1,1).
@param DeltaTransform        Change in transform in world space for the component. Scale is ignored.
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

### AddWorldTransformKeepScale
```angelscript
void AddWorldTransformKeepScale(FTransform DeltaTransform, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Adds a delta to the transform of the component in world space. Scale is unchanged.
@param DeltaTransform        Change in transform in world space for the component. Scale is ignored since we preserve the original scale.
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

### AttachTo
```angelscript
bool AttachTo(USceneComponent InParent, FName InSocketName, EAttachLocation AttachType, bool bWeldSimulatedBodies)
```

### AttachToComponent
```angelscript
bool AttachToComponent(USceneComponent Parent, FName SocketName, EAttachmentRule LocationRule, EAttachmentRule RotationRule, EAttachmentRule ScaleRule, bool bWeldSimulatedBodies)
```
Attach this component to another scene component, optionally at a named socket. It is valid to call this on components whether or not they have been Registered.
@param  Parent                                        Parent to attach to.
@param  SocketName                            Optional socket to attach to on the parent.
@param  LocationRule                          How to handle translation when attaching.
@param  RotationRule                          How to handle rotation when attaching.
@param  ScaleRule                                     How to handle scale when attaching.
@param  bWeldSimulatedBodies          Whether to weld together simulated physics bodies. This transfers the shapes in the welded object into the parent (if simulated), which can result in permanent changes that persist even after subsequently detaching.
@return True if attachment is successful (or already attached to requested parent/socket), false if attachment is rejected and there is no change in AttachParent.

### DetachFromComponent
```angelscript
void DetachFromComponent(EDetachmentRule LocationRule, EDetachmentRule RotationRule, EDetachmentRule ScaleRule, bool bCallModify)
```
Detach this component from whatever it is attached to. Automatically unwelds components that are welded together (see AttachToComponent), though note that some effects of welding may not be undone.
@param LocationRule                          How to handle translations when detaching.
@param RotationRule                          How to handle rotation when detaching.
@param ScaleRule                                     How to handle scales when detaching.
@param bCallModify                           If true, call Modify() on the component and the current attach parent component

### GetWorldLocation
```angelscript
FVector GetWorldLocation()
```
Return location of the component, in world space

### GetWorldRotation
```angelscript
FRotator GetWorldRotation()
```
Returns rotation of the component, in world space.

### GetWorldScale
```angelscript
FVector GetWorldScale()
```
Returns scale of the component, in world space.

### GetWorldTransform
```angelscript
FTransform GetWorldTransform()
```
Get the current component-to-world transform for this component

### SetRelativeLocation
```angelscript
void SetRelativeLocation(FVector NewLocation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Set the location of the component relative to its parent
@param NewLocation           New location of the component relative to its parent.
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

### SetRelativeLocationAndRotation
```angelscript
void SetRelativeLocationAndRotation(FVector NewLocation, FRotator NewRotation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Set the location and rotation of the component relative to its parent
@param NewLocation           New location of the component relative to its parent.
@param NewRotation           New rotation of the component relative to its parent.
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

### SetRelativeRotation
```angelscript
void SetRelativeRotation(FRotator NewRotation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Set the rotation of the component relative to its parent
@param NewRotation           New rotation of the component relative to its parent
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination (currently not supported for rotation).
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).

### SetRelativeTransform
```angelscript
void SetRelativeTransform(FTransform NewTransform, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Set the transform of the component relative to its parent
@param NewTransform          New transform of the component relative to its parent.
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination (currently not supported for rotation).
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).

### SetWorldLocation
```angelscript
void SetWorldLocation(FVector NewLocation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Put this component at the specified location in world space. Updates relative location to achieve the final world location.
@param NewLocation           New location in world space for the component.
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

### SetWorldLocationAndRotation
```angelscript
void SetWorldLocationAndRotation(FVector NewLocation, FRotator NewRotation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Set the relative location and rotation of the component to put it at the supplied pose in world space.
@param NewLocation           New location in world space for the component.
@param NewRotation           New rotation in world space for the component.
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

### SetWorldRotation
```angelscript
void SetWorldRotation(FRotator NewRotation, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
* Put this component at the specified rotation in world space. Updates relative rotation to achieve the final world rotation.
* @param NewRotation           New rotation in world space for the component.
* @param SweepHitResult        Hit result from any impact if sweep is true.
* @param bSweep                        Whether we sweep to the destination (currently not supported for rotation).
* @param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
*                                                      If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
*                                                      If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
*                                                      If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

### SetWorldTransform
```angelscript
void SetWorldTransform(FTransform NewTransform, bool bSweep, FHitResult& SweepHitResult, bool bTeleport)
```
Set the transform of the component in world space.
@param NewTransform          New transform in world space for the component.
@param SweepHitResult        Hit result from any impact if sweep is true.
@param bSweep                        Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
                                                     Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
@param bTeleport                     Whether we teleport the physics state (if physics collision is enabled for this object).
                                                     If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
                                                     If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
                                                     If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

### ResetRelativeTransform
```angelscript
void ResetRelativeTransform()
```
Reset the transform of the component relative to its parent. Sets relative location to zero, relative rotation to no rotation, and Scale to 1.

### SetAbsolute
```angelscript
void SetAbsolute(bool bNewAbsoluteLocation, bool bNewAbsoluteRotation, bool bNewAbsoluteScale)
```
Set which parts of the relative transform should be relative to parent, and which should be relative to world

### SetHiddenInGame
```angelscript
void SetHiddenInGame(bool NewHidden, bool bPropagateToChildren)
```
Changes the value of bHiddenInGame, if false this will disable Visibility during gameplay

### SetMobility
```angelscript
void SetMobility(EComponentMobility NewMobility)
```
Set how often this component is allowed to move during runtime. Causes a component re-register if the component is already registered

### SetRelativeScale3D
```angelscript
void SetRelativeScale3D(FVector NewScale3D)
```
Set the non-uniform scale of the component relative to its parent

### SetShouldUpdatePhysicsVolume
```angelscript
void SetShouldUpdatePhysicsVolume(bool bInShouldUpdatePhysicsVolume)
```
Sets whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.

### SetVisibility
```angelscript
void SetVisibility(bool bNewVisibility, bool bPropagateToChildren)
```
Set visibility of the component, if during game use this to turn on/off

### SetWorldScale3D
```angelscript
void SetWorldScale3D(FVector NewScale)
```
Set the relative scale of the component to put it at the supplied scale in world space.
@param NewScale              New scale in world space for this component.

### ToggleVisibility
```angelscript
void ToggleVisibility(bool bPropagateToChildren)
```
Toggle visibility of the component

### AddLocalOffset
```angelscript
void AddLocalOffset(FVector DeltaLocation)
```

### AddLocalRotation
```angelscript
void AddLocalRotation(FRotator DeltaRotation)
```

### AddLocalRotation
```angelscript
void AddLocalRotation(FQuat DeltaRotation)
```

### AddLocalTransform
```angelscript
void AddLocalTransform(FTransform DeltaTransform)
```

### AddRelativeLocation
```angelscript
void AddRelativeLocation(FVector DeltaLocation)
```

### AddRelativeRotation
```angelscript
void AddRelativeRotation(FRotator DeltaRotation)
```

### AddRelativeRotation
```angelscript
void AddRelativeRotation(FQuat DeltaRotation)
```

### AddWorldOffset
```angelscript
void AddWorldOffset(FVector DeltaLocation)
```

### AddWorldRotation
```angelscript
void AddWorldRotation(FRotator DeltaRotation)
```

### AddWorldRotation
```angelscript
void AddWorldRotation(FQuat DeltaRotation)
```

### AddWorldTransform
```angelscript
void AddWorldTransform(FTransform DeltaTransform)
```

### AttachToComponent
```angelscript
void AttachToComponent(USceneComponent Parent, FName SocketName, EAttachmentRule AttachmentRule)
```

### GetBounds
```angelscript
FBoxSphereBounds GetBounds()
```

### GetComponentQuat
```angelscript
FQuat GetComponentQuat()
```

### GetRelativeLocation
```angelscript
FVector GetRelativeLocation()
```

### GetRelativeRotation
```angelscript
FRotator GetRelativeRotation()
```

### GetRelativeScale3D
```angelscript
FVector GetRelativeScale3D()
```

### GetSocketQuaternion
```angelscript
FQuat GetSocketQuaternion(FName SocketName)
```

### IsAttachedTo
```angelscript
bool IsAttachedTo(const USceneComponent CheckComponent)
```

### IsAttachedTo
```angelscript
bool IsAttachedTo(const AActor CheckActor)
```

### SetbVisualizeComponent
```angelscript
void SetbVisualizeComponent(bool bVisualize)
```

### SetComponentQuat
```angelscript
void SetComponentQuat(FQuat NewRotation)
```

### SetRelativeLocation
```angelscript
void SetRelativeLocation(FVector NewLocation)
```

### SetRelativeLocationAndRotation
```angelscript
void SetRelativeLocationAndRotation(FVector NewLocation, FRotator NewRotation)
```

### SetRelativeLocationAndRotation
```angelscript
void SetRelativeLocationAndRotation(FVector NewLocation, FQuat NewRotation)
```

### SetRelativeRotation
```angelscript
void SetRelativeRotation(FRotator NewRotation)
```

### SetRelativeRotation
```angelscript
void SetRelativeRotation(FQuat NewRotation)
```

### SetRelativeTransform
```angelscript
void SetRelativeTransform(FTransform NewTransform)
```

### SetWorldLocation
```angelscript
void SetWorldLocation(FVector NewLocation)
```

### SetWorldLocationAndRotation
```angelscript
void SetWorldLocationAndRotation(FVector NewLocation, FRotator NewRotation)
```

### SetWorldLocationAndRotation
```angelscript
void SetWorldLocationAndRotation(FVector NewLocation, FQuat NewRotation)
```

### SetWorldRotation
```angelscript
void SetWorldRotation(FRotator NewRotation)
```

### SetWorldRotation
```angelscript
void SetWorldRotation(FQuat NewRotation)
```

### SetWorldTransform
```angelscript
void SetWorldTransform(FTransform NewTransform)
```

