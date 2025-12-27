# FVersionedNiagaraEmitterData

Struct containing all of the data that can be different between different emitter versions.

## 属性

### bLocalSpace
- **类型**: `bool`

### bDeterminism
- **类型**: `bool`

### RandomSeed
- **类型**: `int`

### SimTarget
- **类型**: `ENiagaraSimTarget`

### CalculateBoundsMode
- **类型**: `ENiagaraEmitterCalculateBoundMode`
- **描述**: How should we calculate bounds for the emitter.
Note: If this is greyed out it means fixed bounds are enabled in the System Properties and these bounds are therefore ignored.

### FixedBounds
- **类型**: `FBox`

### Platforms
- **类型**: `FNiagaraPlatformSet`

### ScalabilityOverrides
- **类型**: `FNiagaraEmitterScalabilityOverrides`

### MaxGPUParticlesSpawnPerFrame
- **类型**: `int`

### AllocationMode
- **类型**: `EParticleAllocationMode`

### PreAllocationCount
- **类型**: `int`
- **描述**: The emitter will allocate at least this many particles on it's first tick.
This can aid performance by avoiding many allocations as an emitter ramps up to it's max size.

### AttributesToPreserve
- **类型**: `TArray<FString>`
- **描述**: An allow list of Particle attributes (e.g. "Particle.Position" or "Particle.Age") that will not be removed from the DataSet  even if they aren't read by the VM.
          Used in conjunction with UNiagaraSystem::bTrimAttributes

### AddEmitterDefaultViewState
- **类型**: `ENiagaraEmitterDefaultSummaryState`
- **描述**: This determines how emitters will be added to a system by default. If summary view is setup, consider setting this to 'Summary'.

### SimStageExecutionLoopEditorData
- **类型**: `TArray<FNiagaraSimStageExecutionLoopEditorData>`

### bInterpolatedSpawning
- **类型**: `bool`

### bRequiresPersistentIDs
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FVersionedNiagaraEmitterData& opAssign(FVersionedNiagaraEmitterData Other)
```

