# UAbilityTask_MoveToLocation

**继承自**: `UAbilityTask`

Move to a location, ignoring clipping, over a given length of time. Ends when the TargetLocation is reached.
This will RESET your character's current movement mode! If you wish to maintain PHYS_Flying or PHYS_Custom, you must
reset it on completion.!

## 属性

### OnTargetLocationReached
- **类型**: `FMoveToLocationDelegate`

