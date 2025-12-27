# FPointerEvent

FPointerEvent describes a mouse or touch action (e.g. Press, Release, Move, etc).
It is passed to event handlers dealing with pointer-based input.

## 方法

### IsRepeat
```angelscript
bool IsRepeat()
```

### IsShiftDown
```angelscript
bool IsShiftDown()
```

### IsLeftShiftDown
```angelscript
bool IsLeftShiftDown()
```

### IsRightShiftDown
```angelscript
bool IsRightShiftDown()
```

### IsControlDown
```angelscript
bool IsControlDown()
```

### IsLeftControlDown
```angelscript
bool IsLeftControlDown()
```

### IsRightControlDown
```angelscript
bool IsRightControlDown()
```

### IsAltDown
```angelscript
bool IsAltDown()
```

### IsLeftAltDown
```angelscript
bool IsLeftAltDown()
```

### IsRightAltDown
```angelscript
bool IsRightAltDown()
```

### IsCommandDown
```angelscript
bool IsCommandDown()
```

### IsLeftCommandDown
```angelscript
bool IsLeftCommandDown()
```

### IsRightCommandDown
```angelscript
bool IsRightCommandDown()
```

### AreCapsLocked
```angelscript
bool AreCapsLocked()
```

### GetUserIndex
```angelscript
uint GetUserIndex()
```

### GetPlatformUserid
```angelscript
FPlatformUserId GetPlatformUserid()
```

### GetInputDeviceId
```angelscript
FInputDeviceId GetInputDeviceId()
```

### GetScreenSpacePosition
```angelscript
FVector2D GetScreenSpacePosition()
```

### GetLastScreenSpacePosition
```angelscript
FVector2D GetLastScreenSpacePosition()
```

### GetCursorDelta
```angelscript
FVector2D GetCursorDelta()
```

### GetGestureDelta
```angelscript
FVector2D GetGestureDelta()
```

### IsMouseButtonDown
```angelscript
bool IsMouseButtonDown(FKey MouseButton)
```

### GetEffectingButton
```angelscript
FKey GetEffectingButton()
```

### GetWheelDelta
```angelscript
float32 GetWheelDelta()
```

### GetPointerIndex
```angelscript
uint GetPointerIndex()
```

### GetTouchpadIndex
```angelscript
uint GetTouchpadIndex()
```

### GetTouchForce
```angelscript
float32 GetTouchForce()
```

### IsTouchEvent
```angelscript
bool IsTouchEvent()
```

### IsTouchForceChangedEvent
```angelscript
bool IsTouchForceChangedEvent()
```

### IsTouchFirstMoveEvent
```angelscript
bool IsTouchFirstMoveEvent()
```

### IsDirectionInvertedFromDevice
```angelscript
bool IsDirectionInvertedFromDevice()
```

### opAssign
```angelscript
FPointerEvent& opAssign(FPointerEvent Other)
```

