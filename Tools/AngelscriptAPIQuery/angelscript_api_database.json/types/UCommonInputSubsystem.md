# UCommonInputSubsystem

**继承自**: `ULocalPlayerSubsystem`

## 属性

### OnInputMethodChanged
- **类型**: `FInputMethodChangedDelegate`

## 方法

### GetCurrentGamepadName
```angelscript
FName GetCurrentGamepadName()
```

### GetCurrentInputType
```angelscript
ECommonInputType GetCurrentInputType()
```
The current input type based on the last input received on the device.

### GetDefaultInputType
```angelscript
ECommonInputType GetDefaultInputType()
```
The default input type for the current platform.

### IsInputMethodActive
```angelscript
bool IsInputMethodActive(ECommonInputType InputMethod)
```

### IsUsingPointerInput
```angelscript
bool IsUsingPointerInput()
```

### SetCurrentInputType
```angelscript
void SetCurrentInputType(ECommonInputType NewInputType)
```

### SetGamepadInputType
```angelscript
void SetGamepadInputType(FName InGamepadInputType)
```

### ShouldShowInputKeys
```angelscript
bool ShouldShowInputKeys()
```
Should display indicators for the current input device on screen.  This is needed when capturing videos, but we don't want to reveal the capture source device.

