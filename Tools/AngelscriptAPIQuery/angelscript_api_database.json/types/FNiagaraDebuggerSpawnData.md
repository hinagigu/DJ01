# FNiagaraDebuggerSpawnData

## 属性

### SystemsToSpawn
- **类型**: `TArray<TSoftObjectPtr<UNiagaraSystem>>`
- **描述**: List of all the systems we want to spawn.

### bSpawnAllAtOnce
- **类型**: `bool`

### TimeBetweenSpawns
- **类型**: `float32`
- **描述**: The time delay we should use between spawning if we have a list to spawn.

### bKillBeforeSpawn
- **类型**: `bool`
- **描述**: Should we kill systems we spawn before we spawn another.

### bWorldLocation
- **类型**: `bool`
- **描述**: When true the location is a world location, when false it's relative to the player and is in camera space.

### Location
- **类型**: `FVector`
- **描述**: The location we should use to spawn the system at, either world or local to the player depending on WorldLocation flag.

### bAttachToPlayer
- **类型**: `bool`
- **描述**: Should we attach to the player controlled by the camera or not

### bAutoActivate
- **类型**: `bool`
- **描述**: Should we auto activate or not

### bAutoDestroy
- **类型**: `bool`
- **描述**: Should we auto destroy when complete or not

### bDoPreCullCheck
- **类型**: `bool`
- **描述**: Should we perform the pre cull check or not

## 方法

### opAssign
```angelscript
FNiagaraDebuggerSpawnData& opAssign(FNiagaraDebuggerSpawnData Other)
```

