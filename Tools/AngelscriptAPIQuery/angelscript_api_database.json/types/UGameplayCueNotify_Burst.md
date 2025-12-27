# UGameplayCueNotify_Burst

**继承自**: `UGameplayCueNotify_Static`

UGameplayCueNotify_Burst

    This is a non-instanced gameplay cue notify for effects that are one-offs.
    Since it is not instanced, it cannot do latent actions such as delays and time lines.

## 属性

### DefaultSpawnCondition
- **类型**: `FGameplayCueNotify_SpawnCondition`

### DefaultPlacementInfo
- **类型**: `FGameplayCueNotify_PlacementInfo`

### BurstEffects
- **类型**: `FGameplayCueNotify_BurstEffects`

## 方法

### OnBurst
```angelscript
void OnBurst(AActor Target, FGameplayCueParameters Parameters, FGameplayCueNotify_SpawnResult SpawnResults)
```

