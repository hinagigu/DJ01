# UProgressBar

**继承自**: `UWidget`

The progress bar widget is a simple bar that fills up that can be restyled to fit any number of uses.

* No Children

## 属性

### WidgetStyle
- **类型**: `FProgressBarStyle`

### BarFillType
- **类型**: `EProgressBarFillType`

### BarFillStyle
- **类型**: `EProgressBarFillStyle`

### BorderPadding
- **类型**: `FVector2D`

### bIsMarquee
- **类型**: `bool`

### Percent
- **类型**: `float32`

### FillColorAndOpacity
- **类型**: `FLinearColor`

## 方法

### SetFillColorAndOpacity
```angelscript
void SetFillColorAndOpacity(FLinearColor InColor)
```
Sets the fill color of the progress bar.

### SetIsMarquee
```angelscript
void SetIsMarquee(bool InbIsMarquee)
```
Sets the progress bar to show as a marquee.

### SetPercent
```angelscript
void SetPercent(float32 InPercent)
```
Sets the current value of the ProgressBar.

