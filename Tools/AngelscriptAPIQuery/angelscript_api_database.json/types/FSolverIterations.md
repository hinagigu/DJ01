# FSolverIterations

Solver settings for use by the Legacy RigidBody AnimNode (RBAN) solver.
Thse settings are no longer used by default and will eventually be deprecated and then removed.

@note These settings have no effect when the Physics Asset is used in a world simulation (ragdoll).

## 属性

### SolverIterations
- **类型**: `int`

### JointIterations
- **类型**: `int`

### CollisionIterations
- **类型**: `int`

### SolverPushOutIterations
- **类型**: `int`

### JointPushOutIterations
- **类型**: `int`

### CollisionPushOutIterations
- **类型**: `int`

## 方法

### opAssign
```angelscript
FSolverIterations& opAssign(FSolverIterations Other)
```

