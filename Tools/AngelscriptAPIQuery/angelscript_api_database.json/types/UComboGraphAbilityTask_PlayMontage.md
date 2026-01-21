# UComboGraphAbilityTask_PlayMontage

**继承自**: `UAbilityTask`

This task is a variation of PlayMontageAndWaitForEvent that combines PlayMontageAndWait and WaitForEvent into one task.

The added functionality here is that it is a ticking task to optionally trigger AnimNotifyStates Begin and End event, without having
them actually registered in the Animation Asset (Sequence or Montage)

## 属性

### OnCompleted
- **类型**: `FComboGraphPlayMontageEventDelegate`

### OnBlendOut
- **类型**: `FComboGraphPlayMontageEventDelegate`

### OnInterrupted
- **类型**: `FComboGraphPlayMontageEventDelegate`

### OnCancelled
- **类型**: `FComboGraphPlayMontageEventDelegate`

### EventReceived
- **类型**: `FComboGraphPlayMontageEventDelegate`

## 方法

### UnbindAllDelegate
```angelscript
void UnbindAllDelegate()
```
Unbinds all animation delegate on this Ability Task (except OnCanceled)

