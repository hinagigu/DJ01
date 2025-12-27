# UEnvQueryGenerator_PathingGrid

**继承自**: `UEnvQueryGenerator_SimpleGrid`

Navigation grid, generates points on navmesh
with paths to/from context no further than given limit

## 属性

### PathToItem
- **类型**: `FAIDataProviderBoolValue`
- **描述**: pathfinding direction

### NavigationFilter
- **类型**: `TSubclassOf<UNavigationQueryFilter>`
- **描述**: navigation filter to use in pathfinding

### ScanRangeMultiplier
- **类型**: `FAIDataProviderFloatValue`
- **描述**: multiplier for max distance between point and context

