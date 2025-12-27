# AFunctionalAITestBase

**继承自**: `AFunctionalTest`

AFunctionalAITestBase

Base abstract class defining a Functional AI Test.
You can derive from this base class to create a test with a different type of SpawnSets.

## 属性

### SpawnLocationRandomizationRange
- **类型**: `float32`

### SpawnedPawns
- **类型**: `TArray<TObjectPtr<APawn>>`

### PendingDelayedSpawns
- **类型**: `TArray<FPendingDelayedSpawn>`

### CurrentSpawnSetIndex
- **类型**: `int`

### CurrentSpawnSetName
- **类型**: `FString`

### OnAISpawned
- **类型**: `FFunctionalTestAISpawned`

### OnAllAISPawned
- **类型**: `FFunctionalTestEventSignature`

### NavMeshDebugOrigin
- **类型**: `FVector`
- **描述**: navmesh debug: log navoctree modifiers around this point

### NavMeshDebugExtent
- **类型**: `FVector`
- **描述**: navmesh debug: extent around NavMeshDebugOrigin

### bWaitForNavMesh
- **类型**: `bool`

### bDebugNavMeshOnTimeout
- **类型**: `bool`

## 方法

### IsOneOfSpawnedPawns
```angelscript
bool IsOneOfSpawnedPawns(AActor Actor)
```

