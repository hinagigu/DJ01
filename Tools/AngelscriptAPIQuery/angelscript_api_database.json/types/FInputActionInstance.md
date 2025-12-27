# FInputActionInstance

Run time queryable action instance
Generated from UInputAction templates above

## 属性

### SourceAction
- **类型**: `const UInputAction`
- **描述**: The source action that this instance is created from

### TriggerEvent
- **类型**: `ETriggerEvent`
- **描述**: Trigger state

### LastTriggeredWorldTime
- **类型**: `float32`
- **描述**: The last time that this evaluated to a Triggered State

### Triggers
- **类型**: `TArray<TObjectPtr<UInputTrigger>>`

### Modifiers
- **类型**: `TArray<TObjectPtr<UInputModifier>>`

### ElapsedProcessedTime
- **类型**: `float32`
- **描述**: Total trigger processing/evaluation time (How long this action has been in event Started, Ongoing, or Triggered

### ElapsedTriggeredTime
- **类型**: `float32`
- **描述**: Triggered time (How long this action has been in event Triggered only)

## 方法

### opAssign
```angelscript
FInputActionInstance& opAssign(FInputActionInstance Other)
```

