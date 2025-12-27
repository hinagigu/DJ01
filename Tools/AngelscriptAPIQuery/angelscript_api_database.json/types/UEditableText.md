# UEditableText

**继承自**: `UWidget`

Editable text box widget

## 属性

### WidgetStyle
- **类型**: `FEditableTextStyle`

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
- **描述**: Additional options for the virtual keyboard

### VirtualKeyboardTrigger
- **类型**: `EVirtualKeyboardTrigger`

### VirtualKeyboardDismissAction
- **类型**: `EVirtualKeyboardDismissAction`
- **描述**: What action should be taken when the virtual keyboard is dismissed?

### ShapedTextOptions
- **类型**: `FShapedTextOptions`

### OnTextChanged
- **类型**: `FOnEditableTextChangedEvent__EditableText`

### OnTextCommitted
- **类型**: `FOnEditableTextCommittedEvent__EditableText`

### OverflowPolicy
- **类型**: `ETextOverflowPolicy`

### IsReadOnly
- **类型**: `bool`

### IsPassword
- **类型**: `bool`

### MinimumDesiredWidth
- **类型**: `float32`

## 方法

### GetFont
```angelscript
FSlateFontInfo GetFont()
```

### GetHintText
```angelscript
FText GetHintText()
```
Gets the Hint text that appears when there is no text in the text box

### GetJustification
```angelscript
ETextJustify GetJustification()
```

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

### SetIsPassword
```angelscript
void SetIsPassword(bool InbIsPassword)
```

### SetIsReadOnly
```angelscript
void SetIsReadOnly(bool InbIsReadyOnly)
```

### SetJustification
```angelscript
void SetJustification(ETextJustify InJustification)
```

### SetMinimumDesiredWidth
```angelscript
void SetMinimumDesiredWidth(float32 InMinDesiredWidth)
```
Set the minimum desired width for this text box

@param InMinDesiredWidth new minimum desired width

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

