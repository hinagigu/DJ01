# UCommonTextBlock

**继承自**: `UTextBlock`

Text block with automatic scrolling for FX / large texts, also supports a larger set of default styling, & custom mobile scaling.

## 属性

### ScrollStyle
- **类型**: `TSubclassOf<UCommonTextScrollStyle>`

### bIsScrollingEnabled
- **类型**: `bool`

### bAutoCollapseWithEmptyText
- **类型**: `bool`

### Style
- **类型**: `TSubclassOf<UCommonTextStyle>`

## 方法

### GetMargin
```angelscript
FMargin GetMargin()
```

### GetMobileFontSizeMultiplier
```angelscript
float32 GetMobileFontSizeMultiplier()
```

### ResetScrollState
```angelscript
void ResetScrollState()
```

### SetApplyLineHeightToBottomLine
```angelscript
void SetApplyLineHeightToBottomLine(bool InApplyLineHeightToBottomLine)
```

### SetLineHeightPercentage
```angelscript
void SetLineHeightPercentage(float32 InLineHeightPercentage)
```

### SetMargin
```angelscript
void SetMargin(FMargin InMargin)
```

### SetMobileFontSizeMultiplier
```angelscript
void SetMobileFontSizeMultiplier(float32 InMobileFontSizeMultiplier)
```
Sets the new value and then applies the FontSizeMultiplier

### SetScrollingEnabled
```angelscript
void SetScrollingEnabled(bool bInIsScrollingEnabled)
```

### SetStyle
```angelscript
void SetStyle(TSubclassOf<UCommonTextStyle> InStyle)
```

### SetTextCase
```angelscript
void SetTextCase(bool bUseAllCaps)
```

### SetWrapTextWidth
```angelscript
void SetWrapTextWidth(int InWrapTextAt)
```

