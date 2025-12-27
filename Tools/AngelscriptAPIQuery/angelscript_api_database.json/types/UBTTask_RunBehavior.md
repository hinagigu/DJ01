# UBTTask_RunBehavior

**继承自**: `UBTTaskNode`

RunBehavior task allows pushing subtrees on execution stack.
Subtree asset can't be changed in runtime!

This limitation is caused by support for subtree's root level decorators,
which are injected into parent tree, and structure of running tree
cannot be modified in runtime (see: BTNode: ExecutionIndex, MemoryOffset)

Use RunBehaviorDynamic task for subtrees that need to be changed in runtime.

## 属性

### BehaviorAsset
- **类型**: `UBehaviorTree`
- **描述**: behavior to run

