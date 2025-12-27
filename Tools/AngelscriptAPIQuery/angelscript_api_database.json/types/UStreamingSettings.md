# UStreamingSettings

**继承自**: `UDeveloperSettings`

Streaming settings.

## 属性

### TimeLimitExceededMultiplier
- **类型**: `float32`
- **描述**: Multiplier for time limit exceeded warning time threshold.

### TimeLimitExceededMinTime
- **类型**: `float32`
- **描述**: Minimum time the time limit exceeded warning will be triggered by.

### MinBulkDataSizeForAsyncLoading
- **类型**: `int`
- **描述**: Minimum time the time limit exceeded warning will be triggered by.

### AsyncLoadingTimeLimit
- **类型**: `float32`
- **描述**: Maximum amount of time to spend doing asynchronous loading (ms per frame).

### PriorityAsyncLoadingExtraTime
- **类型**: `float32`
- **描述**: Additional time to spend asynchronous loading during a high priority load.

### LevelStreamingActorsUpdateTimeLimit
- **类型**: `float32`
- **描述**: Maximum allowed time to spend for actor registration steps during level streaming (ms per frame).

### PriorityLevelStreamingActorsUpdateExtraTime
- **类型**: `float32`
- **描述**: Additional time to spend on actor registration steps during a high priority load.

### LevelStreamingComponentsRegistrationGranularity
- **类型**: `int`
- **描述**: Batching granularity used to register actor components during level streaming.

### LevelStreamingAddPrimitiveGranularity
- **类型**: `int`
- **描述**: Batching granularity used to add primitives to scene in parallel when registering actor components during level streaming.

### LevelStreamingUnregisterComponentsTimeLimit
- **类型**: `float32`
- **描述**: Maximum allowed time to spend while unregistering components during level streaming (ms per frame).

### LevelStreamingComponentsUnregistrationGranularity
- **类型**: `int`
- **描述**: Batching granularity used to unregister actor components during level streaming.

### AsyncLoadingThreadEnabled
- **类型**: `bool`

### WarnIfTimeLimitExceeded
- **类型**: `bool`

### UseBackgroundLevelStreaming
- **类型**: `bool`

### AsyncLoadingUseFullTimeLimit
- **类型**: `bool`

### FlushStreamingOnExit
- **类型**: `bool`

### EventDrivenLoaderEnabled
- **类型**: `bool`

