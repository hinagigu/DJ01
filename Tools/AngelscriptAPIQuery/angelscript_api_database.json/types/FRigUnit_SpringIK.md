# FRigUnit_SpringIK

The Spring IK solver uses a verlet integrator to perform an IK solve.
It support custom constraints including distance, length etc.
Note: This node operates in world space!

## 属性

### StartBone
- **类型**: `FName`

### EndBone
- **类型**: `FName`

### HierarchyStrength
- **类型**: `float32`
- **描述**: Sets the coefficient of the springs along the hierarchy. Values between 1 and 2048 are common.

### EffectorStrength
- **类型**: `float32`
- **描述**: Sets the coefficient of the springs towards the effector. Values between 1 and 2048 are common.

### EffectorRatio
- **类型**: `float32`
- **描述**: Defines the equilibrium of the effector springs.
This value ranges from 0.0 (zero distance) to 1.0 (distance in initial pose)

### RootStrength
- **类型**: `float32`
- **描述**: Sets the coefficient of the springs towards the root. Values between 1 and 2048 are common.

### RootRatio
- **类型**: `float32`
- **描述**: Defines the equilibrium of the root springs.
This value ranges from 0.0 (zero distance) to 1.0 (distance in initial pose)

### Damping
- **类型**: `float32`
- **描述**: The higher the value to more quickly the simulation calms down. Values between 0.0001 and 0.75 are common.

### PoleVector
- **类型**: `FVector`

### bFlipPolePlane
- **类型**: `bool`

### PoleVectorKind
- **类型**: `EControlRigVectorKind`

### PoleVectorSpace
- **类型**: `FName`

### PrimaryAxis
- **类型**: `FVector`

### SecondaryAxis
- **类型**: `FVector`

### bLiveSimulation
- **类型**: `bool`

### Iterations
- **类型**: `int`
- **描述**: Drives how precise the solver operates. Values between 4 and 24 are common.
This is only used if the simulation is not live (bLiveSimulation setting).

### bLimitLocalPosition
- **类型**: `bool`

### bPropagateToChildren
- **类型**: `bool`
- **描述**: If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

### DebugSettings
- **类型**: `FRigUnit_SpringIK_DebugSettings`

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_SpringIK& opAssign(FRigUnit_SpringIK Other)
```

