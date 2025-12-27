# AGameplayCueNotify_BurstLatent

**继承自**: `AGameplayCueNotify_Actor`

AGameplayCueNotify_BurstLatent

    This is an instanced gameplay cue notify for effects that are one-offs.
    Since it is instanced, it can do latent things like time lines or delays.

## 属性

### DefaultSpawnCondition
- **类型**: `FGameplayCueNotify_SpawnCondition`

### DefaultPlacementInfo
- **类型**: `FGameplayCueNotify_PlacementInfo`

### BurstEffects
- **类型**: `FGameplayCueNotify_BurstEffects`

### BurstSpawnResults
- **类型**: `FGameplayCueNotify_SpawnResult`
- **描述**: Results of spawned burst effects.

## 方法

### OnBurst
```angelscript
void OnBurst(AActor Target, FGameplayCueParameters Parameters, FGameplayCueNotify_SpawnResult SpawnResults)
```

