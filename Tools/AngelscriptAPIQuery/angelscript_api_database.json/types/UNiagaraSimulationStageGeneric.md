# UNiagaraSimulationStageGeneric

**继承自**: `UNiagaraSimulationStageBase`

## 属性

### IterationSource
- **类型**: `ENiagaraIterationSource`
- **描述**: Select what we should be iterating over, particles or data interfaces.
The source provides things such as element count (when not overriden) and stack context variables (i.e. attributes on grids)

### NumIterations
- **类型**: `FNiagaraParameterBindingWithValue`
- **描述**: Number of times (or iterations) the simulation stage will execute in a row.
For example, setting this to 10 will mean this simulation stage runs 10 times in a row before the next stage.
Can also be bound to a attribute so the simulation can dynamically decide

### ExecuteBehavior
- **类型**: `ENiagaraSimStageExecuteBehavior`
- **描述**: Controls when the simulation stage should execute, only valid for data interface iteration stages

### ParticleIterationStateRange
- **类型**: `FIntPoint`
- **描述**: The inclusive range used to check particle state binding against when enabled.

### OverrideGpuDispatchNumThreadsX
- **类型**: `FNiagaraParameterBindingWithValue`
- **描述**: Parameter binding / constant value for Num Threads X

### OverrideGpuDispatchNumThreadsY
- **类型**: `FNiagaraParameterBindingWithValue`
- **描述**: Parameter binding / constant value for Num Threads Y

### OverrideGpuDispatchNumThreadsZ
- **类型**: `FNiagaraParameterBindingWithValue`
- **描述**: Parameter binding / constant value for Num Threads Z

### DirectDispatchType
- **类型**: `ENiagaraGpuDispatchType`
- **描述**: Dimensions to use for dispatch.

### DirectDispatchElementType
- **类型**: `ENiagaraDirectDispatchElementType`
- **描述**: Customizes what the element count means for a direct dispatch.

### ElementCountX
- **类型**: `FNiagaraParameterBindingWithValue`
- **描述**: Integer binding to override the number of elements the stage will execute along X.
For example, if you want to iterate over a custom source such as triangles on a mesh you can
set an int to the triangle count in an emitter script and bind that as the element count.

### ElementCountY
- **类型**: `FNiagaraParameterBindingWithValue`
- **描述**: Integer binding to override the number of elements the stage will execute along Y.
For example, if you want to iterate over a 2D texture you can set an int to the texture height
in an emitter script and bind that as the element count.

### ElementCountZ
- **类型**: `FNiagaraParameterBindingWithValue`
- **描述**: Integer binding to override the number of elements the stage will execute along Z.
For example, if you want to iterate over a 3D texture you can set an int to the texture depth
in an emitter script and bind that as the element count.

### bDisablePartialParticleUpdate
- **类型**: `bool`

### bParticleIterationStateEnabled
- **类型**: `bool`

### bGpuDispatchForceLinear
- **类型**: `bool`

### bOverrideGpuDispatchNumThreads
- **类型**: `bool`

