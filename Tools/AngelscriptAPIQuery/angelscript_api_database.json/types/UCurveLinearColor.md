# UCurveLinearColor

**继承自**: `UCurveBase`

## 属性

### FloatCurves
- **类型**: `FRichCurve`
- **描述**: Keyframe data, one curve for red, green, blue, and alpha

### AdjustHue
- **类型**: `float32`
- **描述**: Properties for adjusting the color of the gradient

### AdjustSaturation
- **类型**: `float32`

### AdjustBrightness
- **类型**: `float32`

### AdjustBrightnessCurve
- **类型**: `float32`

### AdjustVibrance
- **类型**: `float32`

### AdjustMinAlpha
- **类型**: `float32`

### AdjustMaxAlpha
- **类型**: `float32`

## 方法

### GetClampedLinearColorValue
```angelscript
FLinearColor GetClampedLinearColorValue(float32 InTime)
```

### GetLinearColorValue
```angelscript
FLinearColor GetLinearColorValue(float32 InTime)
```

### GetUnadjustedLinearColorValue
```angelscript
FLinearColor GetUnadjustedLinearColorValue(float32 InTime)
```

