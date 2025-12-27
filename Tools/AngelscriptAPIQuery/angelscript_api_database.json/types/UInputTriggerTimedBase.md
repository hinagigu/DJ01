# UInputTriggerTimedBase

**继承自**: `UInputTrigger`

Base class for building triggers that have firing conditions governed by elapsed time.
This class transitions state to Ongoing once input is actuated, and will track Ongoing input time until input is released.
Inheriting classes should provide the logic for Triggered transitions.

## 属性

### HeldDuration
- **类型**: `float32`
- **描述**: How long have we been actuating this trigger?

### bAffectedByTimeDilation
- **类型**: `bool`

