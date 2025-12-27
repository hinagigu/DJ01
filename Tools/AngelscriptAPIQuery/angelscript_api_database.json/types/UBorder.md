# UBorder

**继承自**: `UContentWidget`

A border is a container widget that can contain one child widget, providing an opportunity
to surround it with a background image and adjustable padding.

* Single Child
* Image

## 属性

### Background
- **类型**: `FSlateBrush`

### bFlipForRightToLeftFlowDirection
- **类型**: `bool`
- **描述**: Flips the background image if the localization's flow direction is RightToLeft

### OnMouseButtonDownEvent
- **类型**: `FOnPointerEvent__Widget`

### OnMouseButtonUpEvent
- **类型**: `FOnPointerEvent__Widget`

### OnMouseMoveEvent
- **类型**: `FOnPointerEvent__Widget`

### OnMouseDoubleClickEvent
- **类型**: `FOnPointerEvent__Widget`

### bShowEffectWhenDisabled
- **类型**: `bool`

### HorizontalAlignment
- **类型**: `EHorizontalAlignment`

### VerticalAlignment
- **类型**: `EVerticalAlignment`

### ContentColorAndOpacity
- **类型**: `FLinearColor`

### Padding
- **类型**: `FMargin`

### BrushColor
- **类型**: `FLinearColor`

### DesiredSizeScale
- **类型**: `FVector2D`

## 方法

### GetDynamicMaterial
```angelscript
UMaterialInstanceDynamic GetDynamicMaterial()
```

### SetBrush
```angelscript
void SetBrush(FSlateBrush InBrush)
```

### SetBrushColor
```angelscript
void SetBrushColor(FLinearColor InBrushColor)
```

### SetBrushFromAsset
```angelscript
void SetBrushFromAsset(USlateBrushAsset Asset)
```

### SetBrushFromMaterial
```angelscript
void SetBrushFromMaterial(UMaterialInterface Material)
```

### SetBrushFromTexture
```angelscript
void SetBrushFromTexture(UTexture2D Texture)
```

### SetContentColorAndOpacity
```angelscript
void SetContentColorAndOpacity(FLinearColor InContentColorAndOpacity)
```

### SetDesiredSizeScale
```angelscript
void SetDesiredSizeScale(FVector2D InScale)
```
Sets the DesiredSizeScale of this border.

@param InScale    The X and Y multipliers for the desired size

### SetHorizontalAlignment
```angelscript
void SetHorizontalAlignment(EHorizontalAlignment InHorizontalAlignment)
```

### SetPadding
```angelscript
void SetPadding(FMargin InPadding)
```

### SetShowEffectWhenDisabled
```angelscript
void SetShowEffectWhenDisabled(bool bInShowEffectWhenDisabled)
```

### SetVerticalAlignment
```angelscript
void SetVerticalAlignment(EVerticalAlignment InVerticalAlignment)
```

