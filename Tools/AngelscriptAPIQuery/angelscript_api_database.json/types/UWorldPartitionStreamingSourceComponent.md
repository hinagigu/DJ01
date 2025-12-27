# UWorldPartitionStreamingSourceComponent

**继承自**: `UActorComponent`

## 属性

### DefaultVisualizerLoadingRange
- **类型**: `float32`
- **描述**: Value used by debug visualizer when grid loading range is chosen.

### TargetBehavior
- **类型**: `EStreamingSourceTargetBehavior`

### TargetGrids
- **类型**: `TArray<FName>`

### DebugColor
- **类型**: `FColor`
- **描述**: Color used for debugging.

### Shapes
- **类型**: `TArray<FStreamingSourceShape>`

### Priority
- **类型**: `EStreamingSourcePriority`

### bStreamingSourceEnabled
- **类型**: `bool`

### TargetState
- **类型**: `EStreamingSourceTargetState`

## 方法

### DisableStreamingSource
```angelscript
void DisableStreamingSource()
```
Disable the component

### EnableStreamingSource
```angelscript
void EnableStreamingSource()
```
Enable the component

### IsStreamingCompleted
```angelscript
bool IsStreamingCompleted()
```
Returns true if streaming is completed for this streaming source component.

### IsStreamingSourceEnabled
```angelscript
bool IsStreamingSourceEnabled()
```
Returns true if the component is active.

