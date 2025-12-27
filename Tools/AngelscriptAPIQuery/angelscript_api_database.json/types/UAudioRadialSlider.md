# UAudioRadialSlider

**继承自**: `UWidget`

An audio radial slider widget.

## 属性

### Value
- **类型**: `float32`
- **描述**: The normalized linear (0 - 1) slider value position.

### IsUnitsTextReadOnly
- **类型**: `bool`
- **描述**: Whether to set the units part of the text label read only.

### IsValueTextReadOnly
- **类型**: `bool`
- **描述**: Whether to set the value part of the text label read only.

### OnValueChanged
- **类型**: `FOnAudioRadialSliderValueChangedEvent`

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

### SetCenterBackgroundColor
```angelscript
void SetCenterBackgroundColor(FLinearColor InValue)
```
Sets the label background color

### SetHandStartEndRatio
```angelscript
void SetHandStartEndRatio(FVector2D InHandStartEndRatio)
```
Sets the start and end of the hand as a ratio to the slider radius (so 0.0 to 1.0 is from the slider center to the handle).

### SetOutputRange
```angelscript
void SetOutputRange(FVector2D InOutputRange)
```
Sets the output range

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

### SetSliderBarColor
```angelscript
void SetSliderBarColor(FLinearColor InValue)
```
Sets the slider bar color

### SetSliderProgressColor
```angelscript
void SetSliderProgressColor(FLinearColor InValue)
```
Sets the slider progress color

### SetSliderThickness
```angelscript
void SetSliderThickness(float32 InThickness)
```
Sets the slider thickness

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

### SetWidgetLayout
```angelscript
void SetWidgetLayout(EAudioRadialSliderLayout InLayout)
```
Sets the widget layout

