# FMovieSceneSpawnable

MovieSceneSpawnable describes an object that can be spawned for this MovieScene

## 属性

### SpawnTransform
- **类型**: `FTransform`
- **描述**: Optional spawn transform

### Tags
- **类型**: `TArray<FName>`
- **描述**: Array of tags that can be used for grouping and categorizing.

### bContinuouslyRespawn
- **类型**: `bool`
- **描述**: When enabled, this spawnable will always be respawned if it gets destroyed externally. When disabled, this object will only ever be spawned once for each spawn key even if it is destroyed externally.

### bNetAddressableName
- **类型**: `bool`
- **描述**: When enabled, the actor will be spawned with a unique name so that it can be addressable between clients and servers.

### DynamicBinding
- **类型**: `FMovieSceneDynamicBinding`
- **描述**: Optional user-defined spawning information

## 方法

### opAssign
```angelscript
FMovieSceneSpawnable& opAssign(FMovieSceneSpawnable Other)
```

