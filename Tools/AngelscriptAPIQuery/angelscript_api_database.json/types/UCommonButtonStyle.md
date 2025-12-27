# UCommonButtonStyle

**继承自**: `UObject`

---- All properties must be EditDefaultsOnly, BlueprintReadOnly !!! -----
*       we return the CDO to blueprints, so we cannot allow any changes (blueprint doesn't support const variables)

## 属性

### bSingleMaterial
- **类型**: `bool`

### SingleMaterialBrush
- **类型**: `FSlateBrush`

### NormalBase
- **类型**: `FSlateBrush`

### NormalHovered
- **类型**: `FSlateBrush`

### NormalPressed
- **类型**: `FSlateBrush`

### SelectedBase
- **类型**: `FSlateBrush`

### SelectedHovered
- **类型**: `FSlateBrush`

### SelectedPressed
- **类型**: `FSlateBrush`

### Disabled
- **类型**: `FSlateBrush`

### MinWidth
- **类型**: `int`

### MinHeight
- **类型**: `int`

### PressedSlateSound
- **类型**: `FSlateSound`

### SelectedPressedSlateSound
- **类型**: `FCommonButtonStyleOptionalSlateSound`

### LockedPressedSlateSound
- **类型**: `FCommonButtonStyleOptionalSlateSound`

### HoveredSlateSound
- **类型**: `FSlateSound`

### SelectedHoveredSlateSound
- **类型**: `FCommonButtonStyleOptionalSlateSound`

### LockedHoveredSlateSound
- **类型**: `FCommonButtonStyleOptionalSlateSound`

### ButtonPadding
- **类型**: `FMargin`

### CustomPadding
- **类型**: `FMargin`

### NormalTextStyle
- **类型**: `TSubclassOf<UCommonTextStyle>`

### NormalHoveredTextStyle
- **类型**: `TSubclassOf<UCommonTextStyle>`

### SelectedTextStyle
- **类型**: `TSubclassOf<UCommonTextStyle>`

### SelectedHoveredTextStyle
- **类型**: `TSubclassOf<UCommonTextStyle>`

### DisabledTextStyle
- **类型**: `TSubclassOf<UCommonTextStyle>`

## 方法

### GetButtonPadding
```angelscript
void GetButtonPadding(FMargin& OutButtonPadding)
```

### GetCustomPadding
```angelscript
void GetCustomPadding(FMargin& OutCustomPadding)
```

### GetDisabledBrush
```angelscript
void GetDisabledBrush(FSlateBrush& Brush)
```

### GetDisabledTextStyle
```angelscript
UCommonTextStyle GetDisabledTextStyle()
```

### GetMaterialBrush
```angelscript
void GetMaterialBrush(FSlateBrush& Brush)
```

### GetNormalBaseBrush
```angelscript
void GetNormalBaseBrush(FSlateBrush& Brush)
```

### GetNormalHoveredBrush
```angelscript
void GetNormalHoveredBrush(FSlateBrush& Brush)
```

### GetNormalHoveredTextStyle
```angelscript
UCommonTextStyle GetNormalHoveredTextStyle()
```

### GetNormalPressedBrush
```angelscript
void GetNormalPressedBrush(FSlateBrush& Brush)
```

### GetNormalTextStyle
```angelscript
UCommonTextStyle GetNormalTextStyle()
```

### GetSelectedBaseBrush
```angelscript
void GetSelectedBaseBrush(FSlateBrush& Brush)
```

### GetSelectedHoveredBrush
```angelscript
void GetSelectedHoveredBrush(FSlateBrush& Brush)
```

### GetSelectedHoveredTextStyle
```angelscript
UCommonTextStyle GetSelectedHoveredTextStyle()
```

### GetSelectedPressedBrush
```angelscript
void GetSelectedPressedBrush(FSlateBrush& Brush)
```

### GetSelectedTextStyle
```angelscript
UCommonTextStyle GetSelectedTextStyle()
```

