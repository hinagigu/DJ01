# UComboBoxKey

**继承自**: `UWidget`

The combobox allows you to display a list of options to the user in a dropdown menu for them to select one.
Use OnGenerateConentWidgetEvent to return a custom built widget.

## 属性

### Options
- **类型**: `TArray<FName>`

### WidgetStyle
- **类型**: `FComboBoxStyle`

### ItemStyle
- **类型**: `FTableRowStyle`

### ScrollBarStyle
- **类型**: `FScrollBarStyle`

### ForegroundColor
- **类型**: `FSlateColor`

### ContentPadding
- **类型**: `FMargin`

### MaxListHeight
- **类型**: `float32`

### bHasDownArrow
- **类型**: `bool`

### bEnableGamepadNavigationMode
- **类型**: `bool`

### bIsFocusable
- **类型**: `bool`

### OnGenerateContentWidget
- **类型**: `FGenerateWidgetEvent__ComboBoxKey`
- **描述**: Called when the widget is needed for the content.

### OnGenerateItemWidget
- **类型**: `FGenerateWidgetEvent__ComboBoxKey`
- **描述**: Called when the widget is needed for the item.

### OnSelectionChanged
- **类型**: `FOnSelectionChangedEvent__ComboBoxKey`

### OnOpening
- **类型**: `FOnOpeningEvent__ComboBoxKey`

## 方法

### AddOption
```angelscript
void AddOption(FName Option)
```
Add an element to the option list.

### ClearOptions
```angelscript
void ClearOptions()
```
Remove all the elements of the option list.

### ClearSelection
```angelscript
void ClearSelection()
```
Clear the current selection.

### GetSelectedOption
```angelscript
FName GetSelectedOption()
```
Get the current selected option

### IsOpen
```angelscript
bool IsOpen()
```
Is the combobox menu opened.

### RemoveOption
```angelscript
bool RemoveOption(FName Option)
```
Remove an element to the option list.

### SetSelectedOption
```angelscript
void SetSelectedOption(FName Option)
```
Set the current selected option.

