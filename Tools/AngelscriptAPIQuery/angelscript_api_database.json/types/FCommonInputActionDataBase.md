# FCommonInputActionDataBase

## 属性

### DisplayName
- **类型**: `FText`

### HoldDisplayName
- **类型**: `FText`

### NavBarPriority
- **类型**: `int`

### KeyboardInputTypeInfo
- **类型**: `FCommonInputTypeInfo`
- **描述**: Key to bind to for each input method

### DefaultGamepadInputTypeInfo
- **类型**: `FCommonInputTypeInfo`
- **描述**: Default input state for gamepads

### GamepadInputOverrides
- **类型**: `TMap<FName,FCommonInputTypeInfo>`
- **描述**: Override the input state for each input method

### TouchInputTypeInfo
- **类型**: `FCommonInputTypeInfo`
- **描述**: Override the displayed brush for each input method

## 方法

### opAssign
```angelscript
FCommonInputActionDataBase& opAssign(FCommonInputActionDataBase Other)
```

