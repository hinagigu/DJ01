# UCommonTextStyle

**继承自**: `UObject`

* ---- All properties must be EditDefaultsOnly, BlueprintReadOnly !!! -----
* We return the CDO to blueprints, so we cannot allow any changes (blueprint doesn't support const variables)

## 属性

### bUsesDropShadow
- **类型**: `bool`

### Font
- **类型**: `FSlateFontInfo`

### Color
- **类型**: `FLinearColor`

### ShadowOffset
- **类型**: `FVector2D`

### ShadowColor
- **类型**: `FLinearColor`

### Margin
- **类型**: `FMargin`

### StrikeBrush
- **类型**: `FSlateBrush`

### LineHeightPercentage
- **类型**: `float32`

### ApplyLineHeightToBottomLine
- **类型**: `bool`

## 方法

### GetApplyLineHeightToBottomLine
```angelscript
bool GetApplyLineHeightToBottomLine()
```

### GetColor
```angelscript
void GetColor(FLinearColor& OutColor)
```

### GetFont
```angelscript
void GetFont(FSlateFontInfo& OutFont)
```

### GetLineHeightPercentage
```angelscript
float32 GetLineHeightPercentage()
```

### GetMargin
```angelscript
void GetMargin(FMargin& OutMargin)
```

### GetShadowColor
```angelscript
void GetShadowColor(FLinearColor& OutColor)
```

### GetShadowOffset
```angelscript
void GetShadowOffset(FVector2D& OutShadowOffset)
```

### GetStrikeBrush
```angelscript
void GetStrikeBrush(FSlateBrush& OutStrikeBrush)
```

