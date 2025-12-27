# UPanelWidget

**继承自**: `UWidget`

The base class for all UMG panel widgets.  Panel widgets layout a collection of child widgets.

## 方法

### AddChild
```angelscript
UPanelSlot AddChild(UWidget Content)
```
Adds a new child widget to the container.  Returns the base slot type,
requires casting to turn it into the type specific to the container.

### ClearChildren
```angelscript
void ClearChildren()
```
Remove all child widgets from the panel widget.

### GetAllChildren
```angelscript
TArray<UWidget> GetAllChildren()
```
Gets all widgets in the container

### GetChildAt
```angelscript
UWidget GetChildAt(int Index)
```
Gets the widget at an index.
@param Index The index of the widget.
@return The widget at the given index, or nothing if there is no widget there.

### GetChildIndex
```angelscript
int GetChildIndex(const UWidget Content)
```
Gets the index of a specific child widget

### GetChildrenCount
```angelscript
int GetChildrenCount()
```
Gets number of child widgets in the container.

### HasAnyChildren
```angelscript
bool HasAnyChildren()
```
Returns true if there are any child widgets in the panel

### HasChild
```angelscript
bool HasChild(UWidget Content)
```
Returns true if panel contains this widget

### RemoveChild
```angelscript
bool RemoveChild(UWidget Content)
```
Removes a specific widget from the container.
@return true if the widget was found and removed.

### RemoveChildAt
```angelscript
bool RemoveChildAt(int Index)
```
Removes a child by it's index.

