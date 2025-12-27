# USynthKnob

**继承自**: `UWidget`

A simple widget that shows a sliding bar with a handle that allows you to control the value between 0..1.

* No Children

## 属性

### MouseSpeed
- **类型**: `float32`

### MouseFineTuneSpeed
- **类型**: `float32`

### ParameterName
- **类型**: `FText`

### ParameterUnits
- **类型**: `FText`

### WidgetStyle
- **类型**: `FSynthKnobStyle`

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

### StepSize
- **类型**: `float32`

### ShowTooltipInfo
- **类型**: `bool`

### Locked
- **类型**: `bool`

## 方法

### GetValue
```angelscript
float32 GetValue()
```
Gets the current value of the slider.

### SetLocked
```angelscript
void SetLocked(bool InValue)
```
Sets the handle to be interactive or fixed

### SetStepSize
```angelscript
void SetStepSize(float32 InValue)
```
Sets the amount to adjust the value by, when using a controller or keyboard

### SetValue
```angelscript
void SetValue(float32 InValue)
```
Sets the current value of the slider.

