# UInputKeySelector

**继承自**: `UWidget`

A widget for selecting a single key or a single key with a modifier.

## 属性

### WidgetStyle
- **类型**: `FButtonStyle`

### TextStyle
- **类型**: `FTextBlockStyle`

### Margin
- **类型**: `FMargin`

### OnKeySelected
- **类型**: `FOnKeySelected__InputKeySelector`

### OnIsSelectingKeyChanged
- **类型**: `FOnIsSelectingKeyChanged__InputKeySelector`

### bAllowModifierKeys
- **类型**: `bool`

### bAllowGamepadKeys
- **类型**: `bool`

### SelectedKey
- **类型**: `FInputChord`

### KeySelectionText
- **类型**: `FText`

### NoKeySpecifiedText
- **类型**: `FText`

### EscapeKeys
- **类型**: `TArray<FKey>`

## 方法

### GetIsSelectingKey
```angelscript
bool GetIsSelectingKey()
```
Returns true if the widget is currently selecting a key, otherwise returns false.

### SetAllowGamepadKeys
```angelscript
void SetAllowGamepadKeys(bool bInAllowGamepadKeys)
```
Sets whether or not gamepad keys are allowed in the selected key.

### SetAllowModifierKeys
```angelscript
void SetAllowModifierKeys(bool bInAllowModifierKeys)
```
Sets whether or not modifier keys are allowed in the selected key.

### SetEscapeKeys
```angelscript
void SetEscapeKeys(TArray<FKey> InKeys)
```
Sets escape keys.

### SetKeySelectionText
```angelscript
void SetKeySelectionText(FText InKeySelectionText)
```
Sets the text which is displayed while selecting keys.

### SetNoKeySpecifiedText
```angelscript
void SetNoKeySpecifiedText(FText InNoKeySpecifiedText)
```
Sets the text to display when no key text is available or not selecting a key.

### SetSelectedKey
```angelscript
void SetSelectedKey(FInputChord InSelectedKey)
```
Sets the currently selected key.

### SetTextBlockVisibility
```angelscript
void SetTextBlockVisibility(ESlateVisibility InVisibility)
```
Sets the visibility of the text block.

