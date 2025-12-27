# FAnimNode_RigidBody

Controller that simulates physics based on the physics asset of the skeletal mesh component

## 属性

### OverridePhysicsAsset
- **类型**: `UPhysicsAsset`
- **描述**: Physics asset to use. If empty use the skeletal mesh's default physics asset in case Default To Skeletal Mesh Physics Asset is set to True.

### bDefaultToSkeletalMeshPhysicsAsset
- **类型**: `bool`
- **描述**: Use the skeletal mesh physics asset as default in case set to True. The Override Physics Asset will always have priority over this.

### bUseLocalLODThresholdOnly
- **类型**: `bool`

### OverrideWorldGravity
- **类型**: `FVector`
- **描述**: Override gravity

### ExternalForce
- **类型**: `FVector`
- **描述**: Applies a uniform external force in world space. This allows for easily faking inertia of movement while still simulating in component space for example

### ComponentLinearAccScale
- **类型**: `FVector`
- **描述**: When using non-world-space sim, this controls how much of the components world-space acceleration is passed on to the local-space simulation.

### ComponentLinearVelScale
- **类型**: `FVector`
- **描述**: When using non-world-space sim, this applies a 'drag' to the bodies in the local space simulation, based on the components world-space velocity.

### ComponentAppliedLinearAccClamp
- **类型**: `FVector`
- **描述**: When using non-world-space sim, this is an overall clamp on acceleration derived from ComponentLinearAccScale and ComponentLinearVelScale, to ensure it is not too large.

### SimSpaceSettings
- **类型**: `FSimSpaceSettings`
- **描述**: Settings for the system which passes motion of the simulation's space
into the simulation. This allows the simulation to pass a
fraction of the world space motion onto the bodies which allows Bone-Space
and Component-Space simulations to react to world-space movement in a
controllable way.
This system is a superset of the functionality provided by ComponentLinearAccScale,
ComponentLinearVelScale, and ComponentAppliedLinearAccClamp. In general
you should not have both systems enabled.

### CachedBoundsScale
- **类型**: `float32`
- **描述**: Scale of cached bounds (vs. actual bounds).
Increasing this may improve performance, but overlaps may not work as well.
(A value of 1.0 effectively disables cached bounds).

### BaseBoneRef
- **类型**: `FBoneReference`
- **描述**: Matters if SimulationSpace is BaseBone

### OverlapChannel
- **类型**: `ECollisionChannel`
- **描述**: The channel we use to find static geometry to collide with

### SimulationSpace
- **类型**: `ESimulationSpace`
- **描述**: What space to simulate the bodies in. This affects how velocities are generated

### bForceDisableCollisionBetweenConstraintBodies
- **类型**: `bool`
- **描述**: Whether to allow collisions between two bodies joined by a constraint

### bUseExternalClothCollision
- **类型**: `bool`
- **描述**: If true, kinematic objects will be added to the simulation at runtime to represent any cloth colliders defined for the parent object.

### WorldSpaceMinimumScale
- **类型**: `float32`
- **描述**: For world-space simulations, if the magnitude of the component's 3D scale is less than WorldSpaceMinimumScale, do not update the node.

### EvaluationResetTime
- **类型**: `float32`
- **描述**: If the node is not evaluated for this amount of time (seconds), either because a lower LOD was in use for a while or the component was
not visible, reset the simulation to the default pose on the next evaluation. Set to 0 to disable time-based reset.

### SimulationTiming
- **类型**: `ESimulationTiming`
- **描述**: Whether the physics simulation runs synchronously with the node's evaluation or is run in the background until the next frame.

### ComponentPose
- **类型**: `FComponentSpacePoseLink`

### LODThreshold
- **类型**: `int`

### AlphaInputType
- **类型**: `EAnimAlphaInputType`

### bAlphaBoolEnabled
- **类型**: `bool`

### Alpha
- **类型**: `float32`

### AlphaScaleBias
- **类型**: `FInputScaleBias`

### AlphaBoolBlend
- **类型**: `FInputAlphaBoolBlend`

### AlphaCurveName
- **类型**: `FName`

### AlphaScaleBiasClamp
- **类型**: `FInputScaleBiasClamp`

### bEnableWorldGeometry
- **类型**: `bool`

### bOverrideWorldGravity
- **类型**: `bool`

### bTransferBoneVelocities
- **类型**: `bool`

### bFreezeIncomingPoseOnStart
- **类型**: `bool`

### bClampLinearTranslationLimitToRefPose
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FAnimNode_RigidBody& opAssign(FAnimNode_RigidBody Other)
```

