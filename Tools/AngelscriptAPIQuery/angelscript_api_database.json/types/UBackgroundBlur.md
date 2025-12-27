# UBackgroundBlur

**继承自**: `UContentWidget`

A background blur is a container widget that can contain one child widget, providing an opportunity
to surround it with adjustable padding and apply a post-process Gaussian blur to all content beneath the widget.

* Single Child
* Blur Effect

## 属性

### bApplyAlphaToBlur
- **类型**: `bool`

### Padding
- **类型**: `FMargin`

### HorizontalAlignment
- **类型**: `EHorizontalAlignment`

### VerticalAlignment
- **类型**: `EVerticalAlignment`

### BlurStrength
- **类型**: `float32`

### BlurRadius
- **类型**: `int`

### CornerRadius
- **类型**: `FVector4`

### LowQualityFallbackBrush
- **类型**: `FSlateBrush`

## 方法

### SetApplyAlphaToBlur
```angelscript
void SetApplyAlphaToBlur(bool bInApplyAlphaToBlur)
```

### SetBlurRadius
```angelscript
void SetBlurRadius(int InBlurRadius)
```

### SetBlurStrength
```angelscript
void SetBlurStrength(float32 InStrength)
```

### SetCornerRadius
```angelscript
void SetCornerRadius(FVector4 InCornerRadius)
```

### SetHorizontalAlignment
```angelscript
void SetHorizontalAlignment(EHorizontalAlignment InHorizontalAlignment)
```

### SetLowQualityFallbackBrush
```angelscript
void SetLowQualityFallbackBrush(FSlateBrush InBrush)
```

### SetPadding
```angelscript
void SetPadding(FMargin InPadding)
```

### SetVerticalAlignment
```angelscript
void SetVerticalAlignment(EVerticalAlignment InVerticalAlignment)
```

