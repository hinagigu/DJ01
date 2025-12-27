# FChaosSolverConfiguration

## 属性

### PositionIterations
- **类型**: `int`
- **描述**: The number of position iterations to run during the constraint solver step

### VelocityIterations
- **类型**: `int`
- **描述**: The number of velocity iterations to run during the constraint solver step

### ProjectionIterations
- **类型**: `int`
- **描述**: The number of projection iterations to run during the constraint solver step

### CollisionMarginFraction
- **类型**: `float32`
- **描述**: A collision margin as a fraction of size used by some boxes and convex shapes to improve collision detection results.
The core geometry of shapes that support a margin are reduced in size by the margin, and the margin
is added back on during collision detection. The net result is a shape of the same size but with rounded corners.

### CollisionMarginMax
- **类型**: `float32`
- **描述**: An upper limit on the collision margin that will be subtracted from boxes and convex shapes. See CollisionMarginFraction

### CollisionCullDistance
- **类型**: `float32`
- **描述**: During collision detection, if tweo shapes are at least this far apart we do not calculate their nearest features
during the collision detection step.

### CollisionMaxPushOutVelocity
- **类型**: `float32`
- **描述**: The maximum speed at which two bodies can be extracted from each other when they start a frame inter-penetrating. This can
happen because they spawned on top of each other, or the solver failed to fully reolve collisions last frame. A value of
zero means "no limit". A non-zero value can be used to prevent explosive behaviour when bodies start deeply penetrating.
An alternative to using this approach is to increase the number of Velocity Iterations, which is more expensive but will
ensure the bodies are depenetrated in a single frame without explosive behaviour.

### CollisionInitialOverlapDepenetrationVelocity
- **类型**: `float32`
- **描述**: If two bodies start off in overlapping each other, they will depentrate at this speed when they wake.
If set to a large value, initially-overlapping objects will tend to "explode" apart at a speed that depends on the
overlap amount and the timestep (this is the original, previously untunable behaviour). If set to zero,
initially-overlapping objects will remain stationary and go to sleep until acted on by some other object or force.
A negative value (-1) disables the feature and is equivalent to infinity.
This property can be overridden per Body (see FBodyInstance::MaxDepenetrationVelocity)

### ClusterConnectionFactor
- **类型**: `float32`

### ClusterUnionConnectionType
- **类型**: `EClusterUnionMethod`

### bGenerateCollisionData
- **类型**: `bool`

### CollisionFilterSettings
- **类型**: `FSolverCollisionFilterSettings`

### bGenerateBreakData
- **类型**: `bool`

### BreakingFilterSettings
- **类型**: `FSolverBreakingFilterSettings`

### bGenerateTrailingData
- **类型**: `bool`

### TrailingFilterSettings
- **类型**: `FSolverTrailingFilterSettings`

## 方法

### opAssign
```angelscript
FChaosSolverConfiguration& opAssign(FChaosSolverConfiguration Other)
```

