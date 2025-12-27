# UCommonNumericTextBlock

**继承自**: `UCommonTextBlock`

Numeric text block that provides interpolation, and some type support (numbers, percents, seconds, distance).

## 属性

### OnInterpolationStartedEvent
- **类型**: `FOnInterpolationStarted__CommonNumericTextBlock`

### OnInterpolationUpdatedEvent
- **类型**: `FOnInterpolationUpdated__CommonNumericTextBlock`

### OnOutroEvent
- **类型**: `FOnOutro__CommonNumericTextBlock`

### OnInterpolationEndedEvent
- **类型**: `FOnInterpolationEnded__CommonNumericTextBlock`

### CurrentNumericValue
- **类型**: `float32`

### FormattingSpecification
- **类型**: `FCommonNumberFormattingOptions`

### EaseOutInterpolationExponent
- **类型**: `float32`

### InterpolationUpdateInterval
- **类型**: `float32`

### PostInterpolationShrinkDuration
- **类型**: `float32`

### PerformSizeInterpolation
- **类型**: `bool`

### NumericType
- **类型**: `ECommonNumericType`

## 方法

### GetTargetValue
```angelscript
float32 GetTargetValue()
```
Returns the value this widget will ultimately show if it is interpolating, or the current value if it is not.

### InterpolateToValue
```angelscript
void InterpolateToValue(float32 TargetValue, float32 MaximumInterpolationDuration, float32 MinimumChangeRate, float32 OutroOffset)
```
Starts an ongoing process of interpolating the current numeric value to the specified target value.
The interpolation process may take the specified maximum duration or complete sooner if the minimum change rate causes the target to be reached prematurely.
Optionally, an outro duration can be specified in order to trigger an outro event before interpolation completes.

TargetValue                                  The value to be interpolated to.
MaximumInterpolationDuration The duration, in seconds, for the interpolation to take, at most. Must be greater than 0.
MinimumChangeRate                    The minimum change in numeric value per second. Must be greater than or equal to 0.
OutroDuration                                The time offset, in seconds, *before* the end of the InterpolationDuration elapses, at which to trigger an outro event. Must be less than or equal to MaximumInterpolationDuration

### IsInterpolatingNumericValue
```angelscript
bool IsInterpolatingNumericValue()
```

### SetCurrentValue
```angelscript
void SetCurrentValue(float32 NewValue)
```
Sets the current numeric value. NOTE: Cancels any ongoing interpolation!

### SetNumericType
```angelscript
void SetNumericType(ECommonNumericType InNumericType)
```

