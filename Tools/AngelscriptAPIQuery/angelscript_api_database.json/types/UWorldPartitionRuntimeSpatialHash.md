# UWorldPartitionRuntimeSpatialHash

**继承自**: `UWorldPartitionRuntimeHash`

## 属性

### Grids
- **类型**: `TArray<FSpatialHashRuntimeGrid>`

### UseAlignedGridLevels
- **类型**: `EWorldPartitionCVarProjectDefaultOverride`
- **描述**: Disable to help break the pattern caused by world partition promotion of actors to upper grid levels that are always aligned on child levels.

### SnapNonAlignedGridLevelsToLowerLevels
- **类型**: `EWorldPartitionCVarProjectDefaultOverride`
- **描述**: Disable to avoid snapping higher levels cells to child cells. Only used when bUseAlignedGridLevels is false.

### PlaceSmallActorsUsingLocation
- **类型**: `EWorldPartitionCVarProjectDefaultOverride`
- **描述**: Enable to place actors smaller than a cell size into their corresponding cell using their location instead of their bounding box.

### PlacePartitionActorsUsingLocation
- **类型**: `EWorldPartitionCVarProjectDefaultOverride`
- **描述**: Enable to place partitioned actors into their corresponding cell using their location instead of their bounding box.

### bEnableZCulling
- **类型**: `bool`
- **描述**: Whether this hash enables Z culling.

