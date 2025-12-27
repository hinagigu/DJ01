# UTextBlock

**继承自**: `UTextLayoutWidget`

A simple static text widget.

* No Children
* Text

## 属性

### bWrapWithInvalidationPanel
- **类型**: `bool`

### bSimpleTextMode
- **类型**: `bool`

### ColorAndOpacity
- **类型**: `FSlateColor`

### Font
- **类型**: `FSlateFontInfo`

### StrikeBrush
- **类型**: `FSlateBrush`

### ShadowOffset
- **类型**: `FVector2D`

### ShadowColorAndOpacity
- **类型**: `FLinearColor`

### MinDesiredWidth
- **类型**: `float32`

### TextTransformPolicy
- **类型**: `ETextTransformPolicy`

### TextOverflowPolicy
- **类型**: `ETextOverflowPolicy`

## 方法

### GetDynamicFontMaterial
```angelscript
UMaterialInstanceDynamic GetDynamicFontMaterial()
```

### GetDynamicOutlineMaterial
```angelscript
UMaterialInstanceDynamic GetDynamicOutlineMaterial()
```

### GetText
```angelscript
FText GetText()
```
Gets the widget text
@return The widget text

### SetAutoWrapText
```angelscript
void SetAutoWrapText(bool InAutoTextWrap)
```
Set the auto wrap for this text block.

@param InAutoTextWrap to turn wrap on or off.

### SetColorAndOpacity
```angelscript
void SetColorAndOpacity(FSlateColor InColorAndOpacity)
```
Sets the color and opacity of the text in this text block

@param InColorAndOpacity             The new text color and opacity

### SetFont
```angelscript
void SetFont(FSlateFontInfo InFontInfo)
```
Dynamically set the font info for this text block

@param InFontInfo The new font info

### SetFontMaterial
```angelscript
void SetFontMaterial(UMaterialInterface InMaterial)
```

### SetFontOutlineMaterial
```angelscript
void SetFontOutlineMaterial(UMaterialInterface InMaterial)
```

### SetMinDesiredWidth
```angelscript
void SetMinDesiredWidth(float32 InMinDesiredWidth)
```
Set the minimum desired width for this text block

@param InMinDesiredWidth new minimum desired width

### SetOpacity
```angelscript
void SetOpacity(float32 InOpacity)
```
Sets the opacity of the text in this text block

@param InOpacity              The new text opacity

### SetShadowColorAndOpacity
```angelscript
void SetShadowColorAndOpacity(FLinearColor InShadowColorAndOpacity)
```
Sets the color and opacity of the text drop shadow
Note: if opacity is zero no shadow will be drawn

@param InShadowColorAndOpacity               The new drop shadow color and opacity

### SetShadowOffset
```angelscript
void SetShadowOffset(FVector2D InShadowOffset)
```
Sets the offset that the text drop shadow should be drawn at

@param InShadowOffset                The new offset

### SetStrikeBrush
```angelscript
void SetStrikeBrush(FSlateBrush InStrikeBrush)
```
Dynamically set the strike brush for this text block

@param InStrikeBrush The new brush to use to strike through text

### SetText
```angelscript
void SetText(FText InText)
```
Directly sets the widget text.
Warning: This will wipe any binding created for the Text property!
@param InText The text to assign to the widget

### SetTextOverflowPolicy
```angelscript
void SetTextOverflowPolicy(ETextOverflowPolicy InOverflowPolicy)
```
Set the text overflow policy for this text block.

@param InOverflowPolicy the new text overflow policy.

### SetTextTransformPolicy
```angelscript
void SetTextTransformPolicy(ETextTransformPolicy InTransformPolicy)
```
Set the text transformation policy for this text block.

@param InTransformPolicy the new text transformation policy.

