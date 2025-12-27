# AGameplayCueNotify_Looping

**继承自**: `AGameplayCueNotify_Actor`

AGameplayCueNotify_Looping

    This is an instanced gameplay cue notify for continuous looping effects.
    The game is responsible for defining the start/stop by adding/removing the gameplay cue.

## 属性

### DefaultSpawnCondition
- **类型**: `FGameplayCueNotify_SpawnCondition`

### DefaultPlacementInfo
- **类型**: `FGameplayCueNotify_PlacementInfo`

### ApplicationEffects
- **类型**: `FGameplayCueNotify_BurstEffects`

### ApplicationSpawnResults
- **类型**: `FGameplayCueNotify_SpawnResult`
- **描述**: Results of spawned application effects.

### LoopingEffects
- **类型**: `FGameplayCueNotify_LoopingEffects`

### LoopingSpawnResults
- **类型**: `FGameplayCueNotify_SpawnResult`
- **描述**: Results of spawned looping effects.

### RecurringEffects
- **类型**: `FGameplayCueNotify_BurstEffects`

### RecurringSpawnResults
- **类型**: `FGameplayCueNotify_SpawnResult`
- **描述**: Results of spawned recurring effects.

### RemovalEffects
- **类型**: `FGameplayCueNotify_BurstEffects`

### RemovalSpawnResults
- **类型**: `FGameplayCueNotify_SpawnResult`
- **描述**: Results of spawned removal effects.

## 方法

### OnApplication
```angelscript
void OnApplication(AActor Target, FGameplayCueParameters Parameters, FGameplayCueNotify_SpawnResult SpawnResults)
```

### OnLoopingStart
```angelscript
void OnLoopingStart(AActor Target, FGameplayCueParameters Parameters, FGameplayCueNotify_SpawnResult SpawnResults)
```

### OnRecurring
```angelscript
void OnRecurring(AActor Target, FGameplayCueParameters Parameters, FGameplayCueNotify_SpawnResult SpawnResults)
```

### OnRemoval
```angelscript
void OnRemoval(AActor Target, FGameplayCueParameters Parameters, FGameplayCueNotify_SpawnResult SpawnResults)
```

