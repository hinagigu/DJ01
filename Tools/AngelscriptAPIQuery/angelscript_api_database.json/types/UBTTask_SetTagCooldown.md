# UBTTask_SetTagCooldown

**继承自**: `UBTTaskNode`

Cooldown task node.
Sets a cooldown tag value.  Use with cooldown tag decorators to prevent behavior tree execution.

## 属性

### CooldownTag
- **类型**: `FGameplayTag`
- **描述**: Gameplay tag that will be used for the cooldown.

### bAddToExistingDuration
- **类型**: `bool`
- **描述**: True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time).

### CooldownDuration
- **类型**: `float32`
- **描述**: Value we will add or set to the Cooldown tag when this task runs.

