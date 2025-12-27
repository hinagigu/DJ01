# USkeletalMeshComponent

**继承自**: `USkinnedMeshComponent`

SkeletalMeshComponent is used to create an instance of an animated SkeletalMesh asset.

@see https://docs.unrealengine.com/latest/INT/Engine/Content/Types/SkeletalMeshes/
@see USkeletalMesh

## 属性

### AnimBlueprintGeneratedClass
- **类型**: `UAnimBlueprintGeneratedClass`

### AnimationData
- **类型**: `FSingleAnimationPlayData`

### GlobalAnimRateScale
- **类型**: `float32`

### KinematicBonesUpdateType
- **类型**: `EKinematicBonesUpdateToPhysics`

### PhysicsTransformUpdateMode
- **类型**: `EPhysicsTransformUpdateMode`

### ClothVelocityScale
- **类型**: `float32`

### ClothBlendWeight
- **类型**: `float32`

### bWaitForParallelClothTask
- **类型**: `bool`

### OnConstraintBroken
- **类型**: `FConstraintBrokenSignature`

### OnPlasticDeformation
- **类型**: `FPlasticDeformationEventSignature`

### ClothingSimulationFactory
- **类型**: `TSubclassOf<UClothingSimulationFactory>`
- **描述**: Class of the object responsible for

### OnAnimInitialized
- **类型**: `FOnAnimInitialized`

### bDisablePostProcessBlueprint
- **类型**: `bool`

### AnimClass
- **类型**: `TSubclassOf<UAnimInstance>`

### bUpdateOverlapsOnAnimationFinalize
- **类型**: `bool`

### bEnablePhysicsOnDedicatedServer
- **类型**: `bool`

### bUpdateMeshWhenKinematic
- **类型**: `bool`

### bUpdateJointsFromAnimation
- **类型**: `bool`

### bAllowClothActors
- **类型**: `bool`

### bDisableClothSimulation
- **类型**: `bool`

### bDisableRigidBodyAnimNode
- **类型**: `bool`

### bAllowAnimCurveEvaluation
- **类型**: `bool`

### bCollideWithEnvironment
- **类型**: `bool`

### bCollideWithAttachedChildren
- **类型**: `bool`

### bForceCollisionUpdate
- **类型**: `bool`

### bResetAfterTeleport
- **类型**: `bool`

### bDeferKinematicBoneUpdate
- **类型**: `bool`

### bNoSkeletonUpdate
- **类型**: `bool`

### bPauseAnims
- **类型**: `bool`

### bUseRefPoseOnInitAnim
- **类型**: `bool`

### bEnablePerPolyCollision
- **类型**: `bool`

### bIncludeComponentLocationIntoBounds
- **类型**: `bool`

### bPropagateCurvesToFollowers
- **类型**: `bool`

### bSkipKinematicUpdateWhenInterpolating
- **类型**: `bool`

### bSkipBoundsUpdateWhenInterpolating
- **类型**: `bool`

### bUpdateAnimationInEditor
- **类型**: `bool`

### bUpdateClothInEditor
- **类型**: `bool`

### bOverrideDefaultAnimatingRig
- **类型**: `bool`

## 方法

### GetLinkedAnimInstances
```angelscript
TArray<UAnimInstance> GetLinkedAnimInstances()
```

### AccumulateAllBodiesBelowPhysicsBlendWeight
```angelscript
void AccumulateAllBodiesBelowPhysicsBlendWeight(FName InBoneName, float32 AddPhysicsBlendWeight, bool bSkipCustomPhysicsType)
```
Accumulate AddPhysicsBlendWeight to physics blendweight for all of the bones below passed in bone to be simulated

### AddForceToAllBodiesBelow
```angelscript
void AddForceToAllBodiesBelow(FVector Force, FName BoneName, bool bAccelChange, bool bIncludeSelf)
```
Add a force to all rigid bodies below.
This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

@param  Force            Force vector to apply. Magnitude indicates strength of force.
@param  BoneName         If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body.
@param  bAccelChange If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no effect).
@param  bIncludeSelf If false, Force is only applied to bodies below but not given bone name.

### AddImpulseToAllBodiesBelow
```angelscript
void AddImpulseToAllBodiesBelow(FVector Impulse, FName BoneName, bool bVelChange, bool bIncludeSelf)
```
Add impulse to all single rigid bodies below. Good for one time instant burst.

@param  Impulse         Magnitude and direction of impulse to apply.
@param  BoneName        If a SkeletalMeshComponent, name of body to apply impulse to. 'None' indicates root body.
@param  bVelChange      If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no effect).
@param bIncludeSelf If false, Force is only applied to bodies below but not given bone name.

### AllowAnimCurveEvaluation
```angelscript
void AllowAnimCurveEvaluation(FName NameOfCurve, bool bAllow)
```

### BindClothToLeaderPoseComponent
```angelscript
void BindClothToLeaderPoseComponent()
```
If this component has a valid LeaderPoseComponent then this function makes cloth items on the follower component
take the transforms of the cloth items on the leader component instead of simulating separately.
@Note This will FORCE any cloth actor on the leader component to simulate in local space. Also
The meshes used in the components must be identical for the cloth to bind correctly

### BreakConstraint
```angelscript
void BreakConstraint(FVector Impulse, FVector HitLocation, FName InBoneName)
```
Break a constraint off a Gore mesh.

@param       Impulse vector of impulse
@param       HitLocation     location of the hit
@param       InBoneName      Name of bone to break constraint for

### ClearMorphTargets
```angelscript
void ClearMorphTargets()
```
Clear all Morph Target that are set to this mesh

### FindConstraintBoneName
```angelscript
FName FindConstraintBoneName(int ConstraintIndex)
```
Find Constraint Name from index

@param       ConstraintIndex Index of constraint to look for
@return      Constraint Joint Name

### ForceClothNextUpdateTeleport
```angelscript
void ForceClothNextUpdateTeleport()
```
Used to indicate we should force 'teleport' during the next call to UpdateClothState,
This will transform positions and velocities and thus keep the simulation state, just translate it to a new pose.

### ForceClothNextUpdateTeleportAndReset
```angelscript
void ForceClothNextUpdateTeleportAndReset()
```
Used to indicate we should force 'teleport and reset' during the next call to UpdateClothState.
This can be used to reset it from a bad state or by a teleport where the old state is not important anymore.

### GetAllowClothActors
```angelscript
bool GetAllowClothActors()
```

### GetAllowedAnimCurveEvaluate
```angelscript
bool GetAllowedAnimCurveEvaluate()
```

### GetAllowRigidBodyAnimNode
```angelscript
bool GetAllowRigidBodyAnimNode()
```

### GetAnimationMode
```angelscript
EAnimationMode GetAnimationMode()
```

### GetAnimInstance
```angelscript
UAnimInstance GetAnimInstance()
```
Returns the animation instance that is driving the class (if available). This is typically an instance of
the class set as AnimBlueprintGeneratedClass (generated by an animation blueprint)
Since this instance is transient, it is not safe to be used during construction script

### GetBoneLinearVelocity
```angelscript
FVector GetBoneLinearVelocity(FName InBoneName)
```

### GetBoneMass
```angelscript
float32 GetBoneMass(FName BoneName, bool bScaleMass)
```
Returns the mass (in kg) of the given bone

@param BoneName         Name of the body to return. 'None' indicates root body.
@param bScaleMass       If true, the mass is scaled by the bone's MassScale.

### GetClothingSimulationInteractor
```angelscript
UClothingSimulationInteractor GetClothingSimulationInteractor()
```
Get the current interactor for a clothing simulation, if the current simulation supports runtime interaction.

### GetClothMaxDistanceScale
```angelscript
float32 GetClothMaxDistanceScale()
```
Get/Set the max distance scale of clothing mesh vertices

### GetConstraintByName
```angelscript
FConstraintInstanceAccessor GetConstraintByName(FName ConstraintName, bool bIncludesTerminated)
```
Gets a constraint by its name
@param ConstraintName         name of the constraint
@param IncludesTerminated whether or not to return a terminated constraint

### GetConstraints
```angelscript
void GetConstraints(bool bIncludesTerminated, TArray<FConstraintInstanceAccessor>& OutConstraints)
```
Gets all the constraints
@param IncludesTerminated whether or not to return terminated constraints
@param OutConstraints returned list of constraints matching the parameters

### GetConstraintsFromBody
```angelscript
void GetConstraintsFromBody(FName BodyName, bool bParentConstraints, bool bChildConstraints, bool bIncludesTerminated, TArray<FConstraintInstanceAccessor>& OutConstraints)
```
Gets all the constraints attached to a body
@param BodyName name of the body to get the attached constraints from
@param bParentConstraints return constraints where BodyName is the child of the constraint
@param bChildConstraints return constraints where BodyName is the parent of the constraint
@param bParentConstraints return constraints attached to the parent of the body
@param IncludesTerminated whether or not to return terminated constraints
@param OutConstraints returned list of constraints matching the parameters

### GetCurrentJointAngles
```angelscript
void GetCurrentJointAngles(FName InBoneName, float32& Swing1Angle, float32& TwistAngle, float32& Swing2Angle)
```
Gets the current Angular state for a named bone constraint
@param InBoneName  Name of bone to get constraint ranges for
@param Swing1Angle current angular state of the constraint
@param TwistAngle  current angular state of the constraint
@param Swing2Angle current angular state of the constraint

### GetDefaultAnimatingRig
```angelscript
TSoftObjectPtr<UObject> GetDefaultAnimatingRig()
```

### GetDefaultAnimatingRigOverride
```angelscript
TSoftObjectPtr<UObject> GetDefaultAnimatingRigOverride()
```

### GetDisableAnimCurves
```angelscript
bool GetDisableAnimCurves()
```

### GetDisablePostProcessBlueprint
```angelscript
bool GetDisablePostProcessBlueprint()
```
Gets whether the post process blueprint is currently disabled for this component

### GetFloatAttribute
```angelscript
bool GetFloatAttribute(FName BoneName, FName AttributeName, float32 DefaultValue, float32& OutValue, ECustomBoneAttributeLookup LookupType)
```
Get float type attribute value.

@param BoneName Name of the bone to retrieve try and retrieve the attribute from
@param AttributeName Name of the attribute to retrieve
@param DefaultValue In case the attribute could not be found
@param OutValue Retrieved attribute value if found, otherwise is set to DefaultValue
@param LookupType Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)
@return Whether or not the atttribute was successfully retrieved

### GetFloatAttribute_Ref
```angelscript
bool GetFloatAttribute_Ref(FName BoneName, FName AttributeName, float32& OutValue, ECustomBoneAttributeLookup LookupType)
```
Get float type attribute value.

@param BoneName Name of the bone to retrieve try and retrieve the attribute from
@param AttributeName Name of the attribute to retrieve
@param OutValue (reference) Retrieved attribute value if found, otherwise is set to DefaultValue
@param LookupType Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)
@return Whether or not the atttribute was successfully retrieved

### GetIntegerAttribute
```angelscript
bool GetIntegerAttribute(FName BoneName, FName AttributeName, int DefaultValue, int& OutValue, ECustomBoneAttributeLookup LookupType)
```
Get integer type attribute value.

@param BoneName Name of the bone to retrieve try and retrieve the attribute from
@param AttributeName Name of the attribute to retrieve
@param DefaultValue In case the attribute could not be found
@param OutValue Retrieved attribute value if found, otherwise is set to DefaultValue
@param LookupType Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)
@return Whether or not the atttribute was successfully retrieved

### GetIntegerAttribute_Ref
```angelscript
bool GetIntegerAttribute_Ref(FName BoneName, FName AttributeName, int& OutValue, ECustomBoneAttributeLookup LookupType)
```
Get integer type attribute value.

@param BoneName Name of the bone to retrieve try and retrieve the attribute from
@param AttributeName Name of the attribute to retrieve
@param OutValue (reference) Retrieved attribute value if found, otherwise is set to DefaultValue
@param LookupType Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)
@return Whether or not the atttribute was successfully retrieved

### GetLinkedAnimGraphInstanceByTag
```angelscript
UAnimInstance GetLinkedAnimGraphInstanceByTag(FName InTag)
```
Returns the a tagged linked instance node. If no linked instances are found or none are tagged with the
supplied name, this will return NULL.

### GetLinkedAnimLayerInstanceByClass
```angelscript
UAnimInstance GetLinkedAnimLayerInstanceByClass(TSubclassOf<UAnimInstance> InClass)
```
Gets the first layer linked instance corresponding to the specified class

### GetLinkedAnimLayerInstanceByGroup
```angelscript
UAnimInstance GetLinkedAnimLayerInstanceByGroup(FName InGroup)
```
Gets the layer linked instance corresponding to the specified group

### GetMorphTarget
```angelscript
float32 GetMorphTarget(FName MorphTargetName)
```
Get Morph target with given name

### GetPlayRate
```angelscript
float32 GetPlayRate()
```
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

### GetPosition
```angelscript
float32 GetPosition()
```
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

### GetPostProcessInstance
```angelscript
UAnimInstance GetPostProcessInstance()
```
Returns the active post process instance is one is available. This is set on the mesh that this
component is using, and is evaluated immediately after the main instance.

### GetSkeletalCenterOfMass
```angelscript
FVector GetSkeletalCenterOfMass()
```
Returns the center of mass of the skeletal mesh, instead of the root body's location

### GetSkeletalMeshAsset
```angelscript
USkeletalMesh GetSkeletalMeshAsset()
```
Get the SkeletalMesh rendered for this mesh.

### GetStringAttribute
```angelscript
bool GetStringAttribute(FName BoneName, FName AttributeName, FString DefaultValue, FString& OutValue, ECustomBoneAttributeLookup LookupType)
```
Get string type attribute value.

@param BoneName Name of the bone to retrieve try and retrieve the attribute from
@param AttributeName Name of the attribute to retrieve
@param DefaultValue In case the attribute could not be found
@param OutValue Retrieved attribute value if found, otherwise is set to DefaultValue
@param LookupType Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)
@return Whether or not the atttribute was successfully retrieved

### GetStringAttribute_Ref
```angelscript
bool GetStringAttribute_Ref(FName BoneName, FName AttributeName, FString& OutValue, ECustomBoneAttributeLookup LookupType)
```
Get string type attribute value.

@param BoneName Name of the bone to retrieve try and retrieve the attribute from
@param AttributeName Name of the attribute to retrieve
@param OutValue (reference) Retrieved attribute value if found, otherwise is set to DefaultValue
@param LookupType Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)
@return Whether or not the atttribute was successfully retrieved

### GetTeleportDistanceThreshold
```angelscript
float32 GetTeleportDistanceThreshold()
```
Gets the teleportation distance threshold.

@return Threshold value.

### GetTeleportRotationThreshold
```angelscript
float32 GetTeleportRotationThreshold()
```
Gets the teleportation rotation threshold.

@return Threshold in degrees.

### GetTransformAttribute
```angelscript
bool GetTransformAttribute(FName BoneName, FName AttributeName, FTransform DefaultValue, FTransform& OutValue, ECustomBoneAttributeLookup LookupType)
```
Get FTransform type attribute value.

@param BoneName Name of the bone to retrieve try and retrieve the attribute from
@param AttributeName Name of the attribute to retrieve
@param OutValue (reference) Retrieved attribute value if found, otherwise is set to DefaultValue
@param LookupType Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)
@return Whether or not the atttribute was successfully retrieved

### GetTransformAttribute_Ref
```angelscript
bool GetTransformAttribute_Ref(FName BoneName, FName AttributeName, FTransform& OutValue, ECustomBoneAttributeLookup LookupType)
```
Get FTransform type attribute value.

@param BoneName Name of the bone to retrieve try and retrieve the attribute from
@param AttributeName Name of the attribute to retrieve
@param OutValue (reference) Retrieved attribute value if found, otherwise is set to DefaultValue
@param LookupType Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)
@return Whether or not the atttribute was successfully retrieved

### HasValidAnimationInstance
```angelscript
bool HasValidAnimationInstance()
```
Returns whether there are any valid instances to run, currently this means whether we have
have an animation instance or a post process instance available to process.

### IsBodyGravityEnabled
```angelscript
bool IsBodyGravityEnabled(FName BoneName)
```
Checks whether or not gravity is enabled on the given bone.
NAME_None indicates the root body should be queried.
If the bone name given is otherwise invalid, false is returned.

@param BoneName The name of the bone to check.
@return True if gravity is enabled on the bone.

### IsClothingSimulationSuspended
```angelscript
bool IsClothingSimulationSuspended()
```
Gets whether or not the clothing simulation is currently suspended

### IsPlaying
```angelscript
bool IsPlaying()
```
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

### GetClosestPointOnPhysicsAsset
```angelscript
bool GetClosestPointOnPhysicsAsset(FVector WorldPosition, FVector& ClosestWorldPosition, FVector& Normal, FName& BoneName, float32& Distance)
```
Given a world position, find the closest point on the physics asset. Note that this is independent of collision and welding. This is based purely on animation position
@param      WorldPosition                           The point we want the closest point to (i.e. for all bodies in the physics asset, find the one that has a point closest to WorldPosition)
@param      ClosestPointOnPhysicsAsset      The data associated with the closest point (position, normal, etc...)
@return     true if we found a closest point

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
Runs through all nodes, attempting to find linked instance by name/tag, then sets the class of each node if the tag matches

### OverrideAnimationData
```angelscript
void OverrideAnimationData(UAnimationAsset InAnimToPlay, bool bIsLooping, bool bIsPlaying, float32 Position, float32 PlayRate)
```
This overrides current AnimationData parameter in the SkeletalMeshComponent. This will serialize when the component serialize
so it can be used during construction script. However note that this will override current existing data
This can be useful if you'd like to make a blueprint with custom default animation per component
This sets single player mode, which means you can't use AnimBlueprint with it

### Play
```angelscript
void Play(bool bLooping)
```
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

### PlayAnimation
```angelscript
void PlayAnimation(UAnimationAsset NewAnimToPlay, bool bLooping)
```
Animation play functions
       *
       * These changes status of animation instance, which is transient data, which means it won't serialize with this component
       * Because of that reason, it is not safe to be used during construction script
       * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

### ResetAllBodiesSimulatePhysics
```angelscript
void ResetAllBodiesSimulatePhysics()
```
Allows you to reset bodies Simulate state based on where bUsePhysics is set to true in the BodySetup.

### ResetAllowedAnimCurveEvaluation
```angelscript
void ResetAllowedAnimCurveEvaluation()
```
By reset, it will allow all the curves to be evaluated

### ResetAnimInstanceDynamics
```angelscript
void ResetAnimInstanceDynamics(ETeleportType InTeleportType)
```
Informs any active anim instances (main instance, linked instances, post instance) that a dynamics reset is required
for example if a teleport occurs.

### ResetClothTeleportMode
```angelscript
void ResetClothTeleportMode()
```
Reset the teleport mode of a next update to 'Continuous'

### ResumeClothingSimulation
```angelscript
void ResumeClothingSimulation()
```
Resumes a previously suspended clothing simulation, teleporting the clothing on the next tick

### SetAllBodiesBelowLinearVelocity
```angelscript
void SetAllBodiesBelowLinearVelocity(FName InBoneName, FVector LinearVelocity, bool bIncludeSelf)
```
set the linear velocity of the child bodies to match that of the given parent bone

### SetAllBodiesBelowPhysicsBlendWeight
```angelscript
void SetAllBodiesBelowPhysicsBlendWeight(FName InBoneName, float32 PhysicsBlendWeight, bool bSkipCustomPhysicsType, bool bIncludeSelf)
```
Set all of the bones below passed in bone to be simulated

### SetAllBodiesBelowPhysicsDisabled
```angelscript
void SetAllBodiesBelowPhysicsDisabled(FName InBoneName, bool bDisabled, bool bIncludeSelf)
```
[WARNING: Chaos Only]
Set all of the bones below passed in bone to be disabled or not for the associated physics solver
Bodies will not be colliding or be part of the physics simulation.
This is different from SetAllBodiesBelowSimulatePhysics that changes bodies to Kinematic/simulated

### SetAllBodiesBelowSimulatePhysics
```angelscript
void SetAllBodiesBelowSimulatePhysics(FName InBoneName, bool bNewSimulate, bool bIncludeSelf)
```
Set all of the bones below passed in bone to be simulated

### SetAllBodiesPhysicsBlendWeight
```angelscript
void SetAllBodiesPhysicsBlendWeight(float32 PhysicsBlendWeight, bool bSkipCustomPhysicsType)
```

### SetAllBodiesSimulatePhysics
```angelscript
void SetAllBodiesSimulatePhysics(bool bNewSimulate)
```
Set bSimulatePhysics to true for all bone bodies. Does not change the component bSimulatePhysics flag.

### SetAllMotorsAngularDriveParams
```angelscript
void SetAllMotorsAngularDriveParams(float32 InSpring, float32 InDamping, float32 InForceLimit, bool bSkipCustomPhysicsType)
```
Set Angular Drive motors params for all constraint instances

### SetAllMotorsAngularPositionDrive
```angelscript
void SetAllMotorsAngularPositionDrive(bool bEnableSwingDrive, bool bEnableTwistDrive, bool bSkipCustomPhysicsType)
```
Enable or Disable AngularPositionDrive. If motor is in SLERP mode it will be turned on if either EnableSwingDrive OR EnableTwistDrive are enabled. In Twist and Swing mode the twist and the swing can be controlled individually.

### SetAllMotorsAngularVelocityDrive
```angelscript
void SetAllMotorsAngularVelocityDrive(bool bEnableSwingDrive, bool bEnableTwistDrive, bool bSkipCustomPhysicsType)
```
Enable or Disable AngularVelocityDrive. If motor is in SLERP mode it will be turned on if either EnableSwingDrive OR EnableTwistDrive are enabled. In Twist and Swing mode the twist and the swing can be controlled individually.

### SetAllowAnimCurveEvaluation
```angelscript
void SetAllowAnimCurveEvaluation(bool bInAllow)
```

### SetAllowClothActors
```angelscript
void SetAllowClothActors(bool bInAllow)
```
Sets whether cloth assets should be created/simulated in this component.
This will update the conditional flag and you will want to call RecreateClothingActors for it to take effect.
@param bInAllow Whether to allow the creation of cloth assets and simulation.

### SetAllowedAnimCurvesEvaluation
```angelscript
void SetAllowedAnimCurvesEvaluation(TArray<FName> List, bool bAllow)
```
resets, and then only allow the following list to be allowed/disallowed

### SetAllowRigidBodyAnimNode
```angelscript
void SetAllowRigidBodyAnimNode(bool bInAllow, bool bReinitAnim)
```
Sets whether or not to allow rigid body animation nodes for this component

### SetAngularLimits
```angelscript
void SetAngularLimits(FName InBoneName, float32 Swing1LimitAngle, float32 TwistLimitAngle, float32 Swing2LimitAngle)
```
Sets the Angular Motion Ranges for a named constraint
@param InBoneName  Name of bone to adjust constraint ranges for
@param Swing1LimitAngle       Size of limit in degrees, 0 means locked, 180 means free
@param TwistLimitAngle        Size of limit in degrees, 0 means locked, 180 means free
@param Swing2LimitAngle       Size of limit in degrees, 0 means locked, 180 means free

### SetAnimation
```angelscript
void SetAnimation(UAnimationAsset NewAnimToPlay)
```
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

### SetAnimationMode
```angelscript
void SetAnimationMode(EAnimationMode InAnimationMode, bool bForceInitAnimScriptInstance)
```
Set the Animation Mode
@param InAnimationMode : Requested AnimationMode
@param bForceInitAnimScriptInstance : Init AnimScriptInstance if the AnimationMode is AnimationBlueprint even if the new animation mode is the same as current (this allows to use BP construction script to do this)

### SetAnimClass
```angelscript
void SetAnimClass(UClass NewClass)
```
Set the anim instance class. Clears and re-initializes the anim instance with the new class and sets animation mode to 'AnimationBlueprint'

### SetBodyNotifyRigidBodyCollision
```angelscript
void SetBodyNotifyRigidBodyCollision(bool bNewNotifyRigidBodyCollision, FName BoneName)
```
Changes the value of bNotifyRigidBodyCollision for a given body
@param bNewNotifyRigidBodyCollision   The value to assign to bNotifyRigidBodyCollision
@param BoneName                                               Name of the body to turn hit notifies on/off. None implies root body

### SetBodySimulatePhysics
```angelscript
void SetBodySimulatePhysics(FName InBoneName, bool bSimulate)
```
Set a single bone to be simulated (or not)

### SetClothMaxDistanceScale
```angelscript
void SetClothMaxDistanceScale(float32 Scale)
```

### SetConstraintProfile
```angelscript
void SetConstraintProfile(FName JointName, FName ProfileName, bool bDefaultIfNotFound)
```
Sets the constraint profile properties (limits, motors, etc...) to match the constraint profile as defined in the physics asset. If profile name is not found the joint is set to use the default constraint profile.

### SetConstraintProfileForAll
```angelscript
void SetConstraintProfileForAll(FName ProfileName, bool bDefaultIfNotFound)
```
Sets the constraint profile properties (limits, motors, etc...) to match the constraint profile as defined in the physics asset for all constraints. If profile name is not found the joint is set to use the default constraint profile.

### SetDefaultAnimatingRigOverride
```angelscript
void SetDefaultAnimatingRigOverride(TSoftObjectPtr<UObject> InAnimatingRig)
```

### SetDisableAnimCurves
```angelscript
void SetDisableAnimCurves(bool bInDisableAnimCurves)
```

### SetDisablePostProcessBlueprint
```angelscript
void SetDisablePostProcessBlueprint(bool bInDisablePostProcess)
```
Sets whether the post process blueprint is currently running for this component.
If it is not currently running, and is set to run, the instance will be reinitialized

### SetEnableBodyGravity
```angelscript
void SetEnableBodyGravity(bool bEnableGravity, FName BoneName)
```
Enables or disables gravity for the given bone.
NAME_None indicates the root body will be edited.
If the bone name given is otherwise invalid, nothing happens.

@param bEnableGravity   Whether gravity should be enabled or disabled.
@param BoneName                 The name of the bone to modify.

### SetEnableGravityOnAllBodiesBelow
```angelscript
void SetEnableGravityOnAllBodiesBelow(bool bEnableGravity, FName BoneName, bool bIncludeSelf)
```
Enables or disables gravity to all bodies below the given bone.
NAME_None indicates all bodies will be edited.
In that case, consider using UPrimitiveComponent::EnableGravity.

@param bEnableGravity   Whether gravity should be enabled or disabled.
@param BoneName                 The name of the top most bone.
@param bIncludeSelf             Whether the bone specified should be edited.

### SetEnablePhysicsBlending
```angelscript
void SetEnablePhysicsBlending(bool bNewBlendPhysics)
```
Disable physics blending of bones *

### SetMorphTarget
```angelscript
void SetMorphTarget(FName MorphTargetName, float32 Value, bool bRemoveZeroWeight)
```
Set Morph Target with Name and Value(0-1)

@param bRemoveZeroWeight : Used by editor code when it should stay in the active list with zero weight

### SetNotifyRigidBodyCollisionBelow
```angelscript
void SetNotifyRigidBodyCollisionBelow(bool bNewNotifyRigidBodyCollision, FName BoneName, bool bIncludeSelf)
```
Changes the value of bNotifyRigidBodyCollision on all bodies below a given bone
@param bNewNotifyRigidBodyCollision   The value to assign to bNotifyRigidBodyCollision
@param BoneName                                               Name of the body to turn hit notifies on (and below)
@param bIncludeSelf                                   Whether to modify the given body (useful for roots with multiple children)

### SetPhysicsBlendWeight
```angelscript
void SetPhysicsBlendWeight(float32 PhysicsBlendWeight)
```
This is global set up for setting physics blend weight
This does multiple things automatically
If PhysicsBlendWeight == 1.f, it will enable Simulation, and if PhysicsBlendWeight == 0.f, it will disable Simulation.
Also it will respect each body's setup, so if the body is fixed, it won't simulate. Vice versa
So if you'd like all bodies to change manually, do not use this function, but SetAllBodiesPhysicsBlendWeight

### SetPlayRate
```angelscript
void SetPlayRate(float32 Rate)
```
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

### SetPosition
```angelscript
void SetPosition(float32 InPos, bool bFireNotifies)
```
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

### SetSkeletalMeshAsset
```angelscript
void SetSkeletalMeshAsset(USkeletalMesh NewMesh)
```
Set the SkeletalMesh rendered for this mesh.

### SetTeleportDistanceThreshold
```angelscript
void SetTeleportDistanceThreshold(float32 Threshold)
```
Sets the teleportation distance threshold.

@param threshold Threshold value.

### SetTeleportRotationThreshold
```angelscript
void SetTeleportRotationThreshold(float32 Threshold)
```
Sets the teleportation rotation threshold.

@param threshold Threshold in degrees.

### SetUpdateAnimationInEditor
```angelscript
void SetUpdateAnimationInEditor(bool NewUpdateState)
```
Sets whether or not to force tick component in order to update animation and refresh transform for this component
This is supported only in the editor

### SetUpdateClothInEditor
```angelscript
void SetUpdateClothInEditor(bool NewUpdateState)
```
Sets whether or not to animate cloth in the editor. Requires Update Animation In Editor to also be true.
This is supported only in the editor

### SnapshotPose
```angelscript
void SnapshotPose(FPoseSnapshot& Snapshot)
```
Takes a snapshot of this skeletal mesh component's pose and saves it to the specified snapshot.
The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1
and then used it at LOD0 any bones not in LOD1 will use the reference pose

### Stop
```angelscript
void Stop()
```
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

### SuspendClothingSimulation
```angelscript
void SuspendClothingSimulation()
```
Stops simulating clothing, but does not show clothing ref pose. Keeps the last known simulation state

### TermBodiesBelow
```angelscript
void TermBodiesBelow(FName ParentBoneName)
```
Terminate physics on all bodies below the named bone, effectively disabling collision forever. If you terminate, you won't be able to re-init later.

### ToggleDisablePostProcessBlueprint
```angelscript
void ToggleDisablePostProcessBlueprint()
```
Toggles whether the post process blueprint will run for this component

### UnbindClothFromLeaderPoseComponent
```angelscript
void UnbindClothFromLeaderPoseComponent(bool bRestoreSimulationSpace)
```
If this component has a valid LeaderPoseComponent and has previously had its cloth bound to the
MCP, this function will unbind the cloth and resume simulation.
@param bRestoreSimulationSpace if true and the leader pose cloth was originally simulating in world
space, we will restore this setting. This will cause the leader component to reset which may be
undesirable.

### UnlinkAnimClassLayers
```angelscript
void UnlinkAnimClassLayers(TSubclassOf<UAnimInstance> InClass)
```
Runs through all layer nodes, attempting to find layer nodes that are currently running the specified class, then resets each to its default value.
State sharing rules are as with SetLayerOverlay.
If InClass is null, does nothing.

