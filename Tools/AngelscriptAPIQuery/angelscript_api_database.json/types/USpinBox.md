# USpinBox

**继承自**: `UWidget`

A numerical entry box that allows for direct entry of the number or allows the user to click and slide the number.

## 属性

### WidgetStyle
- **类型**: `FSpinBoxStyle`

### bEnableSlider
- **类型**: `bool`

### SliderExponent
- **类型**: `float32`

### Font
- **类型**: `FSlateFontInfo`

### Justification
- **类型**: `ETextJustify`

### MinDesiredWidth
- **类型**: `float32`

### KeyboardType
- **类型**: `EVirtualKeyboardType`
- **描述**: If we're on a platform that requires a virtual keyboard, what kind of keyboard should this widget use?

### ClearKeyboardFocusOnCommit
- **类型**: `bool`

### SelectAllTextOnCommit
- **类型**: `bool`

### OnValueChanged
- **类型**: `FOnSpinBoxValueChangedEvent__SpinBox`

### OnValueCommitted
- **类型**: `FOnSpinBoxValueCommittedEvent__SpinBox`

### OnBeginSliderMovement
- **类型**: `FOnSpinBoxBeginSliderMovement__SpinBox`

### OnEndSliderMovement
- **类型**: `FOnSpinBoxValueChangedEvent__SpinBox`

### bAlwaysUsesDeltaSnap
- **类型**: `bool`

### ForegroundColor
- **类型**: `FSlateColor`

### bOverride_MinValue
- **类型**: `bool`

### bOverride_MaxValue
- **类型**: `bool`

### bOverride_MinSliderValue
- **类型**: `bool`

### bOverride_MaxSliderValue
- **类型**: `bool`

## 方法

### ClearMaxSliderValue
```angelscript
void ClearMaxSliderValue()
```
Clear the maximum value that can be specified using the slider.

### ClearMaxValue
```angelscript
void ClearMaxValue()
```
Clear the maximum value that can be manually set in the spin box.

### ClearMinSliderValue
```angelscript
void ClearMinSliderValue()
```
Clear the minimum value that can be specified using the slider.

### ClearMinValue
```angelscript
void ClearMinValue()
```
Clear the minimum value that can be manually set in the spin box.

### GetAlwaysUsesDeltaSnap
```angelscript
bool GetAlwaysUsesDeltaSnap()
```
Get whether the spin box uses delta snap on type.

### GetDelta
```angelscript
float32 GetDelta()
```
Get the current delta for the spin box.

### GetMaxFractionalDigits
```angelscript
int GetMaxFractionalDigits()
```
Get the current Max Fractional Digits for the spin box.

### GetMaxSliderValue
```angelscript
float32 GetMaxSliderValue()
```
Get the current maximum value that can be specified using the slider.

### GetMaxValue
```angelscript
float32 GetMaxValue()
```
Get the current maximum value that can be manually set in the spin box.

### GetMinFractionalDigits
```angelscript
int GetMinFractionalDigits()
```
Get the current Min Fractional Digits for the spin box.

### GetMinSliderValue
```angelscript
float32 GetMinSliderValue()
```
Get the current minimum value that can be specified using the slider.

### GetMinValue
```angelscript
float32 GetMinValue()
```
Get the current minimum value that can be manually set in the spin box.

### GetValue
```angelscript
float32 GetValue()
```
Get the current value of the spin box.

### SetAlwaysUsesDeltaSnap
```angelscript
void SetAlwaysUsesDeltaSnap(bool bNewValue)
```
Set whether the spin box uses delta snap on type.

### SetDelta
```angelscript
void SetDelta(float32 NewValue)
```
Set the delta for the spin box.

### SetForegroundColor
```angelscript
void SetForegroundColor(FSlateColor InForegroundColor)
```

### SetMaxFractionalDigits
```angelscript
void SetMaxFractionalDigits(int NewValue)
```
Set the Max Fractional Digits for the spin box.

### SetMaxSliderValue
```angelscript
void SetMaxSliderValue(float32 NewValue)
```
Set the maximum value that can be specified using the slider.

### SetMaxValue
```angelscript
void SetMaxValue(float32 NewValue)
```
Set the maximum value that can be manually set in the spin box.

### SetMinFractionalDigits
```angelscript
void SetMinFractionalDigits(int NewValue)
```
Set the Min Fractional Digits for the spin box.

### SetMinSliderValue
```angelscript
void SetMinSliderValue(float32 NewValue)
```
Set the minimum value that can be specified using the slider.

### SetMinValue
```angelscript
void SetMinValue(float32 NewValue)
```
Set the minimum value that can be manually set in the spin box.

### SetValue
```angelscript
void SetValue(float32 NewValue)
```
Set the value of the spin box.

