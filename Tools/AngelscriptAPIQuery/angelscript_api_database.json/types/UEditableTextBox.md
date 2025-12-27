# UEditableTextBox

**继承自**: `UWidget`

Allows the user to type in custom text.  Only permits a single line of text to be entered.

* No Children
* Text Entry

## 属性

### WidgetStyle
- **类型**: `FEditableTextBoxStyle`

### MinimumDesiredWidth
- **类型**: `float32`

### IsCaretMovedWhenGainFocus
- **类型**: `bool`

### SelectAllTextWhenFocused
- **类型**: `bool`

### RevertTextOnEscape
- **类型**: `bool`

### ClearKeyboardFocusOnCommit
- **类型**: `bool`

### SelectAllTextOnCommit
- **类型**: `bool`

### AllowContextMenu
- **类型**: `bool`
- **描述**: Whether the context menu can be opened

### KeyboardType
- **类型**: `EVirtualKeyboardType`
- **描述**: If we're on a platform that requires a virtual keyboard, what kind of keyboard should this widget use?

### VirtualKeyboardOptions
- **类型**: `FVirtualKeyboardOptions`
- **描述**: Additional options to use for the virtual keyboard summoned by this widget

### VirtualKeyboardTrigger
- **类型**: `EVirtualKeyboardTrigger`
- **描述**: The type of event that will trigger the display of the virtual keyboard

### VirtualKeyboardDismissAction
- **类型**: `EVirtualKeyboardDismissAction`
- **描述**: What action should be taken when the virtual keyboard is dismissed?

### ShapedTextOptions
- **类型**: `FShapedTextOptions`

### OnTextChanged
- **类型**: `FOnEditableTextBoxChangedEvent__EditableTextBox`

### OnTextCommitted
- **类型**: `FOnEditableTextBoxCommittedEvent__EditableTextBox`

### OverflowPolicy
- **类型**: `ETextOverflowPolicy`

### HintText
- **类型**: `FText`

### IsReadOnly
- **类型**: `bool`

### IsPassword
- **类型**: `bool`

### Justification
- **类型**: `ETextJustify`

## 方法

### ClearError
```angelscript
void ClearError()
```

### GetText
```angelscript
FText GetText()
```
Gets the widget text
@return The widget text

### HasError
```angelscript
bool HasError()
```

### SetError
```angelscript
void SetError(FText InError)
```

### SetForegroundColor
```angelscript
void SetForegroundColor(FLinearColor color)
```

### SetHintText
```angelscript
void SetHintText(FText InText)
```
Sets the Hint text that appears when there is no text in the text box
@param InHintText The text that appears when there is no text in the text box

### SetIsPassword
```angelscript
void SetIsPassword(bool bIsPassword)
```

### SetIsReadOnly
```angelscript
void SetIsReadOnly(bool bReadOnly)
```
Sets the Text as Readonly to prevent it from being modified interactively by the user

### SetJustification
```angelscript
void SetJustification(ETextJustify InJustification)
```

### SetText
```angelscript
void SetText(FText InText)
```
Directly sets the widget text.
Warning: This will wipe any binding created for the Text property!
@param InText The text to assign to the widget

### SetTextOverflowPolicy
```angelscript
void SetTextOverflowPolicy(ETextOverflowPolicy InOverflowPolicy)
```
Set the text overflow policy for this text box.

@param InOverflowPolicy the new text overflow policy.

