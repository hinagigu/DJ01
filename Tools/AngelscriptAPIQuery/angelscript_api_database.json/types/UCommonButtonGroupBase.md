# UCommonButtonGroupBase

**继承自**: `UCommonWidgetGroupBase`

Manages an arbitrary collection of CommonButton widgets.
Ensures that no more (and optionally, no less) than one button in the group is selected at a time

## 属性

### OnSelectedButtonBaseChanged
- **类型**: `FSimpleButtonBaseGroupDelegate`

### OnHoveredButtonBaseChanged
- **类型**: `FSimpleButtonBaseGroupDelegate`

### OnButtonBaseClicked
- **类型**: `FSimpleButtonBaseGroupDelegate`

### OnButtonBaseDoubleClicked
- **类型**: `FSimpleButtonBaseGroupDelegate`

### OnSelectionCleared
- **类型**: `FOnSelectionCleared`

### bSelectionRequired
- **类型**: `bool`

## 方法

### DeselectAll
```angelscript
void DeselectAll()
```
Deselects all buttons in the group.

### FindButtonIndex
```angelscript
int FindButtonIndex(const UCommonButtonBase ButtonToFind)
```
Find the button index of the specified button, if possible
@param ButtonToFind  Button to find the index of
@return Index of the button in the group. INDEX_NONE if not found

### GetButtonBaseAtIndex
```angelscript
UCommonButtonBase GetButtonBaseAtIndex(int Index)
```

### GetButtonCount
```angelscript
int GetButtonCount()
```

### GetHoveredButtonIndex
```angelscript
int GetHoveredButtonIndex()
```
Get the index of the currently hovered button, if any.
@param The index of the currently hovered button in the group, or -1 if there is no hovered button.

### GetSelectedButtonBase
```angelscript
UCommonButtonBase GetSelectedButtonBase()
```

### GetSelectedButtonIndex
```angelscript
int GetSelectedButtonIndex()
```
Get the index of the currently selected button, if any.
@param The index of the currently selected button in the group, or -1 if there is no selected button.

### HasAnyButtons
```angelscript
bool HasAnyButtons()
```

### SelectButtonAtIndex
```angelscript
void SelectButtonAtIndex(int ButtonIndex, bool bAllowSound)
```
Selects a button at a specific index in the group. Clears all selection if given an invalid index.
@param ButtonIndex The index of the button in the group to select
@param bAllowSound Whether the selected button should play its click sound

### SelectNextButton
```angelscript
void SelectNextButton(bool bAllowWrap)
```
Selects the next button in the group
@param bAllowWrap Whether to wrap to the first button if the last one is currently selected

### SelectPreviousButton
```angelscript
void SelectPreviousButton(bool bAllowWrap)
```
Selects the previous button in the group
@param bAllowWrap Whether to wrap to the first button if the last one is currently selected

### SetSelectionRequired
```angelscript
void SetSelectionRequired(bool bRequireSelection)
```
Sets whether the group should always have a button selected.
@param bRequireSelection True to force the group to always have a button selected.
If true and nothing is selected, will select the first entry. If empty, will select the first button added.

