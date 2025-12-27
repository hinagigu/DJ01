# UStackBox

**继承自**: `UPanelWidget`

A stack box widget is a layout panel allowing child widgets to be automatically laid out
vertically or horizontally.

* Many Children
* Flows Vertical or Horizontal

## 属性

### Orientation
- **类型**: `EOrientation`

## 方法

### AddChildToStackBox
```angelscript
UStackBoxSlot AddChildToStackBox(UWidget Content)
```
Adds a new child widget to the container.

### ReplaceStackBoxChildAt
```angelscript
bool ReplaceStackBoxChildAt(int Index, UWidget Content)
```
Replace the widget at the given index it with a different widget.

