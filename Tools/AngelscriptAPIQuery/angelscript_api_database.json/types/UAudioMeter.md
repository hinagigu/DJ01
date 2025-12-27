# UAudioMeter

**继承自**: `UWidget`

An audio meter widget.

Supports displaying a slower moving peak-hold value as well as the current meter value.

A clipping value is also displayed which shows a customizable color to indicate clipping.

Internal values are stored and interacted with as linear volume values.

## 属性

### WidgetStyle
- **类型**: `FAudioMeterStyle`

### Orientation
- **类型**: `EOrientation`

### BackgroundColor
- **类型**: `FLinearColor`

### MeterBackgroundColor
- **类型**: `FLinearColor`

### MeterValueColor
- **类型**: `FLinearColor`

### MeterPeakColor
- **类型**: `FLinearColor`

### MeterClippingColor
- **类型**: `FLinearColor`

### MeterScaleColor
- **类型**: `FLinearColor`

### MeterScaleLabelColor
- **类型**: `FLinearColor`

## 方法

### GetMeterChannelInfo
```angelscript
TArray<FMeterChannelInfo> GetMeterChannelInfo()
```
Gets the current linear value of the meter.

### SetBackgroundColor
```angelscript
void SetBackgroundColor(FLinearColor InValue)
```
Sets the background color

### SetMeterBackgroundColor
```angelscript
void SetMeterBackgroundColor(FLinearColor InValue)
```
Sets the meter background color

### SetMeterChannelInfo
```angelscript
void SetMeterChannelInfo(TArray<FMeterChannelInfo> InMeterChannelInfo)
```
Sets the current meter values.

### SetMeterClippingColor
```angelscript
void SetMeterClippingColor(FLinearColor InValue)
```
Sets the meter clipping color

### SetMeterPeakColor
```angelscript
void SetMeterPeakColor(FLinearColor InValue)
```
Sets the meter peak color

### SetMeterScaleColor
```angelscript
void SetMeterScaleColor(FLinearColor InValue)
```
Sets the meter scale color

### SetMeterScaleLabelColor
```angelscript
void SetMeterScaleLabelColor(FLinearColor InValue)
```
Sets the meter scale color

### SetMeterValueColor
```angelscript
void SetMeterValueColor(FLinearColor InValue)
```
Sets the meter value color

