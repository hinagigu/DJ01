# UBTDecorator_Loop

**继承自**: `UBTDecorator`

Loop decorator node.
A decorator node that bases its condition on whether its loop counter has been exceeded.

## 属性

### NumLoops
- **类型**: `int`
- **描述**: number of executions

### bInfiniteLoop
- **类型**: `bool`
- **描述**: infinite loop

### InfiniteLoopTimeoutTime
- **类型**: `float32`
- **描述**: timeout (when looping infinitely, when we finish a loop we will check whether we have spent this time looping, if we have we will stop looping). A negative value means loop forever.

