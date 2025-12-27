# UAbilityTask_WaitInputPress

**继承自**: `UAbilityTask`

Waits until the input is pressed from activating an ability. This should be true immediately upon starting the ability, since the key was pressed to activate it.
We expect server to execute this task in parallel and keep its own time. We do not keep track of

## 属性

### OnPress
- **类型**: `FInputPressDelegate`

