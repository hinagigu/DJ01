# FRecastNavMeshGenerationProperties

## 属性

### TilePoolSize
- **类型**: `int`
- **描述**: maximum number of tiles NavMesh can hold

### TileSizeUU
- **类型**: `float32`
- **描述**: size of single tile, expressed in uu

### CellSize
- **类型**: `float32`
- **描述**: horizontal size of voxelization cell

### CellHeight
- **类型**: `float32`
- **描述**: vertical size of voxelization cell

### AgentRadius
- **类型**: `float32`
- **描述**: Radius of largest agent that can freely traverse the generated navmesh

### AgentHeight
- **类型**: `float32`
- **描述**: Size of the tallest agent that will path with this navmesh.

### AgentMaxSlope
- **类型**: `float32`
- **描述**: The maximum slope (angle) that the agent can move on.

### AgentMaxStepHeight
- **类型**: `float32`
- **描述**: Largest vertical step the agent can perform

### MinRegionArea
- **类型**: `float32`
- **描述**: The minimum dimension of area. Areas smaller than this will be discarded

### MergeRegionSize
- **类型**: `float32`
- **描述**: The size limit of regions to be merged with bigger regions (watershed partitioning only)

### MaxSimplificationError
- **类型**: `float32`
- **描述**: How much navigable shapes can get simplified - the higher the value the more freedom

### TileNumberHardLimit
- **类型**: `int`
- **描述**: Absolute hard limit to number of navmesh tiles. Be very, very careful while modifying it while
     having big maps with navmesh. A single, empty tile takes 176 bytes and empty tiles are
     allocated up front (subject to change, but that's where it's at now)
     @note TileNumberHardLimit is always rounded up to the closest power of 2

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

### bSortNavigationAreasByCost
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

### bFixedTilePoolSize
- **类型**: `bool`

### bIsWorldPartitioned
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FRecastNavMeshGenerationProperties& opAssign(FRecastNavMeshGenerationProperties Other)
```

