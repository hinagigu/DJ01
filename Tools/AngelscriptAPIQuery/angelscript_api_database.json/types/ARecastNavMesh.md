# ARecastNavMesh

**继承自**: `ANavigationData`

## 属性

### DrawOffset
- **类型**: `float32`
- **描述**: vertical offset added to navmesh's debug representation for better readability

### TileGenerationDebug
- **类型**: `FRecastNavMeshTileGenerationDebug`

### TilePoolSize
- **类型**: `int`
- **描述**: maximum number of tiles NavMesh can hold

### TileSizeUU
- **类型**: `float32`
- **描述**: size of single tile, expressed in uu

### NavMeshResolutionParams
- **类型**: `FNavMeshResolutionParam`
- **描述**: Resolution params
If using multiple resolutions, it's recommended to chose the highest resolution first and
set it according to the highest desired precision and then the other resolutions.

### AgentRadius
- **类型**: `float32`
- **描述**: Radius of smallest agent to traverse this navmesh

### AgentHeight
- **类型**: `float32`
- **描述**: Size of the tallest agent that will path with this navmesh.

### AgentMaxSlope
- **类型**: `float32`
- **描述**: The maximum slope (angle) that the agent can move on.

### MinRegionArea
- **类型**: `float32`
- **描述**: The minimum dimension of area. Areas smaller than this will be discarded

### MergeRegionSize
- **类型**: `float32`
- **描述**: The size limit of regions to be merged with bigger regions (watershed partitioning only)

### MaxVerticalMergeError
- **类型**: `int`
- **描述**: Maximum vertical deviation between raw contour points to allowing merging (in voxel).
Use a low value (2-5) depending on CellHeight, AgentMaxStepHeight and AgentMaxSlope, to allow more precise contours (also see SimplificationElevationRatio).
Use very high value to deactivate (Recast behavior).

### MaxSimplificationError
- **类型**: `float32`
- **描述**: How much navigable shapes can get simplified - the higher the value the more freedom

### SimplificationElevationRatio
- **类型**: `float32`
- **描述**: When simplifying contours, how much is the vertical error taken into account when comparing with MaxSimplificationError.
Use 0 to deactivate (Recast behavior), use 1 as a typical value.

### MaxSimultaneousTileGenerationJobsCount
- **类型**: `int`
- **描述**: Sets the limit for number of asynchronous tile generators running at one time, also used for some synchronous tasks

### TileNumberHardLimit
- **类型**: `int`
- **描述**: Absolute hard limit to number of navmesh tiles. Be very, very careful while modifying it while
    having big maps with navmesh. A single, empty tile takes 176 bytes and empty tiles are
    allocated up front (subject to change, but that's where it's at now)
    @note TileNumberHardLimit is always rounded up to the closest power of 2

### NavMeshOriginOffset
- **类型**: `FVector`
- **描述**: Use this if you don't want your tiles to start at (0,0,0)

### LedgeSlopeFilterMode
- **类型**: `ENavigationLedgeSlopeFilterMode`
- **描述**: filtering methode used for filtering ledge slopes

### RegionPartitioning
- **类型**: `ERecastPartitioning`
- **描述**: partitioning method for creating navmesh polys

### LayerPartitioning
- **类型**: `ERecastPartitioning`
- **描述**: partitioning method for creating tile layers

### RegionChunkSplits
- **类型**: `int`
- **描述**: number of chunk splits (along single axis) used for region's partitioning: ChunkyMonotone

### LayerChunkSplits
- **类型**: `int`
- **描述**: number of chunk splits (along single axis) used for layer's partitioning: ChunkyMonotone

### TimeSliceFilterLedgeSpansMaxYProcess
- **类型**: `int`
- **描述**: The maximum number of y coords to process when time slicing filter ledge spans during navmesh regeneration.

### TimeSliceLongDurationDebug
- **类型**: `float`
- **描述**: If a single time sliced section of navmesh regen code exceeds this duration then it will trigger debug logging

### InvokerTilePriorityBumpDistanceThresholdInTileUnits
- **类型**: `uint`
- **描述**: If >= 1, when sorting pending tiles by priority, tiles near invokers (within the distance threshold) will have their priority increased.

### InvokerTilePriorityBumpIncrease
- **类型**: `uint8`
- **描述**: Priority increase steps for tiles that are withing near distance.

### HeuristicScale
- **类型**: `float32`
- **描述**: Euclidean distance heuristic scale used while pathfinding

### VerticalDeviationFromGroundCompensation
- **类型**: `float32`
- **描述**: Value added to each search height to compensate for error between navmesh polys and walkable geometry

### bDrawTriangleEdges
- **类型**: `bool`

### bDrawPolyEdges
- **类型**: `bool`

### bDrawFilledPolys
- **类型**: `bool`

### bDrawNavMeshEdges
- **类型**: `bool`

### bDrawTileBounds
- **类型**: `bool`

### bDrawTileResolutions
- **类型**: `bool`

### bDrawPathCollidingGeometry
- **类型**: `bool`

### bDrawTileLabels
- **类型**: `bool`

### bDrawTileBuildTimes
- **类型**: `bool`

### bDrawTileBuildTimesHeatMap
- **类型**: `bool`

### bDrawPolygonLabels
- **类型**: `bool`

### bDrawDefaultPolygonCost
- **类型**: `bool`

### bDrawPolygonFlags
- **类型**: `bool`

### bDrawLabelsOnPathNodes
- **类型**: `bool`

### bDrawNavLinks
- **类型**: `bool`

### bDrawFailedNavLinks
- **类型**: `bool`

### bDrawClusters
- **类型**: `bool`

### bDrawOctree
- **类型**: `bool`

### bDrawOctreeDetails
- **类型**: `bool`

### bDrawMarkedForbiddenPolys
- **类型**: `bool`

### bFixedTilePoolSize
- **类型**: `bool`

### bSortNavigationAreasByCost
- **类型**: `bool`

### bIsWorldPartitioned
- **类型**: `bool`

### bPerformVoxelFiltering
- **类型**: `bool`

### bMarkLowHeightAreas
- **类型**: `bool`

### bUseExtraTopCellWhenMarkingAreas
- **类型**: `bool`

### bFilterLowSpanSequences
- **类型**: `bool`

### bFilterLowSpanFromTileCache
- **类型**: `bool`

### bDoFullyAsyncNavDataGathering
- **类型**: `bool`

## 方法

### ReplaceAreaInTileBounds
```angelscript
bool ReplaceAreaInTileBounds(FBox Bounds, TSubclassOf<UNavArea> OldArea, TSubclassOf<UNavArea> NewArea, bool ReplaceLinks)
```
@return true if any polygon/link has been touched

