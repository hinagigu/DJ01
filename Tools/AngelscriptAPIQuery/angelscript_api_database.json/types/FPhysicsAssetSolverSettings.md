# FPhysicsAssetSolverSettings

Solver iterations settings for use by RigidBody AnimNode (RBAN) in the Anim Graph. Each RBAN node runs its own solver with these settings.

@note These settings have no effect when the Physics Asset is used in a world simulation (i.e., as a ragdoll on a SkeletalMeshComponent).

## 属性

### PositionIterations
- **类型**: `int`

### VelocityIterations
- **类型**: `int`

### ProjectionIterations
- **类型**: `int`

### CullDistance
- **类型**: `float32`

### MaxDepenetrationVelocity
- **类型**: `float32`

### FixedTimeStep
- **类型**: `float32`

### bUseLinearJointSolver
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FPhysicsAssetSolverSettings& opAssign(FPhysicsAssetSolverSettings Other)
```

