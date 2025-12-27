# UCommonAnimatedSwitcher

**继承自**: `UWidgetSwitcher`

A widget switcher that activates / deactivates CommonActivatableWidgets, allowing for associated animations to trigger.

## 属性

### OnActiveWidgetIndexChangedBP
- **类型**: `FOnActiveIndexChangedDelegate`

### TransitionType
- **类型**: `ECommonSwitcherTransition`

### TransitionCurveType
- **类型**: `ETransitionCurve`

### TransitionDuration
- **类型**: `float32`

### TransitionFallbackStrategy
- **类型**: `ECommonSwitcherTransitionFallbackStrategy`

## 方法

### ActivateNextWidget
```angelscript
void ActivateNextWidget(bool bCanWrap)
```

### ActivatePreviousWidget
```angelscript
void ActivatePreviousWidget(bool bCanWrap)
```

### HasWidgets
```angelscript
bool HasWidgets()
```

### IsCurrentlySwitching
```angelscript
bool IsCurrentlySwitching()
```

### IsTransitionPlaying
```angelscript
bool IsTransitionPlaying()
```
Is the switcher playing a transition animation?

### SetDisableTransitionAnimation
```angelscript
void SetDisableTransitionAnimation(bool bDisableAnimation)
```

