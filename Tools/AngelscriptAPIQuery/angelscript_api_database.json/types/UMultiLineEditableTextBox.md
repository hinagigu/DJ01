# UMultiLineEditableTextBox

**继承自**: `UTextLayoutWidget`

Allows a user to enter multiple lines of text

## 属性

### WidgetStyle
- **类型**: `FEditableTextBoxStyle`

### bIsReadOnly
- **类型**: `bool`

### AllowContextMenu
- **类型**: `bool`
- **描述**: Whether the context menu can be opened

### VirtualKeyboardOptions
- **类型**: `FVirtualKeyboardOptions`
- **描述**: Additional options to be used by the virtual keyboard summoned from this widget

### VirtualKeyboardDismissAction
- **类型**: `EVirtualKeyboardDismissAction`
- **描述**: What action should be taken when the virtual keyboard is dismissed?

### OnTextChanged
- **类型**: `FOnMultiLineEditableTextBoxChangedEvent__MultiLineEditableTextBox`

### OnTextCommitted
- **类型**: `FOnMultiLineEditableTextBoxCommittedEvent__MultiLineEditableTextBox`

## 方法

### GetHintText
```angelscript
FText GetHintText()
```
Returns the Hint text that appears when there is no text in the text box

### GetText
```angelscript
FText GetText()
```
Gets the widget text
@return The widget text

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
void SetHintText(FText InHintText)
```
Sets the Hint text that appears when there is no text in the text box
@param InHintText The text that appears when there is no text in the text box

### SetIsReadOnly
```angelscript
void SetIsReadOnly(bool bReadOnly)
```
Sets the Text as Readonly to prevent it from being modified interactively by the user

### SetText
```angelscript
void SetText(FText InText)
```
Directly sets the widget text.
Warning: This will wipe any binding created for the Text property!
@param InText The text to assign to the widget

### SetTextStyle
```angelscript
void SetTextStyle(FTextBlockStyle InTextStyle)
```

