# UWorldPartitionSubsystem

**继承自**: `UTickableWorldSubsystem`

UWorldPartitionSubsystem

## 方法

### IsAllStreamingCompleted
```angelscript
bool IsAllStreamingCompleted()
```
Returns true if world partition is done streaming levels, adding them to the world or removing them from the world.

### IsStreamingCompleted
```angelscript
bool IsStreamingCompleted(EWorldPartitionRuntimeCellState QueryState, TArray<FWorldPartitionStreamingQuerySource> QuerySources, bool bExactState)
```

