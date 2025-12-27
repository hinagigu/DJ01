# FNiagaraSpawnInfo

Data controlling the spawning of particles

## 属性

### Count
- **类型**: `int`
- **描述**: How many particles to spawn.

### InterpStartDt
- **类型**: `float32`
- **描述**: The sub frame delta time at which to spawn the first particle.

### IntervalDt
- **类型**: `float32`
- **描述**: The sub frame delta time between each particle.

### SpawnGroup
- **类型**: `int`
- **描述**: An integer used to identify this spawn info.
Typically this is unused.
An example usage is when using multiple spawn modules to spawn from multiple discreet locations.

## 方法

### opAssign
```angelscript
FNiagaraSpawnInfo& opAssign(FNiagaraSpawnInfo Other)
```

