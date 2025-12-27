# UNavigationInvokerComponent

**继承自**: `UActorComponent`

## 属性

### TileGenerationRadius
- **类型**: `float32`

### TileRemovalRadius
- **类型**: `float32`

### SupportedAgents
- **类型**: `FNavAgentSelector`
- **描述**: restrict navigation generation to specific agents

### Priority
- **类型**: `ENavigationInvokerPriority`
- **描述**: Experimental invocation priority. It will modify the order in which invoked tiles are being built if SortPendingTilesMethod is set to SortByPriority.

