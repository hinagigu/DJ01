# UScaleBox

**继承自**: `UContentWidget`

Allows you to place content with a desired size and have it scale to meet the constraints placed on this box's alloted area.  If
you needed to have a background image scale to fill an area but not become distorted with different aspect ratios, or if you need
to auto fit some text to an area, this is the control for you.

* Single Child
* Aspect Ratio

## 属性

### Stretch
- **类型**: `EStretch`

### StretchDirection
- **类型**: `EStretchDirection`

### UserSpecifiedScale
- **类型**: `float32`

### IgnoreInheritedScale
- **类型**: `bool`

## 方法

### SetIgnoreInheritedScale
```angelscript
void SetIgnoreInheritedScale(bool bInIgnoreInheritedScale)
```

### SetStretch
```angelscript
void SetStretch(EStretch InStretch)
```

### SetStretchDirection
```angelscript
void SetStretchDirection(EStretchDirection InStretchDirection)
```

### SetUserSpecifiedScale
```angelscript
void SetUserSpecifiedScale(float32 InUserSpecifiedScale)
```

