# UGarbageCollectionSettings

**继承自**: `UDeveloperSettings`

Implements the settings for garbage collection.

## 属性

### TimeBetweenPurgingPendingKillObjects
- **类型**: `float32`
- **描述**: Time in seconds (game time) we should wait between purging object references to objects that are pending kill.

### MinGCClusterSize
- **类型**: `int`
- **描述**: Minimum GC cluster size.

### NumRetriesBeforeForcingGC
- **类型**: `int`
- **描述**: Maximum number of times GC can be skipped if worker threads are currently modifying UObject state. 0 = never force GC

### MaxObjectsNotConsideredByGC
- **类型**: `int`
- **描述**: Maximum Object Count Not Considered By GC. Works only in cooked builds.

### SizeOfPermanentObjectPool
- **类型**: `int`
- **描述**: Size Of Permanent Object Pool (bytes). Works only in cooked builds.

### MaxObjectsInGame
- **类型**: `int`
- **描述**: Maximum number of UObjects that can exist in cooked game. Keep this as small as possible.

### MaxObjectsInEditor
- **类型**: `int`
- **描述**: Maximum number of UObjects that can exist in the editor game. Make sure this can hold enough objects for the editor and commadlets within reasonable limit.

### FlushStreamingOnGC
- **类型**: `bool`

### AllowParallelGC
- **类型**: `bool`

### IncrementalBeginDestroyEnabled
- **类型**: `bool`

### MultithreadedDestructionEnabled
- **类型**: `bool`

### CreateGCClusters
- **类型**: `bool`

### AssetClusteringEnabled
- **类型**: `bool`

### ActorClusteringEnabled
- **类型**: `bool`

### UseDisregardForGCOnDedicatedServers
- **类型**: `bool`

### VerifyUObjectsAreNotFGCObjects
- **类型**: `bool`

### GarbageEliminationEnabled
- **类型**: `bool`

### DumpObjectCountsToLogWhenMaxObjectLimitExceeded
- **类型**: `bool`

