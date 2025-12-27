# UBTDecorator_SetTagCooldown

**继承自**: `UBTDecorator`

Set tag cooldown decorator node.
A decorator node that sets a gameplay tag cooldown.

## 属性

### CooldownTag
- **类型**: `FGameplayTag`
- **描述**: Gameplay tag that will be used for the cooldown.

### CooldownDuration
- **类型**: `float32`
- **描述**: Value we will add or set to the Cooldown tag when this task runs.

### bAddToExistingDuration
- **类型**: `bool`
- **描述**: True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time).

