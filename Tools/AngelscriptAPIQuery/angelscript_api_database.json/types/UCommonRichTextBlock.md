# UCommonRichTextBlock

**继承自**: `URichTextBlock`

Text block that supports custom scaling for mobile platforms, with option to only show icons if space is sparse.

## 属性

### InlineIconDisplayMode
- **类型**: `ERichTextInlineIconDisplayMode`

### bTintInlineIcon
- **类型**: `bool`
- **描述**: Toggle it on if the text color should also tint the inline icons.

### DefaultTextStyleOverrideClass
- **类型**: `TSubclassOf<UCommonTextStyle>`

### MobileTextBlockScale
- **类型**: `float32`
- **描述**: Mobile font size multiplier. Activated by default on mobile. See CVar Mobile_PreviewFontSize

### ScrollStyle
- **类型**: `TSubclassOf<UCommonTextScrollStyle>`

### bIsScrollingEnabled
- **类型**: `bool`

### bAutoCollapseWithEmptyText
- **类型**: `bool`

## 方法

### SetScrollingEnabled
```angelscript
void SetScrollingEnabled(bool bInIsScrollingEnabled)
```

