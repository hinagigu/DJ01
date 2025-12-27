# USlider

**继承自**: `UWidget`

A simple widget that shows a sliding bar with a handle that allows you to control the value in a user define range (between 0..1 by default).

* No Children

## 属性

### WidgetStyle
- **类型**: `FSliderStyle`

### Orientation
- **类型**: `EOrientation`

### MouseUsesStep
- **类型**: `bool`

### RequiresControllerLock
- **类型**: `bool`

### IsFocusable
- **类型**: `bool`

### OnMouseCaptureBegin
- **类型**: `FOnMouseCaptureBeginEvent`

### OnMouseCaptureEnd
- **类型**: `FOnMouseCaptureEndEvent`

### OnControllerCaptureBegin
- **类型**: `FOnControllerCaptureBeginEvent`

### OnControllerCaptureEnd
- **类型**: `FOnControllerCaptureEndEvent`

### OnValueChanged
- **类型**: `FOnFloatValueChangedEvent`

### MinValue
- **类型**: `float32`

### MaxValue
- **类型**: `float32`

### SliderBarColor
- **类型**: `FLinearColor`

### SliderHandleColor
- **类型**: `FLinearColor`

### IndentHandle
- **类型**: `bool`

### Locked
- **类型**: `bool`

### StepSize
- **类型**: `float32`

## 方法

### GetNormalizedValue
```angelscript
float32 GetNormalizedValue()
```
Get the current value scaled from 0 to 1

### GetValue
```angelscript
float32 GetValue()
```
Gets the current value of the slider.

### SetIndentHandle
```angelscript
void SetIndentHandle(bool InValue)
```
Sets if the slidable area should be indented to fit the handle.

### SetLocked
```angelscript
void SetLocked(bool InValue)
```
Sets the handle to be interactive or fixed.

### SetMaxValue
```angelscript
void SetMaxValue(float32 InValue)
```
Sets the maximum value of the slider.

### SetMinValue
```angelscript
void SetMinValue(float32 InValue)
```
Sets the minimum value of the slider.

### SetSliderBarColor
```angelscript
void SetSliderBarColor(FLinearColor InValue)
```
Sets the color of the slider bar.

### SetSliderHandleColor
```angelscript
void SetSliderHandleColor(FLinearColor InValue)
```
Sets the color of the handle bar

### SetStepSize
```angelscript
void SetStepSize(float32 InValue)
```
Sets the amount to adjust the value by, when using a controller or keyboard.

### SetValue
```angelscript
void SetValue(float32 InValue)
```
Sets the current value of the slider.

