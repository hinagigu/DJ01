# FDockTabStyle

Represents the appearance of an SDockTab

## 属性

### CloseButtonStyle
- **类型**: `FButtonStyle`
- **描述**: Style used for the close button

### NormalBrush
- **类型**: `FSlateBrush`
- **描述**: Brush used when this tab is in its normal state

### ColorOverlayTabBrush
- **类型**: `FSlateBrush`
- **描述**: Brush used to overlay a given color onto this tab

### ColorOverlayIconBrush
- **类型**: `FSlateBrush`
- **描述**: Brush used to overlay a given color onto this tab

### ForegroundBrush
- **类型**: `FSlateBrush`
- **描述**: Brush used when this tab is in the foreground

### HoveredBrush
- **类型**: `FSlateBrush`
- **描述**: Brush used when this tab is hovered over

### ContentAreaBrush
- **类型**: `FSlateBrush`
- **描述**: Brush used by the SDockingTabStack to draw the content associated with this tab; Documents, Apps, and Tool Panels have different backgrounds

### TabWellBrush
- **类型**: `FSlateBrush`
- **描述**: Brush used by the SDockingTabStack to draw the content associated with this tab; Documents, Apps, and Tool Panels have different backgrounds

### TabTextStyle
- **类型**: `FTextBlockStyle`
- **描述**: Tab Text Style

### TabPadding
- **类型**: `FMargin`
- **描述**: Padding used around this tab

### IconSize
- **类型**: `FDeprecateSlateVector2D`
- **描述**: Icon size for icons in this tab

### OverlapWidth
- **类型**: `float32`
- **描述**: The width that this tab will overlap with side-by-side tabs

### FlashColor
- **类型**: `FSlateColor`
- **描述**: Color used when flashing this tab

### NormalForegroundColor
- **类型**: `FSlateColor`
- **描述**: Foreground Color when the tab is not hovered, pressed, active or in the foreground

### HoveredForegroundColor
- **类型**: `FSlateColor`
- **描述**: Foreground Color when hovered

### ActiveForegroundColor
- **类型**: `FSlateColor`
- **描述**: Foreground Color when Active

### ForegroundForegroundColor
- **类型**: `FSlateColor`
- **描述**: Foreground Color when this tab is the Foreground tab

### IconBorderPadding
- **类型**: `float32`
- **描述**: The padding applied to the border around the tab icon

## 方法

### opAssign
```angelscript
FDockTabStyle& opAssign(FDockTabStyle Other)
```

