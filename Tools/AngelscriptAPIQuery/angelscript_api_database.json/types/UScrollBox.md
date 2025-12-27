# UScrollBox

**继承自**: `UPanelWidget`

An arbitrary scrollable collection of widgets.  Great for presenting 10-100 widgets in a list.  Doesn't support virtualization.

## 属性

### WidgetStyle
- **类型**: `FScrollBoxStyle`

### WidgetBarStyle
- **类型**: `FScrollBarStyle`

### AlwaysShowScrollbarTrack
- **类型**: `bool`

### BackPadScrolling
- **类型**: `bool`

### FrontPadScrolling
- **类型**: `bool`

### NavigationScrollPadding
- **类型**: `float32`

### bAllowRightClickDragScrolling
- **类型**: `bool`

### OnUserScrolled
- **类型**: `FOnUserScrolledEvent`

### OnScrollBarVisibilityChanged
- **类型**: `FOnScrollBarVisibilityChangedEvent`

### bAnimateWheelScrolling
- **类型**: `bool`

### Orientation
- **类型**: `EOrientation`

### ScrollBarVisibility
- **类型**: `ESlateVisibility`

### ConsumeMouseWheel
- **类型**: `EConsumeMouseWheel`

### ScrollbarThickness
- **类型**: `FVector2D`

### ScrollbarPadding
- **类型**: `FMargin`

### AlwaysShowScrollbar
- **类型**: `bool`

### AllowOverscroll
- **类型**: `bool`

### NavigationDestination
- **类型**: `EDescendantScrollDestination`

### ScrollWhenFocusChanges
- **类型**: `EScrollWhenFocusChanges`

### WheelScrollMultiplier
- **类型**: `float32`

## 方法

### EndInertialScrolling
```angelscript
void EndInertialScrolling()
```
Instantly stops any inertial scrolling that is currently in progress

### GetScrollOffset
```angelscript
float32 GetScrollOffset()
```
Gets the scroll offset of the scrollbox in Slate Units.

### GetScrollOffsetOfEnd
```angelscript
float32 GetScrollOffsetOfEnd()
```
Gets the scroll offset of the bottom of the ScrollBox in Slate Units.

### GetViewFraction
```angelscript
float32 GetViewFraction()
```
Gets the fraction currently visible in the scrollbox

### GetViewOffsetFraction
```angelscript
float32 GetViewOffsetFraction()
```

### ScrollToEnd
```angelscript
void ScrollToEnd()
```
Scrolls the ScrollBox to the bottom instantly during the next layout pass.

### ScrollToStart
```angelscript
void ScrollToStart()
```
Scrolls the ScrollBox to the top instantly

### ScrollWidgetIntoView
```angelscript
void ScrollWidgetIntoView(UWidget WidgetToFind, bool AnimateScroll, EDescendantScrollDestination ScrollDestination, float32 Padding)
```
Scrolls the ScrollBox to the widget during the next layout pass.

### SetAllowOverscroll
```angelscript
void SetAllowOverscroll(bool NewAllowOverscroll)
```

### SetAlwaysShowScrollbar
```angelscript
void SetAlwaysShowScrollbar(bool NewAlwaysShowScrollbar)
```

### SetAnimateWheelScrolling
```angelscript
void SetAnimateWheelScrolling(bool bShouldAnimateWheelScrolling)
```

### SetConsumeMouseWheel
```angelscript
void SetConsumeMouseWheel(EConsumeMouseWheel NewConsumeMouseWheel)
```

### SetNavigationDestination
```angelscript
void SetNavigationDestination(EDescendantScrollDestination NewNavigationDestination)
```

### SetOrientation
```angelscript
void SetOrientation(EOrientation NewOrientation)
```

### SetScrollbarPadding
```angelscript
void SetScrollbarPadding(FMargin NewScrollbarPadding)
```

### SetScrollbarThickness
```angelscript
void SetScrollbarThickness(FVector2D NewScrollbarThickness)
```

### SetScrollBarVisibility
```angelscript
void SetScrollBarVisibility(ESlateVisibility NewScrollBarVisibility)
```

### SetScrollOffset
```angelscript
void SetScrollOffset(float32 NewScrollOffset)
```
Updates the scroll offset of the scrollbox.
@param NewScrollOffset is in Slate Units.

### SetScrollWhenFocusChanges
```angelscript
void SetScrollWhenFocusChanges(EScrollWhenFocusChanges NewScrollWhenFocusChanges)
```

### SetWheelScrollMultiplier
```angelscript
void SetWheelScrollMultiplier(float32 NewWheelScrollMultiplier)
```

