# ULevel

**继承自**: `UObject`

A Level is a collection of Actors (lights, volumes, mesh instances etc.).
Multiple Levels can be loaded and unloaded into the World to create a streaming experience.

@see https://docs.unrealengine.com/latest/INT/Engine/Levels
@see UActor

## 属性

### bUseExternalActors
- **类型**: `bool`
- **描述**: Use external actors, new actor spawned in this level will be external and existing external actors will be loaded on load.

### LevelSimplification
- **类型**: `FLevelSimplificationDetails`
- **描述**: Level simplification settings for each LOD

### bUseActorFolders
- **类型**: `bool`
- **描述**: Use actor folder objects, actor folders of this level will be persistent in their own object.

## 方法

### GetLevelScriptActor
```angelscript
ALevelScriptActor GetLevelScriptActor()
```

### IsVisible
```angelscript
bool IsVisible()
```

### IsBeingRemoved
```angelscript
bool IsBeingRemoved()
```

### GetActors
```angelscript
TArray<AActor> GetActors()
```

