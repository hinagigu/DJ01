# UMultiLineEditableText

**继承自**: `UTextLayoutWidget`

Editable text box widget

## 属性

### SelectAllTextWhenFocused
- **类型**: `bool`

### ClearTextSelectionOnFocusLoss
- **类型**: `bool`
- **描述**: Whether to clear text selection when focus is lost

### RevertTextOnEscape
- **类型**: `bool`

### ClearKeyboardFocusOnCommit
- **类型**: `bool`

### AllowContextMenu
- **类型**: `bool`
- **描述**: Whether the context menu can be opened

### VirtualKeyboardOptions
- **类型**: `FVirtualKeyboardOptions`
- **描述**: Additional options for the virtual keyboard

### VirtualKeyboardDismissAction
- **类型**: `EVirtualKeyboardDismissAction`
- **描述**: What action should be taken when the virtual keyboard is dismissed?

### OnTextChanged
- **类型**: `FOnMultiLineEditableTextChangedEvent__MultiLineEditableText`

### OnTextCommitted
- **类型**: `FOnMultiLineEditableTextCommittedEvent__MultiLineEditableText`

### bIsReadOnly
- **类型**: `bool`

### WidgetStyle
- **类型**: `FTextBlockStyle`

## 方法

### GetFont
```angelscript
FSlateFontInfo GetFont()
```

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

### SetFont
```angelscript
void SetFont(FSlateFontInfo InFontInfo)
```

### SetFontMaterial
```angelscript
void SetFontMaterial(UMaterialInterface InMaterial)
```

### SetFontOutlineMaterial
```angelscript
void SetFontOutlineMaterial(UMaterialInterface InMaterial)
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
@param InText The text to assign to the widget

### SetWidgetStyle
```angelscript
void SetWidgetStyle(FTextBlockStyle InWidgetStyle)
```

