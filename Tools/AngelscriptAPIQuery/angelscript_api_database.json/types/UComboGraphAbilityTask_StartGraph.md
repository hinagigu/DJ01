# UComboGraphAbilityTask_StartGraph

**继承自**: `UAbilityTask`

This task is meant to be used to start / activate a Combo Graph Asset from within a Gameplay Ability

## 属性

### OnGraphStart
- **类型**: `FComboGraphAbilityTaskDelegate`

### OnGraphEnd
- **类型**: `FComboGraphAbilityTaskDelegate`

### EventReceived
- **类型**: `FComboGraphAbilityTaskDelegate`

## 方法

### GetCurrentNode
```angelscript
UComboGraphNodeAnimBase GetCurrentNode()
```
Returns the currently active node for the task

### GetPreviousNode
```angelscript
UComboGraphNodeAnimBase GetPreviousNode()
```
Returns the node that was active just before the current one

