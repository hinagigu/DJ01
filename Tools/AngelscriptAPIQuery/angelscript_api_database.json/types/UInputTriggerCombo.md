# UInputTriggerCombo

**继承自**: `UInputTrigger`

UInputTriggerCombo
All actions in the combo array must be completed (based on combo completion event specified - triggered, completed, etc.) to trigger the action this trigger is on.
Actions must also be completed in the order specified by the combo actions array (starting at index 0).
Note: This will only trigger for one frame before resetting the combo trigger's progress

## 属性

### CurrentComboStepIndex
- **类型**: `int`
- **描述**: Keeps track of what action we're currently at in the combo

### CurrentTimeBetweenComboSteps
- **类型**: `float32`
- **描述**: Time elapsed between last combo InputAction trigger and current time

### ComboActions
- **类型**: `TArray<FInputComboStepData>`

### InputCancelActions
- **类型**: `TArray<FInputCancelAction>`

