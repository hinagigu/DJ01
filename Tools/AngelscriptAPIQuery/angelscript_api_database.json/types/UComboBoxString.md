# UComboBoxString

**继承自**: `UWidget`

The combobox allows you to display a list of options to the user in a dropdown menu for them to select one.

## 属性

### DefaultOptions
- **类型**: `TArray<FString>`
- **描述**: The default list of items to be displayed on the combobox.

### WidgetStyle
- **类型**: `FComboBoxStyle`

### ItemStyle
- **类型**: `FTableRowStyle`

### ScrollBarStyle
- **类型**: `FScrollBarStyle`

### ContentPadding
- **类型**: `FMargin`

### MaxListHeight
- **类型**: `float32`

### HasDownArrow
- **类型**: `bool`

### EnableGamepadNavigationMode
- **类型**: `bool`

### Font
- **类型**: `FSlateFontInfo`

### ForegroundColor
- **类型**: `FSlateColor`

### bIsFocusable
- **类型**: `bool`

### OnGenerateWidgetEvent
- **类型**: `FGenerateWidgetForString__Widget`
- **描述**: Called when the widget is needed for the item.

### OnSelectionChanged
- **类型**: `FOnSelectionChangedEvent__ComboBoxString`

### OnOpening
- **类型**: `FOnOpeningEvent__ComboBoxString`

## 方法

### AddOption
```angelscript
void AddOption(FString Option)
```

### ClearOptions
```angelscript
void ClearOptions()
```

### ClearSelection
```angelscript
void ClearSelection()
```

### FindOptionIndex
```angelscript
int FindOptionIndex(FString Option)
```

### GetOptionAtIndex
```angelscript
FString GetOptionAtIndex(int Index)
```

### GetOptionCount
```angelscript
int GetOptionCount()
```
Returns the number of options

### GetSelectedIndex
```angelscript
int GetSelectedIndex()
```

### GetSelectedOption
```angelscript
FString GetSelectedOption()
```

### IsOpen
```angelscript
bool IsOpen()
```

### RefreshOptions
```angelscript
void RefreshOptions()
```
Refreshes the list of options.  If you added new ones, and want to update the list even if it's
currently being displayed use this.

### RemoveOption
```angelscript
bool RemoveOption(FString Option)
```

### SetSelectedIndex
```angelscript
void SetSelectedIndex(int Index)
```

### SetSelectedOption
```angelscript
void SetSelectedOption(FString Option)
```

