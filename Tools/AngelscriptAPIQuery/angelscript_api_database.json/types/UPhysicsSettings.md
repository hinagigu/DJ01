# UPhysicsSettings

**继承自**: `UPhysicsSettingsCore`

Default physics settings.

## 属性

### PhysicsPrediction
- **类型**: `FPhysicsPredictionSettings`
- **描述**: Settings for Networked Physics Prediction, experimental.

### PhysicErrorCorrection
- **类型**: `FRigidBodyErrorCorrection`
- **描述**: Error correction data for replicating simulated physics (rigid bodies)

### DefaultDegreesOfFreedom
- **类型**: `ESettingsDOF`
- **描述**: Useful for constraining all objects in the world, for example if you are making a 2D game using 3D environments.

### bSuppressFaceRemapTable
- **类型**: `bool`
- **描述**: If true, the internal physx face to UE face mapping will not be generated. This is a memory optimization available if you do not rely on face indices returned by scene queries.

### bSupportUVFromHitResults
- **类型**: `bool`
- **描述**: If true, store extra information to allow FindCollisionUV to derive UV info from a line trace hit result, using the FindCollisionUV utility

### bDisableActiveActors
- **类型**: `bool`
- **描述**: If true, physx will not update unreal with any bodies that have moved during the simulation. This should only be used if you have no physx simulation or you are manually updating the unreal data via polling physx.

### bDisableKinematicStaticPairs
- **类型**: `bool`
- **描述**: Whether to disable generating KS pairs, enabling this makes switching between dynamic and static slower for actors - but speeds up contact generation by early rejecting these pairs

### bDisableKinematicKinematicPairs
- **类型**: `bool`
- **描述**: Whether to disable generating KK pairs, enabling this speeds up contact generation, however it is required when using APEX destruction.

### bDisableCCD
- **类型**: `bool`
- **描述**: If true CCD will be ignored. This is an optimization when CCD is never used which removes the need for physx to check it internally.

### AnimPhysicsMinDeltaTime
- **类型**: `float32`
- **描述**: Min Delta Time below which anim dynamics and rigidbody nodes will not simulate.

### bSimulateAnimPhysicsAfterReset
- **类型**: `bool`
- **描述**: Whether to simulate anim physics nodes in the tick where they're reset.

### MinPhysicsDeltaTime
- **类型**: `float32`
- **描述**: Min Physics Delta Time; the simulation will not step if the delta time is below this value

### MaxPhysicsDeltaTime
- **类型**: `float32`
- **描述**: Max Physics Delta Time to be clamped.

### bSubstepping
- **类型**: `bool`
- **描述**: Whether to substep the physics simulation. This feature is still experimental. Certain functionality might not work correctly

### bSubsteppingAsync
- **类型**: `bool`
- **描述**: Whether to substep the async physics simulation. This feature is still experimental. Certain functionality might not work correctly

### bTickPhysicsAsync
- **类型**: `bool`
- **描述**: Whether to tick physics simulation on an async thread. This feature is still experimental. Certain functionality might not work correctly

### AsyncFixedTimeStepSize
- **类型**: `float32`
- **描述**: If using async, the time step size to tick at. This feature is still experimental. Certain functionality might not work correctly

### MaxSubstepDeltaTime
- **类型**: `float32`
- **描述**: Max delta time (in seconds) for an individual simulation substep.

### MaxSubsteps
- **类型**: `int`
- **描述**: Max number of substeps for physics simulation.

### SyncSceneSmoothingFactor
- **类型**: `float32`
- **描述**: Physics delta time smoothing factor for sync scene.

### InitialAverageFrameRate
- **类型**: `float32`
- **描述**: Physics delta time initial average.

### PhysXTreeRebuildRate
- **类型**: `int`
- **描述**: The number of frames it takes to rebuild the PhysX scene query AABB tree. The bigger the number, the smaller fetchResults takes per frame, but the more the tree deteriorates until a new tree is built

### DefaultBroadphaseSettings
- **类型**: `FBroadphaseSettings`
- **描述**: If we want to Enable MPB or not globally. This is then overridden by project settings if not enabled. *

### MinDeltaVelocityForHitEvents
- **类型**: `float32`
- **描述**: Minimum velocity delta required on a collinding object for Chaos to send a hit event

### ChaosSettings
- **类型**: `FChaosPhysicsSettings`
- **描述**: Chaos physics engine settings

## 方法

### GetPhysicsHistoryCount
```angelscript
int GetPhysicsHistoryCount()
```

