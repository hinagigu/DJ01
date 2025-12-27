# UPhysicsSettingsCore

**继承自**: `UDeveloperSettings`

Default physics settings.

## 属性

### DefaultGravityZ
- **类型**: `float32`
- **描述**: Default gravity.

### DefaultTerminalVelocity
- **类型**: `float32`
- **描述**: Default terminal velocity for Physics Volumes.

### DefaultFluidFriction
- **类型**: `float32`
- **描述**: Default fluid friction for Physics Volumes.

### SimulateScratchMemorySize
- **类型**: `int`
- **描述**: Amount of memory to reserve for PhysX simulate(), this is per pxscene and will be rounded up to the next 16K boundary

### RagdollAggregateThreshold
- **类型**: `int`
- **描述**: Threshold for ragdoll bodies above which they will be added to an aggregate before being added to the scene

### TriangleMeshTriangleMinAreaThreshold
- **类型**: `float32`
- **描述**: Triangles from triangle meshes (BSP) with an area less than or equal to this value will be removed from physics collision data. Set to less than 0 to disable.

### bEnableEnhancedDeterminism
- **类型**: `bool`
- **描述**: If set to true, the scene will use enhanced determinism at the cost of a bit more resources. See eENABLE_ENHANCED_DETERMINISM to learn about the specifics

### bEnableShapeSharing
- **类型**: `bool`
- **描述**: Enables shape sharing between sync and async scene for static rigid actors

### bEnablePCM
- **类型**: `bool`
- **描述**: Enables persistent contact manifolds. This will generate fewer contact points, but with more accuracy. Reduces stability of stacking, but can help energy conservation.

### bEnableStabilization
- **类型**: `bool`
- **描述**: Enables stabilization of contacts for slow moving bodies. This will help improve the stability of stacking.

### bWarnMissingLocks
- **类型**: `bool`
- **描述**: Whether to warn when physics locks are used incorrectly. Turning this off is not recommended and should only be used by very advanced users.

### bEnable2DPhysics
- **类型**: `bool`
- **描述**: Can 2D physics be used (Box2D)?

### BounceThresholdVelocity
- **类型**: `float32`
- **描述**: Minimum relative velocity required for an object to bounce. A typical value for simulation stability is about 0.2 * gravity

### FrictionCombineMode
- **类型**: `EFrictionCombineMode`
- **描述**: Friction combine mode, controls how friction is computed for multiple materials.

### RestitutionCombineMode
- **类型**: `EFrictionCombineMode`
- **描述**: Restitution combine mode, controls how restitution is computed for multiple materials.

### MaxAngularVelocity
- **类型**: `float32`
- **描述**: Max angular velocity that a simulated object can achieve.

### MaxDepenetrationVelocity
- **类型**: `float32`
- **描述**: Max velocity which may be used to depenetrate simulated physics objects. 0 means no maximum.

### ContactOffsetMultiplier
- **类型**: `float32`
- **描述**: Contact offset multiplier. When creating a physics shape we look at its bounding volume and multiply its minimum value by this multiplier. A bigger number will generate contact points earlier which results in higher stability at the cost of performance.

### MinContactOffset
- **类型**: `float32`
- **描述**: Min Contact offset.

### MaxContactOffset
- **类型**: `float32`
- **描述**: Max Contact offset.

### bSimulateSkeletalMeshOnDedicatedServer
- **类型**: `bool`
- **描述**: If true, simulate physics for this component on a dedicated server.
This should be set if simulating physics and replicating with a dedicated server.

### DefaultShapeComplexity
- **类型**: `ECollisionTraceFlag`
- **描述**: Determines the default physics shape complexity.

### SolverOptions
- **类型**: `FChaosSolverConfiguration`
- **描述**: Options to apply to Chaos solvers on creation

