# FBodyInstance

Container for a physics representation of an object

## 属性

### ObjectType
- **类型**: `ECollisionChannel`
- **描述**: Enum indicating what type of object this should be considered as when it moves

### CollisionEnabled
- **类型**: `ECollisionEnabled`
- **描述**: Type of collision enabled.

      No Collision      : Will not create any representation in the physics engine. Cannot be used for spatial queries (raycasts, sweeps, overlaps) or simulation (rigid body, constraints). Best performance possible (especially for moving objects)
      Query Only        : Only used for spatial queries (raycasts, sweeps, and overlaps). Cannot be used for simulation (rigid body, constraints). Useful for character movement and things that do not need physical simulation. Performance gains by keeping data out of simulation tree.
      Physics Only      : Only used only for physics simulation (rigid body, constraints). Cannot be used for spatial queries (raycasts, sweeps, overlaps). Useful for jiggly bits on characters that do not need per bone detection. Performance gains by keeping data out of query tree
      Collision Enabled : Can be used for both spatial queries (raycasts, sweeps, overlaps) and simulation (rigid body, constraints).

### SleepFamily
- **类型**: `ESleepFamily`

### DOFMode
- **类型**: `EDOFMode`
- **描述**: [Physx Only] Locks physical movement along specified axis.

### SolverAsyncDeltaTime
- **类型**: `float32`

### CollisionProfileName
- **类型**: `FName`
- **描述**: Collision Profile Name *

### PositionSolverIterationCount
- **类型**: `uint8`

### VelocitySolverIterationCount
- **类型**: `uint8`

### CollisionResponses
- **类型**: `FCollisionResponse`
- **描述**: Custom Channels for Responses

### MaxDepenetrationVelocity
- **类型**: `float32`

### MassInKgOverride
- **类型**: `float32`

### LinearDamping
- **类型**: `float32`

### AngularDamping
- **类型**: `float32`

### CustomDOFPlaneNormal
- **类型**: `FVector`
- **描述**: Locks physical movement along a custom plane for a given normal.

### COMNudge
- **类型**: `FVector`

### MassScale
- **类型**: `float32`

### InertiaTensorScale
- **类型**: `FVector`

### WalkableSlopeOverride
- **类型**: `FWalkableSlopeOverride`

### PhysMaterialOverride
- **类型**: `UPhysicalMaterial`

### MaxAngularVelocity
- **类型**: `float32`

### CustomSleepThresholdMultiplier
- **类型**: `float32`

### StabilizationThresholdMultiplier
- **类型**: `float32`

### bUseCCD
- **类型**: `bool`

### bUseMACD
- **类型**: `bool`

### bIgnoreAnalyticCollisions
- **类型**: `bool`

### bNotifyRigidBodyCollision
- **类型**: `bool`

### bSmoothEdgeCollisions
- **类型**: `bool`

### bLockTranslation
- **类型**: `bool`

### bLockRotation
- **类型**: `bool`

### bLockXTranslation
- **类型**: `bool`

### bLockYTranslation
- **类型**: `bool`

### bLockZTranslation
- **类型**: `bool`

### bLockXRotation
- **类型**: `bool`

### bLockYRotation
- **类型**: `bool`

### bLockZRotation
- **类型**: `bool`

### bOverrideMaxAngularVelocity
- **类型**: `bool`

### bOverrideMaxDepenetrationVelocity
- **类型**: `bool`

### bOverrideWalkableSlopeOnInstance
- **类型**: `bool`

### bInertiaConditioning
- **类型**: `bool`

### bOneWayInteraction
- **类型**: `bool`

### bOverrideSolverAsyncDeltaTime
- **类型**: `bool`

### bSimulatePhysics
- **类型**: `bool`

### bOverrideMass
- **类型**: `bool`

### bEnableGravity
- **类型**: `bool`

### bUpdateKinematicFromSimulation
- **类型**: `bool`

### bAutoWeld
- **类型**: `bool`

### bStartAwake
- **类型**: `bool`

### bGenerateWakeEvents
- **类型**: `bool`

### bUpdateMassWhenScaleChanges
- **类型**: `bool`

## 方法

### GetBodySetup
```angelscript
UBodySetup GetBodySetup()
```

### Weld
```angelscript
bool Weld(FBodyInstance& TheirBody, FTransform TheirTM)
```

### UnWeld
```angelscript
void UnWeld(FBodyInstance& TheirBI)
```

### SetUseCCD
```angelscript
void SetUseCCD(bool bInUseCCD)
```

