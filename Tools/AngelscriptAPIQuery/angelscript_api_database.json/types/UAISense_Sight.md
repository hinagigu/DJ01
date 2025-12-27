# UAISense_Sight

**继承自**: `UAISense`

## 属性

### MaxTracesPerTick
- **类型**: `int`

### MaxAsyncTracesPerTick
- **类型**: `int`
- **描述**: Maximum number of asynchronous traces that can be requested in a single update call

### MinQueriesPerTimeSliceCheck
- **类型**: `int`

### MaxTimeSlicePerTick
- **类型**: `float`

### HighImportanceQueryDistanceThreshold
- **类型**: `float32`

### MaxQueryImportance
- **类型**: `float32`

### SightLimitQueryImportance
- **类型**: `float32`

### PendingQueriesBudgetReductionRatio
- **类型**: `float32`
- **描述**: Defines the amount of async trace queries to prevent based on the number of pending queries at the start of an update.
1 means that the async trace budget is slashed by the pending queries count
0 means that the async trace budget is not impacted by the pending queries

### bUseAsynchronousTraceForDefaultSightQueries
- **类型**: `bool`
- **描述**: Defines if we are allowed to use asynchronous trace queries when there is no IAISightTargetInterface for a Target

