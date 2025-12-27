# URadialSlider

**继承自**: `UWidget`

A simple widget that shows a sliding bar with a handle that allows you to control the value between 0..1.

* No Children

## 属性

### bUseCustomDefaultValue
- **类型**: `bool`
- **描述**: Whether the slider should draw it's progress bar from a custom value on the slider

### WidgetStyle
- **类型**: `FSliderStyle`

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

### SliderRange
- **类型**: `FRuntimeFloatCurve`

### ValueTags
- **类型**: `TArray<float32>`

### SliderHandleStartAngle
- **类型**: `float32`

### SliderHandleEndAngle
- **类型**: `float32`

### AngularOffset
- **类型**: `float32`

### HandStartEndRatio
- **类型**: `FVector2D`

### SliderBarColor
- **类型**: `FLinearColor`

### SliderProgressColor
- **类型**: `FLinearColor`

### SliderHandleColor
- **类型**: `FLinearColor`

### CenterBackgroundColor
- **类型**: `FLinearColor`

### Locked
- **类型**: `bool`

### StepSize
- **类型**: `float32`

### UseVerticalDrag
- **类型**: `bool`

### ShowSliderHandle
- **类型**: `bool`

### ShowSliderHand
- **类型**: `bool`

## 方法

### GetCustomDefaultValue
```angelscript
float32 GetCustomDefaultValue()
```
Gets the current custom default value of the slider.

### GetNormalizedSliderHandlePosition
```angelscript
float32 GetNormalizedSliderHandlePosition()
```
Get the current raw slider alpha from 0 to 1

### GetValue
```angelscript
float32 GetValue()
```
Gets the current value of the slider.

### SetAngularOffset
```angelscript
void SetAngularOffset(float32 InValue)
```
Sets the Angular Offset for the slider.

### SetCenterBackgroundColor
```angelscript
void SetCenterBackgroundColor(FLinearColor InValue)
```
Sets the color of the slider bar

### SetCustomDefaultValue
```angelscript
void SetCustomDefaultValue(float32 InValue)
```
Sets the current custom default value of the slider.

### SetHandStartEndRatio
```angelscript
void SetHandStartEndRatio(FVector2D InValue)
```
Sets the start and end of the hand as a ratio to the slider radius (so 0.0 to 1.0 is from the slider center to the handle).

### SetLocked
```angelscript
void SetLocked(bool InValue)
```
Sets the handle to be interactive or fixed

### SetShowSliderHand
```angelscript
void SetShowSliderHand(bool InShowSliderHand)
```
Whether to show the slider hand.

### SetShowSliderHandle
```angelscript
void SetShowSliderHandle(bool InShowSliderHandle)
```
Whether to show the slider handle (thumb).

### SetSliderBarColor
```angelscript
void SetSliderBarColor(FLinearColor InValue)
```
Sets the color of the slider bar

### SetSliderHandleColor
```angelscript
void SetSliderHandleColor(FLinearColor InValue)
```
Sets the color of the handle bar

### SetSliderHandleEndAngle
```angelscript
void SetSliderHandleEndAngle(float32 InValue)
```
Sets the maximum angle of the slider.

### SetSliderHandleStartAngle
```angelscript
void SetSliderHandleStartAngle(float32 InValue)
```
Sets the minimum angle of the slider.

### SetSliderProgressColor
```angelscript
void SetSliderProgressColor(FLinearColor InValue)
```
Sets the progress color of the slider bar

### SetSliderRange
```angelscript
void SetSliderRange(FRuntimeFloatCurve InSliderRange)
```
Sets the curve for the slider range

### SetStepSize
```angelscript
void SetStepSize(float32 InValue)
```
Sets the amount to adjust the value by, when using a controller or keyboard

### SetUseVerticalDrag
```angelscript
void SetUseVerticalDrag(bool InUseVerticalDrag)
```
Set whether the value is changed when dragging vertically as opposed to along the radial curve.

### SetValue
```angelscript
void SetValue(float32 InValue)
```
Sets the current value of the slider.

### SetValueTags
```angelscript
void SetValueTags(TArray<float32> InValueTags)
```
Adds value tags to the slider.

