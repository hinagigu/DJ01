# UCheckBox

**继承自**: `UContentWidget`

The checkbox widget allows you to display a toggled state of 'unchecked', 'checked' and
'indeterminable.  You can use the checkbox for a classic checkbox, or as a toggle button,
or as radio buttons.

* Single Child
* Toggle

## 属性

### WidgetStyle
- **类型**: `FCheckBoxStyle`

### HorizontalAlignment
- **类型**: `EHorizontalAlignment`

### IsFocusable
- **类型**: `bool`

### OnCheckStateChanged
- **类型**: `FOnCheckBoxComponentStateChanged`

### ClickMethod
- **类型**: `EButtonClickMethod`

### TouchMethod
- **类型**: `EButtonTouchMethod`

### PressMethod
- **类型**: `EButtonPressMethod`

## 方法

### GetCheckedState
```angelscript
ECheckBoxState GetCheckedState()
```
Returns the full current checked state.

### IsChecked
```angelscript
bool IsChecked()
```
Returns true if the checkbox is currently checked

### IsPressed
```angelscript
bool IsPressed()
```
Returns true if this button is currently pressed

### SetCheckedState
```angelscript
void SetCheckedState(ECheckBoxState InCheckedState)
```
Sets the checked state.

### SetClickMethod
```angelscript
void SetClickMethod(EButtonClickMethod InClickMethod)
```
Sets the click method.

### SetIsChecked
```angelscript
void SetIsChecked(bool InIsChecked)
```
Sets the checked state.

### SetPressMethod
```angelscript
void SetPressMethod(EButtonPressMethod InPressMethod)
```
Sets the press method.

### SetTouchMethod
```angelscript
void SetTouchMethod(EButtonTouchMethod InTouchMethod)
```
Sets the touch method.

