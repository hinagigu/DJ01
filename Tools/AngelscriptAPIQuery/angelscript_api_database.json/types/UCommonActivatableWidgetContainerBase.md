# UCommonActivatableWidgetContainerBase

**继承自**: `UWidget`

Base of widgets built to manage N activatable widgets, displaying one at a time.
Intentionally meant to be black boxes that do not expose child/slot modification like a normal panel widget.

## 属性

### TransitionType
- **类型**: `ECommonSwitcherTransition`
- **描述**: The type of transition to play between widgets

### TransitionCurveType
- **类型**: `ETransitionCurve`
- **描述**: The curve function type to apply to the transition animation

### TransitionFallbackStrategy
- **类型**: `ECommonSwitcherTransitionFallbackStrategy`

## 方法

### AddWidget
```angelscript
UCommonActivatableWidget AddWidget(TSubclassOf<UCommonActivatableWidget> ActivatableWidgetClass)
```
Adds a widget of the given class to the container.
Note that all widgets added to the container are pooled, so the caller should not try to cache and re-use the created widget.

It is possible for multiple instances of the same class to be added to the container at once, so any instance created in the past
is not guaranteed to be the one returned this time.

So in practice, you should not trust that any prior state has been retained on the returned widget, and establish all appropriate properties every time.

### ClearWidgets
```angelscript
void ClearWidgets()
```

### GetActiveWidget
```angelscript
UCommonActivatableWidget GetActiveWidget()
```

### GetTransitionDuration
```angelscript
float32 GetTransitionDuration()
```

### RemoveWidget
```angelscript
void RemoveWidget(UCommonActivatableWidget WidgetToRemove)
```

### SetTransitionDuration
```angelscript
void SetTransitionDuration(float32 Duration)
```

