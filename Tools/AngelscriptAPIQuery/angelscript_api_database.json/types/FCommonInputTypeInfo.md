# FCommonInputTypeInfo

## 属性

### Key
- **类型**: `FKey`
- **描述**: Key this action is bound to

### OverrrideState
- **类型**: `EInputActionState`
- **描述**: EInputActionState::Enabled means that the state isn't overriden and the games dynamic control will work

### bActionRequiresHold
- **类型**: `bool`
- **描述**: Enables hold time if true

### HoldTime
- **类型**: `float32`
- **描述**: The hold time in seconds

### HoldRollbackTime
- **类型**: `float32`
- **描述**: Time (in seconds) for hold progress to go from 1.0 (completed) to 0.0.
If the hold interaction was interrupted, then hold progress starts to roll back decreasing its value.
Set to 0.0 to disable the rollback functionality.

### OverrideBrush
- **类型**: `FSlateBrush`
- **描述**: Override the brush specified by the Key Display Data

## 方法

### opAssign
```angelscript
FCommonInputTypeInfo& opAssign(FCommonInputTypeInfo Other)
```

