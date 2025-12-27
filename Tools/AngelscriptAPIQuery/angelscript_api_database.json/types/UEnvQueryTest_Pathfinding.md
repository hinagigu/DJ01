# UEnvQueryTest_Pathfinding

**继承自**: `UEnvQueryTest`

## 属性

### TestMode
- **类型**: `EEnvTestPathfinding`
- **描述**: testing mode

### Context
- **类型**: `TSubclassOf<UEnvQueryContext>`
- **描述**: context: other end of pathfinding test

### PathFromContext
- **类型**: `FAIDataProviderBoolValue`
- **描述**: pathfinding direction

### SkipUnreachable
- **类型**: `FAIDataProviderBoolValue`
- **描述**: if set, items with failed path will be invalidated (PathCost, PathLength)

### FilterClass
- **类型**: `TSubclassOf<UNavigationQueryFilter>`
- **描述**: navigation filter to use in pathfinding

