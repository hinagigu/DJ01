# URichTextBlock

**继承自**: `UTextLayoutWidget`

The rich text block

* Fancy Text
* No Children

## 属性

### DecoratorClasses
- **类型**: `TArray<TSubclassOf<URichTextBlockDecorator>>`

### bOverrideDefaultStyle
- **类型**: `bool`
- **描述**: True to specify the default text style for this rich text inline, overriding any default provided in the style set table

### DefaultTextStyleOverride
- **类型**: `FTextBlockStyle`

### MinDesiredWidth
- **类型**: `float32`

### TextTransformPolicy
- **类型**: `ETextTransformPolicy`

### TextOverflowPolicy
- **类型**: `ETextOverflowPolicy`

## 方法

### ClearAllDefaultStyleOverrides
```angelscript
void ClearAllDefaultStyleOverrides()
```
Remove all overrides made to the default text style and return to the style specified in the style set data table

### GetDecoratorByClass
```angelscript
URichTextBlockDecorator GetDecoratorByClass(TSubclassOf<URichTextBlockDecorator> DecoratorClass)
```

### GetDefaultDynamicMaterial
```angelscript
UMaterialInstanceDynamic GetDefaultDynamicMaterial()
```
Creates a dynamic material for the default font or returns it if it already
exists

### GetText
```angelscript
FText GetText()
```
Returns widgets text.

### GetTextStyleSet
```angelscript
UDataTable GetTextStyleSet()
```

### RefreshTextLayout
```angelscript
void RefreshTextLayout()
```
Causes the text to reflow it's layout and re-evaluate any decorators

### SetAutoWrapText
```angelscript
void SetAutoWrapText(bool InAutoTextWrap)
```
Set the auto wrap for this rich text block
@param InAutoTextWrap to turn wrap on or off

### SetDecorators
```angelscript
void SetDecorators(TArray<TSubclassOf<URichTextBlockDecorator>> InDecoratorClasses)
```
Replaces the existing decorators with the list provided

### SetDefaultColorAndOpacity
```angelscript
void SetDefaultColorAndOpacity(FSlateColor InColorAndOpacity)
```
Sets the color and opacity of the default text in this rich text block
@param InColorAndOpacity             The new text color and opacity

### SetDefaultFont
```angelscript
void SetDefaultFont(FSlateFontInfo InFontInfo)
```
Dynamically set the default font info for this rich text block
@param InFontInfo The new font info

### SetDefaultMaterial
```angelscript
void SetDefaultMaterial(UMaterialInterface InMaterial)
```

### SetDefaultShadowColorAndOpacity
```angelscript
void SetDefaultShadowColorAndOpacity(FLinearColor InShadowColorAndOpacity)
```
Sets the color and opacity of the default text drop shadow
Note: if opacity is zero no shadow will be drawn
@param InShadowColorAndOpacity               The new drop shadow color and opacity

### SetDefaultShadowOffset
```angelscript
void SetDefaultShadowOffset(FVector2D InShadowOffset)
```
Sets the offset that the default text drop shadow should be drawn at
@param InShadowOffset                The new offset

### SetDefaultStrikeBrush
```angelscript
void SetDefaultStrikeBrush(FSlateBrush InStrikeBrush)
```
Dynamically set the default strike brush for this rich text block
@param InStrikeBrush The new brush to use to strike through text

### SetDefaultTextStyle
```angelscript
void SetDefaultTextStyle(FTextBlockStyle InDefaultTextStyle)
```
Wholesale override of the currently established default text style
@param InDefaultTextStyle The new text style to apply to all default (i.e. undecorated) text in the block

### SetMinDesiredWidth
```angelscript
void SetMinDesiredWidth(float32 InMinDesiredWidth)
```
Set the minimum desired width for this rich text block
@param InMinDesiredWidth new minimum desired width

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

### SetTextStyleSet
```angelscript
void SetTextStyleSet(UDataTable NewTextStyleSet)
```

### SetTextTransformPolicy
```angelscript
void SetTextTransformPolicy(ETextTransformPolicy InTransformPolicy)
```
Set the text transformation policy for this text block.
@param InTransformPolicy the new text transformation policy.

