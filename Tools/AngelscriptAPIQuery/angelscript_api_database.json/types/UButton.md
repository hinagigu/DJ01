# UButton

**继承自**: `UContentWidget`

The button is a click-able primitive widget to enable basic interaction, you
can place any other widget inside a button to make a more complex and
interesting click-able element in your UI.

* Single Child
* Clickable

## 属性

### IsFocusable
- **类型**: `bool`

### OnClicked
- **类型**: `FOnButtonClickedEvent`

### OnPressed
- **类型**: `FOnButtonPressedEvent`

### OnReleased
- **类型**: `FOnButtonReleasedEvent`

### OnHovered
- **类型**: `FOnButtonHoverEvent`

### OnUnhovered
- **类型**: `FOnButtonHoverEvent`

### WidgetStyle
- **类型**: `FButtonStyle`

### ColorAndOpacity
- **类型**: `FLinearColor`

### BackgroundColor
- **类型**: `FLinearColor`

### ClickMethod
- **类型**: `EButtonClickMethod`

### TouchMethod
- **类型**: `EButtonTouchMethod`

### PressMethod
- **类型**: `EButtonPressMethod`

## 方法

### IsPressed
```angelscript
bool IsPressed()
```
Returns true if the user is actively pressing the button.  Do not use this for detecting 'Clicks', use the OnClicked event instead.

@return true if the user is actively pressing the button otherwise false.

### SetBackgroundColor
```angelscript
void SetBackgroundColor(FLinearColor InBackgroundColor)
```
Sets the color multiplier for the button background

### SetClickMethod
```angelscript
void SetClickMethod(EButtonClickMethod InClickMethod)
```

### SetColorAndOpacity
```angelscript
void SetColorAndOpacity(FLinearColor InColorAndOpacity)
```
Sets the color multiplier for the button content

### SetPressMethod
```angelscript
void SetPressMethod(EButtonPressMethod InPressMethod)
```

### SetStyle
```angelscript
void SetStyle(FButtonStyle InStyle)
```
Sets the color multiplier for the button background

### SetTouchMethod
```angelscript
void SetTouchMethod(EButtonTouchMethod InTouchMethod)
```

