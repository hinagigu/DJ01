# __HealthSnapshot

## 方法

### LogPerformanceSnapshot
```angelscript
void LogPerformanceSnapshot(FString SnapshotTitle, bool bResetStats)
```
Writes a snapshot to the log. Captures memory stats by default. Also captures performance stats if called after StartHealthSnapshotChart and before SopHealthSnapshotChart.

@param        SnapshotTitle                   The name to be given to the new HealthSnapshot.

### StartPerformanceSnapshots
```angelscript
void StartPerformanceSnapshots()
```
Begins capturing FPS charts that can be used to include performance data in a HealthSnapshot. If snapshots are already running clears all accumulated performance data

### StopPerformanceSnapshots
```angelscript
void StopPerformanceSnapshots()
```
Stops capturing FPS charts only if StartHealthSnapshotChart has first been called. Does nothing if FPS charts are not running. HealthSnapshots captured after this is called will not include performance stats.

