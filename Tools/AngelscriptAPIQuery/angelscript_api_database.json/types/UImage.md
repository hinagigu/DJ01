# UImage

**继承自**: `UWidget`

The image widget allows you to display a Slate Brush, or texture or material in the UI.

* No Children

## 属性

### bFlipForRightToLeftFlowDirection
- **类型**: `bool`

### OnMouseButtonDownEvent
- **类型**: `FOnPointerEvent__Widget`

### Brush
- **类型**: `FSlateBrush`

### ColorAndOpacity
- **类型**: `FLinearColor`

## 方法

### GetDynamicMaterial
```angelscript
UMaterialInstanceDynamic GetDynamicMaterial()
```

### SetBrush
```angelscript
void SetBrush(FSlateBrush InBrush)
```

### SetBrushFromAsset
```angelscript
void SetBrushFromAsset(USlateBrushAsset Asset)
```

### SetBrushFromMaterial
```angelscript
void SetBrushFromMaterial(UMaterialInterface Material)
```

### SetBrushFromSoftMaterial
```angelscript
void SetBrushFromSoftMaterial(TSoftObjectPtr<UMaterialInterface> SoftMaterial)
```

### SetBrushFromSoftTexture
```angelscript
void SetBrushFromSoftTexture(TSoftObjectPtr<UTexture2D> SoftTexture, bool bMatchSize)
```
Sets the Brush to the specified Soft Texture.

  @param SoftTexture Soft Texture to use to set on Brush.
      @param bMatchSize If true, image will change its size to texture size. If false, texture will be stretched to image size.

### SetBrushFromTexture
```angelscript
void SetBrushFromTexture(UTexture2D Texture, bool bMatchSize)
```
Sets the Brush to the specified Texture.

  @param Texture Texture to use to set on Brush.
      @param bMatchSize If true, image will change its size to texture size. If false, texture will be stretched to image size.

### SetBrushFromTextureDynamic
```angelscript
void SetBrushFromTextureDynamic(UTexture2DDynamic Texture, bool bMatchSize)
```
Sets the Brush to the specified Dynamic Texture.

  @param Texture Dynamic Texture to use to set on Brush.
      @param bMatchSize If true, image will change its size to texture size. If false, texture will be stretched to image size.

### SetBrushResourceObject
```angelscript
void SetBrushResourceObject(UObject ResourceObject)
```

### SetBrushTintColor
```angelscript
void SetBrushTintColor(FSlateColor TintColor)
```

### SetColorAndOpacity
```angelscript
void SetColorAndOpacity(FLinearColor InColorAndOpacity)
```

### SetDesiredSizeOverride
```angelscript
void SetDesiredSizeOverride(FVector2D DesiredSize)
```

### SetOpacity
```angelscript
void SetOpacity(float32 InOpacity)
```

