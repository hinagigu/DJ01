# UBTDecorator_TagCooldown

**继承自**: `UBTDecorator`

Cooldown decorator node.
A decorator node that bases its condition on whether a cooldown timer based on a gameplay tag has expired.

## 属性

### CooldownTag
- **类型**: `FGameplayTag`
- **描述**: Gameplay tag that will be used for the cooldown.

### CooldownDuration
- **类型**: `float32`
- **描述**: Value we will add or set to the Cooldown tag when this node is deactivated.

### bAddToExistingDuration
- **类型**: `bool`
- **描述**: True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time).

### bActivatesCooldown
- **类型**: `bool`
- **描述**: Whether or not we are adding/setting to the cooldown tag's value when the decorator deactivates.

