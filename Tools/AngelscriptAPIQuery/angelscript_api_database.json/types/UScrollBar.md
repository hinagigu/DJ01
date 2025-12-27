# UScrollBar

**继承自**: `UWidget`

## 属性

### WidgetStyle
- **类型**: `FScrollBarStyle`

### bAlwaysShowScrollbar
- **类型**: `bool`

### bAlwaysShowScrollbarTrack
- **类型**: `bool`

### Orientation
- **类型**: `EOrientation`

### Thickness
- **类型**: `FVector2D`

### Padding
- **类型**: `FMargin`

## 方法

### SetState
```angelscript
void SetState(float32 InOffsetFraction, float32 InThumbSizeFraction)
```
Set the offset and size of the track's thumb.
Note that the maximum offset is 1.0-ThumbSizeFraction.
If the user can view 1/3 of the items in a single page, the maximum offset will be ~0.667f

@param InOffsetFraction     Offset of the thumbnail from the top as a fraction of the total available scroll space.
@param InThumbSizeFraction  Size of thumbnail as a fraction of the total available scroll space.

