# USizeBox

**继承自**: `UContentWidget`

A widget that allows you to specify the size it reports to have and desire.  Not all widgets report a desired size
that you actually desire.  Wrapping them in a SizeBox lets you have the Size Box force them to be a particular size.

* Single Child
* Fixed Size

## 属性

### WidthOverride
- **类型**: `float32`

### HeightOverride
- **类型**: `float32`

### MinDesiredWidth
- **类型**: `float32`

### MinDesiredHeight
- **类型**: `float32`

### MaxDesiredWidth
- **类型**: `float32`

### MaxDesiredHeight
- **类型**: `float32`

### MinAspectRatio
- **类型**: `float32`

### MaxAspectRatio
- **类型**: `float32`

### bOverride_WidthOverride
- **类型**: `bool`

### bOverride_HeightOverride
- **类型**: `bool`

### bOverride_MinDesiredWidth
- **类型**: `bool`

### bOverride_MinDesiredHeight
- **类型**: `bool`

### bOverride_MaxDesiredWidth
- **类型**: `bool`

### bOverride_MaxDesiredHeight
- **类型**: `bool`

### bOverride_MinAspectRatio
- **类型**: `bool`

### bOverride_MaxAspectRatio
- **类型**: `bool`

## 方法

### ClearHeightOverride
```angelscript
void ClearHeightOverride()
```

### ClearMaxAspectRatio
```angelscript
void ClearMaxAspectRatio()
```

### ClearMaxDesiredHeight
```angelscript
void ClearMaxDesiredHeight()
```

### ClearMaxDesiredWidth
```angelscript
void ClearMaxDesiredWidth()
```

### ClearMinAspectRatio
```angelscript
void ClearMinAspectRatio()
```

### ClearMinDesiredHeight
```angelscript
void ClearMinDesiredHeight()
```

### ClearMinDesiredWidth
```angelscript
void ClearMinDesiredWidth()
```

### ClearWidthOverride
```angelscript
void ClearWidthOverride()
```

### SetHeightOverride
```angelscript
void SetHeightOverride(float32 InHeightOverride)
```
When specified, ignore the content's desired size and report the HeightOverride as the Box's desired height.

### SetMaxAspectRatio
```angelscript
void SetMaxAspectRatio(float32 InMaxAspectRatio)
```

### SetMaxDesiredHeight
```angelscript
void SetMaxDesiredHeight(float32 InMaxDesiredHeight)
```
When specified, will report the MaxDesiredHeight if smaller than the content's desired height.

### SetMaxDesiredWidth
```angelscript
void SetMaxDesiredWidth(float32 InMaxDesiredWidth)
```
When specified, will report the MaxDesiredWidth if smaller than the content's desired width.

### SetMinAspectRatio
```angelscript
void SetMinAspectRatio(float32 InMinAspectRatio)
```

### SetMinDesiredHeight
```angelscript
void SetMinDesiredHeight(float32 InMinDesiredHeight)
```
When specified, will report the MinDesiredHeight if larger than the content's desired height.

### SetMinDesiredWidth
```angelscript
void SetMinDesiredWidth(float32 InMinDesiredWidth)
```
When specified, will report the MinDesiredWidth if larger than the content's desired width.

### SetWidthOverride
```angelscript
void SetWidthOverride(float32 InWidthOverride)
```
When specified, ignore the content's desired size and report the WidthOverride as the Box's desired width.

