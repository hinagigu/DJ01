# FEventReply

Allows users to handle events and return information to the underlying UI layer.

## 方法

### PreventThrottling
```angelscript
FEventReply& PreventThrottling()
```

### SetUserFocus
```angelscript
FEventReply& SetUserFocus(UWidget Widget, EFocusCause FocusCause, bool bAllUsers)
```

### ClearUserFocus
```angelscript
FEventReply& ClearUserFocus(bool bAllUsers)
```

### CaptureMouse
```angelscript
FEventReply& CaptureMouse(UWidget Widget)
```

### UseHighPrecisionMouseMovement
```angelscript
FEventReply& UseHighPrecisionMouseMovement(UWidget Widget)
```

### ReleaseMouseCapture
```angelscript
FEventReply& ReleaseMouseCapture()
```

### LockMouseToWidget
```angelscript
FEventReply& LockMouseToWidget(UWidget Widget)
```

### ReleaseMouseLock
```angelscript
FEventReply& ReleaseMouseLock()
```

### SetMousePos
```angelscript
FEventReply& SetMousePos(FIntPoint NewMousePos)
```

### SetNavigation
```angelscript
FEventReply& SetNavigation(EUINavigation NavigationType, ENavigationGenesis Genesis, ENavigationSource Source)
```

### SetNavigation
```angelscript
FEventReply& SetNavigation(UWidget NavigationDestination, ENavigationGenesis Genesis, ENavigationSource Source)
```

### opAssign
```angelscript
FEventReply& opAssign(FEventReply Other)
```

