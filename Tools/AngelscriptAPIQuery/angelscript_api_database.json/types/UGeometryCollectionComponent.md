# UGeometryCollectionComponent

**继承自**: `UMeshComponent`

GeometryCollectionComponent

## 属性

### ChaosSolverActor
- **类型**: `AChaosSolverActor`
- **描述**: Chaos RBD Solver override. Will use the world's default solver actor if null.

### InitializationFields
- **类型**: `TArray<TObjectPtr<AFieldSystemActor>>`

### ObjectType
- **类型**: `EObjectStateTypeEnum`

### GravityGroupIndex
- **类型**: `int`

### OneWayInteractionLevel
- **类型**: `int`

### bDensityFromPhysicsMaterial
- **类型**: `bool`

### bForceMotionBlur
- **类型**: `bool`

### EnableClustering
- **类型**: `bool`

### ClusterGroupIndex
- **类型**: `int`

### MaxClusterLevel
- **类型**: `int`

### MaxSimulatedLevel
- **类型**: `int`

### DamageModel
- **类型**: `EDamageModelTypeEnum`

### DamageThreshold
- **类型**: `TArray<float32>`

### bUseSizeSpecificDamageThreshold
- **类型**: `bool`

### bUseMaterialDamageModifiers
- **类型**: `bool`

### DamagePropagationData
- **类型**: `FGeometryCollectionDamagePropagationData`

### bAllowRemovalOnSleep
- **类型**: `bool`

### bAllowRemovalOnBreak
- **类型**: `bool`

### CollisionGroup
- **类型**: `int`

### CollisionSampleFraction
- **类型**: `float32`

### InitialVelocityType
- **类型**: `EInitialVelocityTypeEnum`

### InitialLinearVelocity
- **类型**: `FVector`

### InitialAngularVelocity
- **类型**: `FVector`

### NotifyGeometryCollectionPhysicsStateChange
- **类型**: `FNotifyGeometryCollectionPhysicsStateChange__GeometryCollectionComponent`

### NotifyGeometryCollectionPhysicsLoadingStateChange
- **类型**: `FNotifyGeometryCollectionPhysicsLoadingStateChange__GeometryCollectionComponent`

### OnChaosBreakEvent
- **类型**: `FOnChaosBreakEvent`

### OnChaosRemovalEvent
- **类型**: `FOnChaosRemovalEvent`

### OnChaosCrumblingEvent
- **类型**: `FOnChaosCrumblingEvent`

### DesiredCacheTime
- **类型**: `float32`

### CachePlayback
- **类型**: `bool`

### OnChaosPhysicsCollision
- **类型**: `FOnChaosPhysicsCollision`

### bNotifyBreaks
- **类型**: `bool`

### bNotifyCollisions
- **类型**: `bool`

### bNotifyTrailing
- **类型**: `bool`

### bNotifyRemovals
- **类型**: `bool`

### bNotifyCrumblings
- **类型**: `bool`

### bCrumblingEventIncludesChildren
- **类型**: `bool`

### bNotifyGlobalBreaks
- **类型**: `bool`

### bNotifyGlobalCollisions
- **类型**: `bool`

### bNotifyGlobalRemovals
- **类型**: `bool`

### bNotifyGlobalCrumblings
- **类型**: `bool`

### bGlobalCrumblingEventIncludesChildren
- **类型**: `bool`

### bStoreVelocities
- **类型**: `bool`

### bShowBoneColors
- **类型**: `bool`

### bUpdateComponentTransformToRootBone
- **类型**: `bool`

### bUseRootProxyForNavigation
- **类型**: `bool`

### bUpdateNavigationInTick
- **类型**: `bool`

### bEnableRunTimeDataCollection
- **类型**: `bool`

### RunTimeDataCollectionGuid
- **类型**: `FGuid`

### bOverrideCustomRenderer
- **类型**: `bool`

### CustomRendererType
- **类型**: `UClass`

### bEnableReplication
- **类型**: `bool`

### bEnableAbandonAfterLevel
- **类型**: `bool`

### ReplicationAbandonAfterLevel
- **类型**: `int`

### ReplicationMaxPositionAndVelocityCorrectionLevel
- **类型**: `int`

### bUseStaticMeshCollisionForTraces
- **类型**: `bool`

### bEnableDamageFromCollision
- **类型**: `bool`

### AbandonedCollisionProfileName
- **类型**: `FName`

### CollisionProfilePerLevel
- **类型**: `TArray<FName>`

### RestCollection
- **类型**: `const UGeometryCollection`

## 方法

### ApplyAngularVelocity
```angelscript
void ApplyAngularVelocity(int ItemIndex, FVector AngularVelocity)
```
Apply angular velocity on specific piece
@param ItemIndex item index ( from HitResult) of the piece to apply velocity on
@param AngularVelocity linear velocity to apply

### ApplyAssetDefaults
```angelscript
void ApplyAssetDefaults()
```
Apply default values from asset ( damage related data and physics material )

### ApplyBreakingAngularVelocity
```angelscript
void ApplyBreakingAngularVelocity(int ItemIndex, FVector AngularVelocity)
```
Apply linear velocity on breaking pieces for a specific cluster
If ItemIndex does not represent a cluster this will do nothing
@param ItemIndex item index ( from HitResult) of the cluster owning the breaking pieces to apply velocity on
@param AngularVelocity linear velocity to apply

### ApplyBreakingLinearVelocity
```angelscript
void ApplyBreakingLinearVelocity(int ItemIndex, FVector LinearVelocity)
```
Apply linear velocity on breaking pieces for a specific cluster
If ItemIndex does not represent a cluster this will do nothing
@param ItemIndex item index ( from HitResult) of the cluster owning the breaking pieces to apply velocity on
@param LinearVelocity linear velocity to apply

### ApplyExternalStrain
```angelscript
void ApplyExternalStrain(int ItemIndex, FVector Location, float32 Radius, int PropagationDepth, float32 PropagationFactor, float32 Strain)
```
Apply an external strain to specific piece of the geometry collection
@param ItemIndex item index ( from HitResult) of the piece to apply strain on
@param Location world location of where to apply the strain
@param Radius radius from the location point to apply the strain to ( using the center of mass of the pieces )
@param PropagationDepth How many level of connection to follow to propagate the strain through
@param PropagationFactor when using propagation, the factor to multiply the strain from one level to the other, allowing falloff effect
@param Strain strain / damage to apply

### ApplyInternalStrain
```angelscript
void ApplyInternalStrain(int ItemIndex, FVector Location, float32 Radius, int PropagationDepth, float32 PropagationFactor, float32 Strain)
```
Apply an internal strain to specific piece of the geometry collection
@param ItemIndex item index ( from HitResult) of the piece to apply strain on
@param Location world location of where to apply the strain
@param Radius radius from the location point to apply the strain to ( using the center of mass of the pieces )
@param PropagationDepth How many level of connection to follow to propagate the strain through
@param PropagationFactor when using propagation, the factor to multiply the strain from one level to the other, allowing falloff effect
@param Strain strain / damage to apply

### ApplyKinematicField
```angelscript
void ApplyKinematicField(float32 Radius, FVector Position)
```
SetDynamicState
  This function will dispatch a command to the physics thread to apply
  a kinematic to dynamic state change for the geo collection particles within the field.

      @param Radius Radial influence from the position
  @param Position The location of the command

### ApplyLinearVelocity
```angelscript
void ApplyLinearVelocity(int ItemIndex, FVector LinearVelocity)
```
Apply linear velocity on specific piece
@param ItemIndex item index ( from HitResult) of the piece to apply velocity on
@param LinearVelocity linear velocity to apply

### ApplyPhysicsField
```angelscript
void ApplyPhysicsField(bool Enabled, EGeometryCollectionPhysicsTypeEnum Target, UFieldSystemMetaData MetaData, UFieldNodeBase Field)
```
AddPhysicsField
  This function will dispatch a command to the physics thread to apply
  a generic evaluation of a user defined transient field network. See documentation,
  for examples of how to recreate variations of the above generic
  fields using field networks

      @param Enabled Is this force enabled for evaluation.
  @param Target Type of field supported by the solver.
  @param MetaData Meta data used to assist in evaluation
  @param Field Base evaluation node for the field network.

### CrumbleActiveClusters
```angelscript
void CrumbleActiveClusters()
```
Crumbe active clusters for this entire geometry collection
this will apply to internal and regular clusters

### CrumbleCluster
```angelscript
void CrumbleCluster(int ItemIndex)
```
Crumbe a cluster into all its pieces
@param ItemIndex item index ( from HitResult) of the cluster to crumble

### EnableRootProxyForCustomRenderer
```angelscript
void EnableRootProxyForCustomRenderer(bool bEnable)
```
Enable or disable root proxy for custom rendering - this can be set at runtime

### GetDebugInfo
```angelscript
FString GetDebugInfo()
```
RestCollection

### GetInitialLevel
```angelscript
int GetInitialLevel(int ItemIndex)
```
Get the initial level of a specific piece
Initial level means the level as it is in the unbroken state
@param ItemIndex item index ( from HitResult) of the cluster to get level from
@param Level of the piece ( 0 for root level and positive for the rest )

### GetInitialLocalRestTransforms
```angelscript
TArray<FTransform> GetInitialLocalRestTransforms()
```
Get the initial rest transforms in component (local) space  space,
they are the transforms as defined in the rest collection asset

### GetLocalBounds
```angelscript
FBox GetLocalBounds()
```
Get local bounds of the geometry collection

### GetMassAndExtents
```angelscript
void GetMassAndExtents(int ItemIndex, float32& OutMass, FBox& OutExtents)
```
Get mass and extent of a specific piece
@param ItemIndex item index ( from HitResult) of the cluster to get level from
@param Level of the piece ( 0 for root level and positive for the rest )

### GetRootCurrentTransform
```angelscript
FTransform GetRootCurrentTransform()
```
Get the root item current world transform

### GetRootIndex
```angelscript
int GetRootIndex()
```
Get the root item index of the hierarchy

### GetRootInitialTransform
```angelscript
FTransform GetRootInitialTransform()
```
Get the root item initial transform in world space

### IsRootBroken
```angelscript
bool IsRootBroken()
```
return true if the root cluster is not longer active at runtime

### PhysicsCollision
```angelscript
void PhysicsCollision(FChaosPhysicsCollisionInfo CollisionInfo)
```

### RemoveAllAnchors
```angelscript
void RemoveAllAnchors()
```
this will remove anchors on all the pieces ( including the static and kinematic initial states ones ) of the geometry colection

### SetAbandonedParticleCollisionProfileName
```angelscript
void SetAbandonedParticleCollisionProfileName(FName CollisionProfile)
```

### SetAnchoredByBox
```angelscript
void SetAnchoredByBox(FBox WorldSpaceBox, bool bAnchored, int MaxLevel)
```
Set all pieces within a world space bounding box to be anchored or not

### SetAnchoredByIndex
```angelscript
void SetAnchoredByIndex(int Index, bool bAnchored)
```
Set a piece or cluster to be anchored or not

### SetAnchoredByTransformedBox
```angelscript
void SetAnchoredByTransformedBox(FBox Box, FTransform Transform, bool bAnchored, int MaxLevel)
```
Set all pieces within a world transformed bounding box to be anchored or not

### SetEnableDamageFromCollision
```angelscript
void SetEnableDamageFromCollision(bool bValue)
```

### SetLocalRestTransforms
```angelscript
void SetLocalRestTransforms(TArray<FTransform> Transforms, bool bOnlyLeaves)
```
Set the local rest transform, this may be different from the rest collection
If the geometry collection is already simulating those matrices will be overriden by the physics state updates

### SetNotifyBreaks
```angelscript
void SetNotifyBreaks(bool bNewNotifyBreaks)
```
Changes whether or not this component will get future break notifications.

### SetNotifyCrumblings
```angelscript
void SetNotifyCrumblings(bool bNewNotifyCrumblings, bool bNewCrumblingEventIncludesChildren)
```
Changes whether or not this component will get future crumbling notifications.

### SetNotifyGlobalBreaks
```angelscript
void SetNotifyGlobalBreaks(bool bNewNotifyGlobalBreaks)
```
Changes whether or not this component will get future global break notifications.

### SetNotifyGlobalCollision
```angelscript
void SetNotifyGlobalCollision(bool bNewNotifyGlobalCollisions)
```
Changes whether or not this component will get future global collision notifications.

### SetNotifyGlobalCrumblings
```angelscript
void SetNotifyGlobalCrumblings(bool bNewNotifyGlobalCrumblings, bool bGlobalNewCrumblingEventIncludesChildren)
```
Changes whether or not this component will get future global crumbling notifications.

### SetNotifyGlobalRemovals
```angelscript
void SetNotifyGlobalRemovals(bool bNewNotifyGlobalRemovals)
```
Changes whether or not this component will get future global removal notifications.

### SetNotifyRemovals
```angelscript
void SetNotifyRemovals(bool bNewNotifyRemovals)
```
Changes whether or not this component will get future removal notifications.

### SetPerLevelCollisionProfileNames
```angelscript
void SetPerLevelCollisionProfileNames(TArray<FName> ProfileNames)
```

### SetPerParticleCollisionProfileName
```angelscript
void SetPerParticleCollisionProfileName(TArray<int> BoneIds, FName ProfileName)
```

### SetRestCollection
```angelscript
void SetRestCollection(const UGeometryCollection RestCollectionIn, bool bApplyAssetDefaults)
```
RestCollection

