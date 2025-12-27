# UCommonWidgetCarousel

**继承自**: `UPanelWidget`

A widget switcher is like a tab control, but without tabs. At most one widget is visible at time.

## 属性

### OnCurrentPageIndexChanged
- **类型**: `FOnCurrentPageIndexChanged`

## 方法

### BeginAutoScrolling
```angelscript
void BeginAutoScrolling(float32 ScrollInterval)
```

### EndAutoScrolling
```angelscript
void EndAutoScrolling()
```

### GetActiveWidgetIndex
```angelscript
int GetActiveWidgetIndex()
```
Gets the slot index of the currently active widget

### GetMoveSpeed
```angelscript
float32 GetMoveSpeed()
```
Gets the Move Speed.

### GetWidgetAtIndex
```angelscript
UWidget GetWidgetAtIndex(int Index)
```
Get a widget at the provided index

### NextPage
```angelscript
void NextPage()
```

### PreviousPage
```angelscript
void PreviousPage()
```

### SetActiveWidget
```angelscript
void SetActiveWidget(UWidget Widget)
```
Activates the widget and makes it the active index.

### SetActiveWidgetIndex
```angelscript
void SetActiveWidgetIndex(int Index)
```
Activates the widget at the specified index.

### SetMoveSpeed
```angelscript
void SetMoveSpeed(float32 InMoveSpeed)
```
Sets the Move Speed.

