# ANavigationTestingActor

**继承自**: `AActor`

## 属性

### InvokerComponent
- **类型**: `UNavigationInvokerComponent`

### NavAgentProps
- **类型**: `FNavAgentProperties`
- **描述**: @todo document

### QueryingExtent
- **类型**: `FVector`

### ProjectedLocation
- **类型**: `FVector`

### CostLimitFactor
- **类型**: `float32`
- **描述**: this multiplier is used to compute a max node cost allowed to the open list
    (cost limit = CostLimitFactor*InitialHeuristicEstimate)

### MinimumCostLimit
- **类型**: `float32`
- **描述**: minimum cost limit clamping value (in cost units)
    used to allow large deviation in short paths

### RadiusUsedToValidateNavData
- **类型**: `float32`
- **描述**: NavData must be ready for all tiles within radius. When using 0, NavData must be ready at the actor location.

### CostDisplayMode
- **类型**: `ENavCostDisplay`
- **描述**: determines which cost will be shown

### TextCanvasOffset
- **类型**: `FVector2D`
- **描述**: text canvas offset to apply

### PathfindingTime
- **类型**: `float32`
- **描述**: Time in micro seconds

### PathCost
- **类型**: `float`

### PathfindingSteps
- **类型**: `int`

### OtherActor
- **类型**: `ANavigationTestingActor`

### FilterClass
- **类型**: `TSubclassOf<UNavigationQueryFilter>`
- **描述**: "None" will result in default filter being used

### ShowStepIndex
- **类型**: `int`
- **描述**: Show debug steps up to this index. Use -1 to disable.

### OffsetFromCornersDistance
- **类型**: `float32`

### bActAsNavigationInvoker
- **类型**: `bool`

### bProjectedLocationValid
- **类型**: `bool`

### bSearchStart
- **类型**: `bool`

### bBacktracking
- **类型**: `bool`

### bUseHierarchicalPathfinding
- **类型**: `bool`

### bGatherDetailedInfo
- **类型**: `bool`

### bRequireNavigableEndLocation
- **类型**: `bool`

### bDrawDistanceToWall
- **类型**: `bool`

### bDrawIfNavDataIsReadyInRadius
- **类型**: `bool`

### bShowNodePool
- **类型**: `bool`

### bShowBestPath
- **类型**: `bool`

### bShowDiffWithPreviousStep
- **类型**: `bool`

### bShouldBeVisibleInGame
- **类型**: `bool`

### bPathExist
- **类型**: `bool`

### bPathIsPartial
- **类型**: `bool`

### bPathSearchOutOfNodes
- **类型**: `bool`

