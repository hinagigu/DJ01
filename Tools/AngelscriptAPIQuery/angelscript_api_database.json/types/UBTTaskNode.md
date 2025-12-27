# UBTTaskNode

**继承自**: `UBTNode`

Task are leaf nodes of behavior tree, which perform actual actions

Because some of them can be instanced for specific AI, following virtual functions are not marked as const:
 - ExecuteTask
 - AbortTask
 - TickTask
 - OnMessage

If your node is not being instanced (default behavior), DO NOT change any properties of object within those functions!
Template nodes are shared across all behavior tree components using the same tree asset and must store
their runtime properties in provided NodeMemory block (allocation size determined by GetInstanceMemorySize() )

## 属性

### bIgnoreRestartSelf
- **类型**: `bool`

