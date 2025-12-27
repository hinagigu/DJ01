# AChaosSolverActor

**继承自**: `AActor`

## 属性

### Properties
- **类型**: `FChaosSolverConfiguration`

### bHasFloor
- **类型**: `bool`
- **描述**: End deprecated properties

### FloorHeight
- **类型**: `float32`

### ChaosDebugSubstepControl
- **类型**: `FChaosDebugSubstepControl`
- **描述**: * Control to pause/step/substep the solver to the next synchronization point.

## 方法

### SetAsCurrentWorldSolver
```angelscript
void SetAsCurrentWorldSolver()
```
Makes this solver the current world solver. Dynamically spawned objects will have their physics state created in this solver.

### SetSolverActive
```angelscript
void SetSolverActive(bool bActive)
```
Controls whether the solver is able to simulate particles it controls

