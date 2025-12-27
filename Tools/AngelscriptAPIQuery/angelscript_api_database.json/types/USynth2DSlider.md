# USynth2DSlider

**继承自**: `UWidget`

A simple widget that shows a sliding bar with a handle that allows you to control the value between 0..1.

* No Children

## 属性

### ValueX
- **类型**: `float32`

### ValueY
- **类型**: `float32`

### WidgetStyle
- **类型**: `FSynth2DSliderStyle`

### IsFocusable
- **类型**: `bool`

### OnMouseCaptureBegin
- **类型**: `FOnMouseCaptureBeginEventSynth2D`

### OnMouseCaptureEnd
- **类型**: `FOnMouseCaptureEndEventSynth2D`

### OnControllerCaptureBegin
- **类型**: `FOnControllerCaptureBeginEventSynth2D`

### OnControllerCaptureEnd
- **类型**: `FOnControllerCaptureEndEventSynth2D`

### OnValueChangedX
- **类型**: `FOnFloatValueChangedEventSynth2D`

### OnValueChangedY
- **类型**: `FOnFloatValueChangedEventSynth2D`

### SliderHandleColor
- **类型**: `FLinearColor`

### IndentHandle
- **类型**: `bool`

### Locked
- **类型**: `bool`

### StepSize
- **类型**: `float32`

## 方法

### GetValue
```angelscript
FVector2D GetValue()
```
Gets the current value of the slider.

### SetIndentHandle
```angelscript
void SetIndentHandle(bool InValue)
```
Sets if the slidable area should be indented to fit the handle

### SetLocked
```angelscript
void SetLocked(bool InValue)
```
Sets the handle to be interactive or fixed

### SetSliderHandleColor
```angelscript
void SetSliderHandleColor(FLinearColor InValue)
```
Sets the color of the handle bar

### SetStepSize
```angelscript
void SetStepSize(float32 InValue)
```
Sets the amount to adjust the value by, when using a controller or keyboard

### SetValue
```angelscript
void SetValue(FVector2D InValue)
```
Sets the current value of the slider.

