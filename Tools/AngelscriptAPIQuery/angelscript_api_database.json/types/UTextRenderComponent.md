# UTextRenderComponent

**继承自**: `UPrimitiveComponent`

Renders text in the world with given font. Contains usual font related attributes such as Scale, Alignment, Color etc.

## 属性

### Text
- **类型**: `FText`

### TextMaterial
- **类型**: `UMaterialInterface`

### Font
- **类型**: `UFont`

### HorizontalAlignment
- **类型**: `EHorizTextAligment`

### VerticalAlignment
- **类型**: `EVerticalTextAligment`

### TextRenderColor
- **类型**: `FColor`

### XScale
- **类型**: `float32`

### YScale
- **类型**: `float32`

### WorldSize
- **类型**: `float32`

### HorizSpacingAdjust
- **类型**: `float32`

### VertSpacingAdjust
- **类型**: `float32`

### bAlwaysRenderAsText
- **类型**: `bool`

## 方法

### GetTextLocalSize
```angelscript
FVector GetTextLocalSize()
```
Get local size of text

### GetTextWorldSize
```angelscript
FVector GetTextWorldSize()
```
Get world space size of text

### SetText
```angelscript
void SetText(FText Value)
```
Change the text value and signal the primitives to be rebuilt

### SetFont
```angelscript
void SetFont(UFont Value)
```
Change the font and signal the primitives to be rebuilt

### SetHorizontalAlignment
```angelscript
void SetHorizontalAlignment(EHorizTextAligment Value)
```
Change the horizontal alignment and signal the primitives to be rebuilt

### SetHorizSpacingAdjust
```angelscript
void SetHorizSpacingAdjust(float32 Value)
```
Change the text horizontal spacing adjustment and signal the primitives to be rebuilt

### SetTextMaterial
```angelscript
void SetTextMaterial(UMaterialInterface Material)
```
Change the text material and signal the primitives to be rebuilt

### SetTextRenderColor
```angelscript
void SetTextRenderColor(FColor Value)
```
Change the text render color and signal the primitives to be rebuilt

### SetVerticalAlignment
```angelscript
void SetVerticalAlignment(EVerticalTextAligment Value)
```
Change the vertical alignment and signal the primitives to be rebuilt

### SetVertSpacingAdjust
```angelscript
void SetVertSpacingAdjust(float32 Value)
```
Change the text vertical spacing adjustment and signal the primitives to be rebuilt

### SetWorldSize
```angelscript
void SetWorldSize(float32 Value)
```
Change the world size of the text and signal the primitives to be rebuilt

### SetXScale
```angelscript
void SetXScale(float32 Value)
```
Change the text X scale and signal the primitives to be rebuilt

### SetYScale
```angelscript
void SetYScale(float32 Value)
```
Change the text Y scale and signal the primitives to be rebuilt

