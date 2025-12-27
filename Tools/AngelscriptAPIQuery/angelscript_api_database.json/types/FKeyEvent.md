# FKeyEvent

FKeyEvent describes a key action (keyboard/controller key/button pressed or released.)
It is passed to event handlers dealing with key input.

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

### GetKey
```angelscript
FKey GetKey()
```

### GetCharacter
```angelscript
uint GetCharacter()
```

### GetKeyCode
```angelscript
uint GetKeyCode()
```

### opAssign
```angelscript
FKeyEvent& opAssign(FKeyEvent Other)
```

