# UNavigationSystemV1

**继承自**: `UNavigationSystemBase`

## 属性

### DefaultAgentName
- **类型**: `FName`

### CrowdManagerClass
- **类型**: `TSoftClassPtr<UCrowdManagerBase>`

### GeometryExportTriangleCountWarningThreshold
- **类型**: `int`
- **描述**: Warnings are logged if exporting the navigation collision for an object exceed this triangle count.
Use -1 to disable.

### ActiveTilesUpdateInterval
- **类型**: `float32`
- **描述**: Minimal time, in seconds, between active tiles set update

### InvokersMaximumDistanceFromSeed
- **类型**: `float`
- **描述**: When in use, invokers farther away from any invoker seed will be ignored (set to -1 to disable).

### DataGatheringMode
- **类型**: `ENavDataGatheringModeConfig`
- **描述**: Sets how navigation data should be gathered when building collision information

### DirtyAreaWarningSizeThreshold
- **类型**: `float32`
- **描述**: -1 by default, if set to a positive value dirty areas with any dimensions in 2d over the threshold created at runtime will be logged

### GatheringNavModifiersWarningLimitTime
- **类型**: `float32`
- **描述**: -1.0f by default, if set to a positive value, all calls to GetNavigationData will be timed and compared to it.
     Over the limit calls will be logged as warnings.
     In seconds. Non-shipping build only.

### SupportedAgents
- **类型**: `TArray<FNavDataConfig>`
- **描述**: List of agents types supported by this navigation system

### SupportedAgentsMask
- **类型**: `FNavAgentSelector`
- **描述**: NavigationSystem's properties in Project Settings define all possible supported agents,
    but a specific navigation system can choose to support only a subset of agents. Set via
    NavigationSystemConfig

### OnNavigationGenerationFinishedDelegate
- **类型**: `FOnNavDataGenericEvent`

### bAutoCreateNavigationData
- **类型**: `bool`

### bSpawnNavDataInNavBoundsLevel
- **类型**: `bool`

### bAllowClientSideNavigation
- **类型**: `bool`

### bShouldDiscardSubLevelNavData
- **类型**: `bool`

### bTickWhilePaused
- **类型**: `bool`

### bInitialBuildingLocked
- **类型**: `bool`

### bSkipAgentHeightCheckWhenPickingNavData
- **类型**: `bool`

### bGenerateNavigationOnlyAroundNavigationInvokers
- **类型**: `bool`

## 方法

### ReplaceAreaInOctreeData
```angelscript
bool ReplaceAreaInOctreeData(const UObject Object, TSubclassOf<UNavArea> OldArea, TSubclassOf<UNavArea> NewArea)
```

### OnNavigationBoundsUpdated
```angelscript
void OnNavigationBoundsUpdated(ANavMeshBoundsVolume NavVolume)
```
@todo document

### RegisterNavigationInvoker
```angelscript
void RegisterNavigationInvoker(AActor Invoker, float32 TileGenerationRadius, float32 TileRemovalRadius)
```
Registers given actor as a "navigation enforcer" which means navigation system will
    make sure navigation is being generated in specified radius around it.
    @note: you need NavigationSystem's GenerateNavigationOnlyAroundNavigationInvokers to be set to true
            to take advantage of this feature

### ResetMaxSimultaneousTileGenerationJobsCount
```angelscript
void ResetMaxSimultaneousTileGenerationJobsCount()
```
Brings limit of simultaneous navmesh tile generation jobs back to Project Setting's default value

### SetGeometryGatheringMode
```angelscript
void SetGeometryGatheringMode(ENavDataGatheringModeConfig NewMode)
```

### SetMaxSimultaneousTileGenerationJobsCount
```angelscript
void SetMaxSimultaneousTileGenerationJobsCount(int MaxNumberOfJobs)
```
will limit the number of simultaneously running navmesh tile generation jobs to specified number.
    @param MaxNumberOfJobs gets trimmed to be at least 1. You cannot use this function to pause navmesh generation

### UnregisterNavigationInvoker
```angelscript
void UnregisterNavigationInvoker(AActor Invoker)
```
Removes given actor from the list of active navigation enforcers.
    @see RegisterNavigationInvoker for more details

