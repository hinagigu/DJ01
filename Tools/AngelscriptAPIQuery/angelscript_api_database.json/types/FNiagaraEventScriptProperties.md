# FNiagaraEventScriptProperties

## 属性

### ExecutionMode
- **类型**: `EScriptExecutionMode`
- **描述**: Controls which particles have the event script run on them.

### SpawnNumber
- **类型**: `uint`
- **描述**: Controls whether or not particles are spawned as a result of handling the event. Only valid for EScriptExecutionMode::SpawnedParticles. If Random Spawn Number is used, this will act as the maximum spawn range.

### MaxEventsPerFrame
- **类型**: `uint`
- **描述**: Controls how many events are consumed by this event handler. If there are more events generated than this value, they will be ignored.

### SourceEmitterID
- **类型**: `FGuid`
- **描述**: Id of the Emitter Handle that generated the event. If all zeroes, the event generator is assumed to be this emitter.

### SourceEventName
- **类型**: `FName`
- **描述**: The name of the event generated. This will be "Collision" for collision events and the Event Name field on the DataSetWrite node in the module graph for others.

### bRandomSpawnNumber
- **类型**: `bool`
- **描述**: Whether using a random spawn number.

### MinSpawnNumber
- **类型**: `uint`
- **描述**: The minimum spawn number when random spawn is used. Spawn Number is used as the maximum range.

### UpdateAttributeInitialValues
- **类型**: `bool`
- **描述**: Should Event Spawn Scripts modify the Initial values for particle attributes they modify.

## 方法

### opAssign
```angelscript
FNiagaraEventScriptProperties& opAssign(FNiagaraEventScriptProperties Other)
```

