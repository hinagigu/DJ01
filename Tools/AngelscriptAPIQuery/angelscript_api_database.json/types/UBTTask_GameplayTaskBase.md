# UBTTask_GameplayTaskBase

**继承自**: `UBTTaskNode`

Base class for managing gameplay tasks
Since AITask doesn't have any kind of success/failed results, default implemenation will only return EBTNode::Succeeded

In your ExecuteTask:
- use NewBTAITask() helper to create task
- initialize task with values if needed
- use StartGameplayTask() helper to execute and get node result

## 属性

### bWaitForGameplayTask
- **类型**: `bool`

