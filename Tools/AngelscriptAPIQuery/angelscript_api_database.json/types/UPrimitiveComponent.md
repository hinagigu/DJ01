# UPrimitiveComponent

**继承自**: `USceneComponent`

PrimitiveComponents are SceneComponents that contain or generate some sort of geometry, generally to be rendered or used as collision data.
There are several subclasses for the various types of geometry, but the most common by far are the ShapeComponents (Capsule, Sphere, Box), StaticMeshComponent, and SkeletalMeshComponent.
ShapeComponents generate geometry that is used for collision detection but are not rendered, while StaticMeshComponents and SkeletalMeshComponents contain pre-built geometry that is rendered, but can also be used for collision detection.

## 属性

### MinDrawDistance
- **类型**: `float32`

### LDMaxDrawDistance
- **类型**: `float32`

### CachedMaxDrawDistance
- **类型**: `float32`
- **描述**: The distance to cull this primitive at.
A CachedMaxDrawDistance of 0 indicates that the primitive should not be culled by distance.

### IndirectLightingCacheQuality
- **类型**: `EIndirectLightingCacheQuality`

### HLODBatchingPolicy
- **类型**: `EHLODBatchingPolicy`

### ShadowCacheInvalidationBehavior
- **类型**: `EShadowCacheInvalidationBehavior`

### CanCharacterStepUpOn
- **类型**: `ECanBeCharacterBase`

### RayTracingGroupId
- **类型**: `int`

### CustomPrimitiveData
- **类型**: `FCustomPrimitiveData`
- **描述**: Optional user defined default values for the custom primitive data of this primitive

### TranslucencySortPriority
- **类型**: `int`

### RuntimeVirtualTextures
- **类型**: `TArray<TObjectPtr<URuntimeVirtualTexture>>`

### VirtualTextureLodBias
- **类型**: `int8`
- **描述**: Bias to the LOD selected for rendering to runtime virtual textures.

### VirtualTextureCullMips
- **类型**: `int8`
- **描述**: Number of lower mips in the runtime virtual texture to skip for rendering this primitive.
Larger values reduce the effective draw distance in the runtime virtual texture.
This culling method doesn't take into account primitive size or virtual texture size.

### VirtualTextureMinCoverage
- **类型**: `int8`
- **描述**: Set the minimum pixel coverage before culling from the runtime virtual texture.
Larger values reduce the effective draw distance in the runtime virtual texture.

### VirtualTextureRenderPassType
- **类型**: `ERuntimeVirtualTextureMainPassType`

### BodyInstance
- **类型**: `FBodyInstance`

### OnComponentHit
- **类型**: `FComponentHitSignature`

### OnComponentBeginOverlap
- **类型**: `FComponentBeginOverlapSignature`

### OnComponentEndOverlap
- **类型**: `FComponentEndOverlapSignature`

### OnComponentWake
- **类型**: `FComponentWakeSignature`

### OnComponentSleep
- **类型**: `FComponentSleepSignature`

### OnComponentPhysicsStateChanged
- **类型**: `FComponentPhysicsStateChanged`

### OnBeginCursorOver
- **类型**: `FComponentBeginCursorOverSignature`

### OnEndCursorOver
- **类型**: `FComponentEndCursorOverSignature`

### OnClicked
- **类型**: `FComponentOnClickedSignature`

### OnReleased
- **类型**: `FComponentOnReleasedSignature`

### OnInputTouchBegin
- **类型**: `FComponentOnInputTouchBeginSignature`

### OnInputTouchEnd
- **类型**: `FComponentOnInputTouchEndSignature`

### OnInputTouchEnter
- **类型**: `FComponentBeginTouchOverSignature`

### OnInputTouchLeave
- **类型**: `FComponentEndTouchOverSignature`

### RayTracingGroupCullingPriority
- **类型**: `ERayTracingGroupCullingPriority`

### ExcludeFromHLODLevels
- **类型**: `uint8`
- **描述**: Which specific HLOD levels this component should be excluded from

### bGenerateOverlapEvents
- **类型**: `bool`

### LightmapType
- **类型**: `ELightmapType`

### bEnableAutoLODGeneration
- **类型**: `bool`

### bNeverDistanceCull
- **类型**: `bool`

### bAlwaysCreatePhysicsState
- **类型**: `bool`

### bMultiBodyOverlap
- **类型**: `bool`

### bTraceComplexOnMove
- **类型**: `bool`

### bReturnMaterialOnMove
- **类型**: `bool`

### bAllowCullDistanceVolume
- **类型**: `bool`

### bVisibleInReflectionCaptures
- **类型**: `bool`

### bVisibleInRealTimeSkyCaptures
- **类型**: `bool`

### bVisibleInRayTracing
- **类型**: `bool`

### bRenderInMainPass
- **类型**: `bool`

### bRenderInDepthPass
- **类型**: `bool`

### bReceivesDecals
- **类型**: `bool`

### bHoldout
- **类型**: `bool`

### bOwnerNoSee
- **类型**: `bool`

### bOnlyOwnerSee
- **类型**: `bool`

### bTreatAsBackgroundForOcclusion
- **类型**: `bool`

### bUseAsOccluder
- **类型**: `bool`

### bConsiderForActorPlacementWhenHidden
- **类型**: `bool`

### bForceMipStreaming
- **类型**: `bool`

### CastShadow
- **类型**: `bool`

### bEmissiveLightSource
- **类型**: `bool`

### bAffectDynamicIndirectLighting
- **类型**: `bool`

### bAffectIndirectLightingWhileHidden
- **类型**: `bool`

### bAffectDistanceFieldLighting
- **类型**: `bool`

### bCastDynamicShadow
- **类型**: `bool`

### bCastStaticShadow
- **类型**: `bool`

### bCastVolumetricTranslucentShadow
- **类型**: `bool`

### bCastContactShadow
- **类型**: `bool`

### bSelfShadowOnly
- **类型**: `bool`

### bCastFarShadow
- **类型**: `bool`

### bCastInsetShadow
- **类型**: `bool`

### bCastCinematicShadow
- **类型**: `bool`

### bCastHiddenShadow
- **类型**: `bool`

### bCastShadowAsTwoSided
- **类型**: `bool`

### bLightAttachmentsAsGroup
- **类型**: `bool`

### bExcludeFromLightAttachmentGroup
- **类型**: `bool`

### bReceiveMobileCSMShadows
- **类型**: `bool`

### bSingleSampleShadowFromStationaryLights
- **类型**: `bool`

### bIgnoreRadialImpulse
- **类型**: `bool`

### bIgnoreRadialForce
- **类型**: `bool`

### bApplyImpulseOnDamage
- **类型**: `bool`

### bReplicatePhysicsToAutonomousProxy
- **类型**: `bool`

### bFillCollisionUnderneathForNavmesh
- **类型**: `bool`

### bRenderCustomDepth
- **类型**: `bool`

### bVisibleInSceneCaptureOnly
- **类型**: `bool`

### bHiddenInSceneCapture
- **类型**: `bool`

### bStaticWhenNotMoveable
- **类型**: `bool`

### LightingChannels
- **类型**: `FLightingChannels`

### CustomDepthStencilValue
- **类型**: `int`

### TranslucencySortDistanceOffset
- **类型**: `float32`

### CustomDepthStencilWriteMask
- **类型**: `ERendererStencilMask`

## 方法

### GetBoundingBoxExtents
```angelscript
FVector GetBoundingBoxExtents()
```

### GetBoundsOrigin
```angelscript
FVector GetBoundsOrigin()
```

### GetBoundsExtent
```angelscript
FVector GetBoundsExtent()
```

### GetBoundsRadius
```angelscript
float GetBoundsRadius()
```

### GetbSelectable
```angelscript
bool GetbSelectable()
```

### SetbSelectable
```angelscript
void SetbSelectable(bool bSelectable)
```

### SetLightmapType
```angelscript
void SetLightmapType(ELightmapType Type)
```

### AddAngularImpulseInDegrees
```angelscript
void AddAngularImpulseInDegrees(FVector Impulse, FName BoneName, bool bVelChange)
```
Add an angular impulse to a single rigid body. Good for one time instant burst.

@param  AngularImpulse  Magnitude and direction of impulse to apply. Direction is axis of rotation.
@param  BoneName        If a SkeletalMeshComponent, name of body to apply angular impulse to. 'None' indicates root body.
@param  bVelChange      If true, the Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect).

### AddAngularImpulseInRadians
```angelscript
void AddAngularImpulseInRadians(FVector Impulse, FName BoneName, bool bVelChange)
```
Add an angular impulse to a single rigid body. Good for one time instant burst.

@param  AngularImpulse  Magnitude and direction of impulse to apply. Direction is axis of rotation.
@param  BoneName        If a SkeletalMeshComponent, name of body to apply angular impulse to. 'None' indicates root body.
@param  bVelChange      If true, the Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect).

### AddForce
```angelscript
void AddForce(FVector Force, FName BoneName, bool bAccelChange)
```
Add a force to a single rigid body.
This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

@param  Force            Force vector to apply. Magnitude indicates strength of force.
@param  BoneName         If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body.
@param  bAccelChange If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no effect).

### AddForceAtLocation
```angelscript
void AddForceAtLocation(FVector Force, FVector Location, FName BoneName)
```
Add a force to a single rigid body at a particular location in world space.
This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

@param Force            Force vector to apply. Magnitude indicates strength of force.
@param Location         Location to apply force, in world space.
@param BoneName         If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body.

### AddForceAtLocationLocal
```angelscript
void AddForceAtLocationLocal(FVector Force, FVector Location, FName BoneName)
```
Add a force to a single rigid body at a particular location. Both Force and Location should be in body space.
This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

@param Force            Force vector to apply. Magnitude indicates strength of force.
@param Location         Location to apply force, in component space.
@param BoneName         If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body.

### AddImpulse
```angelscript
void AddImpulse(FVector Impulse, FName BoneName, bool bVelChange)
```
Add an impulse to a single rigid body. Good for one time instant burst.

@param  Impulse         Magnitude and direction of impulse to apply.
@param  BoneName        If a SkeletalMeshComponent, name of body to apply impulse to. 'None' indicates root body.
@param  bVelChange      If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no effect).

### AddImpulseAtLocation
```angelscript
void AddImpulseAtLocation(FVector Impulse, FVector Location, FName BoneName)
```
Add an impulse to a single rigid body at a specific location.

@param  Impulse         Magnitude and direction of impulse to apply.
@param  Location        Point in world space to apply impulse at.
@param  BoneName        If a SkeletalMeshComponent, name of bone to apply impulse to. 'None' indicates root body.

### AddRadialForce
```angelscript
void AddRadialForce(FVector Origin, float32 Radius, float32 Strength, ERadialImpulseFalloff Falloff, bool bAccelChange)
```
Add a force to all bodies in this component, originating from the supplied world-space location.

@param Origin           Origin of force in world space.
@param Radius           Radius within which to apply the force.
@param Strength         Strength of force to apply.
@param Falloff              Allows you to control the strength of the force as a function of distance from Origin.
@param bAccelChange If true, Strength is taken as a change in acceleration instead of a physical force (i.e. mass will have no effect).

### AddRadialImpulse
```angelscript
void AddRadialImpulse(FVector Origin, float32 Radius, float32 Strength, ERadialImpulseFalloff Falloff, bool bVelChange)
```
Add an impulse to all rigid bodies in this component, radiating out from the specified position.

@param Origin                Point of origin for the radial impulse blast, in world space
@param Radius                Size of radial impulse. Beyond this distance from Origin, there will be no affect.
@param Strength              Maximum strength of impulse applied to body.
@param Falloff               Allows you to control the strength of the impulse as a function of distance from Origin.
@param bVelChange    If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no effect).

### AddTorqueInDegrees
```angelscript
void AddTorqueInDegrees(FVector Torque, FName BoneName, bool bAccelChange)
```
Add a torque to a single rigid body.
@param Torque           Torque to apply. Direction is axis of rotation and magnitude is strength of torque.
@param BoneName         If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body.
@param bAccelChange If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect).

### AddTorqueInRadians
```angelscript
void AddTorqueInRadians(FVector Torque, FName BoneName, bool bAccelChange)
```
Add a torque to a single rigid body.
@param Torque           Torque to apply. Direction is axis of rotation and magnitude is strength of torque.
@param BoneName         If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body.
@param bAccelChange If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect).

### AddVelocityChangeImpulseAtLocation
```angelscript
void AddVelocityChangeImpulseAtLocation(FVector Impulse, FVector Location, FName BoneName)
```
Add an impulse to a single rigid body at a specific location. The Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect).

@param  Impulse         Magnitude and direction of impulse to apply.
@param  Location        Point in world space to apply impulse at.
@param  BoneName        If a SkeletalMeshComponent, name of bone to apply impulse to. 'None' indicates root body.

### CanCharacterStepUp
```angelscript
bool CanCharacterStepUp(APawn Pawn)
```
Return true if the given Pawn can step up onto this component.
This controls whether they can try to step up on it when they bump in to it, not whether they can walk on it after landing on it.
@param Pawn the Pawn that wants to step onto this component.
@see CanCharacterStepUpOn

### ClearMoveIgnoreActors
```angelscript
void ClearMoveIgnoreActors()
```
Clear the list of actors we ignore when moving.

### ClearMoveIgnoreComponents
```angelscript
void ClearMoveIgnoreComponents()
```
Clear the list of components we ignore when moving.

### CopyArrayOfMoveIgnoreActors
```angelscript
TArray<AActor> CopyArrayOfMoveIgnoreActors()
```
Returns the list of actors we currently ignore when moving.

### CopyArrayOfMoveIgnoreComponents
```angelscript
TArray<UPrimitiveComponent> CopyArrayOfMoveIgnoreComponents()
```
Returns the list of actors we currently ignore when moving.

### CreateDynamicMaterialInstance
```angelscript
UMaterialInstanceDynamic CreateDynamicMaterialInstance(int ElementIndex, UMaterialInterface SourceMaterial, FName OptionalName)
```
Creates a Dynamic Material Instance for the specified element index, optionally from the supplied material.
@param ElementIndex - The index of the skin to replace the material for.  If invalid, the material is unchanged and NULL is returned.

### GetAngularDamping
```angelscript
float32 GetAngularDamping()
```
Returns the angular damping of this component.

### GetBodyInstanceAsyncPhysicsTickHandle
```angelscript
FBodyInstanceAsyncPhysicsTickHandle GetBodyInstanceAsyncPhysicsTickHandle(FName BoneName, bool bGetWelded, int Index)
```
Returns BodyInstanceAsyncPhysicsTickHandle of the component. For use in the Async Physics Tick event

@param BoneName                               Used to get body associated with specific bone. NAME_None automatically gets the root most body
@param bGetWelded                             If the component has been welded to another component and bGetWelded is true we return the single welded BodyInstance that is used in the simulation
@param Index                                  Index used in Components with multiple body instances

@return               Returns the BodyInstanceAsyncPhysicsTickHandle based on various states (does component have multiple bodies? Is the body welded to another body?)

### GetCenterOfMass
```angelscript
FVector GetCenterOfMass(FName BoneName)
```
Get the center of mass of a single body. In the case of a welded body this will return the center of mass of the entire welded body (including its parent and children)
Objects that are not simulated return (0,0,0) as they do not have COM
@param BoneName                 If a SkeletalMeshComponent, name of body to get center of mass of. 'None' indicates root body.

### GetClosestPointOnCollision
```angelscript
float32 GetClosestPointOnCollision(FVector Point, FVector& OutPointOnBody, FName BoneName)
```
Returns the distance and closest point to the collision surface.
Component must have simple collision to be queried for closest point.

@param Point                          World 3D vector
@param OutPointOnBody         Point on the surface of collision closest to Point
@param BoneName                       If a SkeletalMeshComponent, name of body to set center of mass of. 'None' indicates root body.

@return               Success if returns > 0.f, if returns 0.f, it is either not convex or inside of the point
                              If returns < 0.f, this primitive does not have collsion

### GetCollisionEnabled
```angelscript
ECollisionEnabled GetCollisionEnabled()
```
Returns the form of collision for this component

### GetCollisionObjectType
```angelscript
ECollisionChannel GetCollisionObjectType()
```
Gets the collision object type

### GetCollisionProfileName
```angelscript
FName GetCollisionProfileName()
```
Get the collision profile name

### GetCollisionResponseToChannel
```angelscript
ECollisionResponse GetCollisionResponseToChannel(ECollisionChannel Channel)
```
Gets the response type given a specific channel

### GetCustomPrimitiveDataIndexForScalarParameter
```angelscript
int GetCustomPrimitiveDataIndexForScalarParameter(FName ParameterName)
```
Gets the index of the scalar parameter for the custom primitive data array
@param       ParameterName   The parameter name of the custom primitive
@return      The index of the custom primitive, INDEX_NONE (-1) if not found

### GetCustomPrimitiveDataIndexForVectorParameter
```angelscript
int GetCustomPrimitiveDataIndexForVectorParameter(FName ParameterName)
```
Gets the index of the vector parameter for the custom primitive data array
@param       ParameterName   The parameter name of the custom primitive
@return      The index of the custom primitive, INDEX_NONE (-1) if not found

### GetGenerateOverlapEvents
```angelscript
bool GetGenerateOverlapEvents()
```
If true, this component will generate overlap events when it is overlapping other components (eg Begin Overlap).
Both components (this and the other) must have this enabled for overlap events to occur.

@see [Overlap Events](https://docs.unrealengine.com/InteractiveExperiences/Physics/Collision/Overview#overlapandgenerateoverlapevents)
@see UpdateOverlaps(), BeginComponentOverlap(), EndComponentOverlap()

### GetIgnoreBoundsForEditorFocus
```angelscript
bool GetIgnoreBoundsForEditorFocus()
```
Whether or not the bounds of this component should be considered when focusing the editor camera to an actor with this component in it.
Useful for debug components which need a bounds for rendering but don't contribute to the visible part of the mesh in a meaningful way

### GetInertiaTensor
```angelscript
FVector GetInertiaTensor(FName BoneName)
```
Returns the inertia tensor of this component in kg cm^2. The inertia tensor is in local component space.

### GetLinearDamping
```angelscript
float32 GetLinearDamping()
```
Returns the linear damping of this component.

### GetMass
```angelscript
float32 GetMass()
```
Returns the mass of this component in kg.

### GetMassScale
```angelscript
float32 GetMassScale(FName BoneName)
```
Returns the mass scale used to calculate the mass of a single physics body

### GetMaterial
```angelscript
UMaterialInterface GetMaterial(int ElementIndex)
```
Returns the material used by the element at the specified index
@param ElementIndex - The element to access the material of.
@return the material used by the indexed element of this mesh.

### GetMaterialByName
```angelscript
UMaterialInterface GetMaterialByName(FName MaterialSlotName)
```
Returns the material used by the element in the slot with the specified name.
@param MaterialSlotName - The slot name to access the material of.
@return the material used in the slot specified, or null if none exists or the slot name is not found.

### GetMaterialFromCollisionFaceIndex
```angelscript
UMaterialInterface GetMaterialFromCollisionFaceIndex(int FaceIndex, int& SectionIndex)
```
Try and retrieve the material applied to a particular collision face of mesh. Used with face index returned from collision trace.
     @param  FaceIndex               Face index from hit result that was hit by a trace
     @param  SectionIndex    Section of the mesh that the face belongs to
     @return                                 Material applied to section that the hit face belongs to

### GetMaterialIndex
```angelscript
int GetMaterialIndex(FName MaterialSlotName)
```

### GetMaterialSlotNames
```angelscript
TArray<FName> GetMaterialSlotNames()
```

### GetMaxDepenetrationVelocity
```angelscript
float32 GetMaxDepenetrationVelocity(FName BoneName)
```
The maximum velocity used to depenetrate this object from others when spawned or teleported with initial overlaps (does not affect overlaps as a result of normal movement).
A value of zero will allow objects that are spawned overlapping to go to sleep without moving rather than pop out of each other. E.g., use zero if you spawn dynamic rocks
partially embedded in the ground and want them to be interactive but not pop out of the ground when touched.
A negative value means that the config setting CollisionInitialOverlapDepenetrationVelocity will be used.

### GetNumMaterials
```angelscript
int GetNumMaterials()
```
Return number of material elements in this primitive

### GetOverlappingActors
```angelscript
void GetOverlappingActors(TArray<AActor>& OverlappingActors, TSubclassOf<AActor> ClassFilter)
```
Returns a list of actors that this component is overlapping.
@param OverlappingActors             [out] Returned list of overlapping actors
@param ClassFilter                   [optional] If set, only returns actors of this class or subclasses

### GetOverlappingComponents
```angelscript
void GetOverlappingComponents(TArray<UPrimitiveComponent>& OutOverlappingComponents)
```
Returns unique list of components this component is overlapping.

### GetPhysicsAngularVelocityInDegrees
```angelscript
FVector GetPhysicsAngularVelocityInDegrees(FName BoneName)
```
Get the angular velocity of a single body, in degrees per second.
@param BoneName                 If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body.

### GetPhysicsAngularVelocityInRadians
```angelscript
FVector GetPhysicsAngularVelocityInRadians(FName BoneName)
```
Get the angular velocity of a single body, in radians per second.
@param BoneName                 If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body.

### GetPhysicsLinearVelocity
```angelscript
FVector GetPhysicsLinearVelocity(FName BoneName)
```
Get the linear velocity of a single body.
@param BoneName                 If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body.

### GetPhysicsLinearVelocityAtPoint
```angelscript
FVector GetPhysicsLinearVelocityAtPoint(FVector Point, FName BoneName)
```
Get the linear velocity of a point on a single body.
@param Point                    Point is specified in world space.
@param BoneName                 If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body.

### GetStaticWhenNotMoveable
```angelscript
bool GetStaticWhenNotMoveable()
```

### GetUpdateKinematicFromSimulation
```angelscript
bool GetUpdateKinematicFromSimulation()
```
Returns whether this component should be updated by simulation when it is kinematic.

### GetWalkableSlopeOverride
```angelscript
FWalkableSlopeOverride GetWalkableSlopeOverride()
```
Returns the slope override struct for this component.

### IgnoreActorWhenMoving
```angelscript
void IgnoreActorWhenMoving(AActor Actor, bool bShouldIgnore)
```
Tells this component whether to ignore collision with all components of a specific Actor when this component is moved.
Components on the other Actor may also need to be told to do the same when they move.
Does not affect movement of this component when simulating physics.

### IgnoreComponentWhenMoving
```angelscript
void IgnoreComponentWhenMoving(UPrimitiveComponent Component, bool bShouldIgnore)
```
Tells this component whether to ignore collision with another component when this component is moved.
The other components may also need to be told to do the same when they move.
Does not affect movement of this component when simulating physics.

### InvalidateLumenSurfaceCache
```angelscript
void InvalidateLumenSurfaceCache()
```
Invalidates Lumen surface cache and forces it to be refreshed. Useful to make material updates more responsive.

### IsAnyRigidBodyAwake
```angelscript
bool IsAnyRigidBodyAwake()
```
Returns if any body in this component is currently awake and simulating.

### IsExcludedFromHLODLevel
```angelscript
bool IsExcludedFromHLODLevel(EHLODLevelExclusion HLODLevel)
```
Whether this primitive is excluded from the specified HLOD level

### IsGravityEnabled
```angelscript
bool IsGravityEnabled()
```
Returns whether this component is affected by gravity. Returns always false if the component is not simulated.

### IsMaterialSlotNameValid
```angelscript
bool IsMaterialSlotNameValid(FName MaterialSlotName)
```

### IsOverlappingActor
```angelscript
bool IsOverlappingActor(const AActor Other)
```
Check whether this component is overlapping any component of the given Actor.
@param Other Actor to test this component against.
@return Whether this component is overlapping any component of the given Actor.

### IsOverlappingComponent
```angelscript
bool IsOverlappingComponent(const UPrimitiveComponent OtherComp)
```
Check whether this component is overlapping another component.
@param OtherComp Component to test this component against.
@return Whether this component is overlapping another component.

### BoxOverlapComponent
```angelscript
bool BoxOverlapComponent(FVector InBoxCentre, FBox InBox, bool bTraceComplex, bool bShowTrace, bool bPersistentShowTrace, FVector& HitLocation, FVector& HitNormal, FName& BoneName, FHitResult& OutHit)
```
Perform a box overlap against a single component as an AABB (No rotation)
@param InBoxCentre The centre of the box to overlap with the component
@param InBox Description of the box to use in the overlap
@param bTraceComplex Whether or not to trace the complex physics representation or just the simple representation
@param bShowTrace Whether or not to draw the trace in the world (for debugging)
@param bPersistentShowTrace Whether or not to make the debugging draw stay in the world permanently

### IsCollisionEnabled
```angelscript
bool IsCollisionEnabled()
```
Utility to see if there is any form of collision (query or physics) enabled on this component.

### IsPhysicsCollisionEnabled
```angelscript
bool IsPhysicsCollisionEnabled()
```
Utility to see if there is any physics collision enabled on this component.

### IsQueryCollisionEnabled
```angelscript
bool IsQueryCollisionEnabled()
```
Utility to see if there is any query collision enabled on this component.

### LineTraceComponent
```angelscript
bool LineTraceComponent(FVector TraceStart, FVector TraceEnd, bool bTraceComplex, bool bShowTrace, bool bPersistentShowTrace, FVector& HitLocation, FVector& HitNormal, FName& BoneName, FHitResult& OutHit)
```
Perform a line trace against a single component
@param TraceStart The start of the trace in world-space
@param TraceEnd The end of the trace in world-space
@param bTraceComplex Whether or not to trace the complex physics representation or just the simple representation
@param bShowTrace Whether or not to draw the trace in the world (for debugging)
@param bPersistentShowTrace Whether or not to make the debugging draw stay in the world permanently

### SphereOverlapComponent
```angelscript
bool SphereOverlapComponent(FVector InSphereCentre, float32 InSphereRadius, bool bTraceComplex, bool bShowTrace, bool bPersistentShowTrace, FVector& HitLocation, FVector& HitNormal, FName& BoneName, FHitResult& OutHit)
```
Perform a sphere overlap against a single component
@param InSphereCentre The centre of the sphere to overlap with the component
@param InSphereRadius The Radius of the sphere to overlap with the component
@param bTraceComplex Whether or not to trace the complex physics representation or just the simple representation
@param bShowTrace Whether or not to draw the trace in the world (for debugging)
@param bPersistentShowTrace Whether or not to make the debugging draw stay in the world permanently

### SphereTraceComponent
```angelscript
bool SphereTraceComponent(FVector TraceStart, FVector TraceEnd, float32 SphereRadius, bool bTraceComplex, bool bShowTrace, bool bPersistentShowTrace, FVector& HitLocation, FVector& HitNormal, FName& BoneName, FHitResult& OutHit)
```
Perform a sphere trace against a single component
@param TraceStart The start of the trace in world-space
@param TraceEnd The end of the trace in world-space
@param SphereRadius Radius of the sphere to trace against the component
@param bTraceComplex Whether or not to trace the complex physics representation or just the simple representation
@param bShowTrace Whether or not to draw the trace in the world (for debugging)
@param bPersistentShowTrace Whether or not to make the debugging draw stay in the world permanently

### PutRigidBodyToSleep
```angelscript
void PutRigidBodyToSleep(FName BoneName)
```
Force a single body back to sleep.
@param  BoneName        If a SkeletalMeshComponent, name of body to put to sleep. 'None' indicates root body.

### ScaleByMomentOfInertia
```angelscript
FVector ScaleByMomentOfInertia(FVector InputVector, FName BoneName)
```
Scales the given vector by the world space moment of inertia. Useful for computing the torque needed to rotate an object.

### SetAffectDistanceFieldLighting
```angelscript
void SetAffectDistanceFieldLighting(bool NewAffectDistanceFieldLighting)
```
Changes the value of Affect Distance Field Lighting

### SetAffectDynamicIndirectLighting
```angelscript
void SetAffectDynamicIndirectLighting(bool bNewAffectDynamicIndirectLighting)
```
Changes the value of bAffectDynamicIndirectLighting

### SetAffectIndirectLightingWhileHidden
```angelscript
void SetAffectIndirectLightingWhileHidden(bool bNewAffectIndirectLightingWhileHidden)
```
Changes the value of bAffectIndirectLightingWhileHidden

### SetAllMassScale
```angelscript
void SetAllMassScale(float32 InMassScale)
```
Change the mass scale used fo all bodies in this component

### SetAllPhysicsAngularVelocityInDegrees
```angelscript
void SetAllPhysicsAngularVelocityInDegrees(FVector NewAngVel, bool bAddToCurrent)
```
Set the angular velocity of all bodies in this component.

@param NewAngVel                New angular velocity to apply to physics, in degrees per second.
@param bAddToCurrent    If true, NewAngVel is added to the existing angular velocity of all bodies.

### SetAllPhysicsAngularVelocityInRadians
```angelscript
void SetAllPhysicsAngularVelocityInRadians(FVector NewAngVel, bool bAddToCurrent)
```
Set the angular velocity of all bodies in this component.

@param NewAngVel                New angular velocity to apply to physics, in radians per second.
@param bAddToCurrent    If true, NewAngVel is added to the existing angular velocity of all bodies.

### SetAllPhysicsLinearVelocity
```angelscript
void SetAllPhysicsLinearVelocity(FVector NewVel, bool bAddToCurrent)
```
Set the linear velocity of all bodies in this component.

@param NewVel                   New linear velocity to apply to physics.
@param bAddToCurrent    If true, NewVel is added to the existing velocity of the body.

### SetAllUseCCD
```angelscript
void SetAllUseCCD(bool InUseCCD)
```
Set whether all bodies in this component should use Continuous Collision Detection

### SetAngularDamping
```angelscript
void SetAngularDamping(float32 InDamping)
```
Sets the angular damping of this component.

### SetBoundsScale
```angelscript
void SetBoundsScale(float32 NewBoundsScale)
```
Scale the bounds of this object, used for frustum culling. Useful for features like WorldPositionOffset.

### SetCastContactShadow
```angelscript
void SetCastContactShadow(bool bInCastContactShadow)
```
Changes the value of bCastContactShadow.

### SetCastHiddenShadow
```angelscript
void SetCastHiddenShadow(bool NewCastHiddenShadow)
```
Changes the value of CastHiddenShadow.

### SetCastInsetShadow
```angelscript
void SetCastInsetShadow(bool bInCastInsetShadow)
```
Changes the value of CastInsetShadow.

### SetCastShadow
```angelscript
void SetCastShadow(bool NewCastShadow)
```
Changes the value of CastShadow.

### SetCenterOfMass
```angelscript
void SetCenterOfMass(FVector CenterOfMassOffset, FName BoneName)
```
Set the center of mass of a single body. This will offset the physx-calculated center of mass.
Note that in the case where multiple bodies are attached together, the center of mass will be set for the entire group.
@param CenterOfMassOffset               User specified offset for the center of mass of this object, from the calculated location.
@param BoneName                 If a SkeletalMeshComponent, name of body to set center of mass of. 'None' indicates root body.

### SetCollisionEnabled
```angelscript
void SetCollisionEnabled(ECollisionEnabled NewType)
```
Controls what kind of collision is enabled for this body

### SetCollisionObjectType
```angelscript
void SetCollisionObjectType(ECollisionChannel Channel)
```
Changes the collision channel that this object uses when it moves
@param      Channel     The new channel for this component to use

### SetCollisionProfileName
```angelscript
void SetCollisionProfileName(FName InCollisionProfileName, bool bUpdateOverlaps)
```
Set Collision Profile Name
This function is called by constructors when they set ProfileName
This will change current CollisionProfileName to be this, and overwrite Collision Setting

@param InCollisionProfileName : New Profile Name

### SetCollisionResponseToAllChannels
```angelscript
void SetCollisionResponseToAllChannels(ECollisionResponse NewResponse)
```
Changes all ResponseToChannels container for this PrimitiveComponent. to be NewResponse

@param       NewResponse  What the new response should be to the supplied Channel

### SetCollisionResponseToChannel
```angelscript
void SetCollisionResponseToChannel(ECollisionChannel Channel, ECollisionResponse NewResponse)
```
Changes a member of the ResponseToChannels container for this PrimitiveComponent.

@param       Channel      The channel to change the response of
@param       NewResponse  What the new response should be to the supplied Channel

### SetConstraintMode
```angelscript
void SetConstraintMode(EDOFMode ConstraintMode)
```
Sets the constraint mode of the component.
@param ConstraintMode The type of constraint to use.

### SetCullDistance
```angelscript
void SetCullDistance(float32 NewCullDistance)
```
Changes the value of CullDistance.
@param NewCullDistance - The value to assign to CullDistance.

### SetCustomDepthStencilValue
```angelscript
void SetCustomDepthStencilValue(int Value)
```
Sets the CustomDepth stencil value (0 - 255) and marks the render state dirty.

### SetCustomDepthStencilWriteMask
```angelscript
void SetCustomDepthStencilWriteMask(ERendererStencilMask WriteMaskBit)
```
Sets the CustomDepth stencil write mask and marks the render state dirty.

### SetCustomPrimitiveDataFloat
```angelscript
void SetCustomPrimitiveDataFloat(int DataIndex, float32 Value)
```
Set custom primitive data at index DataIndex. This sets the run-time data only, so it doesn't serialize.

### SetCustomPrimitiveDataVector2
```angelscript
void SetCustomPrimitiveDataVector2(int DataIndex, FVector2D Value)
```
Set custom primitive data, two floats at once, from index DataIndex to index DataIndex + 1. This sets the run-time data only, so it doesn't serialize.

### SetCustomPrimitiveDataVector3
```angelscript
void SetCustomPrimitiveDataVector3(int DataIndex, FVector Value)
```
Set custom primitive data, three floats at once, from index DataIndex to index DataIndex + 2. This sets the run-time data only, so it doesn't serialize.

### SetCustomPrimitiveDataVector4
```angelscript
void SetCustomPrimitiveDataVector4(int DataIndex, FVector4 Value)
```
Set custom primitive data, four floats at once, from index DataIndex to index DataIndex + 3. This sets the run-time data only, so it doesn't serialize.

### SetDefaultCustomPrimitiveDataFloat
```angelscript
void SetDefaultCustomPrimitiveDataFloat(int DataIndex, float32 Value)
```
Set default custom primitive data at index DataIndex, and marks the render state dirty

### SetDefaultCustomPrimitiveDataVector2
```angelscript
void SetDefaultCustomPrimitiveDataVector2(int DataIndex, FVector2D Value)
```
Set default custom primitive data, two floats at once, from index DataIndex to index DataIndex + 1, and marks the render state dirty

### SetDefaultCustomPrimitiveDataVector3
```angelscript
void SetDefaultCustomPrimitiveDataVector3(int DataIndex, FVector Value)
```
Set default custom primitive data, three floats at once, from index DataIndex to index DataIndex + 2, and marks the render state dirty

### SetDefaultCustomPrimitiveDataVector4
```angelscript
void SetDefaultCustomPrimitiveDataVector4(int DataIndex, FVector4 Value)
```
Set default custom primitive data, four floats at once, from index DataIndex to index DataIndex + 3, and marks the render state dirty

### SetEmissiveLightSource
```angelscript
void SetEmissiveLightSource(bool NewEmissiveLightSource)
```
Changes the value of EmissiveLightSource.

### SetEnableGravity
```angelscript
void SetEnableGravity(bool bGravityEnabled)
```
Enables/disables whether this component is affected by gravity. This applies only to components with bSimulatePhysics set to true.

### SetExcludedFromHLODLevel
```angelscript
void SetExcludedFromHLODLevel(EHLODLevelExclusion HLODLevel, bool bExcluded)
```
Exclude this primitive from the specified HLOD level

### SetExcludeFromLightAttachmentGroup
```angelscript
void SetExcludeFromLightAttachmentGroup(bool bInExcludeFromLightAttachmentGroup)
```
Changes the value of ExcludeFromLightAttachmentGroup.

### SetGenerateOverlapEvents
```angelscript
void SetGenerateOverlapEvents(bool bInGenerateOverlapEvents)
```
Modifies value returned by GetGenerateOverlapEvents()

### SetHiddenInSceneCapture
```angelscript
void SetHiddenInSceneCapture(bool bValue)
```
Sets bHideInSceneCapture property and marks the render state dirty.

### SetHoldout
```angelscript
void SetHoldout(bool bNewHoldout)
```
Changes the value of bHoldout (Path Tracing only feature)

### SetIgnoreBoundsForEditorFocus
```angelscript
void SetIgnoreBoundsForEditorFocus(bool bIgnore)
```
Set if we should ignore bounds when focusing the editor camera.

### SetLightAttachmentsAsGroup
```angelscript
void SetLightAttachmentsAsGroup(bool bInLightAttachmentsAsGroup)
```
Changes the value of LightAttachmentsAsGroup.

### SetLightingChannels
```angelscript
void SetLightingChannels(bool bChannel0, bool bChannel1, bool bChannel2)
```

### SetLinearDamping
```angelscript
void SetLinearDamping(float32 InDamping)
```
Sets the linear damping of this component.

### SetMassOverrideInKg
```angelscript
void SetMassOverrideInKg(FName BoneName, float32 MassInKg, bool bOverrideMass)
```
Override the mass (in Kg) of a single physics body.
Note that in the case where multiple bodies are attached together, the override mass will be set for the entire group.
Set the Override Mass to false if you want to reset the body's mass to the auto-calculated physx mass.

### SetMassScale
```angelscript
void SetMassScale(FName BoneName, float32 InMassScale)
```
Change the mass scale used to calculate the mass of a single physics body

### SetMaterial
```angelscript
void SetMaterial(int ElementIndex, UMaterialInterface Material)
```
Changes the material applied to an element of the mesh.
@param ElementIndex - The element to access the material of.
@return the material used by the indexed element of this mesh.

### SetMaterialByName
```angelscript
void SetMaterialByName(FName MaterialSlotName, UMaterialInterface Material)
```
Changes the material applied to an element of the mesh.
@param MaterialSlotName - The slot name to access the material of.
@return the material used by the indexed element of this mesh.

### SetMaxDepenetrationVelocity
```angelscript
void SetMaxDepenetrationVelocity(FName BoneName, float32 InMaxDepenetrationVelocity)
```
The maximum velocity used to depenetrate this object from others when spawned or teleported with initial overlaps (does not affect overlaps as a result of normal movement).
A value of zero will allow objects that are spawned overlapping to go to sleep without moving rather than pop out of each other. E.g., use zero if you spawn dynamic rocks
partially embedded in the ground and want them to be interactive but not pop out of the ground when touched.
A negative value means that the config setting CollisionInitialOverlapDepenetrationVelocity will be used.

### SetNotifyRigidBodyCollision
```angelscript
void SetNotifyRigidBodyCollision(bool bNewNotifyRigidBodyCollision)
```
Changes the value of bNotifyRigidBodyCollision

### SetOnlyOwnerSee
```angelscript
void SetOnlyOwnerSee(bool bNewOnlyOwnerSee)
```
Changes the value of bOnlyOwnerSee.

### SetOwnerNoSee
```angelscript
void SetOwnerNoSee(bool bNewOwnerNoSee)
```
Changes the value of bOwnerNoSee.

### SetPhysicsAngularVelocityInDegrees
```angelscript
void SetPhysicsAngularVelocityInDegrees(FVector NewAngVel, bool bAddToCurrent, FName BoneName)
```
Set the angular velocity of a single body.
This should be used cautiously - it may be better to use AddTorque or AddImpulse.

@param NewAngVel                New angular velocity to apply to body, in degrees per second.
@param bAddToCurrent    If true, NewAngVel is added to the existing angular velocity of the body.
@param BoneName                 If a SkeletalMeshComponent, name of body to modify angular velocity of. 'None' indicates root body.

### SetPhysicsAngularVelocityInRadians
```angelscript
void SetPhysicsAngularVelocityInRadians(FVector NewAngVel, bool bAddToCurrent, FName BoneName)
```
Set the angular velocity of a single body.
This should be used cautiously - it may be better to use AddTorque or AddImpulse.

@param NewAngVel                New angular velocity to apply to body, in radians per second.
@param bAddToCurrent    If true, NewAngVel is added to the existing angular velocity of the body.
@param BoneName                 If a SkeletalMeshComponent, name of body to modify angular velocity of. 'None' indicates root body.

### SetPhysicsLinearVelocity
```angelscript
void SetPhysicsLinearVelocity(FVector NewVel, bool bAddToCurrent, FName BoneName)
```
Set the linear velocity of a single body.
This should be used cautiously - it may be better to use AddForce or AddImpulse.

@param NewVel                   New linear velocity to apply to physics.
@param bAddToCurrent    If true, NewVel is added to the existing velocity of the body.
@param BoneName                 If a SkeletalMeshComponent, name of body to modify velocity of. 'None' indicates root body.

### SetPhysicsMaxAngularVelocityInDegrees
```angelscript
void SetPhysicsMaxAngularVelocityInDegrees(float32 NewMaxAngVel, bool bAddToCurrent, FName BoneName)
```
Set the maximum angular velocity of a single body.

@param NewMaxAngVel             New maximum angular velocity to apply to body, in degrees per second.
@param bAddToCurrent    If true, NewMaxAngVel is added to the existing maximum angular velocity of the body.
@param BoneName                 If a SkeletalMeshComponent, name of body to modify maximum angular velocity of. 'None' indicates root body.

### SetPhysicsMaxAngularVelocityInRadians
```angelscript
void SetPhysicsMaxAngularVelocityInRadians(float32 NewMaxAngVel, bool bAddToCurrent, FName BoneName)
```
Set the maximum angular velocity of a single body.

@param NewMaxAngVel             New maximum angular velocity to apply to body, in radians per second.
@param bAddToCurrent    If true, NewMaxAngVel is added to the existing maximum angular velocity of the body.
@param BoneName                 If a SkeletalMeshComponent, name of body to modify maximum angular velocity of. 'None' indicates root body.

### SetPhysMaterialOverride
```angelscript
void SetPhysMaterialOverride(UPhysicalMaterial NewPhysMaterial)
```
Changes the current PhysMaterialOverride for this component.
Note that if physics is already running on this component, this will _not_ alter its mass/inertia etc,
it will only change its surface properties like friction.

### SetReceivesDecals
```angelscript
void SetReceivesDecals(bool bNewReceivesDecals)
```
Changes the value of bReceivesDecals.

### SetRenderCustomDepth
```angelscript
void SetRenderCustomDepth(bool bValue)
```
Sets the bRenderCustomDepth property and marks the render state dirty.

### SetRenderInDepthPass
```angelscript
void SetRenderInDepthPass(bool bValue)
```
Sets bRenderInDepthPass property and marks the render state dirty.

### SetRenderInMainPass
```angelscript
void SetRenderInMainPass(bool bValue)
```
Sets bRenderInMainPass property and marks the render state dirty.

### SetScalarParameterForCustomPrimitiveData
```angelscript
void SetScalarParameterForCustomPrimitiveData(FName ParameterName, float32 Value)
```
Set a scalar parameter for custom primitive data. This sets the run-time data only, so it doesn't serialize.
@param       ParameterName   The parameter name of the custom primitive
@param       Value                   The new value of the custom primitive

### SetScalarParameterForDefaultCustomPrimitiveData
```angelscript
void SetScalarParameterForDefaultCustomPrimitiveData(FName ParameterName, float32 Value)
```
Set a scalar parameter for default custom primitive data. This will be serialized and is useful in construction scripts.
@param       ParameterName   The parameter name of the custom primitive
@param       Value                   The new value of the custom primitive

### SetSimulatePhysics
```angelscript
void SetSimulatePhysics(bool bSimulate)
```
Sets whether or not a single body should use physics simulation, or should be 'fixed' (kinematic).
Note that if this component is currently attached to something, beginning simulation will detach it.

@param  bSimulate       New simulation state for single body

### SetSingleSampleShadowFromStationaryLights
```angelscript
void SetSingleSampleShadowFromStationaryLights(bool bNewSingleSampleShadowFromStationaryLights)
```
Changes the value of bSingleSampleShadowFromStationaryLights.

### SetStaticWhenNotMoveable
```angelscript
void SetStaticWhenNotMoveable(bool bInStaticWhenNotMoveable)
```

### SetTranslucencySortDistanceOffset
```angelscript
void SetTranslucencySortDistanceOffset(float32 NewTranslucencySortDistanceOffset)
```
Changes the value of TranslucencySortDistanceOffset.

### SetTranslucentSortPriority
```angelscript
void SetTranslucentSortPriority(int NewTranslucentSortPriority)
```
Changes the value of TranslucentSortPriority.

### SetUpdateKinematicFromSimulation
```angelscript
void SetUpdateKinematicFromSimulation(bool bUpdateKinematicFromSimulation)
```
Enables/disables whether this component should be updated by simulation when it is kinematic. This is needed if (for example) its velocity needs to be accessed.

### SetUseCCD
```angelscript
void SetUseCCD(bool InUseCCD, FName BoneName)
```
Set whether this component should use Continuous Collision Detection

### SetVectorParameterForCustomPrimitiveData
```angelscript
void SetVectorParameterForCustomPrimitiveData(FName ParameterName, FVector4 Value)
```
Set a vector parameter for custom primitive data. This sets the run-time data only, so it doesn't serialize.
@param       ParameterName   The parameter name of the custom primitive
@param       Value                   The new value of the custom primitive

### SetVectorParameterForDefaultCustomPrimitiveData
```angelscript
void SetVectorParameterForDefaultCustomPrimitiveData(FName ParameterName, FVector4 Value)
```
Set a vector parameter for default custom primitive data. This will be serialized and is useful in construction scripts.
@param       ParameterName   The parameter name of the custom primitive
@param       Value                   The new value of the custom primitive

### SetVisibleInRayTracing
```angelscript
void SetVisibleInRayTracing(bool bNewVisibleInRayTracing)
```
Changes the value of bIsVisibleInRayTracing.

### SetVisibleInSceneCaptureOnly
```angelscript
void SetVisibleInSceneCaptureOnly(bool bValue)
```
Sets bVisibleInSceneCaptureOnly property and marks the render state dirty.

### SetWalkableSlopeOverride
```angelscript
void SetWalkableSlopeOverride(FWalkableSlopeOverride NewOverride)
```
Sets a new slope override for this component instance.

### WakeAllRigidBodies
```angelscript
void WakeAllRigidBodies()
```
Ensure simulation is running for all bodies in this component.

### WakeRigidBody
```angelscript
void WakeRigidBody(FName BoneName)
```
'Wake' physics simulation for a single body.
@param  BoneName        If a SkeletalMeshComponent, name of body to wake. 'None' indicates root body.

### WasRecentlyRendered
```angelscript
bool WasRecentlyRendered(float32 Tolerance)
```
Returns true if this component has been rendered "recently", with a tolerance in seconds to define what "recent" means.
e.g.: If a tolerance of 0.1 is used, this function will return true only if the actor was rendered in the last 0.1 seconds of game time.

@param Tolerance  How many seconds ago the actor last render time can be and still count as having been "recently" rendered.
@return Whether this actor was recently rendered.

