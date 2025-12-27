# UWidgetSwitcher

**继承自**: `UPanelWidget`

A widget switcher is like a tab control, but without tabs. At most one widget is visible at time.

## 方法

### GetActiveWidget
```angelscript
UWidget GetActiveWidget()
```
Get the reference of the currently active widget

### GetActiveWidgetIndex
```angelscript
int GetActiveWidgetIndex()
```
Gets the slot index of the currently active widget

### GetNumWidgets
```angelscript
int GetNumWidgets()
```
Gets the number of widgets that this switcher manages.

### GetWidgetAtIndex
```angelscript
UWidget GetWidgetAtIndex(int Index)
```
Get a widget at the provided index

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

