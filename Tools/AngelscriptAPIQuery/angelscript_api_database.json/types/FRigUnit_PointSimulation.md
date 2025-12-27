# FRigUnit_PointSimulation

Performs point based simulation
Note: Disabled for now.

## 属性

### Points
- **类型**: `TArray<FRigVMSimPoint>`

### Links
- **类型**: `TArray<FCRSimLinearSpring>`

### Forces
- **类型**: `TArray<FCRSimPointForce>`

### CollisionVolumes
- **类型**: `TArray<FCRSimSoftCollision>`

### SimulatedStepsPerSecond
- **类型**: `float32`
- **描述**: The frame rate of the simulation

### IntegratorType
- **类型**: `ERigVMSimPointIntegrateType`
- **描述**: The type of integrator to use

### VerletBlend
- **类型**: `float32`

### BoneTargets
- **类型**: `TArray<FRigUnit_PointSimulation_BoneTarget>`
- **描述**: The bones to map to the simulated points.

### bLimitLocalPosition
- **类型**: `bool`

### bPropagateToChildren
- **类型**: `bool`
- **描述**: If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

### PrimaryAimAxis
- **类型**: `FVector`

### SecondaryAimAxis
- **类型**: `FVector`

### DebugSettings
- **类型**: `FRigUnit_PointSimulation_DebugSettings`

### Bezier
- **类型**: `FRigVMFourPointBezier`
- **描述**: If the simulation has at least four points they will be stored in here.

### ExecuteContext
- **类型**: `FRigVMExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_PointSimulation& opAssign(FRigUnit_PointSimulation Other)
```

