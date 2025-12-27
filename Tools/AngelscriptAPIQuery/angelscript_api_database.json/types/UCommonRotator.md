# UCommonRotator

**继承自**: `UCommonButtonBase`

A button that can rotate between given text labels.

## 属性

### OnRotatedWithDirection
- **类型**: `FOnRotatedWithDirection`

### OnRotated
- **类型**: `FOnRotated`

### MyText
- **类型**: `UCommonTextBlock`
- **描述**: The displayed text

## 方法

### OnOptionSelected
```angelscript
void OnOptionSelected(int Index)
```

### OnOptionsPopulated
```angelscript
void OnOptionsPopulated(int Count)
```

### GetSelectedIndex
```angelscript
int GetSelectedIndex()
```
Gets the current selected index

### GetSelectedText
```angelscript
FText GetSelectedText()
```
Gets the current text value of the slider.

### PopulateTextLabels
```angelscript
void PopulateTextLabels(TArray<FText> Labels)
```
Set the array of texts available

### SetSelectedItem
```angelscript
void SetSelectedItem(int InValue)
```
Sets the current value of the slider.

### ShiftTextLeft
```angelscript
void ShiftTextLeft()
```
Shift the current text left.

### ShiftTextRight
```angelscript
void ShiftTextRight()
```
Shift the current text right.

