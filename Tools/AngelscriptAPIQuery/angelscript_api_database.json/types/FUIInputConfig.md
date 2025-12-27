# FUIInputConfig

Input Config that can be applied on widget activation. Allows for input setup  (Mouse capture,
UI-only input, move / look ignore, etc), to be controlled by widget activation.

## 属性

### bIgnoreMoveInput
- **类型**: `bool`

### bIgnoreLookInput
- **类型**: `bool`

### InputMode
- **类型**: `ECommonInputMode`

### MouseCaptureMode
- **类型**: `EMouseCaptureMode`

### MouseLockMode
- **类型**: `EMouseLockMode`

### bHideCursorDuringViewportCapture
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FUIInputConfig& opAssign(FUIInputConfig Other)
```

