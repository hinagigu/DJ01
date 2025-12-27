# UAudioSliderBase

**继承自**: `UWidget`

An audio slider widget.

## 属性

### Value
- **类型**: `float32`
- **描述**: The normalized linear (0 - 1) slider value.

### IsUnitsTextReadOnly
- **类型**: `bool`
- **描述**: Whether to set the units part of the text label read only.

### IsValueTextReadOnly
- **类型**: `bool`
- **描述**: Whether to set the value part of the text label read only.

### Orientation
- **类型**: `EOrientation`

### OnValueChanged
- **类型**: `FOnFloatValueChangedEvent`

## 方法

### GetOutputValue
```angelscript
float32 GetOutputValue(float32 InSliderValue)
```
Get output value from normalized linear (0 - 1) based on internal lin to output mapping.

### GetSliderValue
```angelscript
float32 GetSliderValue(float32 OutputValue)
```
Get normalized linear (0 - 1) slider value from output based on internal lin to output mapping.

### SetShowLabelOnlyOnHover
```angelscript
void SetShowLabelOnlyOnHover(bool bShowLabelOnlyOnHover)
```
If true, show text label only on hover; if false always show label.

### SetShowUnitsText
```angelscript
void SetShowUnitsText(bool bShowUnitsText)
```
Sets whether to show the units text

### SetSliderBackgroundColor
```angelscript
void SetSliderBackgroundColor(FLinearColor InValue)
```
Sets the slider background color

### SetSliderBarColor
```angelscript
void SetSliderBarColor(FLinearColor InValue)
```
Sets the slider bar color

### SetSliderThumbColor
```angelscript
void SetSliderThumbColor(FLinearColor InValue)
```
Sets the slider thumb color

### SetTextLabelBackgroundColor
```angelscript
void SetTextLabelBackgroundColor(FSlateColor InColor)
```
Sets the label background color

### SetUnitsText
```angelscript
void SetUnitsText(FText Units)
```
Sets the units text

### SetUnitsTextReadOnly
```angelscript
void SetUnitsTextReadOnly(bool bIsReadOnly)
```
Sets whether the units text is read only

### SetValueTextReadOnly
```angelscript
void SetValueTextReadOnly(bool bIsReadOnly)
```
Sets whether the value text is read only

### SetWidgetBackgroundColor
```angelscript
void SetWidgetBackgroundColor(FLinearColor InValue)
```
Sets the widget background color

